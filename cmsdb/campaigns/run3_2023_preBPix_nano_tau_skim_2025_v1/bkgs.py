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
  ("GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay",  ["/GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"],     159160,   1, 1782707149, "h_ggf_htt"            ),
  ("VBFHto2Tau_UncorrelatedDecay_UnFiltered",                     ["/VBFHto2Tau_UncorrelatedDecay_UnFiltered"],                        299664,   1, 3714290882, "h_vbf_htt"            ),
  ("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                149951901, 141, 2806293010, "dy_m10to50"           ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 155735461, 266, 4205285285, "dy_m50toinf_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                  90103222, 348, 1130124365, "dy_m50toinf_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                  47134234, 337, 1377910324, "dy_m50toinf_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    103978251, 243,  236301853, "dy_m50toinf"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                              68706683,  77,   19259918, "dy_tautau_m50toinf_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                              57833582, 157, 3101571558, "dy_tautau_m50toinf_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                              94739940, 521, 2846053279, "dy_tautau_m50toinf_2j"),
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                    47713334, 141, 2034526151, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      104112654, 262, 1193746585, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   151416926, 418, 1609808012, "tt_sl"                ),
  ("TWminusto2L2Nu",                                              ["/TWminusto2L2Nu"],                                                4984812,  13, 2144094551, "st_twchannel_t_dl"    ),
  ("TWminusto4Q",                                                 ["/TWminusto4Q"],                                                   7918700,  16, 2961019086, "st_twchannel_t_fh"    ),
  ("TWminustoLNu2Q",                                              ["/TWminustoLNu2Q"],                                                9649924,  23, 1501271580, "st_twchannel_t_sl"    ),
  ("TbarWplusto2L2Nu",                                            ["/TbarWplusto2L2Nu"],                                              4906798,  13,  412025122, "st_twchannel_tbar_dl" ),
  ("TbarWplusto4Q",                                               ["/TbarWplusto4Q"],                                                 7969722,  16, 2591972628, "st_twchannel_tbar_fh" ),
  ("TbarWplustoLNu2Q",                                            ["/TbarWplustoLNu2Q"],                                              9550319,  23, 1043914345, "st_twchannel_tbar_sl" ),
  ("WW",                                                          ["/WW"],                                                           33507000,  36,  798180476, "ww"                   ),
  ("WWW_4F",                                                      ["/WWW_4F"],                                                         849916,   3, 2469152864, "www"                  ),
  ("WWZ_4F",                                                      ["/WWZ_4F"],                                                        3275962,   9, 1632014525, "wwz"                  ),
  ("WZ",                                                          ["/WZ"],                                                           16770000,  17, 1361197249, "wz"                   ),
  ("WZZ",                                                         ["/WZZ"],                                                           3251476,   9, 3046016889, "wzz"                  ),
  ("WminusHto2Tau_UncorrelatedDecay_UnFiltered",                  ["/WminusHto2Tau_UncorrelatedDecay_UnFiltered"],                      66292,   1,  349669845, "wh_htt"               ),
  ("WplusHto2Tau_UncorrelatedDecay_UnFiltered",                   ["/WplusHto2Tau_UncorrelatedDecay_UnFiltered"],                       64190,   1,  342803527, "wh_htt"               ),
  ("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         135956411, 191, 2145010577, "w_lnu"                ),
  ("ZHto2Tau_UncorrelatedDecay_UnFiltered",                       ["/ZHto2Tau_UncorrelatedDecay_UnFiltered"],                           69949,   1, 3203188888, "zh_htt"               ),
  ("ZZ",                                                          ["/ZZ"],                                                            2517000,   3, 3834398348, "zz"                   ),
  ("ZZZ",                                                         ["/ZZZ"],                                                           3201470,   8, 3176535082, "zzz"                  ),
]

def register_all_datasets(cpn, procs):
  add_merged_datasets(dataset_rows, cpn, procs)

register_all_datasets(cpn, procs)

