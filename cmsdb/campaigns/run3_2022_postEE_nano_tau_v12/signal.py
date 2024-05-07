# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_v12 import campaign_run3_2022_postEE_nano_tau_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="signal",
    processes=[procs.h_ggf_tautau],
    id=11100,
    keys=[
        "/GluGluHToTauTau_M125_v3",
    ],
    n_files=1,
    n_events=287988.0,
    aux={
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)