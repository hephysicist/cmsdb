# coding: utf-8

"""
CMS datasets from the 2023 preBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1 import campaign_run3_2023_preBPix_nano_tau_skim_2025_v1 as cpn


cpn.add_dataset(
    name='data_egamma_Cv123',
    id=67598081 + 17233307 + 21993048 + 67530273 + 17230822 + 21987586,
    is_data=True,
    processes=[procs.data_egamma],
    keys=['/EGamma0_Run2023C_v1', '/EGamma0_Run2023C_v2', '/EGamma0_Run2023C_v3', '/EGamma1_Run2023C_v1', '/EGamma1_Run2023C_v2', '/EGamma1_Run2023C_v3'],
    n_files= 69 + 19 + 24 + 70 + 19 + 24,
    n_events= 67598081 + 17233307 + 21993048 + 67530273 + 17230822 + 21987586, 
    aux={
        'era': 'C',
        'jec_era': 'Cv123'
    }
)

cpn.add_dataset(
    name='data_egamma_Cv4',
    id=160108119 + 159997174,
    is_data=True,
    processes=[procs.data_egamma],
    keys=['/EGamma0_Run2023C_v4', '/EGamma1_Run2023C_v4'],
    n_files=171 + 171,
    n_events= 160108119 + 159997174,
    aux={
        'era': 'C',
        'jec_era': 'Cv4'
    }
)

cpn.add_dataset(
    name='data_mu_Cv123',
    id=54715896 + 17063451 + 20015377 + 54621922 + 17059895 + 20010429,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023C_v1', '/Muon0_Run2023C_v2', '/Muon0_Run2023C_v3', '/Muon1_Run2023C_v1', '/Muon1_Run2023C_v2', '/Muon1_Run2023C_v3'],
    n_files=50 + 16 + 19 + 50 + 16 + 13,
    n_events= 54715896 + 17063451 + 20015377 + 54621922 + 17059895 + 20010429,
    aux={
        'era': 'C',
        'jec_era': 'Cv123'
    }
)


cpn.add_dataset(
    name='data_mu_Cv4',
    id=138943783 + 138834244,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023C_v4', '/Muon1_Run2023C_v4'],
    n_files= 134 + 134,
    n_events= 138943783 + 138834244,
    aux={
        'era': 'C',
        'jec_era': 'Cv4'
    }
)


cpn.add_dataset(
    name='data_tau_Cv123',
    id=14484171 + 5178955 + 6470602,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023C_v1', '/Tau_Run2023C_v2', '/Tau_Run2023C_v3'],
    n_files=22 + 8 + 10,
    n_events= 14484171 + 5178955 + 6470602,
    aux={
        'era': 'C',
        'jec_era': 'Cv123'
    }
)

cpn.add_dataset(
    name='data_tau_Cv4',
    id=45176805,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023C_v4'],
    n_files= 67,
    n_events= 45176805,
    aux={
        'era': 'C',
        'jec_era': 'Cv4'
    }
)

cpn.add_dataset(
    name='data_muoneg_Cv123',
    id=9772655 + 2735170 + 3502967,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2023C_v1','/MuonEG_Run2023C_v2','/MuonEG_Run2023C_v3','/MuonEG_Run2023C_v4'],
    n_files= 13 + 4 + 5,
    n_events= 9772655 + 2735170 + 3502967,
    aux={
        'era': 'C',
        'jec_era': 'Cv123',
    }
)

cpn.add_dataset(
    name='data_muoneg_Cv4',
    id=24205121,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2023C_v4'],
    n_files=32,
    n_events=24205121 ,
    aux={
        'era': 'C',
        'jec_era': 'Cv4',
    }
)