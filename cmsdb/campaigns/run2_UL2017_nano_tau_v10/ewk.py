# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v10 import campaign_run2_UL2017_nano_tau_v10 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_incl",
    id=31,
    processes=[procs.dy_lep],
    keys=[
        "/DYJetsToLL_M-50-madgraphMLM",
    ],
    n_files=35,
    n_events=45178033.0,
    aux={
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="wj_incl",
    id=32,
    processes=[procs.wj],
    keys=[
        "/WJetsToLNu",
    ],
    n_files=15,
    n_events=7148834.0,
    aux={
        "require_triggers"  : ["IsoMu24",]
    },
)

# cpn.add_dataset(
#     name="ww",
#     id=33,
#     processes=[procs.ww],
#     keys=[
#         "/WW",
#     ],
#     n_files=3,
#     n_events=15641718.0,
#     aux={
#         "require_triggers"  : ["IsoMu24"]
#     },
# )

# cpn.add_dataset(
#     name="wz",
#     id=34,
#     processes=[procs.wz],
#     keys=[
#         "/WZ",
#     ],
#     n_files=1,
#     n_events=7538008.0,
#     aux={
#         "require_triggers"  : ["IsoMu24"]
#     },
# )

# cpn.add_dataset(
#     name="zz",
#     id=35,
#     processes=[procs.zz],
#     keys=[
#         "/ZZ",
#     ],
#     n_files=1,
#     n_events=1186860.0,
#     aux={
#         "require_triggers"  : ["IsoMu24"]
#     },
# )

