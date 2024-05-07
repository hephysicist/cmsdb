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
    name="data_mu_f",
    id=13, #I don't understand this number 
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon_Run2022F",
    ],
    n_files=31,
    n_events=109849298,
    aux={
        "era"               : "F", 
        "require_triggers"  : ["IsoMu24",]
                               #"IsoMu27",
                               #"IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=14, #I don't understand this number 
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon_Run2022G",
    ],
    n_files=6,
    n_events=19012034,
    aux={
        "era": "G",
        "require_triggers": ["IsoMu24",]
                             #"IsoMu27",
                             #"IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],   
    },
)

cpn.add_dataset(
    name="data_tau_g",
    id=15, #I don't understand this number 
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2022G",
    ],
    n_files=2,
    n_events=6217888,
    aux={
        "era": "G",
        "require_triggers": ["IsoMu24",]
                             #"IsoMu27",
                             #"IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],   
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=16, #I don't understand this number 
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2022G",
    ],
    n_files=14,
    n_events=40109034,
    aux={
        "era": "G",
        "require_triggers": ["IsoMu24",]
                             #"IsoMu27",
                             #"IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],   
    },
)