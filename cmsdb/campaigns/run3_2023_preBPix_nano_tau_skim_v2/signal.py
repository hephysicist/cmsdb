# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2 import campaign_run3_2022_preEE_nano_tau_skim_v2 as cpn

cpn.add_dataset(
    name='glugluhto2tau_uncorrelateddecay_unfiltered',
    id=11100,
    is_data=True,
    processes=[procs.data_glugluhto2tau],
    keys=['/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered'],
    n_files=1,
    n_events=310379,
)


# cpn.add_dataset(
#     name="signal",
#     id=11100,
#     processes=[procs.h_ggf_tautau],
#     keys=['/GluGluHToTauTau_M125'],
#     n_files=1,
#     n_events=295692,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )
# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-1000_2HDM-II'],
#     id=69,
#     processes=[procs.process_69],
#     keys=['GluGluHto2Tau_M-1000_2HDM-II'],
#     n_files=1,
#     n_events=446596,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-100_2HDM-II'],
#     id=70,
#     processes=[procs.h_ggf_tautau],
#     keys=['/GluGluHto2Tau_M-100_2HDM-II'],
#     n_files=1,
#     n_events=449942,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-105_2HDM-II'],
#     id=71,
#     processes=[procs.process_71],
#     keys=['GluGluHto2Tau_M-105_2HDM-II'],
#     n_files=1,
#     n_events=448536,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-1100_2HDM-II'],
#     id=72,
#     processes=[procs.process_72],
#     keys=['GluGluHto2Tau_M-1100_2HDM-II'],
#     n_files=1,
#     n_events=447987,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-110_2HDM-II'],
#     id=73,
#     processes=[procs.process_73],
#     keys=['GluGluHto2Tau_M-110_2HDM-II'],
#     n_files=1,
#     n_events=449958,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-115_2HDM-II'],
#     id=74,
#     processes=[procs.process_74],
#     keys=['GluGluHto2Tau_M-115_2HDM-II'],
#     n_files=1,
#     n_events=447160,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-1200_2HDM-II'],
#     id=75,
#     processes=[procs.h_ggf_tautau],
#     keys=['/GluGluHto2Tau_M-1200_2HDM-II'],
#     n_files=1,
#     n_events=447983,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-120_2HDM-II'],
#     id=76,
#     processes=[procs.process_76],
#     keys=['GluGluHto2Tau_M-120_2HDM-II'],
#     n_files=1,
#     n_events=449175,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-125_2HDM-II'],
#     id=77,
#     processes=[procs.h_ggf_tautau],
#     keys=['GluGluHto2Tau_M-125_2HDM-II'],
#     n_files=1,
#     n_events=447825,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-130_2HDM-II'],
#     id=78,
#     processes=[procs.process_78],
#     keys=['GluGluHto2Tau_M-130_2HDM-II'],
#     n_files=1,
#     n_events=449968,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-135_2HDM-II'],
#     id=79,
#     processes=[procs.process_79],
#     keys=['GluGluHto2Tau_M-135_2HDM-II'],
#     n_files=1,
#     n_events=449970,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-1400_2HDM-II'],
#     id=80,
#     processes=[procs.process_80],
#     keys=['GluGluHto2Tau_M-1400_2HDM-II'],
#     n_files=1,
#     n_events=446050,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-140_2HDM-II'],
#     id=81,
#     processes=[procs.process_81],
#     keys=['GluGluHto2Tau_M-140_2HDM-II'],
#     n_files=1,
#     n_events=449962,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-1600_2HDM-II'],
#     id=82,
#     processes=[procs.process_82],
#     keys=['GluGluHto2Tau_M-1600_2HDM-II'],
#     n_files=1,
#     n_events=448004,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-160_2HDM-II'],
#     id=83,
#     processes=[procs.process_83],
#     keys=['GluGluHto2Tau_M-160_2HDM-II'],
#     n_files=1,
#     n_events=449972,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-1800_2HDM-II'],
#     id=84,
#     processes=[procs.process_84],
#     keys=['GluGluHto2Tau_M-1800_2HDM-II'],
#     n_files=1,
#     n_events=448684,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-180_2HDM-II'],
#     id=85,
#     processes=[procs.process_85],
#     keys=['GluGluHto2Tau_M-180_2HDM-II'],
#     n_files=1,
#     n_events=449279,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-2000_2HDM-II'],
#     id=86,
#     processes=[procs.process_86],
#     keys=['GluGluHto2Tau_M-2000_2HDM-II'],
#     n_files=1,
#     n_events=446753,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-200_2HDM-II'],
#     id=87,
#     processes=[procs.process_87],
#     keys=['GluGluHto2Tau_M-200_2HDM-II'],
#     n_files=1,
#     n_events=448584,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-2300_2HDM-II'],
#     id=88,
#     processes=[procs.process_88],
#     keys=['GluGluHto2Tau_M-2300_2HDM-II'],
#     n_files=1,
#     n_events=449309,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-250_2HDM-II'],
#     id=89,
#     processes=[procs.process_89],
#     keys=['GluGluHto2Tau_M-250_2HDM-II'],
#     n_files=1,
#     n_events=448594,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-2600_2HDM-II'],
#     id=90,
#     processes=[procs.process_90],
#     keys=['GluGluHto2Tau_M-2600_2HDM-II'],
#     n_files=1,
#     n_events=449332,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-2900_2HDM-II'],
#     id=91,
#     processes=[procs.process_91],
#     keys=['GluGluHto2Tau_M-2900_2HDM-II'],
#     n_files=1,
#     n_events=446066,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-300_2HDM-II'],
#     id=92,
#     processes=[procs.process_92],
#     keys=['GluGluHto2Tau_M-300_2HDM-II'],
#     n_files=1,
#     n_events=448598,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-3200_2HDM-II'],
#     id=93,
#     processes=[procs.process_93],
#     keys=['GluGluHto2Tau_M-3200_2HDM-II'],
#     n_files=1,
#     n_events=449932,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-3500_2HDM-II'],
#     id=94,
#     processes=[procs.process_94],
#     keys=['GluGluHto2Tau_M-3500_2HDM-II'],
#     n_files=1,
#     n_events=449908,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-350_2HDM-II'],
#     id=95,
#     processes=[procs.process_95],
#     keys=['GluGluHto2Tau_M-350_2HDM-II'],
#     n_files=1,
#     n_events=447891,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-400_2HDM-II'],
#     id=96,
#     processes=[procs.process_96],
#     keys=['GluGluHto2Tau_M-400_2HDM-II'],
#     n_files=1,
#     n_events=449301,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-450_2HDM-II'],
#     id=97,
#     processes=[procs.process_97],
#     keys=['GluGluHto2Tau_M-450_2HDM-II'],
#     n_files=1,
#     n_events=449992,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-500_2HDM-II'],
#     id=98,
#     processes=[procs.process_98],
#     keys=['GluGluHto2Tau_M-500_2HDM-II'],
#     n_files=1,
#     n_events=449988,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-600_2HDM-II'],
#     id=99,
#     processes=[procs.process_99],
#     keys=['GluGluHto2Tau_M-600_2HDM-II'],
#     n_files=1,
#     n_events=449300,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-60_2HDM-II'],
#     id=100,
#     processes=[procs.process_100],
#     keys=['GluGluHto2Tau_M-60_2HDM-II'],
#     n_files=1,
#     n_events=447803,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-65_2HDM-II'],
#     id=101,
#     processes=[procs.process_101],
#     keys=['GluGluHto2Tau_M-65_2HDM-II'],
#     n_files=1,
#     n_events=448504,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-700_2HDM-II'],
#     id=102,
#     processes=[procs.process_102],
#     keys=['GluGluHto2Tau_M-700_2HDM-II'],
#     n_files=1,
#     n_events=449994,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-70_2HDM-II'],
#     id=103,
#     processes=[procs.process_103],
#     keys=['GluGluHto2Tau_M-70_2HDM-II'],
#     n_files=1,
#     n_events=448500,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-75_2HDM-II'],
#     id=104,
#     processes=[procs.process_104],
#     keys=['GluGluHto2Tau_M-75_2HDM-II'],
#     n_files=1,
#     n_events=449940,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-800_2HDM-II'],
#     id=105,
#     processes=[procs.process_105],
#     keys=['GluGluHto2Tau_M-800_2HDM-II'],
#     n_files=1,
#     n_events=448646,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-80_2HDM-II'],
#     id=106,
#     processes=[procs.process_106],
#     keys=['GluGluHto2Tau_M-80_2HDM-II'],
#     n_files=1,
#     n_events=448532,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-85_2HDM-II'],
#     id=107,
#     processes=[procs.process_107],
#     keys=['GluGluHto2Tau_M-85_2HDM-II'],
#     n_files=1,
#     n_events=448516,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-900_2HDM-II'],
#     id=108,
#     processes=[procs.process_108],
#     keys=['GluGluHto2Tau_M-900_2HDM-II'],
#     n_files=1,
#     n_events=448622,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-90_2HDM-II'],
#     id=109,
#     processes=[procs.process_109],
#     keys=['GluGluHto2Tau_M-90_2HDM-II'],
#     n_files=1,
#     n_events=448516,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['GluGluHto2Tau_M-95_2HDM-II'],
#     id=110,
#     processes=[procs.process_110],
#     keys=['GluGluHto2Tau_M-95_2HDM-II'],
#     n_files=1,
#     n_events=447820,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )
# cpn.add_dataset(
#     name=['VBFHToTauTau_M125'],
#     id=370,
#     processes=[procs.process_370],
#     keys=['VBFHToTauTau_M125'],
#     n_files=1,
#     n_events=298955,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )
