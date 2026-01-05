# coding: utf-8

"""
CMS bkgs datasets from the 2023 campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1 import  campaign_run3_2023_preBPix_nano_tau_skim_2025_v1 as cpn 

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
  ("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                149951901, 141, 2806293010, "dy_ll_m10to50"           ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 155735461, 266, 4205285285, "dy_ll_m50_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                  90103222, 348, 1130124365, "dy_ll_m50_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                  47134234, 337, 1377910324, "dy_ll_m50_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    103978251, 243,  236301853, "dy_ll_m50"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                              68706683,  77,   19259918, "dy_tt_m50_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                              57833582, 157, 3101571558, "dy_tt_m50_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                              94739940, 521, 2846053279, "dy_tt_m50_2j"),
  #w+jets madgraph
  ("WtoLNu_1J_madgraphMLM",                                        ["/WtoLNu_1J_madgraphMLM"],                                         23085414,  24, 3726269877, "wj_1j"),
  ("WtoLNu_2J_madgraphMLM",                                        ["/WtoLNu_2J_madgraphMLM"],                                         20267771,  25, 2726000750, "wj_2j"),
  ("WtoLNu_3J_madgraphMLM",                                        ["/WtoLNu_3J_madgraphMLM"],                                         15887453,  24, 1064605976, "wj_3j"),
  ("WtoLNu_4J_madgraphMLM",                                        ["/WtoLNu_4J_madgraphMLM"],                                          2962673,   6, 1522086872, "wj_4j"),
  ("WtoLNu_madgraphMLM",                                           ["/WtoLNu_madgraphMLM"],                                           191075090, 166,  308570332, "wj"),
  #ttbar and single top
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                    47713334, 141, 2034526151, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      104112654, 262, 1193746585, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   151416926, 418, 1609808012, "tt_sl"                ),
  ("TWminusto2L2Nu",                                              ["/TWminusto2L2Nu"],                                                4984812,  13, 2144094551, "st_twchannel_t_dl"    ),
  ("TWminusto4Q",                                                 ["/TWminusto4Q"],                                                   7918700,  16, 2961019086, "st_twchannel_t_fh"    ),
  ("TWminustoLNu2Q",                                              ["/TWminustoLNu2Q"],                                                9649924,  23, 1501271580, "st_twchannel_t_sl"    ),
  ("TbarWplusto2L2Nu",                                            ["/TbarWplusto2L2Nu"],                                              4906798,  13,  412025122, "st_twchannel_tbar_dl" ),
  ("TbarWplusto4Q",                                               ["/TbarWplusto4Q"],                                                 7969722,  16, 2591972628, "st_twchannel_tbar_fh" ),
  ("TbarWplustoLNu2Q",                                            ["/TbarWplustoLNu2Q"],                                              9550319,  23, 1043914345, "st_twchannel_tbar_sl" ),
  #Diboson
  ("WW",                                                          ["/WW"],                                                           33507000,  36,  798180476, "ww"                   ),
  ("WZ",                                                          ["/WZ"],                                                           16770000,  17, 1361197249, "wz"                   ),
  ("ZZ",                                                          ["/ZZ"],                                                            2517000,   3, 3834398348, "zz"                   ),
  #Triboson
  #("WWW_4F",                                                      ["/WWW_4F"],                                                         849916,   3, 2469152864, "www"                  ),
  #("WWZ_4F",                                                      ["/WWZ_4F"],                                                        3275962,   9, 1632014525, "wwz"                  ),
  #("WZZ",                                                         ["/WZZ"],                                                           3251476,   9, 3046016889, "wzz"                  ),
  #("ZZZ",                                                         ["/ZZZ"],                                                           3201470,   8, 3176535082, "zzz"                  ),
  #("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         135956411, 191, 2145010577, "w_lnu"                ),

]

add_merged_datasets(dataset_rows, cpn, procs)

