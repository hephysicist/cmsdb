# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v12 import campaign_run3_2022_preEE_nano_tau_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=10, #I don't understand this number 
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon_Run2022C",
    ],
    n_files=9,
    n_events=29275119,
    aux={
        "era"               : "C", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=11, #I don't understand this number 
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon_Run2022D",
    ],
    n_files=5,
    n_events=16356969,
    aux={
        "era"               : "D", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=12, #I don't understand this number 
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon_Run2022E",
    ],
    n_files=9,
    n_events=30654184,
    aux={
        "era"               : "E", 
        "require_triggers"  : ["IsoMu24",]
    },
)


