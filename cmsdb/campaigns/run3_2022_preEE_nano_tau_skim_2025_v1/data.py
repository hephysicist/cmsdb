# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_2025_v1 import campaign_run3_2022_preEE_nano_tau_skim_2025_v1 as cpn


"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

cpn.add_dataset(
    name="data_egamma_C",
    id=263549470,
    is_data=True,
    processes=[procs.data_egamma],
    keys=['/EGamma_Run2022C'],
    n_files=225,
    n_events=263549470,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name='data_egamma_D',
    id=89134996,
    is_data=True,
    processes=[procs.data_egamma],
    keys=['/EGamma_Run2022D'],
    n_files=88,
    n_events=89134996,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name='data_mu_C',
    id=138329693,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022C'],
    n_files=122,
    n_events=138329693,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name='data_mu_D',
    id=75440027,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022D'],
    n_files=67,
    n_events=75440027,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name='data_tau_C',
    id=25903135,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022C'],
    n_files=31,
    n_events=25903135,
    aux={
        'era': 'C',
    }
)

cpn.add_dataset(
    name='data_tau_D',
    id=16686692,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022D'],
    n_files=19,
    n_events=16686692,
    aux={
        'era': 'D',
    }
)

cpn.add_dataset(
    name='data_singlemu_C',
    id=20162441,
    is_data=True,
    processes=[procs.data_singlemu],
    keys=['/SingleMuon_Run2022C'],
    n_files=19,
    n_events=20162441,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name='data_muoneg_C',
    id=15768439,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2022C'],
    n_files=20,
    n_events=15768439,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name='data_muoneg_D',
    id=8007031,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2022D'],
    n_files=10,
    n_events=8007031,
    aux={
        'era': 'D'
    }
)
