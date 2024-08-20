# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v12 import campaign_run3_2022_preEE_nano_tau_v12 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name='dy_incl', #DYto2L_M-50
    id=2212016,
    is_data=False,
    processes=[procs.dy_lep],
    keys=['/DYto2L_M-50_madgraphMLM', '/DYto2L_M-50_madgraphMLM_ext1'],
    n_files=32+31,
    n_events=73914947+71371699,
    aux=None
)

# cpn.add_dataset(
#     name='dy_lep_m10to50',
#     id=2212017,
#     is_data=False,
#     processes=[procs.dy_lep],
#     keys=['/DYto2L_M-10to50_amcatnloFXFX'],
#     n_files=15,
#     n_events=52629903,
#     aux=None
# )
# cpn.add_dataset(
#     name='dy_lep_m10to50',
#     id=2212017,
#     is_data=False,
#     processes=[procs.dy_lep_m10to50],
#     keys=['/DYto2L_M-10to50_madgraphMLM'],
#     n_files=32,
#     n_events=163769744,
#     aux=None,
# )
cpn.add_dataset(
    name='dy_lep_0j',
    id=2212018,
    is_data=False,
    processes=[procs.dy_lep],
    keys=['/DYto2L_M-50_0J_amcatnloFXFX'],
    n_files=42,
    n_events=83840818,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_1j',
    id=2212019,
    is_data=False,
    processes=[procs.dy_lep],
    keys=['/DYto2L_M-50_1J_amcatnloFXFX'],
    n_files=54,
    n_events=46809421,
    aux=None
)

cpn.add_dataset(
    name='dy_lep_2j',
    id=22120110,
    is_data=False,
    processes=[procs.dy_lep],
    keys=['/DYto2L_M-50_2J_amcatnloFXFX'],
    n_files=51,
    n_events=23075468,
    aux=None
)

# cpn.add_dataset(
#     name='wj_incl',
#     id=22120111,
#     is_data=False,
#     processes=[procs.wj],
#     keys=['/WtoLNu_amcatnloFXFX'],
#     n_files=24,
#     n_events=59463375.0,
#     aux=None
# )
cpn.add_dataset(
    name='wj_incl',
    id=414,
    processes=[procs.wj],
    keys=['/WtoLNu_madgraphMLM','/WtoLNu_madgraphMLM_ext1'],
    n_files=21+24,
    n_events=87204163+97491826,
    aux={
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name='ww',
    id=22120112,
    is_data=False,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=5,
    n_events=15405496,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=22120113,
    is_data=False,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=3,
    n_events=7527043.0,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=22120114,
    is_data=False,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=1181750,
    aux=None
)

## DYto2E ##
# cpn.add_dataset(
#     name=['DYto2E_MLL-10to50_powheg'],
#     id=10,
#     processes=[procs.process_10],
#     keys=['DYto2E_MLL-10to50_powheg'],
#     n_files=1,
#     n_events=1356076,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-120to200_powheg'],
#     id=11,
#     processes=[procs.process_11],
#     keys=['DYto2E_MLL-120to200_powheg'],
#     n_files=1,
#     n_events=1482424,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-1500to2500_powheg'],
#     id=12,
#     processes=[procs.process_12],
#     keys=['DYto2E_MLL-1500to2500_powheg'],
#     n_files=1,
#     n_events=586670,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-200to400_powheg'],
#     id=13,
#     processes=[procs.process_13],
#     keys=['DYto2E_MLL-200to400_powheg'],
#     n_files=1,
#     n_events=864092,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-2500to4000_powheg'],
#     id=14,
#     processes=[procs.process_14],
#     keys=['DYto2E_MLL-2500to4000_powheg'],
#     n_files=1,
#     n_events=290470,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-4000to6000_powheg'],
#     id=15,
#     processes=[procs.process_15],
#     keys=['DYto2E_MLL-4000to6000_powheg'],
#     n_files=1,
#     n_events=298946,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-400to800_powheg'],
#     id=16,
#     processes=[procs.process_16],
#     keys=['DYto2E_MLL-400to800_powheg'],
#     n_files=1,
#     n_events=1070267,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-50to120_powheg'],
#     id=17,
#     processes=[procs.process_17],
#     keys=['DYto2E_MLL-50to120_powheg'],
#     n_files=2,
#     n_events=2859284,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-6000_powheg'],
#     id=18,
#     processes=[procs.process_18],
#     keys=['DYto2E_MLL-6000_powheg'],
#     n_files=1,
#     n_events=145094,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2E_MLL-800to1500_powheg'],
#     id=19,
#     processes=[procs.process_19],
#     keys=['DYto2E_MLL-800to1500_powheg'],
#     n_files=1,
#     n_events=610366,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

## DYto2Tau ##

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-10to50_powheg'],
#     id=51,
#     processes=[procs.process_51],
#     keys=['DYto2Tau_MLL-10to50_powheg'],
#     n_files=1,
#     n_events=1338709,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-120to200_powheg'],
#     id=52,
#     processes=[procs.process_52],
#     keys=['DYto2Tau_MLL-120to200_powheg'],
#     n_files=1,
#     n_events=1483110,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-1500to2500_powheg'],
#     id=53,
#     processes=[procs.process_53],
#     keys=['DYto2Tau_MLL-1500to2500_powheg'],
#     n_files=1,
#     n_events=599982,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-200to400_powheg'],
#     id=54,
#     processes=[procs.process_54],
#     keys=['DYto2Tau_MLL-200to400_powheg'],
#     n_files=1,
#     n_events=872968,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-2500to4000_powheg'],
#     id=55,
#     processes=[procs.process_55],
#     keys=['DYto2Tau_MLL-2500to4000_powheg'],
#     n_files=1,
#     n_events=301961,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-4000to6000_powheg'],
#     id=56,
#     processes=[procs.process_56],
#     keys=['DYto2Tau_MLL-4000to6000_powheg'],
#     n_files=1,
#     n_events=303143,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-400to800_powheg'],
#     id=57,
#     processes=[procs.process_57],
#     keys=['DYto2Tau_MLL-400to800_powheg'],
#     n_files=1,
#     n_events=897512,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-50to120_powheg'],
#     id=58,
#     processes=[procs.process_58],
#     keys=['DYto2Tau_MLL-50to120_powheg'],
#     n_files=2,
#     n_events=2907117,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-6000_powheg'],
#     id=59,
#     processes=[procs.process_59],
#     keys=['DYto2Tau_MLL-6000_powheg'],
#     n_files=1,
#     n_events=146995,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )

# cpn.add_dataset(
#     name=['DYto2Tau_MLL-800to1500_powheg'],
#     id=60,
#     processes=[procs.process_60],
#     keys=['DYto2Tau_MLL-800to1500_powheg'],
#     n_files=1,
#     n_events=581124,
#     aux={
#         "require_triggers"  : ["IsoMu24",]
#     },
# )