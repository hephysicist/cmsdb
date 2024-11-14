# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2 import campaign_run3_2022_preEE_nano_tau_skim_v2 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################


cpn.add_dataset(
    name='dy_incl', #DYto2L_M-50
    id=2212016,
    processes=[procs.dy_lep],
    keys=['/DYto2L_M_50_madgraphMLM', '/DYto2L_M_50_madgraphMLM_ext1'],
    n_files=70+69,
    n_events=72652311+71371699,
    aux=None
)

cpn.add_dataset(
    name='wj_incl',
    id=414,
    processes=[procs.wj],
    keys=['/WtoLNu_madgraphMLM','/WtoLNu_madgraphMLM_ext1'],
    n_files=44+51,
    n_events=86093700+97491826,
    aux=None,
)

cpn.add_dataset(
    name='ww',
    id=22120112,
    processes=[procs.ww],
    keys=['/WW'],
    n_files=10,
    n_events=15405496,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=22120113,
    processes=[procs.wz],
    keys=['/WZ'],
    n_files=5,
    n_events=7479528,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=22120114,
    processes=[procs.zz],
    keys=['/ZZ'],
    n_files=1,
    n_events=1181750,
    aux=None
)


# cpn.add_dataset(
#     name="dataset_17",
#     id=17,
#     processes=[procs.process_17],
#     keys=['DYto2TautoMuTauh_M_50_madgraphMLM'],
#     n_files=4,
#     n_events=2930759.0,
# )

# cpn.add_dataset(
#     name="dataset_18",
#     id=18,
#     processes=[procs.process_18],
#     keys=['DYto2L_M_10to50_madgraphMLM'],
#     n_files=67,
#     n_events=160214290.0,
# )

# cpn.add_dataset(
#     name="dataset_19",
#     id=19,
#     processes=[procs.process_19],
#     keys=['DYto2L_M_50_1J_madgraphMLM'],
#     n_files=17,
#     n_events=14855860.0,
# )

# cpn.add_dataset(
#     name="dataset_20",
#     id=20,
#     processes=[procs.process_20],
#     keys=['DYto2L_M_50_2J_madgraphMLM'],
#     n_files=20,
#     n_events=14654880.0,
# )

# cpn.add_dataset(
#     name="dataset_21",
#     id=21,
#     processes=[procs.process_21],
#     keys=['DYto2L_M_50_3J_madgraphMLM'],
#     n_files=14,
#     n_events=8672888.0,
# )

# cpn.add_dataset(
#     name="dataset_22",
#     id=22,
#     processes=[procs.process_22],
#     keys=['DYto2L_M_50_4J_madgraphMLM'],
#     n_files=7,
#     n_events=3258128.0,
# )

# cpn.add_dataset(
#     name="dataset_43",
#     id=43,
#     processes=[procs.process_43],
#     keys=['ZZto2L2Nu_powheg'],
#     n_files=16,
#     n_events=14521499.0,
# )

# cpn.add_dataset(
#     name="dataset_44",
#     id=44,
#     processes=[procs.process_44],
#     keys=['ZZto2L2Nu_powheg_ext1'],
#     n_files=13,
#     n_events=14727726.0,
# )

# cpn.add_dataset(
#     name="dataset_45",
#     id=45,
#     processes=[procs.process_45],
#     keys=['ZZto2L2Q_amcatnloFXFX'],
#     n_files=4,
#     n_events=1310582.0,
# )

# cpn.add_dataset(
#     name="dataset_46",
#     id=46,
#     processes=[procs.process_46],
#     keys=['ZZto2L2Q_powheg'],
#     n_files=16,
#     n_events=14573574.0,
# )

# cpn.add_dataset(
#     name="dataset_47",
#     id=47,
#     processes=[procs.process_47],
#     keys=['ZZto2L2Q_powheg_ext1'],
#     n_files=17,
#     n_events=14905382.0,
# )

# cpn.add_dataset(
#     name="dataset_48",
#     id=48,
#     processes=[procs.process_48],
#     keys=['ZZto2Nu2Q_powheg'],
#     n_files=2,
#     n_events=2927750.0,
# )

# cpn.add_dataset(
#     name="dataset_49",
#     id=49,
#     processes=[procs.process_49],
#     keys=['ZZto2Nu2Q_powheg_ext1'],
#     n_files=2,
#     n_events=2953837.0,
# )

# cpn.add_dataset(
#     name="dataset_50",
#     id=50,
#     processes=[procs.process_50],
#     keys=['ZZto4L_powheg'],
#     n_files=17,
#     n_events=14481306.0,
# )

# cpn.add_dataset(
#     name="dataset_51",
#     id=51,
#     processes=[procs.process_51],
#     keys=['ZZto4L_powheg_ext1'],
#     n_files=18,
#     n_events=14297032.0,
# )



