# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2 import campaign_run3_2022_preEE_nano_tau_skim_v2 as cpn


"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

cpn.add_dataset(
    name='data_e_C',
    id=2212010,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022C'],
    n_files=119,
    n_events=263549470,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name='data_e_D',
    id=2212011,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma_Run2022D'],
    n_files=46,
    n_events=89134996,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name='data_mu_C',
    id=2212012,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022C'],
    n_files=60,
    n_events=138329693,
    aux={
        'era': 'C'
    }
)

cpn.add_dataset(
    name='data_mu_D',
    id=2212013,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon_Run2022D'],
    n_files=34,
    n_events=75440027,
    aux={
        'era': 'D'
    }
)

cpn.add_dataset(
    name='data_tau_C',
    id=2212014,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022C'],
    n_files=22,
    n_events=25903135,
    aux={
        'era': 'C',
    }
)

cpn.add_dataset(
    name='data_tau_D',
    id=2212015,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2022D'],
    n_files=13,
    n_events=16686692,
    aux={
        'era': 'D',
    }
)

cpn.add_dataset(
    name='data_singlemu_C',
    id=2212020,
    is_data=True,
    processes=[procs.data_singlemu],
    keys=['/SingleMuon_Run2022C'],
    n_files=8,
    n_events=20162441,
    aux={
        'era': 'C'
    }
)

