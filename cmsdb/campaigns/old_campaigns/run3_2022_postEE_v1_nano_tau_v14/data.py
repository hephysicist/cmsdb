"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14 import campaign_run3_2022_postEE_v1_nano_tau_v14 as cpn

cpn.add_dataset(
        name="data_e_E",
        id=220156080,
        is_data=True,
        processes=[procs.data_e],
        keys=["/EGamma_Run2022E",],
        n_files=31,
        n_events=148661479,
    aux={"era": "e"},
    )

cpn.add_dataset(
        name="data_e_F",
        id=220173217,
        is_data=True,
        processes=[procs.data_e],
        keys=["/EGamma_Run2022F",],
        n_files=105,
        n_events=464077454,
    aux={"era": "f"},
    )

cpn.add_dataset(
        name="data_e_G",
        id=220170974,
        is_data=True,
        processes=[procs.data_e],
        keys=["/EGamma_Run2022G",],
        n_files=18,
        n_events=76724231,
    aux={"era": "g"},
    )

cpn.add_dataset(
        name="data_mu_E",
        id=220178126,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022E",],
        n_files=29,
        n_events=141480973,
    aux={"era": "e"},
    )

cpn.add_dataset(
        name="data_mu_F",
        id=220140406,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022F",],
        n_files=102,
        n_events=449185088,
    aux={"era": "f"},
    )

cpn.add_dataset(
        name="data_mu_G",
        id=220154444,
        is_data=True,
        processes=[procs.data_mu],
        keys=["/Muon_Run2022G",],
        n_files=18,
        n_events=76689396,
    aux={"era": "g"},
    )

cpn.add_dataset(
        name="data_tau_E",
        id=220188559,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022E",],
        n_files=11,
        n_events=30520481,
    aux={"era": "e"},
    )

cpn.add_dataset(
        name="data_tau_F",
        id=220137395,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022F",],
        n_files=43,
        n_events=115472800,
    aux={"era": "f"},
    )

cpn.add_dataset(
        name="data_tau_G",
        id=220121946,
        is_data=True,
        processes=[procs.data_tau],
        keys=["/Tau_Run2022G",],
        n_files=7,
        n_events=17838713,
    aux={"era": "g"},
    )
