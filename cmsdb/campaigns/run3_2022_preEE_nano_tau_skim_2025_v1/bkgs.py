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
  ("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         55638210,  84, 3758145551, "w_lnu"                ),
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
datasets = [
  ("DYto2E_MLL_10to50_powheg", ["/DYto2E_MLL_10to50_powheg"], 1356076, 1, 6744, 39.6879065775, ["dy_ee_m10to50"], 3213647),
  ("DYto2E_MLL_120to200_powheg", ["/DYto2E_MLL_120to200_powheg"], 1482424, 1, 20.2047670897, 0.108769234229, ["dy_ee_m120to200"], 5842743),
  ("DYto2E_MLL_1500to2500_powheg", ["/DYto2E_MLL_1500to2500_powheg"], 586670, 1, 0.00103683585389, 1.41039508554e-05, ["dy_ee_m1500to2500"], 9424256),
  ("DYto2E_MLL_200to400_powheg", ["/DYto2E_MLL_200to400_powheg"], 864092, 1, 2.85386502357, 0.0263571291414, ["dy_ee_m200to400"], 8810630),
  ("DYto2E_MLL_2500to4000_powheg", ["/DYto2E_MLL_2500to4000_powheg"], 290470, 1, 5.55187803309e-05, 1.52532817349e-06, ["dy_ee_m2500to4000"], 5765637),
  ("DYto2E_MLL_4000to6000_powheg", ["/DYto2E_MLL_4000to6000_powheg"], 298946, 1, 1.45399663398e-06, 3.88146178167e-08, ["dy_ee_m4000to6000"], 9684601),
  ("DYto2E_MLL_400to800_powheg", ["/DYto2E_MLL_400to800_powheg"], 890161, 1, 0.251136389091, 0.00225146781257, ["dy_ee_m400to800"], 4449820),
  ("DYto2E_MLL_50to120_powheg", ["/DYto2E_MLL_50to120_powheg"], 2859284, 1, 2070.87197099, 5.77990387709, ["dy_ee_m50to120"], 5391600),
  ("DYto2E_MLL_6000_powheg", ["/DYto2E_MLL_6000_powheg"], 145094, 1, 3.28409124197e-08, 1.80630224181e-09, ["dy_ee_m6000toinf"], 9328065),
  ("DYto2E_MLL_800to1500_powheg", ["/DYto2E_MLL_800to1500_powheg"], 599902, 1, 0.017871653107, 0.000237743732235, ["dy_ee_m800to1500"], 6366740),
  ("DYto2L_M_10to50_amcatnloFXFX", ["/DYto2L_M_10to50_amcatnloFXFX"], 52363920, 1, 20950, 3.19283544853, ["dy_m10to50"], 6376362),
  ("DYto2L_M_10to50_madgraphMLM", ["/DYto2L_M_10to50_madgraphMLM"], 160214290, 1, 17380, 0.865711491778, ["dy_m10to50"], 8427271),
  ("DYto2L_M_50_0J_amcatnloFXFX", ["/DYto2L_M_50_0J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_0j"], 6221204),
  ("DYto2L_M_50_1J_amcatnloFXFX", ["/DYto2L_M_50_1J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_1j"], 6530649),
  ("DYto2L_M_50_1J_madgraphMLM", ["/DYto2L_M_50_1J_madgraphMLM"], 144024010, 1, 6282.6, 0.348120157465, ["dy_m50toinf_1j"], 5795415),
  ("DYto2L_M_50_2J_amcatnloFXFX", ["/DYto2L_M_50_2J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_2j"], 3938692),
  ("DYto2L_M_50_2J_madgraphMLM", ["/DYto2L_M_50_2J_madgraphMLM"], 144024010, 1, 6282.6, 0.348120157465, ["dy_m50toinf_2j"], 6565747),
  ("DYto2L_M_50_3J_madgraphMLM", ["/DYto2L_M_50_3J_madgraphMLM"], 144024010, 1, 6282.6, 0.348120157465, ["dy_m50toinf_3j"], 5146767),
  ("DYto2L_M_50_4J_madgraphMLM", ["/DYto2L_M_50_4J_madgraphMLM"], 144024010, 1, 6282.6, 0.348120157465, ["dy_m50toinf_4j"], 4873709),
  ("DYto2L_M_50_amcatnloFXFX", ["/DYto2L_M_50_amcatnloFXFX", "/DYto2L_M_50_amcatnloFXFX_ext1"], 230594628, 1, 6282.6, 0.217427706252, ["dy_m50toinf"], 8202741),
  ("DYto2L_M_50_madgraphMLM", ["/DYto2L_M_50_madgraphMLM", "/DYto2L_M_50_madgraphMLM_ext1"], 288048020, 1, 6282.6, 0.174060078733, ["dy_m50toinf"], 6844596),
  ("DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_1j_pt100to200"], 2227527),
  ("DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_2j_pt100to200"], 7693263),
  ("DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_1j_pt200to400"], 2582152),
  ("DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_2j_pt200to400"], 8177082),
  ("DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_1j_pt400to600"], 5057765),
  ("DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_2j_pt400to600"], 4716917),
  ("DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_1j_pt40to100"], 6434572),
  ("DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_2j_pt40to100"], 3454671),
  ("DYto2L_M_50_PTLL_600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_1j_pt600toinf"], 5816837),
  ("DYto2L_M_50_PTLL_600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX"], 115297314, 1, 6282.6, 0.434855412503, ["dy_m50toinf_2j_pt600toinf"], 5579209),
  ("DYto2Mu_MLL_10to50_powheg", ["/DYto2Mu_MLL_10to50_powheg"], 1301142, 1, 6744, 41.3635234279, ["dy_mumu_m10to50"], 8575321),
  ("DYto2Mu_MLL_120to200_powheg", ["/DYto2Mu_MLL_120to200_powheg"], 1438952, 1, 20.2047670897, 0.112055248043, ["dy_mumu_m120to200"], 8461388),
  ("DYto2Mu_MLL_1500to2500_powheg", ["/DYto2Mu_MLL_1500to2500_powheg"], 590493, 1, 0.00103683585389, 1.4012638335e-05, ["dy_mumu_m1500to2500"], 4854795),
  ("DYto2Mu_MLL_200to400_powheg", ["/DYto2Mu_MLL_200to400_powheg"], 849855, 1, 2.85386502357, 0.0267986708722, ["dy_mumu_m200to400"], 3100405),
  ("DYto2Mu_MLL_2500to4000_powheg", ["/DYto2Mu_MLL_2500to4000_powheg"], 299274, 1, 5.55187803309e-05, 1.48045628606e-06, ["dy_mumu_m2500to4000"], 7749731),
  ("DYto2Mu_MLL_4000to6000_powheg", ["/DYto2Mu_MLL_4000to6000_powheg"], 289198, 1, 1.45399663398e-06, 4.0122942544e-08, ["dy_mumu_m4000to6000"], 6082584),
  ("DYto2Mu_MLL_400to800_powheg", ["/DYto2Mu_MLL_400to800_powheg"], 873292, 1, 0.251136389091, 0.00229495843258, ["dy_mumu_m400to800"], 5798998),
  ("DYto2Mu_MLL_50to120_powheg", ["/DYto2Mu_MLL_50to120_powheg"], 2763691, 1, 2070.87197099, 5.97982432816, ["dy_mumu_m50to120"], 5936397),
  ("DYto2Mu_MLL_6000_powheg", ["/DYto2Mu_MLL_6000_powheg"], 145002, 1, 3.28409124197e-08, 1.80744829364e-09, ["dy_mumu_m6000toinf"], 7515104),
  ("DYto2Mu_MLL_800to1500_powheg", ["/DYto2Mu_MLL_800to1500_powheg"], 579456, 1, 0.017871653107, 0.000246132476763, ["dy_mumu_m800to1500"], 8389367),
  ("DYto2Tau_MLL_10to50_powheg", ["/DYto2Tau_MLL_10to50_powheg"], 1338709, 1, 6744, 40.2027756592, ["dy_tautau_m10to50"], 7608462),
  ("DYto2Tau_MLL_120to200_powheg", ["/DYto2Tau_MLL_120to200_powheg"], 1483110, 1, 20.2047670897, 0.108718923938, ["dy_tautau_m120to200"], 5202380),
  ("DYto2Tau_MLL_1500to2500_powheg", ["/DYto2Tau_MLL_1500to2500_powheg"], 599982, 1, 0.00103683585389, 1.37910218112e-05, ["dy_tautau_m1500to2500"], 6616587),
  ("DYto2Tau_MLL_200to400_powheg", ["/DYto2Tau_MLL_200to400_powheg"], 872968, 1, 2.85386502357, 0.0260891400762, ["dy_tautau_m200to400"], 9723398),
  ("DYto2Tau_MLL_2500to4000_powheg", ["/DYto2Tau_MLL_2500to4000_powheg"], 299996, 1, 5.55187803309e-05, 1.47689327375e-06, ["dy_tautau_m2500to4000"], 4674620),
  ("DYto2Tau_MLL_4000to6000_powheg", ["/DYto2Tau_MLL_4000to6000_powheg"], 299998, 1, 1.45399663398e-06, 3.86785069828e-08, ["dy_tautau_m4000to6000"], 6881230),
  ("DYto2Tau_MLL_400to800_powheg", ["/DYto2Tau_MLL_400to800_powheg"], 897512, 1, 0.251136389091, 0.00223302734616, ["dy_tautau_m400to800"], 2326867),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX", ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"], 31651962, 1, 1664.68417309, 0.419716337803, ["dy_tautau_m50toinf_0j"], 4766062),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX", ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"], 26576552, 1, 316.240337878, 0.0949605649522, ["dy_tautau_m50toinf_1j"], 6552571),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX", ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"], 32763798, 1, 116.472030231, 0.0283695251099, ["dy_tautau_m50toinf_2j"], 6641250),
  ("DYto2Tau_MLL_50to120_powheg", ["/DYto2Tau_MLL_50to120_powheg"], 2907117, 1, 2070.87197099, 5.68480273663, ["dy_tautau_m50to120"], 2284197),
  ("DYto2Tau_MLL_6000_powheg", ["/DYto2Tau_MLL_6000_powheg"], 146995, 1, 3.28409124197e-08, 1.78294239582e-09, ["dy_tautau_m6000toinf"], 8137250),
  ("DYto2Tau_MLL_800to1500_powheg", ["/DYto2Tau_MLL_800to1500_powheg"], 581124, 1, 0.017871653107, 0.000245426002807, ["dy_tautau_m800to1500"], 6549755),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay"], 7185840, 0.3848, 3.2759, 0.00139995093964, ["h_ggf_htt"], 4043304),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay"], 159712, 1, 3.2759, 0.163688341264, ["h_ggf_htt"], 7023857),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay"], 6424278, 0.3848, 3.2759, 0.00156590724438, ["h_ggf_htt"], 4230014),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay"], 159083, 1, 3.2759, 0.164335550373, ["h_ggf_htt"], 2533580),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay"], 6703604, 0.3847, 3.2759, 0.0015002689838, ["h_ggf_htt"], 8491715),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"], 158678, 1, 3.2759, 0.164754990358, ["h_ggf_htt"], 5884721),
  ("ST_t_channel_antitop_4f_InclusiveDecays", ["/ST_t_channel_antitop_4f_InclusiveDecays"], 1325389, 1, 75.47, 0.45441812781, ["st_twchannel_tbar_fh"], 4936298),
  ("ST_t_channel_top_4f_InclusiveDecays", ["/ST_t_channel_top_4f_InclusiveDecays"], 2737505, 1, 123.8, 0.360902909766, ["st_twchannel_t_fh"], 4163552),
  ("ST_tW_antitop_2L2Nu", ["/ST_tW_antitop_2L2Nu", "/ST_tW_antitop_2L2Nu_ext1"], 9526522, 1, 3.8, 0.00318327297202, ["st_twchannel_tbar_dl"], 5537868),
  ("ST_tW_antitop_LNu2Q", ["/ST_tW_antitop_LNu2Q", "/ST_tW_antitop_LNu2Q_ext1"], 18365422, 1, 15.9, 0.00690909035469, ["st_twchannel_tbar_sl"], 8836702),
  ("ST_tW_top_2L2Nu", ["/ST_tW_top_2L2Nu", "/ST_tW_top_2L2Nu_ext1"], 9773736, 1, 3.8, 0.00310275620295, ["st_twchannel_t_dl"], 3680016),
  ("ST_tW_top_LNu2Q", ["/ST_tW_top_LNu2Q", "/ST_tW_top_LNu2Q_ext1"], 19287966, 1, 15.8, 0.00653725333195, ["st_twchannel_t_sl"], 9614568),
  ("TTto2L2Nu", ["/TTto2L2Nu", "/TTto2L2Nu_ext1"], 95000770, 1, 98.0438787561, 0.00823603187664, ["tt_dl"], 3839014),
  ("TTto4Q", ["/TTto4Q", "/TTto4Q_ext1"], 210060058, 1, 419.807164414, 0.0159489106439, ["tt_fh"], 2676905),
  ("TTtoLNu2Q", ["/TTtoLNu2Q", "/TTtoLNu2Q_ext1"], 310692304, 1, 405.74895683, 0.0104220121754, ["tt_sl"], 4562330),
  ("VBFHToTauTau_UncorrelatedDecay_Filtered", ["/VBFHToTauTau_UncorrelatedDecay_Filtered"], 5082505, 0.4091, 0.2558, 0.000164314869048, ["h_vbf_htt"], 2123082),
  ("VBFHToTauTau_UncorrelatedDecay_UnFiltered", ["/VBFHToTauTau_UncorrelatedDecay_UnFiltered"], 99878, 1, 0.2558, 0.0204387985342, ["h_vbf_htt"], 4579965),
  ("WminusHToTauTau_UncorrelatedDecay_Filtered", ["/WminusHToTauTau_UncorrelatedDecay_Filtered"], 431839, 0.3944, 0.03561, 0.000259544409267, ["wh_htt"], 3865791),
  ("WminusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WminusHToTauTau_UncorrelatedDecay_UnFiltered"], 27789, 1, 0.03561, 0.0102264221095, ["wh_htt"], 6300044),
  ("WplusHToTauTau_UncorrelatedDecay_Filtered", ["/WplusHToTauTau_UncorrelatedDecay_Filtered"], 716466, 0.3743, 0.05575, 0.000232430851415, ["wh_htt"], 3570517),
  ("WplusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WplusHToTauTau_UncorrelatedDecay_UnFiltered"], 28300, 1, 0.05575, 0.0157211060071, ["wh_htt"], 3975708),
  ("WtoLNu_1J_madgraphMLM", ["/WtoLNu_1J_madgraphMLM"], 183585526, 1, 63425.1, 2.75706739561, ["w_lnu_1j"], 2894715),
  ("WtoLNu_2J_madgraphMLM", ["/WtoLNu_2J_madgraphMLM"], 183585526, 1, 63425.1, 2.75706739561, ["w_lnu_2j"], 6315414),
  ("WtoLNu_3J_madgraphMLM", ["/WtoLNu_3J_madgraphMLM"], 183585526, 1, 63425.1, 2.75706739561, ["w_lnu_ge3j"], 7281391),
  ("WtoLNu_4J_madgraphMLM", ["/WtoLNu_4J_madgraphMLM"], 183585526, 1, 63425.1, 2.75706739561, ["w_lnu_ge3j"], 5121808),
  ("WtoLNu_madgraphMLM", ["/WtoLNu_madgraphMLM", "/WtoLNu_madgraphMLM_ext1"], 367171052, 1, 63425.1, 1.3785336978, ["w_lnu"], 7869086),
  ("WW", ["/WW"], 15405496, 1, 122.27052, 0.063338931626, ["ww"], 9633333),
  ("WWW_4F", ["/WWW_4F"], 408136, 1, 0.2328, 0.00455200501794, ["www"], 6412526),
  ("WWZ_4F", ["/WWZ_4F"], 1774030, 1, 0.1851, 0.000832664633631, ["wwz"], 6847762),
  ("WZ", ["/WZ"], 7479528, 1, 41.1474, 0.0439028653894, ["wz"], 4970310),
  ("WZZ", ["/WZZ"], 1806418, 1, 0.06206, 0.000274168893357, ["wzz"], 6584570),
  ("ZHToTauTau_UncorrelatedDecay_Filtered", ["/ZHToTauTau_UncorrelatedDecay_Filtered"], 613598, 0.3933, 0.0592, 0.000302821270839, ["zh_htt"], 4149687),
  ("ZHToTauTau_UncorrelatedDecay_UnFiltered", ["/ZHToTauTau_UncorrelatedDecay_UnFiltered"], 28992, 1, 0.0592, 0.0162955187638, ["zh_htt"], 4890171),
  ("ZZ", ["/ZZ"], 1181750, 1, 19.431, 0.131218237698, ["zz"], 6714642),
  ("ZZZ", ["/ZZZ"], 1751582, 1, 0.01591, 7.24877076837e-05, ["zzz"], 3272006),
]
