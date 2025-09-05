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
  ("GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay",  ["/GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"],    103106,   1,  383586099, "h_ggf_htt"            ),
  ("VBFHto2Tau_UncorrelatedDecay_UnFiltered",                     ["/VBFHto2Tau_UncorrelatedDecay_UnFiltered"],                       199756,   1,  841880829, "h_vbf_htt"            ),
  ("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                74917918,  71, 2676360070, "dy_m10to50"           ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 76989083, 133, 3770998535, "dy_m50toinf_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                 42819115, 162, 1497302255, "dy_m50toinf_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                 23588533, 170, 1212313238, "dy_m50toinf_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    63684562, 149, 3178417364, "dy_m50toinf"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                             35162586,  40,  961141806, "dy_tautau_m50toinf_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                             36023045,  97, 2159151046, "dy_tautau_m50toinf_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                             37570255, 208, 2446290367, "dy_tautau_m50toinf_2j"),
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                   24357456,  70, 4011623041, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      52422350, 131, 2259192852, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   63358614, 174, 3383451082, "tt_sl"                ),
  ("TWminusto2L2Nu",                                              ["/TWminusto2L2Nu"],                                               2478922,   7,  208275232, "st_twchannel_t_dl"    ),
  ("TWminusto4Q",                                                 ["/TWminusto4Q"],                                                  3933816,   8, 3326015714, "st_twchannel_t_fh"    ),
  ("TWminustoLNu2Q",                                              ["/TWminustoLNu2Q"],                                               4943196,  12,  719181931, "st_twchannel_t_sl"    ),
  ("TbarWplusto2L2Nu",                                            ["/TbarWplusto2L2Nu"],                                             2487898,   7, 3918917922, "st_twchannel_tbar_dl" ),
  ("TbarWplusto4Q",                                               ["/TbarWplusto4Q"],                                                3975836,   8, 3760630163, "st_twchannel_tbar_fh" ),
  ("TbarWplustoLNu2Q",                                            ["/TbarWplustoLNu2Q"],                                             5146462,  12, 3475123817, "st_twchannel_tbar_sl" ),
  ("WW",                                                          ["/WW"],                                                          16545000,  18, 2388590455, "ww"                   ),
  ("WWW_4F",                                                      ["/WWW_4F"],                                                        423054,   2, 1386472685, "www"                  ),
  ("WWZ_4F",                                                      ["/WWZ_4F"],                                                       1585526,   5, 2697542704, "wwz"                  ),
  ("WZ",                                                          ["/WZ"],                                                           8379000,   9, 4042228682, "wz"                   ),
  ("WZZ",                                                         ["/WZZ"],                                                          1625116,   5,  587043658, "wzz"                  ),
  ("WminusHto2Tau_UncorrelatedDecay_UnFiltered",                  ["/WminusHto2Tau_UncorrelatedDecay_UnFiltered"],                     28420,   1,  135171825, "wh_htt"               ),
  ("WplusHto2Tau_UncorrelatedDecay_UnFiltered",                   ["/WplusHto2Tau_UncorrelatedDecay_UnFiltered"],                      28316,   1, 2701689366, "wh_htt"               ),
  ("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         64991689,  91, 2516868007, "w_lnu"                ),
  ("ZHto2Tau_UncorrelatedDecay_UnFiltered",                       ["/ZHto2Tau_UncorrelatedDecay_UnFiltered"],                          29949,   1, 4242094042, "zh_htt"               ),
  ("ZZ",                                                          ["/ZZ"],                                                           1254000,   2, 1161952647, "zz"                   ),
  ("ZZZ",                                                         ["/ZZZ"],                                                          1589388,   4,  707067929, "zzz"                  ),
]

def register_all_datasets(cpn, procs):
  add_merged_datasets(dataset_rows, cpn, procs)

register_all_datasets(cpn, procs)

