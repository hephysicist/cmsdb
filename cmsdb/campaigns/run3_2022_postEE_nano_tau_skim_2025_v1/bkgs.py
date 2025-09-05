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
  ("GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay",  ["/GluGluHto2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"],     445092,   1, 1221936734, "h_ggf_htt"            ),
  ("VBFHto2Tau_UncorrelatedDecay_UnFiltered",                     ["/VBFHto2Tau_UncorrelatedDecay_UnFiltered"],                        396754,   1, 3201507122, "h_vbf_htt"            ),
  ("DYto2L_M_10to50_amcatnloFXFX",                                ["/DYto2L_M_10to50_amcatnloFXFX"],                                168535477, 139, 1895014020, "dy_m10to50"           ),
  ("DYto2L_M_50_0J_amcatnloFXFX",                                 ["/DYto2L_M_50_0J_amcatnloFXFX"],                                 275262495, 425, 1078589252, "dy_m50toinf_0j"       ),
  ("DYto2L_M_50_1J_amcatnloFXFX",                                 ["/DYto2L_M_50_1J_amcatnloFXFX"],                                 151393596, 539, 4189203628, "dy_m50toinf_1j"       ),
  ("DYto2L_M_50_2J_amcatnloFXFX",                                 ["/DYto2L_M_50_2J_amcatnloFXFX"],                                  84618132, 560, 3905898197, "dy_m50toinf_2j"       ),
  ("DYto2L_M_50_amcatnloFXFX",                                    ["/DYto2L_M_50_amcatnloFXFX"],                                    143381450, 317, 4072667752, "dy_m50toinf"          ),
  ("DYto2L_M_50_amcatnloFXFX_ext1",                               ["/DYto2L_M_50_amcatnloFXFX_ext1"],                               240058361, 554, 2565332299, "dy_m50toinf"          ),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"],                             100595369, 109, 3729619275, "dy_tautau_m50toinf_0j"),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"],                              87692299, 228, 1740022435, "dy_tautau_m50toinf_1j"),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX",                             ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"],                             112976268, 595, 1993066714, "dy_tautau_m50toinf_2j"),
  ("TTto2L2Nu",                                                   ["/TTto2L2Nu"],                                                    83445808, 238,  481041747, "tt_dl"                ),
  ("TTto2L2Nu_ext1",                                              ["/TTto2L2Nu_ext1"],                                               84236946, 233, 3676565014, "tt_dl"                ),
  ("TTto4Q",                                                      ["/TTto4Q"],                                                      178011279, 466,  954044713, "tt_fh"                ),
  ("TTto4Q_ext1",                                                 ["/TTto4Q_ext1"],                                                 185398097, 458, 1796602938, "tt_fh"                ),
  ("TTtoLNu2Q",                                                   ["/TTtoLNu2Q"],                                                   264626088, 712,  974897688, "tt_sl"                ),
  ("TTtoLNu2Q_ext1",                                              ["/TTtoLNu2Q_ext1"],                                              273257101, 739, 2314749232, "tt_sl"                ),
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
  ("WW",                                                          ["/WW"],                                                           53112080,  53,  443727516, "ww"                   ),
  ("WWW_4F",                                                      ["/WWW_4F"],                                                        1345746,   4, 3973511632, "www"                  ),
  ("WWZ_4F",                                                      ["/WWZ_4F"],                                                        5249916,  14,  515645709, "wwz"                  ),
  ("WZ",                                                          ["/WZ"],                                                           26722782,  26, 1690550817, "wz"                   ),
  ("WZZ",                                                         ["/WZZ"],                                                           5229208,  14,  363955451, "wzz"                  ),
  ("WminusHto2Tau_UncorrelatedDecay_UnFiltered",                  ["/WminusHto2Tau_UncorrelatedDecay_UnFiltered"],                      63910,   1, 2986674282, "wh_htt"               ),
  ("WplusHto2Tau_UncorrelatedDecay_UnFiltered",                   ["/WplusHto2Tau_UncorrelatedDecay_UnFiltered"],                       66154,   1, 2058886370, "wh_htt"               ),
  ("WtoLNu_amcatnloFXFX",                                         ["/WtoLNu_amcatnloFXFX"],                                         195475400, 261, 1538031583, "w_lnu"                ),
  ("ZHto2Tau_UncorrelatedDecay_UnFiltered",                       ["/ZHto2Tau_UncorrelatedDecay_UnFiltered"],                           69650,   1, 1072228519, "zh_htt"               ),
  ("ZZ",                                                          ["/ZZ"],                                                            4043040,   4, 3513629804, "zz"                   ),
  ("ZZZ",                                                         ["/ZZZ"],                                                           5063206,  11,  493426600, "zzz"                  ),
]

