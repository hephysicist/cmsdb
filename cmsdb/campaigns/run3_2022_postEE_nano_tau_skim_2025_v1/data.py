"""
CMS TAUPOG skimmed datasets from the 2022 postEE data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_tau_skim_2025_v1 import campaign_run3_2022_postEE_nano_tau_skim_2025_v1 as cpn

cpn.add_dataset(
        name="data_egamma_E",
        id=148661479,
        is_data=True,
        processes=[procs.data_egamma],
        keys=["/EGamma_Run2022E",],
        n_files=152,
        n_events=148661479,
    aux={"era": "E"},
    )

cpn.add_dataset(
        name="data_egamma_F",
        id=464077454,
        is_data=True,
        processes=[procs.data_egamma],
        keys=["/EGamma_Run2022F",],
        n_files=473,
        n_events=464077454,
    aux={"era": "F"},
    )

cpn.add_dataset(
        name="data_egamma_G",
        id=76724231,
        is_data=True,
        processes=[procs.data_egamma],
        keys=["/EGamma_Run2022G",],
        n_files=78,
        n_events=76724231,
    aux={"era": "G"},
    )

cpn.add_dataset(
        name="data_tau_E",
        id=30520481,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022E",],
        n_files=36,
        n_events=30520481,
    aux={"era": "E"},
    )

cpn.add_dataset(
        name="data_tau_F",
        id=115472800,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022F",],
        n_files=138,
        n_events=115472800,
    aux={"era": "F"},
    )

cpn.add_dataset(
        name="data_tau_G",
        id=17838713,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022G",],
        n_files=22,
        n_events=17838713,
    aux={"era": "G"},
    )

cpn.add_dataset(
        name="data_mu_E",
        id=141480973,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022E",],
        n_files=126,
        n_events=141480973,
    aux={"era": "E"},
    )

cpn.add_dataset(
        name="data_mu_F",
        id=449185088,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022F",],
        n_files=404,
        n_events=449185088,
    aux={"era": "F"},
    )

cpn.add_dataset(
        name="data_mu_G",
        id=76689396,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022G",],
        n_files=70,
        n_events=76689396,
    aux={"era": "G"},
    )

cpn.add_dataset(
    name='data_muoneg_E',
    id=12868267,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2022E'],
    n_files=16,
    n_events=12868267,
    aux={
        'era': 'E'
    }
)

cpn.add_dataset(
    name='data_muoneg_F',
    id=38159099,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2022F'],
    n_files=47,
    n_events=38159099,
    aux={
        'era': 'F'
    }
)

cpn.add_dataset(
    name='data_muoneg_G',
    id=6238527,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=['/MuonEG_Run2022G'],
    n_files=8,
    n_events=6238527,
    aux={
        'era': 'G'
    }
)