# Each entry: (name, keys, eff(sumw), filter_efficiency, xs_pb, norm_weight, proc_names, rand_id)
datasets = [
  ("DYto2E_MLL_10to50_powheg", ["/DYto2E_MLL_10to50_powheg"], 1353930, 1, 6744, 47.075952228, ["dy_ee_m10to50"], 2160698),
  ("DYto2E_MLL_120to200_powheg", ["/DYto2E_MLL_120to200_powheg"], 1461328, 1, 20.2047670897, 0.130672411508, ["dy_ee_m120to200"], 6247350),
  ("DYto2E_MLL_1500to2500_powheg", ["/DYto2E_MLL_1500to2500_powheg"], 577980, 1, 0.00103683585389, 1.69541085419e-05, ["dy_ee_m1500to2500"], 6512232),
  ("DYto2E_MLL_200to400_powheg", ["/DYto2E_MLL_200to400_powheg"], 863488, 1, 2.85386502357, 0.0312359619795, ["dy_ee_m200to400"], 4543682),
  ("DYto2E_MLL_2500to4000_powheg", ["/DYto2E_MLL_2500to4000_powheg"], 277996, 1, 5.55187803309e-05, 1.88746598119e-06, ["dy_ee_m2500to4000"], 8967597),
  ("DYto2E_MLL_4000to6000_powheg", ["/DYto2E_MLL_4000to6000_powheg"], 300000, 1, 1.45399663398e-06, 4.58057406259e-08, ["dy_ee_m4000to6000"], 3676513),
  ("DYto2E_MLL_400to800_powheg", ["/DYto2E_MLL_400to800_powheg"], 892982, 1, 0.251136389091, 0.00265793712897, ["dy_ee_m400to800"], 9064712),
  ("DYto2E_MLL_50to120_powheg", ["/DYto2E_MLL_50to120_powheg"], 2851770, 1, 2070.87197099, 6.86303979558, ["dy_ee_m50to120"], 5137961),
  ("DYto2E_MLL_6000_powheg", ["/DYto2E_MLL_6000_powheg"], 150000, 1, 3.28409124197e-08, 2.06919642185e-09, ["dy_ee_m6000toinf"], 3401047),
  ("DYto2E_MLL_800to1500_powheg", ["/DYto2E_MLL_800to1500_powheg"], 590856, 1, 0.017871653107, 0.000285864903656, ["dy_ee_m800to1500"], 8901714),
  ("DYto2L_M_10to50_amcatnloFXFX", ["/DYto2L_M_10to50_amcatnloFXFX"], 74917918, 1, 20950, 2.64287176267, ["dy_m10to50"], 2347147),
  ("DYto2L_M_10to50_madgraphMLM", ["/DYto2L_M_10to50_madgraphMLM"], 150291788, 1, 17380, 1.09292984125, ["dy_m10to50"], 2592399),
  ("DYto2L_M_50_0J_amcatnloFXFX", ["/DYto2L_M_50_0J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_0j"], 6690046),
  ("DYto2L_M_50_1J_amcatnloFXFX", ["/DYto2L_M_50_1J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_1j"], 3132543),
  ("DYto2L_M_50_1J_madgraphMLM", ["/DYto2L_M_50_1J_madgraphMLM"], 69398459, 1, 6282.6, 0.855593243072, ["dy_m50toinf_1j"], 8491178),
  ("DYto2L_M_50_2J_amcatnloFXFX", ["/DYto2L_M_50_2J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_2j"], 8063160),
  ("DYto2L_M_50_2J_madgraphMLM", ["/DYto2L_M_50_2J_madgraphMLM"], 69398459, 1, 6282.6, 0.855593243072, ["dy_m50toinf_2j"], 2869724),
  ("DYto2L_M_50_3J_madgraphMLM", ["/DYto2L_M_50_3J_madgraphMLM"], 69398459, 1, 6282.6, 0.855593243072, ["dy_m50toinf_3j"], 4117029),
  ("DYto2L_M_50_4J_madgraphMLM", ["/DYto2L_M_50_4J_madgraphMLM"], 69398459, 1, 6282.6, 0.855593243072, ["dy_m50toinf_4j"], 5622377),
  ("DYto2L_M_50_amcatnloFXFX", ["/DYto2L_M_50_amcatnloFXFX", "/DYto2L_M_50_amcatnloFXFX_ext1"], 127369124, 1, 6282.6, 0.466179327731, ["dy_m50toinf"], 3902858),
  ("DYto2L_M_50_madgraphMLM", ["/DYto2L_M_50_madgraphMLM", "/DYto2L_M_50_madgraphMLM_ext1"], 138796918, 1, 6282.6, 0.427796621536, ["dy_m50toinf"], 7351278),
  ("DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_1j_pt100to200"], 9368032),
  ("DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_2j_pt100to200"], 4864612),
  ("DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_1j_pt200to400"], 2847670),
  ("DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_2j_pt200to400"], 8702112),
  ("DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_1j_pt400to600"], 6987201),
  ("DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_2j_pt400to600"], 7477740),
  ("DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_1j_pt40to100"], 7878585),
  ("DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_2j_pt40to100"], 6225014),
  ("DYto2L_M_50_PTLL_600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_1j_pt600toinf"], 4427777),
  ("DYto2L_M_50_PTLL_600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX"], 63684562, 1, 6282.6, 0.932358655462, ["dy_m50toinf_2j_pt600toinf"], 6558027),
  ("DYto2Mu_MLL_10to50_powheg", ["/DYto2Mu_MLL_10to50_powheg"], 1347608, 1, 6744, 47.2967984755, ["dy_mumu_m10to50"], 8977144),
  ("DYto2Mu_MLL_120to200_powheg", ["/DYto2Mu_MLL_120to200_powheg"], 1480694, 1, 20.2047670897, 0.128963346758, ["dy_mumu_m120to200"], 5040304),
  ("DYto2Mu_MLL_1500to2500_powheg", ["/DYto2Mu_MLL_1500to2500_powheg"], 599982, 1, 0.00103683585389, 1.63323827299e-05, ["dy_mumu_m1500to2500"], 3614898),
  ("DYto2Mu_MLL_200to400_powheg", ["/DYto2Mu_MLL_200to400_powheg"], 887338, 1, 2.85386502357, 0.030396397244, ["dy_mumu_m200to400"], 2322196),
  ("DYto2Mu_MLL_2500to4000_powheg", ["/DYto2Mu_MLL_2500to4000_powheg"], 291000, 1, 5.55187803309e-05, 1.80312025054e-06, ["dy_mumu_m2500to4000"], 8464150),
  ("DYto2Mu_MLL_4000to6000_powheg", ["/DYto2Mu_MLL_4000to6000_powheg"], 294000, 1, 1.45399663398e-06, 4.67405516591e-08, ["dy_mumu_m4000to6000"], 9358232),
  ("DYto2Mu_MLL_400to800_powheg", ["/DYto2Mu_MLL_400to800_powheg"], 890928, 1, 0.251136389091, 0.00266406490009, ["dy_mumu_m400to800"], 9110792),
  ("DYto2Mu_MLL_50to120_powheg", ["/DYto2Mu_MLL_50to120_powheg"], 2794886, 1, 2070.87197099, 7.00272247163, ["dy_mumu_m50to120"], 7084025),
  ("DYto2Mu_MLL_6000_powheg", ["/DYto2Mu_MLL_6000_powheg"], 150000, 1, 3.28409124197e-08, 2.06919642185e-09, ["dy_mumu_m6000toinf"], 7490730),
  ("DYto2Mu_MLL_800to1500_powheg", ["/DYto2Mu_MLL_800to1500_powheg"], 583854, 1, 0.017871653107, 0.000289293202606, ["dy_mumu_m800to1500"], 6235656),
  ("DYto2Tau_MLL_10to50_powheg", ["/DYto2Tau_MLL_10to50_powheg"], 1377334, 1, 6744, 46.2760260039, ["dy_tautau_m10to50"], 4244151),
  ("DYto2Tau_MLL_120to200_powheg", ["/DYto2Tau_MLL_120to200_powheg"], 1484592, 1, 20.2047670897, 0.128624735796, ["dy_tautau_m120to200"], 5256854),
  ("DYto2Tau_MLL_1500to2500_powheg", ["/DYto2Tau_MLL_1500to2500_powheg"], 587970, 1, 0.00103683585389, 1.66660470008e-05, ["dy_tautau_m1500to2500"], 6590560),
  ("DYto2Tau_MLL_200to400_powheg", ["/DYto2Tau_MLL_200to400_powheg"], 896382, 1, 2.85386502357, 0.0300897143603, ["dy_tautau_m200to400"], 3788758),
  ("DYto2Tau_MLL_2500to4000_powheg", ["/DYto2Tau_MLL_2500to4000_powheg"], 290996, 1, 5.55187803309e-05, 1.80314503604e-06, ["dy_tautau_m2500to4000"], 8110595),
  ("DYto2Tau_MLL_4000to6000_powheg", ["/DYto2Tau_MLL_4000to6000_powheg"], 297000, 1, 1.45399663398e-06, 4.62684248746e-08, ["dy_tautau_m4000to6000"], 2968025),
  ("DYto2Tau_MLL_400to800_powheg", ["/DYto2Tau_MLL_400to800_powheg"], 880992, 1, 0.251136389091, 0.00269411074482, ["dy_tautau_m400to800"], 8899821),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX", ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"], 35162586, 1, 1664.68417309, 0.44743381843, ["dy_tautau_m50toinf_0j"], 6387708),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX", ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"], 33432375, 1, 316.240337878, 0.0893979991934, ["dy_tautau_m50toinf_1j"], 4839145),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX", ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"], 36561651, 1, 116.472030231, 0.0301074247909, ["dy_tautau_m50toinf_2j"], 2089501),
  ("DYto2Tau_MLL_50to120_powheg", ["/DYto2Tau_MLL_50to120_powheg"], 2798486, 1, 2070.87197099, 6.99371410036, ["dy_tautau_m50to120"], 8478558),
  ("DYto2Tau_MLL_6000_powheg", ["/DYto2Tau_MLL_6000_powheg"], 150000, 1, 3.28409124197e-08, 2.06919642185e-09, ["dy_tautau_m6000toinf"], 8324966),
  ("DYto2Tau_MLL_800to1500_powheg", ["/DYto2Tau_MLL_800to1500_powheg"], 584898, 1, 0.017871653107, 0.000288776835473, ["dy_tautau_m800to1500"], 4134273),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay"], 9103069, 0.3848, 3.2759, 0.00130874678532, ["h_ggf_htt"], 2038943),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay"], 103696, 1, 3.2759, 0.298570156033, ["h_ggf_htt"], 4556055),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay"], 9115963, 0.3848, 3.2759, 0.00130689563904, ["h_ggf_htt"], 9063819),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay"], 103290, 1, 3.2759, 0.299743739955, ["h_ggf_htt"], 6596849),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay"], 8623785, 0.3847, 3.2759, 0.00138112397714, ["h_ggf_htt"], 6277488),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"], 103106, 1, 3.2759, 0.300278654007, ["h_ggf_htt"], 4577156),
  ("ST_t_channel_antitop_4f_InclusiveDecays", ["/ST_t_channel_antitop_4f_InclusiveDecays"], 1375656, 1, 75.47, 0.518492246608, ["st_twchannel_tbar_fh"], 2591338),
  ("ST_t_channel_top_4f_InclusiveDecays", ["/ST_t_channel_top_4f_InclusiveDecays"], 2719204, 1, 123.8, 0.430285407053, ["st_twchannel_t_fh"], 7590706),
  ("ST_tW_antitop_2L2Nu", ["/ST_tW_antitop_2L2Nu", "/ST_tW_antitop_2L2Nu_ext1"], 4975796, 1, 3.8, 0.00721769943945, ["st_twchannel_tbar_dl"], 2895047),
  ("ST_tW_antitop_LNu2Q", ["/ST_tW_antitop_LNu2Q", "/ST_tW_antitop_LNu2Q_ext1"], 10292924, 1, 15.9, 0.0145994374388, ["st_twchannel_tbar_sl"], 3016023),
  ("ST_tW_top_2L2Nu", ["/ST_tW_top_2L2Nu", "/ST_tW_top_2L2Nu_ext1"], 4957844, 1, 3.8, 0.00724383421503, ["st_twchannel_t_dl"], 8150753),
  ("ST_tW_top_LNu2Q", ["/ST_tW_top_LNu2Q", "/ST_tW_top_LNu2Q_ext1"], 9886392, 1, 15.8, 0.0151041755172, ["st_twchannel_t_sl"], 9156428),
  ("TTto2L2Nu", ["/TTto2L2Nu", "/TTto2L2Nu_ext1"], 48714912, 1, 98.0438787561, 0.0190211304933, ["tt_dl"], 3281921),
  ("TTto4Q", ["/TTto4Q", "/TTto4Q_ext1"], 104844700, 1, 419.807164414, 0.0378426139889, ["tt_fh"], 5663630),
  ("TTtoLNu2Q", ["/TTtoLNu2Q", "/TTtoLNu2Q_ext1"], 152100988, 1, 405.74895683, 0.0252117585916, ["tt_sl"], 8352204),
  ("VBFHToTauTau_UncorrelatedDecay_Filtered", ["/VBFHToTauTau_UncorrelatedDecay_Filtered"], 7048003, 0.4091, 0.2558, 0.000140327149234, ["h_vbf_htt"], 5758897),
  ("VBFHToTauTau_UncorrelatedDecay_UnFiltered", ["/VBFHToTauTau_UncorrelatedDecay_UnFiltered"], 199756, 1, 0.2558, 0.0121025941649, ["h_vbf_htt"], 9353462),
  ("WminusHToTauTau_UncorrelatedDecay_Filtered", ["/WminusHToTauTau_UncorrelatedDecay_Filtered"], 718725, 0.3944, 0.03561, 0.000184681711898, ["wh_htt"], 8245626),
  ("WminusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WminusHToTauTau_UncorrelatedDecay_UnFiltered"], 28420, 1, 0.03561, 0.0118420165376, ["wh_htt"], 5934763),
  ("WplusHToTauTau_UncorrelatedDecay_Filtered", ["/WplusHToTauTau_UncorrelatedDecay_Filtered"], 952493, 0.3743, 0.05575, 0.000207052590911, ["wh_htt"], 8155148),
  ("WplusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WplusHToTauTau_UncorrelatedDecay_UnFiltered"], 28316, 1, 0.05575, 0.0186076158356, ["wh_htt"], 4718628),
  ("WtoLNu_1J_madgraphMLM", ["/WtoLNu_1J_madgraphMLM"], 94639090, 1, 63425.1, 6.33385866348, ["w_lnu_1j"], 7745585),
  ("WtoLNu_2J_madgraphMLM", ["/WtoLNu_2J_madgraphMLM"], 94639090, 1, 63425.1, 6.33385866348, ["w_lnu_2j"], 6846644),
  ("WtoLNu_3J_madgraphMLM", ["/WtoLNu_3J_madgraphMLM"], 94639090, 1, 63425.1, 6.33385866348, ["w_lnu_ge3j"], 3600773),
  ("WtoLNu_4J_madgraphMLM", ["/WtoLNu_4J_madgraphMLM"], 94639090, 1, 63425.1, 6.33385866348, ["w_lnu_ge3j"], 8964533),
  ("WtoLNu_madgraphMLM", ["/WtoLNu_madgraphMLM", "/WtoLNu_madgraphMLM_ext1"], 189278180, 1, 63425.1, 3.16692933174, ["w_lnu"], 9455910),
  ("WW", ["/WW"], 16545000, 1, 122.27052, 0.069844586553, ["ww"], 7360906),
  ("WWW_4F", ["/WWW_4F"], 423054, 1, 0.2328, 0.0052007374945, ["www"], 3179315),
  ("WWZ_4F", ["/WWZ_4F"], 1585526, 1, 0.1851, 0.00110334368531, ["wwz"], 3571402),
  ("WZ", ["/WZ"], 8379000, 1, 41.1474, 0.0464117528822, ["wz"], 5510474),
  ("WZZ", ["/WZZ"], 1625116, 1, 0.06206, 0.000360915196208, ["wzz"], 9411219),
  ("ZHToTauTau_UncorrelatedDecay_Filtered", ["/ZHToTauTau_UncorrelatedDecay_Filtered"], 1007812, 0.3933, 0.0592, 0.000218345321707, ["zh_htt"], 3721829),
  ("ZHToTauTau_UncorrelatedDecay_UnFiltered", ["/ZHToTauTau_UncorrelatedDecay_UnFiltered"], 29949, 1, 0.0592, 0.0186817322782, ["zh_htt"], 2626154),
  ("ZZ", ["/ZZ"], 1254000, 1, 19.431, 0.146445279904, ["zz"], 9460037),
  ("ZZZ", ["/ZZZ"], 1589388, 1, 0.01591, 9.46058545805e-05, ["zzz"], 8594335),
]