def register_all_datasets(cpn, procs):
  add_merged_datasets(dataset_rows, cpn, procs)

register_all_datasets(cpn, procs)

# # Each entry: (name, keys, eff(sumw), filter_efficiency, xs_pb, norm_weight, proc_names, rand_id)
datasets = [
  ("DYto2E_MLL_10to50_powheg", ["/DYto2E_MLL_10to50_powheg"], 4764222, 1, 6744, 37.755155994, ["dy_ee_m10to50"], 6796551),
  ("DYto2E_MLL_120to200_powheg", ["/DYto2E_MLL_120to200_powheg"], 5184446, 1, 20.2047670897, 0.103944661857, ["dy_ee_m120to200"], 4833479),
  ("DYto2E_MLL_1500to2500_powheg", ["/DYto2E_MLL_1500to2500_powheg"], 2053882, 1, 0.00103683585389, 1.34643445164e-05, ["dy_ee_m1500to2500"], 2889932),
  ("DYto2E_MLL_200to400_powheg", ["/DYto2E_MLL_200to400_powheg"], 3134891, 1, 2.85386502357, 0.0242807267459, ["dy_ee_m200to400"], 8916126),
  ("DYto2E_MLL_2500to4000_powheg", ["/DYto2E_MLL_2500to4000_powheg"], 986486, 1, 5.55187803309e-05, 1.50106565461e-06, ["dy_ee_m2500to4000"], 4683160),
  ("DYto2E_MLL_4000to6000_powheg", ["/DYto2E_MLL_4000to6000_powheg"], 1027654, 1, 1.45399663398e-06, 3.77369834814e-08, ["dy_ee_m4000to6000"], 4010344),
  ("DYto2E_MLL_400to800_powheg", ["/DYto2E_MLL_400to800_powheg"], 2972468, 1, 0.251136389091, 0.00225342524425, ["dy_ee_m400to800"], 2815323),
  ("DYto2E_MLL_50to120_powheg", ["/DYto2E_MLL_50to120_powheg"], 10192192, 1, 2070.87197099, 5.41921462515, ["dy_ee_m50to120"], 9102043),
  ("DYto2E_MLL_6000_powheg", ["/DYto2E_MLL_6000_powheg"], 525000, 1, 3.28409124197e-08, 1.66842469292e-09, ["dy_ee_m6000toinf"], 4774705),
  ("DYto2E_MLL_800to1500_powheg", ["/DYto2E_MLL_800to1500_powheg"], 2003864, 1, 0.017871653107, 0.000237874112302, ["dy_ee_m800to1500"], 7253508),
  ("DYto2L_M_10to50_amcatnloFXFX", ["/DYto2L_M_10to50_amcatnloFXFX"], 168535477, 1, 20950, 3.31545692899, ["dy_m10to50"], 8397046),
  ("DYto2L_M_10to50_madgraphMLM", ["/DYto2L_M_10to50_madgraphMLM"], 520125461, 1, 17380, 0.891235251412, ["dy_m10to50"], 2883396),
  ("DYto2L_M_50_0J_amcatnloFXFX", ["/DYto2L_M_50_0J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_0j"], 7253877),
  ("DYto2L_M_50_1J_amcatnloFXFX", ["/DYto2L_M_50_1J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_1j"], 7761939),
  ("DYto2L_M_50_1J_madgraphMLM", ["/DYto2L_M_50_1J_madgraphMLM"], 494841164, 1, 6282.6, 0.338629108915, ["dy_m50toinf_1j"], 7007618),
  ("DYto2L_M_50_2J_amcatnloFXFX", ["/DYto2L_M_50_2J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_2j"], 6190865),
  ("DYto2L_M_50_2J_madgraphMLM", ["/DYto2L_M_50_2J_madgraphMLM"], 494841164, 1, 6282.6, 0.338629108915, ["dy_m50toinf_2j"], 7443403),
  ("DYto2L_M_50_3J_madgraphMLM", ["/DYto2L_M_50_3J_madgraphMLM"], 494841164, 1, 6282.6, 0.338629108915, ["dy_m50toinf_3j"], 4387517),
  ("DYto2L_M_50_4J_madgraphMLM", ["/DYto2L_M_50_4J_madgraphMLM"], 494841164, 1, 6282.6, 0.338629108915, ["dy_m50toinf_4j"], 5290249),
  ("DYto2L_M_50_amcatnloFXFX", ["/DYto2L_M_50_amcatnloFXFX", "/DYto2L_M_50_amcatnloFXFX_ext1"], 766880474, 1, 6282.6, 0.218505527395, ["dy_m50toinf"], 4498229),
  ("DYto2L_M_50_madgraphMLM", ["/DYto2L_M_50_madgraphMLM", "/DYto2L_M_50_madgraphMLM_ext1"], 989682328, 1, 6282.6, 0.169314554458, ["dy_m50toinf"], 9585537),
  ("DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_1J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_1j_pt100to200"], 5420794),
  ("DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_100to200_2J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_2j_pt100to200"], 7050646),
  ("DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_1J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_1j_pt200to400"], 6796862),
  ("DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_200to400_2J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_2j_pt200to400"], 3047427),
  ("DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_1J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_1j_pt400to600"], 5932100),
  ("DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_400to600_2J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_2j_pt400to600"], 4861352),
  ("DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_1J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_1j_pt40to100"], 6898123),
  ("DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_40to100_2J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_2j_pt40to100"], 7398792),
  ("DYto2L_M_50_PTLL_600_1J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_1J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_1j_pt600toinf"], 5873971),
  ("DYto2L_M_50_PTLL_600_2J_amcatnloFXFX", ["/DYto2L_M_50_PTLL_600_2J_amcatnloFXFX"], 383440237, 1, 6282.6, 0.437011054789, ["dy_m50toinf_2j_pt600toinf"], 8474320),
  ("DYto2Mu_MLL_10to50_powheg", ["/DYto2Mu_MLL_10to50_powheg"], 4597120, 1, 6744, 39.1275287136, ["dy_mumu_m10to50"], 6850368),
  ("DYto2Mu_MLL_120to200_powheg", ["/DYto2Mu_MLL_120to200_powheg"], 4859532, 1, 20.2047670897, 0.110894523667, ["dy_mumu_m120to200"], 4107527),
  ("DYto2Mu_MLL_1500to2500_powheg", ["/DYto2Mu_MLL_1500to2500_powheg"], 2006612, 1, 0.00103683585389, 1.37815256981e-05, ["dy_mumu_m1500to2500"], 5017452),
  ("DYto2Mu_MLL_200to400_powheg", ["/DYto2Mu_MLL_200to400_powheg"], 3038276, 1, 2.85386502357, 0.0250528364602, ["dy_mumu_m200to400"], 4234363),
  ("DYto2Mu_MLL_2500to4000_powheg", ["/DYto2Mu_MLL_2500to4000_powheg"], 1000170, 1, 5.55187803309e-05, 1.4805285635e-06, ["dy_mumu_m2500to4000"], 3005848),
  ("DYto2Mu_MLL_4000to6000_powheg", ["/DYto2Mu_MLL_4000to6000_powheg"], 994896, 1, 1.45399663398e-06, 3.89795134593e-08, ["dy_mumu_m4000to6000"], 6012591),
  ("DYto2Mu_MLL_400to800_powheg", ["/DYto2Mu_MLL_400to800_powheg"], 2927264, 1, 0.251136389091, 0.00228822355241, ["dy_mumu_m400to800"], 7399608),
  ("DYto2Mu_MLL_50to120_powheg", ["/DYto2Mu_MLL_50to120_powheg"], 9669500, 1, 2070.87197099, 5.7121542943, ["dy_mumu_m50to120"], 2548203),
  ("DYto2Mu_MLL_6000_powheg", ["/DYto2Mu_MLL_6000_powheg"], 503888, 1, 3.28409124197e-08, 1.73832868372e-09, ["dy_mumu_m6000toinf"], 8983127),
  ("DYto2Mu_MLL_800to1500_powheg", ["/DYto2Mu_MLL_800to1500_powheg"], 2088078, 1, 0.017871653107, 0.000228280442673, ["dy_mumu_m800to1500"], 2184627),
  ("DYto2Tau_MLL_10to50_powheg", ["/DYto2Tau_MLL_10to50_powheg"], 4815253, 1, 6744, 37.3550350937, ["dy_tautau_m10to50"], 3137851),
  ("DYto2Tau_MLL_120to200_powheg", ["/DYto2Tau_MLL_120to200_powheg"], 5194901, 1, 20.2047670897, 0.103735467988, ["dy_tautau_m120to200"], 5205379),
  ("DYto2Tau_MLL_1500to2500_powheg", ["/DYto2Tau_MLL_1500to2500_powheg"], 1995673, 1, 0.00103683585389, 1.38570671869e-05, ["dy_tautau_m1500to2500"], 5886395),
  ("DYto2Tau_MLL_200to400_powheg", ["/DYto2Tau_MLL_200to400_powheg"], 3009278, 1, 2.85386502357, 0.0252942505641, ["dy_tautau_m200to400"], 5691075),
  ("DYto2Tau_MLL_2500to4000_powheg", ["/DYto2Tau_MLL_2500to4000_powheg"], 1049992, 1, 5.55187803309e-05, 1.41027765293e-06, ["dy_tautau_m2500to4000"], 7499225),
  ("DYto2Tau_MLL_4000to6000_powheg", ["/DYto2Tau_MLL_4000to6000_powheg"], 1047456, 1, 1.45399663398e-06, 3.70235714174e-08, ["dy_tautau_m4000to6000"], 2583504),
  ("DYto2Tau_MLL_400to800_powheg", ["/DYto2Tau_MLL_400to800_powheg"], 3106940, 1, 0.251136389091, 0.00215589436195, ["dy_tautau_m400to800"], 2024719),
  ("DYto2Tau_MLL_50_0J_amcatnloFXFX", ["/DYto2Tau_MLL_50_0J_amcatnloFXFX"], 100595369, 1, 1664.68417309, 0.441371777854, ["dy_tautau_m50toinf_0j"], 4419049),
  ("DYto2Tau_MLL_50_1J_amcatnloFXFX", ["/DYto2Tau_MLL_50_1J_amcatnloFXFX"], 86891040, 1, 316.240337878, 0.0970717742563, ["dy_tautau_m50toinf_1j"], 2255149),
  ("DYto2Tau_MLL_50_2J_amcatnloFXFX", ["/DYto2Tau_MLL_50_2J_amcatnloFXFX"], 107261589, 1, 116.472030231, 0.0289619711742, ["dy_tautau_m50toinf_2j"], 6337789),
  ("DYto2Tau_MLL_50to120_powheg", ["/DYto2Tau_MLL_50to120_powheg"], 9961938, 1, 2070.87197099, 5.54447096024, ["dy_tautau_m50to120"], 3696297),
  ("DYto2Tau_MLL_6000_powheg", ["/DYto2Tau_MLL_6000_powheg"], 523113, 1, 3.28409124197e-08, 1.67444311991e-09, ["dy_tautau_m6000toinf"], 4342131),
  ("DYto2Tau_MLL_800to1500_powheg", ["/DYto2Tau_MLL_800to1500_powheg"], 2078006, 1, 0.017871653107, 0.000229386907533, ["dy_tautau_m800to1500"], 3545402),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay"], 21495773, 0.3848, 3.2759, 0.0015640957279, ["h_ggf_htt"], 7899113),
  ("GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_UnFiltered_ProdAndDecay"], 448150, 1, 3.2759, 0.194965574093, ["h_ggf_htt"], 9241663),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay"], 20689379, 0.3848, 3.2759, 0.00162505828315, ["h_ggf_htt"], 2232291),
  ("GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_MM_UnFiltered_ProdAndDecay"], 441570, 1, 3.2759, 0.197870829155, ["h_ggf_htt"], 9098251),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay"], 19599725, 0.3847, 3.2759, 0.00171495821166, ["h_ggf_htt"], 5830906),
  ("GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay", ["/GluGluHTo2Tau_UncorrelatedDecay_SM_UnFiltered_ProdAndDecay"], 445092, 1, 3.2759, 0.196305083061, ["h_ggf_htt"], 4860650),
  ("ST_t_channel_antitop_4f_InclusiveDecays", ["/ST_t_channel_antitop_4f_InclusiveDecays"], 4794814, 1, 75.47, 0.419810486705, ["st_twchannel_tbar_fh"], 9352674),
  ("ST_t_channel_top_4f_InclusiveDecays", ["/ST_t_channel_top_4f_InclusiveDecays"], 9368799, 1, 123.8, 0.352441808176, ["st_twchannel_t_fh"], 3486129),
  ("ST_tW_antitop_2L2Nu", ["/ST_tW_antitop_2L2Nu", "/ST_tW_antitop_2L2Nu_ext1"], 33564406, 1, 3.8, 0.00301964110433, ["st_twchannel_tbar_dl"], 4106302),
  ("ST_tW_antitop_LNu2Q", ["/ST_tW_antitop_LNu2Q", "/ST_tW_antitop_LNu2Q_ext1"], 67514018, 1, 15.9, 0.00628136263494, ["st_twchannel_tbar_sl"], 2944794),
  ("ST_tW_top_2L2Nu", ["/ST_tW_top_2L2Nu", "/ST_tW_top_2L2Nu_ext1"], 33150676, 1, 3.8, 0.00305732709644, ["st_twchannel_t_dl"], 3445465),
  ("ST_tW_top_LNu2Q", ["/ST_tW_top_LNu2Q", "/ST_tW_top_LNu2Q_ext1"], 65023616, 1, 15.8, 0.0064809201014, ["st_twchannel_t_sl"], 3061303),
  ("TTto2L2Nu", ["/TTto2L2Nu", "/TTto2L2Nu_ext1"], 335365592, 1, 98.0438787561, 0.0077974514482, ["tt_dl"], 5946967),
  ("TTto4Q", ["/TTto4Q", "/TTto4Q_ext1"], 726818832, 1, 419.807164414, 0.0154054494107, ["tt_fh"], 3730217),
  ("TTtoLNu2Q", ["/TTtoLNu2Q", "/TTtoLNu2Q_ext1"], 1075766378, 1, 405.74895683, 0.010059818445, ["tt_sl"], 9746087),
  ("VBFHToTauTau_UncorrelatedDecay_Filtered", ["/VBFHToTauTau_UncorrelatedDecay_Filtered"], 14552639, 0.4091, 0.2558, 0.000191795741915, ["h_vbf_htt"], 7583829),
  ("VBFHToTauTau_UncorrelatedDecay_UnFiltered", ["/VBFHToTauTau_UncorrelatedDecay_UnFiltered"], 396754, 1, 0.2558, 0.0171960984892, ["h_vbf_htt"], 4736960),
  ("WminusHToTauTau_UncorrelatedDecay_Filtered", ["/WminusHToTauTau_UncorrelatedDecay_Filtered"], 1480135, 0.3944, 0.03561, 0.000253080246783, ["wh_htt"], 3347517),
  ("WminusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WminusHToTauTau_UncorrelatedDecay_UnFiltered"], 63910, 1, 0.03561, 0.0148611991394, ["wh_htt"], 9878203),
  ("WplusHToTauTau_UncorrelatedDecay_Filtered", ["/WplusHToTauTau_UncorrelatedDecay_Filtered"], 2025321, 0.3743, 0.05575, 0.000274803038645, ["wh_htt"], 6460876),
  ("WplusHToTauTau_UncorrelatedDecay_UnFiltered", ["/WplusHToTauTau_UncorrelatedDecay_UnFiltered"], 66154, 1, 0.05575, 0.0224770576987, ["wh_htt"], 2287206),
  ("WtoLNu_1J_madgraphMLM", ["/WtoLNu_1J_madgraphMLM"], 683448011, 1, 63425.1, 2.47517764694, ["w_lnu_1j"], 3499368),
  ("WtoLNu_2J_madgraphMLM", ["/WtoLNu_2J_madgraphMLM"], 683448011, 1, 63425.1, 2.47517764694, ["w_lnu_2j"], 5580405),
  ("WtoLNu_3J_madgraphMLM", ["/WtoLNu_3J_madgraphMLM"], 683448011, 1, 63425.1, 2.47517764694, ["w_lnu_ge3j"], 2544423),
  ("WtoLNu_4J_madgraphMLM", ["/WtoLNu_4J_madgraphMLM"], 683448011, 1, 63425.1, 2.47517764694, ["w_lnu_ge3j"], 6499767),
  ("WtoLNu_madgraphMLM", ["/WtoLNu_madgraphMLM", "/WtoLNu_madgraphMLM_ext1"], 1366896022, 1, 63425.1, 1.23758882347, ["w_lnu"], 9750473),
  ("WW", ["/WW"], 53112080, 1, 122.27052, 0.0614015235006, ["ww"], 5571300),
  ("WWW_4F", ["/WWW_4F"], 1345746, 1, 0.2328, 0.00461392548074, ["www"], 4542621),
  ("WWZ_4F", ["/WWZ_4F"], 5249916, 1, 0.1851, 0.000940382983271, ["wwz"], 4772869),
  ("WZ", ["/WZ"], 26722782, 1, 41.1474, 0.0410687445858, ["wz"], 9795625),
  ("WZZ", ["/WZZ"], 5229208, 1, 0.06206, 0.0003165385087, ["wzz"], 4295994),
  ("ZHToTauTau_UncorrelatedDecay_Filtered", ["/ZHToTauTau_UncorrelatedDecay_Filtered"], 1863291, 0.3933, 0.0592, 0.000333284920558, ["zh_htt"], 4782805),
  ("ZHToTauTau_UncorrelatedDecay_UnFiltered", ["/ZHToTauTau_UncorrelatedDecay_UnFiltered"], 69650, 1, 0.0592, 0.0226699876525, ["zh_htt"], 5655544),
  ("ZZ", ["/ZZ"], 4043040, 1, 19.431, 0.128185178158, ["zz"], 6022263),
  ("ZZZ", ["/ZZZ"], 5063206, 1, 0.01591, 8.38098917958e-05, ["zzz"], 3462972),
]
