# coding: utf-8

"""
CMS bkgs datasets from the 2023 BPix campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_skim_2025_v1 import campaign_run3_2023_postBPix_nano_tau_skim_2025_v1 as cpn  # TODO: adjust if needed

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
  #DY amc@nlo
  #("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                74917918,  71, 2676360070, "dy_m10to50"         ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 76989083, 133, 3770998535, "dy_ll_m50_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                 42819115, 162, 1497302255, "dy_ll_m50_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                 23588533, 170, 1212313238, "dy_ll_m50_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    63684562, 149, 3178417364, "dy_ll_m50"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                             35162586,  40,  961141806, "dy_tt_m50_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                             36023045,  97, 2159151046, "dy_tt_m50_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                             37570255, 208, 2446290367, "dy_tt_m50_2j"),
  #w+jets madgraph
  ("WtoLNu_1J_madgraphMLM",                                        ["/WtoLNu_1J_madgraphMLM"],                                        11369658, 12, 1147845960, "wj_1j"),
  ("WtoLNu_2J_madgraphMLM",                                        ["/WtoLNu_2J_madgraphMLM"],                                         9459992, 12,  940284051, "wj_2j"),
  ("WtoLNu_3J_madgraphMLM",                                        ["/WtoLNu_3J_madgraphMLM"],                                         7718351, 12, 2768533989, "wj_3j"),
  ("WtoLNu_4J_madgraphMLM",                                        ["/WtoLNu_4J_madgraphMLM"],                                         1436944,  3, 3234452261, "wj_4j"),
  ("WtoLNu_madgraphMLM",                                           ["/WtoLNu_madgraphMLM"],                                           94639090, 82, 2950261722, "wj"),
  #w+jets amc@nlo
  ("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         64991689,  91, 2516868007, "w_lnu"                ),
  #ttbar 
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                   24357456,  70, 4011623041, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      52422350, 131, 2259192852, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   63358614, 174, 3383451082, "tt_sl"                ),
  #single top
  ("TWminusto2L2Nu",                                              ["/TWminusto2L2Nu"],                                               2478922,   7,  208275232, "st_twchannel_t_dl"    ),
  ("TWminusto4Q",                                                 ["/TWminusto4Q"],                                                  3933816,   8, 3326015714, "st_twchannel_t_fh"    ),
  ("TWminustoLNu2Q",                                              ["/TWminustoLNu2Q"],                                               4943196,  12,  719181931, "st_twchannel_t_sl"    ),
  ("TbarWplusto2L2Nu",                                            ["/TbarWplusto2L2Nu"],                                             2487898,   7, 3918917922, "st_twchannel_tbar_dl" ),
  ("TbarWplusto4Q",                                               ["/TbarWplusto4Q"],                                                3975836,   8, 3760630163, "st_twchannel_tbar_fh" ),
  ("TbarWplustoLNu2Q",                                            ["/TbarWplustoLNu2Q"],                                             5146462,  12, 3475123817, "st_twchannel_tbar_sl" ),
  #Diboson
  ("WW",                                                          ["/WW"],                                                          16913262,  18, 2388590455, "ww"                   ), # OLD value was 16545000
  ("WZ",                                                          ["/WZ"],                                                           8379000,   9, 4042228682, "wz"                   ),
  ("ZZ",                                                          ["/ZZ"],                                                           1254000,   2, 1161952647, "zz"                   ),
  #Triboson
  #("WWW_4F",                                                      ["/WWW_4F"],                                                        423054,   2, 1386472685, "www"                  ),
  #("WWZ_4F",                                                      ["/WWZ_4F"],                                                       1585526,   5, 2697542704, "wwz"                  ),
  #("WZZ",                                                         ["/WZZ"],                                                          1625116,   5,  587043658, "wzz"                  ),
  #("ZZZ",                                                         ["/ZZZ"],                                                          1589388,   4,  707067929, "zzz"                  ),
]

add_merged_datasets(dataset_rows, cpn, procs)