# Each entry: (name, keys, eff(sumw), filter_efficiency, xs_pb, norm_weight, proc_names, rand_id)
datasets = [
  ("DYto2E_MLL_10to50_powheg", ["/DYto2E_MLL_10to50_powheg"], 2724758, 1, 6744, 44.0416125028, ["dy_ee_m10to50"], 3826561),
  ("DYto2E_MLL_120to200_powheg", ["/DYto2E_MLL_120to200_powheg"], 2960190, 1, 20.2047670897, 0.12145288836, ["dy_ee_m120to200"], 9449626),
  ("DYto2E_MLL_1500to2500_powheg", ["/DYto2E_MLL_1500to2500_powheg"], 1153954, 1, 0.00103683585389, 1.59880352111e-05, ["dy_ee_m1500to2500"], 4393436),
  ("DYto2E_MLL_200to400_powheg", ["/DYto2E_MLL_200to400_powheg"], 1723816, 1, 2.85386502357, 0.0294588716135, ["dy_ee_m200to400"], 7861303),
  ("DYto2E_MLL_2500to4000_powheg", ["/DYto2E_MLL_2500to4000_powheg"], 589996, 1, 5.55187803309e-05, 1.67442012693e-06, ["dy_ee_m2500to4000"], 4979462),
  ("DYto2E_MLL_4000to6000_powheg", ["/DYto2E_MLL_4000to6000_powheg"], 593000, 1, 1.45399663398e-06, 4.36297067539e-08, ["dy_ee_m4000to6000"], 4010870),
  ("DYto2E_MLL_400to800_powheg", ["/DYto2E_MLL_400to800_powheg"], 1785988, 1, 0.251136389091, 0.00250210018628, ["dy_ee_m400to800"], 6223128),
  ("DYto2E_MLL_50to120_powheg", ["/DYto2E_MLL_50to120_powheg"], 5785264, 1, 2070.87197099, 6.36947524812, ["dy_ee_m50to120"], 5468473),
  ("DYto2E_MLL_6000_powheg", ["/DYto2E_MLL_6000_powheg"], 297000, 1, 3.28409124197e-08, 1.96757978315e-09, ["dy_ee_m6000toinf"], 2962828),
  ("DYto2E_MLL_800to1500_powheg", ["/DYto2E_MLL_800to1500_powheg"], 1191706, 1, 0.017871653107, 0.000266851216144, ["dy_ee_m800to1500"], 6882928),
  ("DYto2L_M_10to50_amcatnloFXFX", ["/DYto2L_M_10to50_amcatnloFXFX"], 149951901, 1, 20950, 2.48602583571, ["dy_m10to50"], 4466947),
  ("DYto2L_M_10to50_madgraphMLM", ["/DYto2L_M_10to50_madgraphMLM"], 306998077, 1, 17380, 1.00736696145, ["dy_m10to50"], 5134546),
  ("DYto2L_M_50_0J_amcatnloFXFX", ["/DYto2L_M_50_0J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_0j"], 7202051),
  ("DYto2L_M_50_1J_amcatnloFXFX", ["/DYto2L_M_50_1J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_1j"], 8770027),
  ("DYto2L_M_50_1J_madgraphMLM", ["/DYto2L_M_50_1J_madgraphMLM"], 130559088, 1, 6282.6, 0.856260457334, ["dy_m50toinf_1j"], 7818051),
  ("DYto2L_M_50_2J_amcatnloFXFX", ["/DYto2L_M_50_2J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_2j"], 5090154),
  ("DYto2L_M_50_2J_madgraphMLM", ["/DYto2L_M_50_2J_madgraphMLM"], 130559088, 1, 6282.6, 0.856260457334, ["dy_m50toinf_2j"], 7425746),
  ("DYto2L_M_50_3J_madgraphMLM", ["/DYto2L_M_50_3J_madgraphMLM"], 130559088, 1, 6282.6, 0.856260457334, ["dy_m50toinf_3j"], 4176207),
  ("DYto2L_M_50_4J_madgraphMLM", ["/DYto2L_M_50_4J_madgraphMLM"], 130559088, 1, 6282.6, 0.856260457334, ["dy_m50toinf_4j"], 2195316),
  ("DYto2L_M_50_amcatnloFXFX", ["/DYto2L_M_50_amcatnloFXFX", "/DYto2L_M_50_amcatnloFXFX_ext1"], 207956502, 1, 6282.6, 0.537576768819, ["dy_m50toinf"], 4738802),
  ("DYto2L_M_50_madgraphMLM", ["/DYto2L_M_50_madgraphMLM", "/DYto2L_M_50_madgraphMLM_ext1"], 261118176, 1, 6282.6, 0.428130228667, ["dy_m50toinf"], 2009051),
  ("DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_1j_pt100to200"], 3449849),
  ("DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_2j_pt100to200"], 7809318),
  ("DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_1j_pt200to400"], 6097173),
  ("DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_2j_pt200to400"], 4508300),
  ("DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_1j_pt400to600"], 4638967),
  ("DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_2j_pt400to600"], 3359451),
  ("DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_1j_pt40to100"], 9138248),
  ("DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_2j_pt40to100"], 7934215),
  ("DYto2L_M_50_PTLL_600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_1j_pt600toinf"], 4693403),
  ("DYto2L_M_50_PTLL_600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX"], 103978251, 1, 6282.6, 1.07515353764, ["dy_m50toinf_2j_pt600toinf"], 6393491),
  ("DYto2Mu_MLL_10to50_powheg", ["/DYto2Mu_MLL_10to50_powheg"], 2752462, 1, 6744, 43.5983261531, ["dy_mumu_m10to50"], 2475669),
  ("DYto2Mu_MLL_120to200_powheg", ["/DYto2Mu_MLL_120to200_powheg"], 2966092, 1, 20.2047670897, 0.121211218531, ["dy_mumu_m120to200"], 5598540),
  ("DYto2Mu_MLL_1500to2500_powheg", ["/DYto2Mu_MLL_1500to2500_powheg"], 1190936, 1, 0.00103683585389, 1.54915605742e-05, ["dy_mumu_m1500to2500"], 9911614),
  ("DYto2Mu_MLL_200to400_powheg", ["/DYto2Mu_MLL_200to400_powheg"], 1768750, 1, 2.85386502357, 0.0287104871968, ["dy_mumu_m200to400"], 9438078),
  ("DYto2Mu_MLL_2500to4000_powheg", ["/DYto2Mu_MLL_2500to4000_powheg"], 599994, 1, 5.55187803309e-05, 1.6465184272e-06, ["dy_mumu_m2500to4000"], 7280703),
  ("DYto2Mu_MLL_4000to6000_powheg", ["/DYto2Mu_MLL_4000to6000_powheg"], 558000, 1, 1.45399663398e-06, 4.63663371059e-08, ["dy_mumu_m4000to6000"], 2560620),
  ("DYto2Mu_MLL_400to800_powheg", ["/DYto2Mu_MLL_400to800_powheg"], 1795008, 1, 0.251136389091, 0.00248952701464, ["dy_mumu_m400to800"], 6431005),
  ("DYto2Mu_MLL_50to120_powheg", ["/DYto2Mu_MLL_50to120_powheg"], 5742092, 1, 2070.87197099, 6.41736423795, ["dy_mumu_m50to120"], 5855483),
  ("DYto2Mu_MLL_6000_powheg", ["/DYto2Mu_MLL_6000_powheg"], 300000, 1, 3.28409124197e-08, 1.94790398532e-09, ["dy_mumu_m6000toinf"], 9262020),
  ("DYto2Mu_MLL_800to1500_powheg", ["/DYto2Mu_MLL_800to1500_powheg"], 1178762, 1, 0.017871653107, 0.000269781512626, ["dy_mumu_m800to1500"], 5682128),
  ("DYto2Tau_MLL_10to50_powheg", ["/DYto2Tau_MLL_10to50_powheg"], 2726694, 1, 6744, 44.0103421946, ["dy_tautau_m10to50"], 4937323),
  ("DYto2Tau_MLL_120to200_powheg", ["/DYto2Tau_MLL_120to200_powheg"], 2933334, 1, 20.2047670897, 0.122564844506, ["dy_tautau_m120to200"], 9008554),
  ("DYto2Tau_MLL_1500to2500_powheg", ["/DYto2Tau_MLL_1500to2500_powheg"], 1163964, 1, 0.00103683585389, 1.58505393501e-05, ["dy_tautau_m1500to2500"], 9103869),
  ("DYto2Tau_MLL_200to400_powheg", ["/DYto2Tau_MLL_200to400_powheg"], 1786556, 1, 2.85386502357, 0.0284243394718, ["dy_tautau_m200to400"], 6961881),
  ("DYto2Tau_MLL_2500to4000_powheg", ["/DYto2Tau_MLL_2500to4000_powheg"], 599992, 1, 5.55187803309e-05, 1.64652391567e-06, ["dy_tautau_m2500to4000"], 8831391),
  ("DYto2Tau_MLL_4000to6000_powheg", ["/DYto2Tau_MLL_4000to6000_powheg"], 593998, 1, 1.45399663398e-06, 4.35564027237e-08, ["dy_tautau_m4000to6000"], 2770000),
  ("DYto2Tau_MLL_400to800_powheg", ["/DYto2Tau_MLL_400to800_powheg"], 1794884, 1, 0.251136389091, 0.00248969900422, ["dy_tautau_m400to800"], 3787641),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX", ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"], 68706683, 1, 1664.68417309, 0.431128223377, ["dy_tautau_m50toinf_0j"], 5509319),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX", ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"], 55789337, 1, 316.240337878, 0.100864804545, ["dy_tautau_m50toinf_1j"], 7319203),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX", ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"], 87552487, 1, 116.472030231, 0.0236715526531, ["dy_tautau_m50toinf_2j"], 8744175),
  ("DYto2Tau_MLL_50to120_powheg", ["/DYto2Tau_MLL_50to120_powheg"], 5706960, 1, 2070.87197099, 6.45686948075, ["dy_tautau_m50to120"], 4223727),
  ("DYto2Tau_MLL_6000_powheg", ["/DYto2Tau_MLL_6000_powheg"], 294000, 1, 3.28409124197e-08, 1.98765712788e-09, ["dy_tautau_m6000toinf"], 4036035),
  ("DYto2Tau_MLL_800to1500_powheg", ["/DYto2Tau_MLL_800to1500_powheg"], 1142774, 1, 0.017871653107, 0.000278277415645, ["dy_tautau_m800to1500"], 4990905),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay"], 16406657, 0.3848, 3.2759, 0.00136715950715, ["h_ggf_htt"], 6631120),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay"], 159652, 1, 3.2759, 0.36511515421, ["h_ggf_htt"], 7634543),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay"], 18105720, 0.3848, 3.2759, 0.00123886358002, ["h_ggf_htt"], 7355543),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay"], 158922, 1, 3.2759, 0.366792291816, ["h_ggf_htt"], 4729795),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay"], 17266134, 0.3847, 3.2759, 0.00129876716824, ["h_ggf_htt"], 8942784),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"], 159160, 1, 3.2759, 0.366243808746, ["h_ggf_htt"], 3368828),
  ("ST_t_channel_antitop_4f_InclusiveDecays", ["/ST_t_channel_antitop_4f_InclusiveDecays"], 2662016, 1, 75.47, 0.50447224209, ["st_twchannel_tbar_fh"], 8456062),
  ("ST_t_channel_top_4f_InclusiveDecays", ["/ST_t_channel_top_4f_InclusiveDecays"], 5437414, 1, 123.8, 0.405136927223, ["st_twchannel_t_fh"], 6106248),
  ("ST_tW_antitop_2L2Nu", ["/ST_tW_antitop_2L2Nu", "/ST_tW_antitop_2L2Nu_ext1"], 9813596, 1, 3.8, 0.00689015524992, ["st_twchannel_tbar_dl"], 3714936),
  ("ST_tW_antitop_LNu2Q", ["/ST_tW_antitop_LNu2Q", "/ST_tW_antitop_LNu2Q_ext1"], 19038070, 1, 15.9, 0.0148609916867, ["st_twchannel_tbar_sl"], 3918709),
  ("ST_tW_top_2L2Nu", ["/ST_tW_top_2L2Nu", "/ST_tW_top_2L2Nu_ext1"], 9969624, 1, 3.8, 0.00678232198125, ["st_twchannel_t_dl"], 3173010),
  ("ST_tW_top_LNu2Q", ["/ST_tW_top_LNu2Q", "/ST_tW_top_LNu2Q_ext1"], 19299848, 1, 15.8, 0.0145672235346, ["st_twchannel_t_sl"], 8945583),
  ("TTto2L2Nu", ["/TTto2L2Nu", "/TTto2L2Nu_ext1"], 95426668, 1, 98.0438787561, 0.0182820255087, ["tt_dl"], 9726906),
  ("TTto4Q", ["/TTto4Q", "/TTto4Q_ext1"], 208225308, 1, 419.807164414, 0.0358748355583, ["tt_fh"], 3442904),
  ("TTtoLNu2Q", ["/TTtoLNu2Q", "/TTtoLNu2Q_ext1"], 302833852, 1, 405.74895683, 0.0238411158137, ["tt_sl"], 7035163),
  ("VBFHToTauTau_UncorrelatedDecay_Filtered", ["/VBFHToTauTau_UncorrelatedDecay_Filtered"], 12453012, 0.4091, 0.2558, 0.000149530298158, ["h_vbf_htt"], 7518841),
  ("VBFHToTauTau_UncorrelatedDecay_UnFiltered", ["/VBFHToTauTau_UncorrelatedDecay_UnFiltered"], 299664, 1, 0.2558, 0.0151893627529, ["h_vbf_htt"], 6468594),
  ("WminusHToTauTau_UncorrelatedDecay_Filtered", ["/WminusHToTauTau_UncorrelatedDecay_Filtered"], 1248957, 0.3944, 0.03561, 0.000200094420942, ["wh_htt"], 6292268),
  ("WminusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WminusHToTauTau_UncorrelatedDecay_UnFiltered"], 66292, 1, 0.03561, 0.00955838321366, ["wh_htt"], 8781372),
  ("WplusHToTauTau_UncorrelatedDecay_Filtered", ["/WplusHToTauTau_UncorrelatedDecay_Filtered"], 1802553, 0.3743, 0.05575, 0.000205991946783, ["wh_htt"], 7748239),
  ("WplusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WplusHToTauTau_UncorrelatedDecay_UnFiltered"], 64190, 1, 0.05575, 0.0154543620502, ["wh_htt"], 2297394),
  ("WtoLNu_1J_madgraphMLM", ["/WtoLNu_1J_madgraphMLM"], 191075090, 1, 63425.1, 5.90650633424, ["w_lnu_1j"], 6461648),
  ("WtoLNu_2J_madgraphMLM", ["/WtoLNu_2J_madgraphMLM"], 191075090, 1, 63425.1, 5.90650633424, ["w_lnu_2j"], 8622383),
  ("WtoLNu_3J_madgraphMLM", ["/WtoLNu_3J_madgraphMLM"], 191075090, 1, 63425.1, 5.90650633424, ["w_lnu_ge3j"], 9741512),
  ("WtoLNu_4J_madgraphMLM", ["/WtoLNu_4J_madgraphMLM"], 191075090, 1, 63425.1, 5.90650633424, ["w_lnu_ge3j"], 4794660),
  ("WtoLNu_madgraphMLM", ["/WtoLNu_madgraphMLM", "/WtoLNu_madgraphMLM_ext1"], 382150180, 1, 63425.1, 2.95325316712, ["w_lnu"], 7748250),
  ("WW", ["/WW"], 33507000, 1, 122.27052, 0.064932152472, ["ww"], 4810610),
  ("WWW_4F", ["/WWW_4F"], 849916, 1, 0.2328, 0.00487394424861, ["www"], 6958670),
  ("WWZ_4F", ["/WWZ_4F"], 3275962, 1, 0.1851, 0.00100540525195, ["wwz"], 5052833),
  ("WZ", ["/WZ"], 16770000, 1, 41.1474, 0.0436599186404, ["wz"], 4536647),
  ("WZZ", ["/WZZ"], 3251476, 1, 0.06206, 0.000339629030016, ["wzz"], 7103464),
  ("ZHToTauTau_UncorrelatedDecay_Filtered", ["/ZHToTauTau_UncorrelatedDecay_Filtered"], 1803008, 0.3933, 0.0592, 0.000229784952613, ["zh_htt"], 6327436),
  ("ZHToTauTau_UncorrelatedDecay_UnFiltered", ["/ZHToTauTau_UncorrelatedDecay_UnFiltered"], 69949, 1, 0.0592, 0.015059612003, ["zh_htt"], 7920214),
  ("ZZ", ["/ZZ"], 2517000, 1, 19.431, 0.137367983313, ["zz"], 3167509),
  ("ZZZ", ["/ZZZ"], 3201470, 1, 0.01591, 8.84289217141e-05, ["zzz"], 6588648),
]


