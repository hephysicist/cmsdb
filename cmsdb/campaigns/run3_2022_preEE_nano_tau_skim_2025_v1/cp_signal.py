"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_2025_v1 import campaign_run3_2022_preEE_nano_tau_skim_2025_v1 as cpn  # TODO: adjust if needed

### prod CP-even datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_sm_filtered",
        id=22000000,
        processes=[procs.h_ggf_htt_sm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=6703604,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_prod_sm_filtered",
        id=22000001,
        processes=[procs.h_ggf_htt_mm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=6703604,
    )

cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_sm_filtered",
        id=22000002,
        processes=[procs.h_ggf_htt_cpo_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=6703604,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_sm_filtered",
        id=22000003,
        processes=[procs.h_ggf_htt_flat_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=6703604,
    )

### prod CP-odd datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_cpo_filtered",
        id=22000010,
        processes=[procs.h_ggf_htt_sm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=7185840,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_cpo_filtered",
        id=22000011,
        processes=[procs.h_ggf_htt_mm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=7185840,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_cpo_filtered",
        id=22000012,
        processes=[procs.h_ggf_htt_cpo_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=7185840,
    )
cpn.add_dataset(
        name="h_ggf_htt_flat_prod_cpo_filtered",
        id=22000013,
        processes=[procs.h_ggf_htt_flat_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=7185840,
    )

### prod Max. mixing datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_mm_filtered",
        id=22000020,
        processes=[procs.h_ggf_htt_sm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=17,
        n_events=6424278,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_mm_filtered",
        id=22000021,
        processes=[procs.h_ggf_htt_mm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=17,
        n_events=6424278,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_mm_filtered",
        id=22000022,
        processes=[procs.h_ggf_htt_cpo_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=17,
        n_events=6424278,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_mm_filtered",
        id=22000023,
        processes=[procs.h_ggf_htt_flat_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=17,
        n_events=6424278,
    )


#VBF signal samples 
cpn.add_dataset(
        name="h_vbf_htt_sm_filtered",
        id=22000030,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=13,
        n_events=5082505,
    )

cpn.add_dataset(
        name="h_vbf_htt_cpo_filtered",
        id=22000031,
        processes=[procs.h_vbf_htt_cpo],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=13,
        n_events=5082505,
    )

cpn.add_dataset(
        name="h_vbf_htt_mm_filtered",
        id=22000032,
        processes=[procs.h_vbf_htt_mm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=13,
        n_events=5082505,
    )

cpn.add_dataset(
        name="h_vbf_htt_flat_filtered",
        id=22000033,
        processes=[procs.h_vbf_htt_flat],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=13,
        n_events=5082505,
    )

#VH signal samples 
### ZH ###
cpn.add_dataset(
        name="zh_htt_sm_filtered",
        id=22000040,
        processes=[procs.zh_htt_sm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=2,
        n_events=613598.0,
    )
cpn.add_dataset(
        name="zh_htt_mm_filtered",
        id=22000041,
        processes=[procs.zh_htt_mm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=2,
        n_events=613598.0,
    )

cpn.add_dataset(
        name="zh_htt_cpo_filtered",
        id=22000042,
        processes=[procs.zh_htt_cpo],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=2,
        n_events=613598.0,
    )

cpn.add_dataset(
        name="zh_htt_flat_filtered",
        id=22000043,
        processes=[procs.zh_htt_flat],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=2,
        n_events=613598.0,
    )

### W^+H ###
cpn.add_dataset(
        name="wph_htt_sm_filtered",
        id=22000050,
        processes=[procs.wph_htt_sm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=716466.0,
    )

cpn.add_dataset(
        name="wph_htt_mm_filtered",
        id=22000051,
        processes=[procs.wph_htt_mm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=716466.0,
    )

cpn.add_dataset(
        name="wph_htt_cpo_filtered",
        id=22000052,
        processes=[procs.wph_htt_cpo],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=716466.0,
    )

cpn.add_dataset(
        name="wph_htt_flat_filtered",
        id=22000053,
        processes=[procs.wph_htt_flat],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=716466.0,
    )

### W^-H ###
cpn.add_dataset(
        name="wmh_htt_sm_filtered",
        id=22000054,
        processes=[procs.wmh_htt_sm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=1,
        n_events=431839.0,
    )

cpn.add_dataset(
        name="wmh_htt_mm_filtered",
        id=22000055,
        processes=[procs.wmh_htt_mm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=1,
        n_events=431839.0,
    )

cpn.add_dataset(
        name="wmh_htt_cpo_filtered",
        id=22000056,
        processes=[procs.wmh_htt_cpo],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=1,
        n_events=431839.0,
    )

cpn.add_dataset(
        name="wmh_htt_flat_filtered",
        id=22000057,
        processes=[procs.wmh_htt_flat],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=1,
        n_events=431839.0,
    )