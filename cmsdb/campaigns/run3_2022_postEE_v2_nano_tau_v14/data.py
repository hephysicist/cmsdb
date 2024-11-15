"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v2_nano_tau_v14 import campaign_run3_2022_postEE_v2_nano_tau_v14 as cpn

cpn.add_dataset(
        name="data_e_E",
        id=220146437,
        is_data=True,
        processes=[procs.data_e],
        keys=["/EGamma_Run2022E",],
        n_files=78,
        n_events=148661479,
    aux={"era": "E"},
    )

cpn.add_dataset(
        name="data_e_F",
        id=220192395,
        is_data=True,
        processes=[procs.data_e],
        keys=["/EGamma_Run2022F",],
        n_files=254,
        n_events=464077454,
    aux={"era": "F"},
    )

cpn.add_dataset(
        name="data_e_G",
        id=220174572,
        is_data=True,
        processes=[procs.data_e],
        keys=["/EGamma_Run2022G",],
        n_files=43,
        n_events=76724231,
    aux={"era": "G"},
    )

cpn.add_dataset(
        name="data_tau_E",
        id=220188922,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022E",],
        n_files=25,
        n_events=30520481,
    aux={"era": "E"},
    )

cpn.add_dataset(
        name="data_tau_F",
        id=220186813,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022F",],
        n_files=95,
        n_events=115472800,
    aux={"era": "F"},
    )

cpn.add_dataset(
        name="data_tau_G",
        id=220169353,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022G",],
        n_files=15,
        n_events=17838713,
    aux={"era": "G"},
    )

cpn.add_dataset(
        name="data_mu_E",
        id=220134795,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022E",],
        n_files=64,
        n_events=141480973,
    aux={"era": "E"},
    )

cpn.add_dataset(
        name="data_mu_F",
        id=220132955,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022F",],
        n_files=215,
        n_events=449185088,
    aux={"era": "F"},
    )

cpn.add_dataset(
        name="data_mu_G",
        id=220118007,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022G",],
        n_files=38,
        n_events=76689396,
    aux={"era": "G"},
    )
