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
    name="dy_incl",
    id=31,
    processes=[procs.dy_lep],
    keys=[
        "/DYto2L-4Jets_MLL-50",
    ],
    n_files=17,
    n_events=74992583.0,
    aux={
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="wj_incl",
    id=32,
    processes=[procs.wj],
    keys=[
        "/WJetsToLNu-4Jets",
    ],
    n_files=9,
    n_events=87902408.0,
    aux={
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="ww",
    id=33,
    processes=[procs.ww],
    keys=[
        "/WW",
    ],
    n_files=3,
    n_events=15641718.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

cpn.add_dataset(
    name="wz",
    id=34,
    processes=[procs.wz],
    keys=[
        "/WZ",
    ],
    n_files=1,
    n_events=7538008.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

cpn.add_dataset(
    name="zz",
    id=35,
    processes=[procs.zz],
    keys=[
        "/ZZ",
    ],
    n_files=1,
    n_events=1186860.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

