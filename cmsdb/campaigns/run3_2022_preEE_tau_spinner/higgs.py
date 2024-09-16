"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_tau_spinner import campaign_run3_2022_preEE_tau_spinner as cpn

cpn.add_dataset(
    name="h_ggf_htt_filtered",
    id=220124532,
    processes=[procs.h_ggf_htt],
    keys=["/GluGluHTo2Tau_UncorrelatedDecay_Filtered"],
    n_files=6,
    n_events=8056751,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="h_ggf_htt_unfiltered",
    id=220189711,
    processes=[procs.h_ggf_htt],
    keys=["/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered"],
    n_files=1,
    n_events=199291,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="h_vbf_htt_filtered",
    id=220121929,
    processes=[procs.h_vbf_htt],
    keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered"],
    n_files=5,
    n_events=5082505,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="h_vbf_htt_ubfiltered",
    id=220160944,
    processes=[procs.h_vbf_htt],
    keys=["/VBFHToTauTau_UncorrelatedDecay_UnFiltered"],
    n_files=1,
    n_events=99878,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="wmh_htt_filtered",
    id=220136769,
    processes=[procs.wmh_htt],
    keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
    n_files=1,
    n_events=431839,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="wmh_htt_unfiltered",
    id=220134348,
    processes=[procs.wmh_htt],
    keys=["/WminusHToTauTau_UncorrelatedDecay_UnFiltered"],
    n_files=1,
    n_events=27789,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="wph_htt_filtered",
    id=220176808,
    processes=[procs.wph_htt],
    keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
    n_files=1,
    n_events=716466,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="wph_htt_unfiltered",
    id=220176475,
    processes=[procs.wph_htt],
    keys=["/WplusHToTauTau_UncorrelatedDecay_UnFiltered"],
    n_files=1,
    n_events=28300,
    aux={ "is_signal" : True},
    )

cpn.add_dataset(
    name="zh_htt_unfiltered",
    id=220139120,
    processes=[procs.zh_htt],
    keys=["/ZHToTauTau_UncorrelatedDecay_UnFiltered"],
    n_files=1,
    n_events=28992,
    aux={ "is_signal" : True},
    )
