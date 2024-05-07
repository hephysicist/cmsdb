# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v12 import campaign_run3_2022_postEE_nano_tau_v12 as cpn


#
# Drell-Yan
#

# jet binned, madgraph
cpn.add_dataset(
    name="dy_incl",
    id=31,
    processes=[procs.dy_lep],
    keys=[
        "/DYJetsToLL_M-50",
    ],
    n_files=22,
    n_events=96296977.0,
    aux={
        "require_triggers"  : ["IsoMu24",]
                               #"IsoMu27","IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="wj_incl",
    id=32,
    processes=[procs.wj],
    keys=[
        "/WtoLNu-4Jets",
    ],
    n_files=32,
    n_events=348424568.0,
    aux={
        "require_triggers"  : ["IsoMu24",]
                               #"IsoMu27","IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

# cpn.add_dataset(
#     name="ww",
#     id=33,
#     processes=[procs.ww],
#     keys=[
#         "/WW",
#     ],
#     n_files=8,
#     n_events=53558480.0,
#     aux={
#         "require_triggers"  : ["IsoMu24", "IsoMu27",
#                                "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
#     },
# )

# cpn.add_dataset(
#     name="wz",
#     id=33,
#     processes=[procs.wz],
#     keys=[
#         "/WZ",
#     ],
#     n_files=4,
#     n_events=27064288.0,
#     aux={
#         "require_triggers"  : ["IsoMu24", "IsoMu27",
#                                "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
#     },
# )

# cpn.add_dataset(
#     name="zz",
#     id=33,
#     processes=[procs.zz],
#     keys=[
#         "/ZZ",
#     ],
#     n_files=1,
#     n_events=4097040.0,
#     aux={
#         "require_triggers"  : ["IsoMu24", "IsoMu27",
#                                "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
#     },
# )

