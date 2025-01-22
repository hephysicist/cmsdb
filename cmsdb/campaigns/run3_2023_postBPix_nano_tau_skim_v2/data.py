# coding: utf-8

"""
CMS datasets from the 2023 preBPix E data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_skim_v2  import campaign_run3_2023_postBPix_nano_tau_skim_v2 as cpn



"""
CMS datasets from the 2023 preBPix data-taking campaign /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023/
"""

cpn.add_dataset(
    name='data_e_D',
    id=2212010,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023D_v1', '/EGamma0_Run2023D_v2', '/EGamma1_Run2023D_v1', '/EGamma1_Run2023D_v2'],
    n_files=64 + 14 + 64 + 14,
    n_events= 105892646 + 22657211 + 105850543 + 22653287,
    aux={
        'era': 'D'
    }
)


cpn.add_dataset(
    name='data_mu_D',
    id=2212011,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023D_v1', '/Muon0_Run2023D_v2', '/Muon1_Run2023D_v1', '/Muon1_Run2023D_v2'],
    n_files= 53 + 12 + 53 + 12,
    n_events= 100211533 + 21462916 + 100281976 + 21463645,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name='data_tau_D',
    id=2212012,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023D_v1', '/Tau_Run2023D_v2'],
    n_files=31 + 7,
    n_events= 32092659 + 7246202,
    aux={
        'era': 'D',
    }
)

