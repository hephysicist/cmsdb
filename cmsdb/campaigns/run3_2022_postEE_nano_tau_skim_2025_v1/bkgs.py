# coding: utf-8

"""
CMS bkgs datasets from the 2022 post-EE campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_skim_2025_v1 import campaign_run3_2022_postEE_nano_tau_skim_2025_v1 as cpn  # TODO: adjust if needed

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
  #("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                168535477, 139, 1895014020, "dy_m10to50"           ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 275262495, 425, 1078589252, "dy_ll_m50_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                 151393596, 539, 4189203628, "dy_ll_m50_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                  84618132, 560, 3905898197, "dy_ll_m50_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    143381450, 317, 4072667752, "dy_ll_m50"          ),
  ("DYto2L_M_50_amcatnloFXFX_ext1",                               ["/DYto2L_M_50_amcatnloFXFX_ext1"],                               240058361, 554, 2565332299, "dy_ll_m50"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                             100595369, 109, 3729619275, "dy_tt_m50_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                              87692299, 228, 1740022435, "dy_tt_m50_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                             112976268, 595, 1993066714, "dy_tt_m50_2j"),
  #w+jets madgraph
  ("WtoLNu_1J_madgraphMLM",                                       ["/WtoLNu_1J_madgraphMLM"],                                         42695566,  41, 2676975567, "wj_1j"),
  ("WtoLNu_2J_madgraphMLM",                                       ["/WtoLNu_2J_madgraphMLM"],                                         36349344,  43, 3824042516, "wj_2j"),
  ("WtoLNu_3J_madgraphMLM",                                       ["/WtoLNu_3J_madgraphMLM"],                                         27828446,  39, 2128716642, "wj_3j"),
  ("WtoLNu_4J_madgraphMLM",                                       ["/WtoLNu_4J_madgraphMLM"],                                          4906634,  10,  455870882, "wj_4j"),
  ("WtoLNu_madgraphMLM",                                          ["/WtoLNu_madgraphMLM"],                                           342750582, 281, 3506143279, "wj"),
  ("WtoLNu_madgraphMLM_ext1",                                     ["/WtoLNu_madgraphMLM_ext1"],                                      341334203, 285, 2794945238, "wj"),
  #ttbar _
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                    83445808, 238,  481041747, "tt_dl"                ),
  ("TTto2L2Nu_ext1",                                              ["/TTto2L2Nu_ext1"],                                               84236946, 233, 3676565014, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      178011279, 466,  954044713, "tt_fh"                ),
  ("TTto4Q_ext1",                                                 ["/TTto4Q_ext1"],                                                 185398097, 458, 1796602938, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   264626088, 712,  974897688, "tt_sl"                ),
  ("TTtoLNu2Q_ext1",                                              ["/TTtoLNu2Q_ext1"],                                              273257101, 739, 2314749232, "tt_sl"                ),
  #single top
  ("TWminusto2L2Nu",                                              ["/TWminusto2L2Nu"],                                                8065066,  20, 3769865861, "st_twchannel_t_dl"    ),
  ("TWminusto2L2Nu_ext1",                                         ["/TWminusto2L2Nu_ext1"],                                           8510272,  21, 1220353833, "st_twchannel_t_dl"    ),
  ("TWminusto4Q",                                                 ["/TWminusto4Q"],                                                  13459714,  26,  360718874, "st_twchannel_t_fh"    ),
  ("TWminusto4Q_ext1",                                            ["/TWminusto4Q_ext1"],                                             13999444,  27, 3323803668, "st_twchannel_t_fh"    ),
  ("TWminustoLNu2Q",                                              ["/TWminustoLNu2Q"],                                               16686824,  38, 3322169806, "st_twchannel_t_sl"    ),
  ("TWminustoLNu2Q_ext1",                                         ["/TWminustoLNu2Q_ext1"],                                          15824984,  36,  442938383, "st_twchannel_t_sl"    ),
  ("TbarWplusto2L2Nu",                                            ["/TbarWplusto2L2Nu"],                                              8259727,  20, 3186488965, "st_twchannel_tbar_dl" ),
  ("TbarWplusto2L2Nu_ext1",                                       ["/TbarWplusto2L2Nu_ext1"],                                         8522476,  21,  447531145, "st_twchannel_tbar_dl" ),
  ("TbarWplusto4Q",                                               ["/TbarWplusto4Q"],                                                13418632,  25, 1514482258, "st_twchannel_tbar_fh" ),
  ("TbarWplusto4Q_ext1",                                          ["/TbarWplusto4Q_ext1"],                                           12556124,  24, 2343502866, "st_twchannel_tbar_fh" ),
  ("TbarWplustoLNu2Q",                                            ["/TbarWplustoLNu2Q"],                                             16485400,  37, 2606377422, "st_twchannel_tbar_sl" ),
  ("TbarWplustoLNu2Q_ext1",                                       ["/TbarWplustoLNu2Q_ext1"],                                        17271609,  39, 1215783855, "st_twchannel_tbar_sl" ),
  #diboson
  ("WW",                                                          ["/WW"],                                                           53112080,  53,  443727516, "ww"                   ),
  ("WZ",                                                          ["/WZ"],                                                           26722782,  26, 1690550817, "wz"                   ),
  ("ZZ",                                                          ["/ZZ"],                                                            4043040,   4, 3513629804, "zz"                   ),
  #triboson
  # ("WZZ",                                                         ["/WZZ"],                                                           5229208,  14,  363955451, "wzz"                  ),
  # ("ZZZ",                                                         ["/ZZZ"],                                                           5063206,  11,  493426600, "zzz"                  ),
  # ("WWW_4F",                                                      ["/WWW_4F"],                                                        1345746,   4, 3973511632, "www"                  ),
  # ("WWZ_4F",                                                      ["/WWZ_4F"],                                                        5249916,  14,  515645709, "wwz"                  ),
]

add_merged_datasets(dataset_rows, cpn, procs)
