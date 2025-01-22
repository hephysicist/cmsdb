# coding: utf-8

"""
CMS datasets from the 2023 preBPix E data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2  import campaign_run3_2023_preBPix_nano_tau_skim_v2 as cpn

"""
CMS datasets from the 2023 preBPix data-taking campaign /eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023/
"""

cpn.add_dataset(
    name='data_e_Cv123',
    id=2212010,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023C_v1', '/EGamma0_Run2023C_v2', '/EGamma0_Run2023C_v3', '/EGamma1_Run2023C_v1', '/EGamma1_Run2023C_v2', '/EGamma1_Run2023C_v3'],
    n_files=38 + 11 + 13 + 38 + 11 + 13,
    n_events= 67598081 + 17233307 + 21993048 + 67530273 + 17230822 + 21987586, 
    aux={
        'era': 'C',
        'jec_era': 'Cv123'
    }
)

cpn.add_dataset(
    name='data_e_Cv4',
    id=221201001,
    is_data=True,
    processes=[procs.data_e],
    keys=['/EGamma0_Run2023C_v4', '/EGamma1_Run2023C_v4'],
    n_files=94 + 94,
    n_events= 160108119 + 159997174,
    aux={
        'era': 'C',
        'jec_era': 'Cv4'
    }
)

cpn.add_dataset(
    name='data_mu_Cv123',
    id=2212011,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023C_v1', '/Muon0_Run2023C_v2', '/Muon0_Run2023C_v3', '/Muon1_Run2023C_v1', '/Muon1_Run2023C_v2', '/Muon1_Run2023C_v3'],
    n_files=27 + 9 + 11 + 27 + 9 + 11,
    n_events= 54715896 + 17063451 + 20015377 + 54621922 + 17059895 + 20010429,
    aux={
        'era': 'C',
        'jec_era': 'Cv123'
    }
)


cpn.add_dataset(
    name='data_mu_Cv4',
    id=221201101,
    is_data=True,
    processes=[procs.data_mu],
    keys=['/Muon0_Run2023C_v4', '/Muon1_Run2023C_v4'],
    n_files= 75 + 75,
    n_events= 138943783 + 138834244,
    aux={
        'era': 'C',
        'jec_era': 'Cv4'
    }
)


cpn.add_dataset(
    name='data_tau_Cv123',
    id=2212012,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023C_v1', '/Tau_Run2023C_v2', '/Tau_Run2023C_v3'],
    n_files=15 + 5 + 7,
    n_events= 14484171 + 5178955 + 6470602,
    aux={
        'era': 'C',
        'jec_era': 'Cv123'
    }
)



cpn.add_dataset(
    name='data_tau_Cv4',
    id=221201201,
    is_data=True,
    processes=[procs.data_tau],
    keys=['/Tau_Run2023C_v4'],
    n_files= 45,
    n_events= 45176805,
    aux={
        'era': 'C',
        'jec_era': 'Cv4'
    }
)

