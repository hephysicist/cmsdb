# coding: utf-8

"""
CMS datasets from the 2023 postBPix E data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_skim_2025_v1  import campaign_run3_2023_postBPix_nano_tau_skim_2025_v1 as cpn


cpn.add_dataset(
    name='data_egamma_2023_D',
    id=105892646 + 22657211 + 105850543 + 22653287,
    is_data=True,
    processes=[procs.data_egamma],
    keys=['/EGamma0_Run2023D_v1', '/EGamma0_Run2023D_v2', '/EGamma1_Run2023D_v1', '/EGamma1_Run2023D_v2'],
    n_files=117 + 26 + 117 + 26,
    n_events= 105892646 + 22657211 + 105850543 + 22653287,
    aux={
        'era': 'D'
    }
)


cpn.add_dataset(
    name='data_mu_2023_D',
    id=100211533 + 21462916 + 100281976 + 21463645,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023D_v1', '/Muon0_Run2023D_v2', '/Muon1_Run2023D_v1', '/Muon1_Run2023D_v2'],
    n_files= 94 + 21 + 95 + 21,
    n_events= 100211533 + 21462916 + 100281976 + 21463645,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name='data_tau_2023_D',
    id=32092659 + 7246202,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023D_v1', '/Tau_Run2023D_v2'],
    n_files= 45 + 11,
    n_events= 32092659 + 7246202,
    aux={
        'era': 'D',
    }
)

cpn.add_dataset(
    name='data_muoneg_2023_D',
    id=17530531 + 3751587,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2023D_v1','/MuonEG_Run2023D_v2'],
    n_files=23 + 5,
    n_events=17530531 + 3751587,
    aux={
        'era': 'D'
    }
)

