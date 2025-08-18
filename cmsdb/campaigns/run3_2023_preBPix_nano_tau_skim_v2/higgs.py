
"""
SM signal datasets for the 2023 preBPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2  import campaign_run3_2023_preBPix_nano_tau_skim_v2 as cpn


### prod CP-even datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_sm_filtered",
        id=23000000,
        processes=[procs.h_ggf_htt_sm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=35,
        n_events=21456982,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_prod_sm_filtered",
        id=23000001,
        processes=[procs.h_ggf_htt_mm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=35,
        n_events=21456982,
    )

cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_sm_filtered",
        id=23000002,
        processes=[procs.h_ggf_htt_cpo_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=35,
        n_events=21456982,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_sm_filtered",
        id=23000003,
        processes=[procs.h_ggf_htt_flat_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=35,
        n_events=21456982,
    )

### prod CP-odd datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_cpo_filtered",
        id=23000010,
        processes=[procs.h_ggf_htt_sm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=33,
        n_events=20252897,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_cpo_filtered",
        id=23000011,
        processes=[procs.h_ggf_htt_mm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=33,
        n_events=20252897,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_cpo_filtered",
        id=23000012,
        processes=[procs.h_ggf_htt_cpo_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=33,
        n_events=20252897,
    )
cpn.add_dataset(
        name="h_ggf_htt_flat_prod_cpo_filtered",
        id=23000013,
        processes=[procs.h_ggf_htt_flat_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=33,
        n_events=20252897,
    )

### prod Max. mixing datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_mm_filtered",
        id=23000020,
        processes=[procs.h_ggf_htt_sm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=37,
        n_events=22449164,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_mm_filtered",
        id=23000021,
        processes=[procs.h_ggf_htt_mm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=37,
        n_events=22449164,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_mm_filtered",
        id=23000022,
        processes=[procs.h_ggf_htt_cpo_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=37,
        n_events=22449164,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_mm_filtered",
        id=23000023,
        processes=[procs.h_ggf_htt_flat_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=37,
        n_events=22449164,
    )


#VBF signal samples 
cpn.add_dataset(
        name="h_vbf_htt_sm_filtered",
        id=23000030,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )

cpn.add_dataset(
        name="h_vbf_htt_cpo_filtered",
        id=23000031,
        processes=[procs.h_vbf_htt_cpo],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )

cpn.add_dataset(
        name="h_vbf_htt_mm_filtered",
        id=23000032,
        processes=[procs.h_vbf_htt_mm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )

cpn.add_dataset(
        name="h_vbf_htt_flat_filtered",
        id=23000033,
        processes=[procs.h_vbf_htt_flat],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )

#VH signal samples 
### ZH ###
cpn.add_dataset(
        name="zh_htt_sm_filtered",
        id=23000040,
        processes=[procs.zh_htt_sm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=5,
        n_events=1803008,
    )
cpn.add_dataset(
        name="zh_htt_mm_filtered",
        id=23000041,
        processes=[procs.zh_htt_mm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=5,
        n_events=1803008,
    )

cpn.add_dataset(
        name="zh_htt_cpo_filtered",
        id=23000042,
        processes=[procs.zh_htt_cpo],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=5,
        n_events=1803008,
    )

cpn.add_dataset(
        name="zh_htt_flat_filtered",
        id=23000043,
        processes=[procs.zh_htt_flat],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=5,
        n_events=1803008,
    )

### WH ###
#Wplus H
cpn.add_dataset(
        name="wph_htt_sm_filtered",
        id=23000050,
        processes=[procs.wph_htt_sm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=1802553,
    )

cpn.add_dataset(
        name="wph_htt_mm_filtered",
        id=23000051,
        processes=[procs.wph_htt_mm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=1802553,
    )

cpn.add_dataset(
        name="wph_htt_cpo_filtered",
        id=23000052,
        processes=[procs.wph_htt_cpo],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=1802553,
    )

cpn.add_dataset(
        name="wph_htt_flat_filtered",
        id=23000053,
        processes=[procs.wph_htt_flat],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=4,
        n_events=1802553,
    )

#Wminus H
cpn.add_dataset(
        name="wmh_htt_sm_filtered",
        id=23000054,
        processes=[procs.wmh_htt_sm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=1248957,
    )

cpn.add_dataset(
        name="wmh_htt_mm_filtered",
        id=23000055,
        processes=[procs.wmh_htt_mm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=1248957,
    )

cpn.add_dataset(
        name="wmh_htt_cpo_filtered",
        id=23000056,
        processes=[procs.wmh_htt_cpo],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=1248957,
    )

cpn.add_dataset(
        name="wmh_htt_flat_filtered",
        id=23000057,
        processes=[procs.wmh_htt_flat],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=1248957,
    )

































