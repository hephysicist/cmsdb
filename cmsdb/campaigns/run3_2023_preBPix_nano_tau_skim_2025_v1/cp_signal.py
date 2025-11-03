# coding: utf-8

"""
signals for CP analysis from the 2022 post-EE campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1 import campaign_run3_2023_preBPix_nano_tau_skim_2025_v1 as cpn  # TODO: adjust if needed

import re
from collections import OrderedDict

def _base_name(name: str) -> str:
  m = re.match(r'^(.*)_ext\d+$', name)
  return m.group(1) if m else name

def _ext_number(s: str) -> int:
  m = re.search(r'_ext(\d+)$', s)
  return int(m.group(1)) if m else 0

def _key_sort_key(key: str):
  n = _ext_number(key)
  # base (no ext) first, then _ext1, _ext2, ...
  return (0, 0) if n == 0 else (1, n)

def add_merged_datasets(dataset_rows, cpn, procs):
  """
  dataset_rows: iterable of (name, key_or_keys, n_evt, n_files, pid, proc)
  Groups *_extX with their base sample, then calls cpn.add_dataset once per base.
  """
  groups = {}  # base_name -> accumulator
  for name, key, n_evt, n_files, pid, proc in dataset_rows:
    base = _base_name(name)
    g = groups.get(base)
    if g is None:
      g = {
        "name": base,
        "proc": proc,
        "id": None,            # prefer non-ext id; fallback to first seen
        "keys": OrderedDict(), # preserve insertion order, avoid dups
        "n_events": 0,
        "n_files": 0,
      }
      groups[base] = g

    if g["proc"] != proc:
      raise ValueError(f"Process mismatch for {base}: {g['proc']} vs {proc}")

    if not re.search(r'_ext\d+$', name):
      g["id"] = pid
    elif g["id"] is None:
      g["id"] = pid

    # --- FIX: accept string OR list of strings for 'key' ---
    keys_in = key if isinstance(key, (list, tuple)) else [key]
    for k in keys_in:
      if not isinstance(k, str):
        raise TypeError(f"key must be a string, got {type(k).__name__}: {k}")
      g["keys"][k] = True

    g["n_events"] += int(n_evt)
    g["n_files"]  += int(n_files)

  # emit one add per base sample with sorted keys (base first, then ext1, ext2, ...)
  for base, g in groups.items():
    keys = list(g["keys"].keys())
    keys.sort(key=_key_sort_key)
    cpn.add_dataset(
      name=g["name"],
      id=g["id"],
      is_data=False,
      processes=[getattr(procs, g["proc"])],
      keys=keys,
      n_files=g["n_files"],
      n_events=g["n_events"],
    )

# ---- your datasets (name, key, n_evt, n_files, pid, proc) ----

dataset_rows = [
    #ggH SM production
    ("h_ggf_htt_sm_prod_sm_filtered",  ["/GluGluHto2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay"],    17266134,  45,  23000000, "h_ggf_htt_sm_prod_sm"),
    ("h_ggf_htt_sm_prod_cpo_filtered", ["/GluGluHto2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay"], 16406657,  42,  23000010, "h_ggf_htt_sm_prod_cpo"),
    ("h_ggf_htt_sm_prod_mm_filtered",  ["/GluGluHto2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay"],    18105720,  47,  23000020, "h_ggf_htt_sm_prod_mm"),
    ("h_vbf_htt_sm_filtered",          ["/VBFHto2Tau_UncorrelatedDecay_Filtered"],                       12453012,  31,  23000030, "h_vbf_htt_sm"),
    ("zh_htt_sm_filtered",             ["/ZHto2Tau_UncorrelatedDecay_Filtered"],                         1803008,    6,  23000040, "zh_htt_sm"),
    ("wph_htt_sm_filtered",            ["/WplusHto2Tau_UncorrelatedDecay_Filtered"],                     1802553,    5,  23000050, "wph_htt_sm"),
    ("wmh_htt_sm_filtered",            ["/WminusHto2Tau_UncorrelatedDecay_Filtered"],                    1248957,    4,  23000060, "wmh_htt_sm"),
]

dataset_rows_cp = []
for name, key, n_evt, n_files, pid, proc in dataset_rows:
    dataset_rows_cp.append((name, key, n_evt, n_files, pid, proc))
    for idx, the_cp_var in enumerate(['htt_mm','htt_cpo','htt_flat']):
        cp_name = name.replace('htt_sm', the_cp_var)
        cp_proc = proc.replace('htt_sm', the_cp_var)
        cp_pid=pid+idx+1
        dataset_rows_cp.append((cp_name, key, n_evt, n_files, cp_pid, cp_proc))
add_merged_datasets(dataset_rows_cp, cpn, procs)
