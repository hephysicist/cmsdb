"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14 import campaign_run3_2022_postEE_v1_nano_tau_v14 as cpn

cpn.add_dataset(
        name="dy_incl_m10_50",
        id=220119662,
        is_mc=True,
        processes=[procs.dy_lep],
        keys=["/DYto2L_M-10to50_madgraphMLM",],
        n_files=101,
        n_events=520125461,
    )

cpn.add_dataset(
        name="dy_incl_m50",
        id=220119663,
        is_mc=True,
        processes=[procs.dy_lep],
        keys=["/DYto2L_M-50_madgraphMLM","DYto2L_M-50_madgraphMLM_ext1"],
        n_files=103+108,
        n_events=240687634+254153530,
    )

cpn.add_dataset(
    name='wj_incl',
    id=220119664,
    processes=[procs.wj],
    keys=["WtoLNu_madgraphMLM","WtoLNu_madgraphMLM_ext1"],
    n_files=80+81
    n_events=342750582+341334203
)

cpn.add_dataset(
        name="zz",
        id=220140873,
        processes=[procs.zz],
        keys=["/ZZ",],
        n_files=2,
        n_events=4043040,
    )

cpn.add_dataset(
        name="wz",
        id=220153410,
        processes=[procs.wz],
        keys=["/WZ",],
        n_files=8,
        n_events=27003640,
    )

cpn.add_dataset(
        name="ww",
        id=220190280,
        processes=[procs.ww],
        keys=["/WW",],
        n_files=16,
        n_events=53112080,
    )
