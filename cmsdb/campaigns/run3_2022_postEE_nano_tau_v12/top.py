# coding: utf-8

"""
Top quark datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v12 import campaign_run3_2022_postEE_nano_tau_v12 as cpn


#
# ttbar
#
# semileptonic
cpn.add_dataset(
    name="tt_sl",
    id=41,
    processes=[procs.tt_sl],
    keys=[
        "/TTtoLNu2Q",
    ],
    n_files=142,
    n_events=268461541.0,
    aux={
        "require_triggers"  : ["IsoMu24"]s
                               #"IsoMu27",
                               #"IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)
# leptionic
cpn.add_dataset(
    name="tt_dl",
    id=42,
    processes=[procs.tt_dl],
    keys=[
        "/TTTo2L2Nu",
    ],ssh l
    n_files=56,
    n_events=85077258.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
                               #"IsoMu27",
                               #"IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="tt_fh",
    id=43,
    processes=[procs.tt_fh],
    keys=[
        "/TTto4Q",
    ],
    n_files=35,
    n_events=181311721.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
                                #, "IsoMu27",
                                #IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

# single top

cpn.add_dataset(
    name="st_tchannel_t",
    id=43,
    processes=[procs.st_tchannel_t],
    keys=[
        "/TBbarQ_t-channel",
    ],
    n_files=2,
    n_events=9575922.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
                                #, "IsoMu27",
                                #IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="st_tchannel_tbar",
    id=43,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/TbarBQ_t-channel",
    ],
    n_files=1,
    n_events=4818516.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
                                #, "IsoMu27",
                                #IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)