"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v2_nano_tau_v14 import campaign_run3_2022_postEE_v2_nano_tau_v14 as cpn

### prod CP-even datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_sm_filtered",
        id=22100000,
        processes=[procs.h_ggf_htt_sm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=38,
        n_events=24356269,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_prod_sm_filtered",
        id=22100001,
        processes=[procs.h_ggf_htt_mm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=38,
        n_events=24356269,
    )

cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_sm_filtered",
        id=22100002,
        processes=[procs.h_ggf_htt_cpo_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=38,
        n_events=24356269,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_sm_filtered",
        id=22100003,
        processes=[procs.h_ggf_htt_flat_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=38,
        n_events=24356269,
    )

### prod CP-odd datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_cpo_filtered",
        id=22100010,
        processes=[procs.h_ggf_htt_sm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=42,
        n_events=26545013,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_cpo_filtered",
        id=22100011,
        processes=[procs.h_ggf_htt_mm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=42,
        n_events=26545013,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_cpo_filtered",
        id=22100012,
        processes=[procs.h_ggf_htt_cpo_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=42,
        n_events=26545013,
    )
cpn.add_dataset(
        name="h_ggf_htt_flat_prod_cpo_filtered",
        id=22100013,
        processes=[procs.h_ggf_htt_flat_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=42,
        n_events=26545013,
    )

### prod Max. mixing datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_mm_filtered",
        id=22100020,
        processes=[procs.h_ggf_htt_sm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=40,
        n_events=25643123,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_mm_filtered",
        id=22100021,
        processes=[procs.h_ggf_htt_mm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=40,
        n_events=25643123,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_mm_filtered",
        id=22100022,
        processes=[procs.h_ggf_htt_cpo_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=40,
        n_events=25643123,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_mm_filtered",
        id=22100023,
        processes=[procs.h_ggf_htt_flat_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=40,
        n_events=25643123,
    )


#VBF signal samples 
cpn.add_dataset(
        name="h_vbf_htt_sm_filtered",
        id=22100030,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

cpn.add_dataset(
        name="h_vbf_htt_cpo_filtered",
        id=22100031,
        processes=[procs.h_vbf_htt_cpo],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

cpn.add_dataset(
        name="h_vbf_htt_mm_filtered",
        id=22100032,
        processes=[procs.h_vbf_htt_mm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

cpn.add_dataset(
        name="h_vbf_htt_flat_filtered",
        id=22100033,
        processes=[procs.h_vbf_htt_flat],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=26,
        n_events=14552639,
    )

#VH signal samples 
### ZH ###
cpn.add_dataset(
        name="zh_htt_sm_filtered",
        id=22100040,
        processes=[procs.zh_htt_sm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=4,
        n_events=1863291,
    )
cpn.add_dataset(
        name="zh_htt_mm_filtered",
        id=22100041,
        processes=[procs.zh_htt_mm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=4,
        n_events=1863291,
    )

cpn.add_dataset(
        name="zh_htt_cpo_filtered",
        id=22100042,
        processes=[procs.zh_htt_cpo],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=4,
        n_events=1863291,
    )

cpn.add_dataset(
        name="zh_htt_flat_filtered",
        id=22100043,
        processes=[procs.zh_htt_flat],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=4,
        n_events=1863291,
    )

### WH ###

cpn.add_dataset(
        name="wph_htt_sm_filtered",
        id=22100050,
        processes=[procs.wph_htt_sm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=5,
        n_events=1480135,
    )

cpn.add_dataset(
        name="wmh_htt_sm_filtered",
        id=22100051,
        processes=[procs.wmh_htt_sm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=2025321,
    )


cpn.add_dataset(
        name="wph_htt_mm_filtered",
        id=22100052,
        processes=[procs.wph_htt_mm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=5,
        n_events=1480135,
    )

cpn.add_dataset(
        name="wmh_htt_mm_filtered",
        id=22100053,
        processes=[procs.wmh_htt_mm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=2025321,
    )


cpn.add_dataset(
        name="wph_htt_cpo_filtered",
        id=22100054,
        processes=[procs.wph_htt_cpo],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=5,
        n_events=1480135,
    )

cpn.add_dataset(
        name="wmh_htt_cpo_filtered",
        id=22100055,
        processes=[procs.wmh_htt_cpo],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=2025321,
    )


cpn.add_dataset(
        name="wph_htt_flat_filtered",
        id=22100056,
        processes=[procs.wph_htt_flat],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=5,
        n_events=1480135,
    )

cpn.add_dataset(
        name="wmh_htt_flat_filtered",
        id=22100057,
        processes=[procs.wmh_htt_flat],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=2025321,
    )

