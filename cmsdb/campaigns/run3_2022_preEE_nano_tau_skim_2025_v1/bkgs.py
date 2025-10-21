# coding: utf-8

"""
CMS bkgs datasets from the 2022 pre-EE campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_2025_v1 import campaign_run3_2022_preEE_nano_tau_skim_2025_v1 as cpn  # TODO: adjust if needed
# Merge *_extX datasets with their base sample and register once per base.
# Indentation uses 2 spaces.

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
  ("GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay",  ["/GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"],    158678,   1, 2693954882, "h_ggf_htt_sm_prod_sm"            ),
  ("VBFHto2Tau_UncorrelatedDecay_UnFiltered",                     ["/VBFHto2Tau_UncorrelatedDecay_UnFiltered"],                        99878,   1,  896795747, "h_vbf_htt_sm"            ),
  #("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                52363920,  48, 2602844442, "dy_m10to50"           ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 70152268, 120, 2577421953, "dy_ll_m50_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                 45431665, 171,  542870889, "dy_ll_m50_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                 21946124, 154,  824633104, "dy_ll_m50_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    48541588, 117, 3909617802, "dy_ll_m50"          ),
  ("DYto2L_M_50_amcatnloFXFX_ext1",                               ["/DYto2L_M_50_amcatnloFXFX_ext1"],                               66755726, 157, 2411443415, "dy_ll_m50"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                             31651962,  37,  936866557, "dy_tt_m50_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                             25513383,  70, 2385291541, "dy_tt_m50_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                             32763798, 182, 2672935788, "dy_tt_m50_2j"),
  ("DYto2Tau_MLL_50_0J_Filtered_amcatnloFXFX",                    ["/DYto2Tau_MLL_50_0J_Filtered_amcatnloFXFX"],                    10573523, 21, 2672935787, "dy_tt_m50_0j"),
  ("DYto2Tau_MLL_50_1J_Filtered_amcatnloFXFX",                    ["/DYto2Tau_MLL_50_1J_Filtered_amcatnloFXFX"],                     9627320, 40, 2672935786, "dy_tt_m50_1j"),
  ("DYto2Tau_MLL_50_2J_Filtered_amcatnloFXFX",                    ["/DYto2Tau_MLL_50_2J_Filtered_amcatnloFXFX"],                    10255583, 77, 2672935785, "dy_tt_m50_2j"),
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                   23610071,  69, 3100293127, "tt_dl"                ),
  ("TTto2L2Nu_ext1",                                              ["/TTto2L2Nu_ext1"],                                              23890314,  69, 3929317461, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      52883494, 139, 2341281799, "tt_fh"                ),
  ("TTto4Q_ext1",                                                 ["/TTto4Q_ext1"],                                                 52146535, 134,  327063403, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   65881840, 186, 2659018572, "tt_sl"                ),
  ("TTtoLNu2Q_ext1",                                              ["/TTtoLNu2Q_ext1"],                                              76380270, 212, 3102673779, "tt_sl"                ),
  ("TWminusto2L2Nu",                                              ["/TWminusto2L2Nu"],                                               2386952,   6, 3517241542, "st_twchannel_t_dl"    ),
  ("TWminusto2L2Nu_ext1",                                         ["/TWminusto2L2Nu_ext1"],                                          2499916,   7, 4078018809, "st_twchannel_t_dl"    ),
  ("TWminusto4Q",                                                 ["/TWminusto4Q"],                                                  3861851,   8, 1844136267, "st_twchannel_t_fh"    ),
  ("TWminusto4Q_ext1",                                            ["/TWminusto4Q_ext1"],                                             3909424,   8, 2351790418, "st_twchannel_t_fh"    ),
  ("TWminustoLNu2Q",                                              ["/TWminustoLNu2Q"],                                               4743805,  12, 4145219469, "st_twchannel_t_sl"    ),
  ("TWminustoLNu2Q_ext1",                                         ["/TWminustoLNu2Q_ext1"],                                          4900178,  12, 2714373087, "st_twchannel_t_sl"    ),
  ("TbarWplusto2L2Nu",                                            ["/TbarWplusto2L2Nu"],                                             2327604,   6, 4158502851, "st_twchannel_tbar_dl" ),
  ("TbarWplusto2L2Nu_ext1",                                       ["/TbarWplusto2L2Nu_ext1"],                                        2435657,   7, 3226081319, "st_twchannel_tbar_dl" ),
  ("TbarWplusto4Q",                                               ["/TbarWplusto4Q"],                                                3762818,   8,  595953404, "st_twchannel_tbar_fh" ),
  ("TbarWplusto4Q_ext1",                                          ["/TbarWplusto4Q_ext1"],                                           3999850,   8,  743954343, "st_twchannel_tbar_fh" ),
  ("TbarWplustoLNu2Q",                                            ["/TbarWplustoLNu2Q"],                                             4366325,  11, 3513411720, "st_twchannel_tbar_sl" ),
  ("TbarWplustoLNu2Q_ext1",                                       ["/TbarWplustoLNu2Q_ext1"],                                        4816386,  12, 2459022081, "st_twchannel_tbar_sl" ),
  ("WW",                                                          ["/WW"],                                                          15405496,  16, 2536448793, "ww"                   ),
  #("WWW_4F",                                                      ["/WWW_4F"],                                                        372028,   1, 1602636030, "www"                 ),
  #("WWZ_4F",                                                      ["/WWZ_4F"],                                                       1774030,   5, 2917961763, "wwz"                 ),
  ("WZ",                                                          ["/WZ"],                                                           7479528,   8, 3919470500, "wz"                   ),
  #("WZZ",                                                         ["/WZZ"],                                                          1806418,   5, 2297343689, "wzz"                 ),
  ("WminusHto2Tau_UncorrelatedDecay_UnFiltered",                  ["/WminusHto2Tau_UncorrelatedDecay_UnFiltered"],                     27789,   1, 1056944567, "wmh_htt_flat"         ),
  ("WplusHto2Tau_UncorrelatedDecay_UnFiltered",                   ["/WplusHto2Tau_UncorrelatedDecay_UnFiltered"],                      28300,   1, 1400713916, "wph_htt_flat"         ),
  #("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         55638210,  84, 3758145551, "w_lnu"                ),
  ("WtoLNu_madgraphMLM",                                          ["/WtoLNu_madgraphMLM"],                                          87204163,  76, 3758145552, "wj"                   ),
  ("WtoLNu_madgraphMLM_ext1",                                     ["/WtoLNu_madgraphMLM_ext1"],                                     97491826,  87, 3758145543, "wj"                   ),
  ("WtoLNu_1J_madgraphMLM",                                       ["/WtoLNu_1J_madgraphMLM"],                                       11896625,  13, 3758145564, "wj_1j"                   ),  
  ("WtoLNu_2J_madgraphMLM",                                       ["/WtoLNu_2J_madgraphMLM"],                                        9283334,  12, 3758145585, "wj_2j"                   ),  
  ("WtoLNu_3J_madgraphMLM",                                       ["/WtoLNu_3J_madgraphMLM"],                                        8221862,  13, 3758145546, "wj_3j"                   ),  
  ("WtoLNu_4J_madgraphMLM",                                       ["/WtoLNu_4J_madgraphMLM"],                                        1463885,   3, 3758174557, "wj_4j"                   ),  
  ("ZHto2Tau_UncorrelatedDecay_UnFiltered",                       ["/ZHto2Tau_UncorrelatedDecay_UnFiltered"],                          28992,   1, 4033200945, "zh_htt_flat"          ),
  ("ZZ",                                                          ["/ZZ"],                                                           1181750,   2, 1546658281, "zz"                   ),
  #("ZZZ",                                                         ["/ZZZ"],                                                          1751582,   4, 2151038362, "zzz"                 ),
]

def register_all_datasets(cpn, procs):
  add_merged_datasets(dataset_rows, cpn, procs)

register_all_datasets(cpn, procs)

"""
CMS datasets from the 2022 pre-EE data-taking campaign
Generated from Run3_2022.yaml with _ext1 merged into base samples.
Lumi used for weights: 7980.4
"""