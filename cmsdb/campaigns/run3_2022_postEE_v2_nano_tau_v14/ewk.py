"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v2_nano_tau_v14 import campaign_run3_2022_postEE_v2_nano_tau_v14 as cpn

cpn.add_dataset(
        name="wj_incl_madgraph",
        id=220113368,
#        is_mc=True,
        processes=[procs.wj],
        keys=["/WtoLNu_madgraphMLM","/WtoLNu_madgraphMLM_ext1",],
        n_files=344,
        n_events=683448011,
    )

cpn.add_dataset(
        name="dy_lep_madgraph",
        id=220154049,
#        is_mc=True,
        processes=[procs.dy_lep],
        keys=["/DYto2L_M_50_madgraphMLM","/DYto2L_M_50_madgraphMLM_ext1",],
        n_files=464,
        n_events=494841164,
    )

cpn.add_dataset(
        name="ww",
        id=220144633,
#        is_mc=True,
        processes=[procs.ww],
        keys=["/WW",],
        n_files=34,
        n_events=53112080,
    )

cpn.add_dataset(
        name="wz",
        id=220150919,
#        is_mc=True,
        processes=[procs.wz],
        keys=["/WZ",],
        n_files=17,
        n_events=26722782,
    )

cpn.add_dataset(
        name="zz",
        id=220134326,
#        is_mc=True,
        processes=[procs.zz],
        keys=["/ZZ",],
        n_files=3,
        n_events=4043040,
    )

# cpn.add_dataset(
#         name="wj_1j_madgraph",
#         id=220110111,
#         is_mc=True,
#         processes=[procs.wj_1j],
#         keys=["/WtoLNu_1J_madgraphMLM",],
#         n_files=25,
#         n_events=42695566,
#     )

# cpn.add_dataset(
#         name="wj_2j_madgraph",
#         id=220149908,
#         is_mc=True,
#         processes=[procs.wj_2j],
#         keys=["/WtoLNu_2J_madgraphMLM",],
#         n_files=29,
#         n_events=36349344,
#     )

# cpn.add_dataset(
#         name="wj_3j_madgraph",
#         id=220119946,
#         is_mc=True,
#         processes=[procs.wj_3j],
#         keys=["/WtoLNu_3J_madgraphMLM",],
#         n_files=28,
#         n_events=27828446,
#     )

# cpn.add_dataset(
#         name="wj_4j_madgraph",
#         id=220131835,
#         is_mc=True,
#         processes=[procs.wj_4j],
#         keys=["/WtoLNu_4J_madgraphMLM",],
#         n_files=7,
#         n_events=4906634,
#     )

# cpn.add_dataset(
#         name="dy_lep_m10_50_madgraph",
#         id=220162390,
#         is_mc=True,
#         processes=[procs.dy_lep_m10_50],
#         keys=["/DYto2L_M_10to50_madgraphMLM",],
#         n_files=215,
#         n_events=520125461,
#     )

# cpn.add_dataset(
#         name="dy_lep_m50_1j_madgraph",
#         id=220119413,
#         is_mc=True,
#         processes=[procs.dy_lep_m50_1j],
#         keys=["/DYto2L_M_50_1J_madgraphMLM",],
#         n_files=61,
#         n_events=48939365,
#     )

# cpn.add_dataset(
#         name="dy_lep_m50_2j_madgraph",
#         id=220140739,
#         is_mc=True,
#         processes=[procs.dy_lep_m50_2j],
#         keys=["/DYto2L_M_50_2J_madgraphMLM",],
#         n_files=65,
#         n_events=49862030,
#     )

# cpn.add_dataset(
#         name="dy_lep_m50_3j_madgraph",
#         id=220157082,
#         is_mc=True,
#         processes=[procs.dy_lep_m50_3j],
#         keys=["/DYto2L_M_50_3J_madgraphMLM",],
#         n_files=44,
#         n_events=28613025,
#     )

# cpn.add_dataset(
#         name="dy_lep_m50_4j_madgraph",
#         id=220153531,
#         is_mc=True,
#         processes=[procs.dy_lep_m50_4j],
#         keys=["/DYto2L_M_50_4J_madgraphMLM",],
#         n_files=18,
#         n_events=9376714,
#     )