# cpn.add_dataset(
#     name="dataset_53",
#     id=53,
#     processes=[procs.process_53],
#     keys=['WZto2L2Q_powheg'],
#     n_files=5,
#     n_events=4163435.0,
# )

# cpn.add_dataset(
#     name="dataset_54",
#     id=54,
#     processes=[procs.process_54],
#     keys=['WZto2L2Q_powheg_ext1'],
#     n_files=5,
#     n_events=4269337.0,
# )

# cpn.add_dataset(
#     name="dataset_55",
#     id=55,
#     processes=[procs.process_55],
#     keys=['WZto3LNu_amcatnloFXFX'],
#     n_files=4,
#     n_events=1906322.0,
# )

# cpn.add_dataset(
#     name="dataset_56",
#     id=56,
#     processes=[procs.process_56],
#     keys=['WZto3LNu_powheg'],
#     n_files=4,
#     n_events=2791528.0,
# )

# cpn.add_dataset(
#     name="dataset_57",
#     id=57,
#     processes=[procs.process_57],
#     keys=['WZtoL3Nu_amcatnloFXFX'],
#     n_files=2,
#     n_events=1128058.0,
# )

# cpn.add_dataset(
#     name="dataset_58",
#     id=58,
#     processes=[procs.process_58],
#     keys=['WZtoLNu2Q_amcatnloFXFX'],
#     n_files=4,
#     n_events=1404272.0,
# )

# cpn.add_dataset(
#     name="dataset_59",
#     id=59,
#     processes=[procs.process_59],
#     keys=['WZtoLNu2Q_powheg'],
#     n_files=9,
#     n_events=8896204.0,
# )

# cpn.add_dataset(
#     name="dataset_60",
#     id=60,
#     processes=[procs.process_60],
#     keys=['WZtoLNu2Q_powheg_ext1'],
#     n_files=10,
#     n_events=8722878.0,
# )



# cpn.add_dataset(
#     name="dataset_62",
#     id=62,
#     processes=[procs.process_62],
#     keys=['WWto2L2Nu_powheg'],
#     n_files=8,
#     n_events=6133972.0,
# )

# cpn.add_dataset(
#     name="dataset_63",
#     id=63,
#     processes=[procs.process_63],
#     keys=['WWto2L2Nu_powheg_ext1'],
#     n_files=9,
#     n_events=6598672.0,
# )

# cpn.add_dataset(
#     name="dataset_64",
#     id=64,
#     processes=[procs.process_64],
#     keys=['WWto4Q_amcatnloFXFX'],
#     n_files=9,
#     n_events=6813648.0,
# )

# cpn.add_dataset(
#     name="dataset_65",
#     id=65,
#     processes=[procs.process_65],
#     keys=['WWto4Q_powheg'],
#     n_files=20,
#     n_events=28172516.0,
# )

# cpn.add_dataset(
#     name="dataset_66",
#     id=66,
#     processes=[procs.process_66],
#     keys=['WWto4Q_powheg_ext1'],
#     n_files=38,
#     n_events=28188069.0,
# )

# cpn.add_dataset(
#     name="dataset_67",
#     id=67,
#     processes=[procs.process_67],
#     keys=['WWtoLNu2Q_amcatnloFXFX'],
#     n_files=28,
#     n_events=14248541.0,
# )

# cpn.add_dataset(
#     name="dataset_68",
#     id=68,
#     processes=[procs.process_68],
#     keys=['WWtoLNu2Q_powheg'],
#     n_files=29,
#     n_events=27103682.0,
# )

# cpn.add_dataset(
#     name="dataset_69",
#     id=69,
#     processes=[procs.process_69],
#     keys=['WWtoLNu2Q_powheg_ext1'],
#     n_files=29,
#     n_events=26557496.0,
# )

# cpn.add_dataset(
#     name="dataset_75",
#     id=75,
#     processes=[procs.process_75],
#     keys=['WtoLNu_1J_madgraphMLM'],
#     n_files=8,
#     n_events=11896625.0,
# )

# cpn.add_dataset(
#     name="dataset_76",
#     id=76,
#     processes=[procs.process_76],
#     keys=['WtoLNu_2J_madgraphMLM'],
#     n_files=8,
#     n_events=9283334.0,
# )

# cpn.add_dataset(
#     name="dataset_77",
#     id=77,
#     processes=[procs.process_77],
#     keys=['WtoLNu_3J_madgraphMLM'],
#     n_files=9,
#     n_events=8221862.0,
# )

# cpn.add_dataset(
#     name="dataset_78",
#     id=78,
#     processes=[procs.process_78],
#     keys=['WtoLNu_4J_madgraphMLM'],
#     n_files=3,
#     n_events=1463885.0,
# )

