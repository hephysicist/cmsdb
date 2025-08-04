"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v2_nano_tau_v14 import campaign_run3_2022_postEE_v2_nano_tau_v14 as cpn

cpn.add_dataset(
        name="h_ggf_htt_filtered",
        id=220136895,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_Filtered",],
        n_files=32,
        n_events=21340204,
    )

cpn.add_dataset(
        name="h_ggf_htt_cpo_filtered",
        id=2202368951,
        processes=[procs.h_ggf_htt_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=42,
        n_events=26545013,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_filtered",
        id=2203368952,
        processes=[procs.h_ggf_htt_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=40,
        n_events=25643123,
    )

cpn.add_dataset(
        name="h_ggf_htt_sm_filtered",
        id=2204368953,
        processes=[procs.h_ggf_htt_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=38,
        n_events=24356269,
    )

#VBF signal samples 
cpn.add_dataset(
        name="h_vbf_htt_filtered",
        id=2204368954,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

cpn.add_dataset(
        name="h_vbf_htt_sm_filtered",
        id=2204368955,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

cpn.add_dataset(
        name="h_vbf_htt_cpo_filtered",
        id=2204368956,
        processes=[procs.h_vbf_htt_cpo],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

cpn.add_dataset(
        name="h_vbf_htt_mm_filtered",
        id=2204368957,
        processes=[procs.h_vbf_htt_mm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

