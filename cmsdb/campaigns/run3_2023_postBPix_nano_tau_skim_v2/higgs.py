
"""
SM signal datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_skim_v2  import campaign_run3_2023_postBPix_nano_tau_skim_v2 as cpn

### prod CP-even datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_sm_filtered",
        id=23100000,
        processes=[procs.h_ggf_htt_sm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=10717909,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_prod_sm_filtered",
        id=23100001,
        processes=[procs.h_ggf_htt_mm_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=10717909,
    )

cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_sm_filtered",
        id=23100002,
        processes=[procs.h_ggf_htt_cpo_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=10717909,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_sm_filtered",
        id=23100003,
        processes=[procs.h_ggf_htt_flat_prod_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=10717909,
    )

### prod CP-odd datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_cpo_filtered",
        id=23100010,
        processes=[procs.h_ggf_htt_sm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11235783,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_cpo_filtered",
        id=23100011,
        processes=[procs.h_ggf_htt_mm_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11235783,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_cpo_filtered",
        id=23100012,
        processes=[procs.h_ggf_htt_cpo_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11235783,
    )
cpn.add_dataset(
        name="h_ggf_htt_flat_prod_cpo_filtered",
        id=23100013,
        processes=[procs.h_ggf_htt_flat_prod_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11235783,
    )

### prod Max. mixing datasets ###
cpn.add_dataset(
        name="h_ggf_htt_sm_prod_mm_filtered",
        id=23100020,
        processes=[procs.h_ggf_htt_sm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11301507,
    )
cpn.add_dataset(
        name="h_ggf_htt_mm_prod_mm_filtered",
        id=23100021,
        processes=[procs.h_ggf_htt_mm_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11301507,
    )
cpn.add_dataset(
        name="h_ggf_htt_cpo_prod_mm_filtered",
        id=23100022,
        processes=[procs.h_ggf_htt_cpo_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11301507,
    )

cpn.add_dataset(
        name="h_ggf_htt_flat_prod_mm_filtered",
        id=23100023,
        processes=[procs.h_ggf_htt_flat_prod_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11301507,
    )


#VBF signal samples 
cpn.add_dataset(
        name="h_vbf_htt_sm_filtered",
        id=23100030,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=14,
        n_events=7048003,
    )

cpn.add_dataset(
        name="h_vbf_htt_cpo_filtered",
        id=23100031,
        processes=[procs.h_vbf_htt_cpo],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=14,
        n_events=7048003,
    )

cpn.add_dataset(
        name="h_vbf_htt_mm_filtered",
        id=23100032,
        processes=[procs.h_vbf_htt_mm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=14,
        n_events=7048003,
    )

cpn.add_dataset(
        name="h_vbf_htt_flat_filtered",
        id=23100033,
        processes=[procs.h_vbf_htt_flat],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=14,
        n_events=7048003,
    )

#VH signal samples 
### ZH ###
cpn.add_dataset(
        name="zh_htt_sm_filtered",
        id=23100040,
        processes=[procs.zh_htt_sm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=3,
        n_events=1007812,
    )
cpn.add_dataset(
        name="zh_htt_mm_filtered",
        id=23100041,
        processes=[procs.zh_htt_mm],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=3,
        n_events=1007812,
    )

cpn.add_dataset(
        name="zh_htt_cpo_filtered",
        id=23100042,
        processes=[procs.zh_htt_cpo],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=3,
        n_events=1007812,
    )

cpn.add_dataset(
        name="zh_htt_flat_filtered",
        id=23100043,
        processes=[procs.zh_htt_flat],
        keys=["/ZHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=3,
        n_events=1007812,
    )

### WH ###
#Wplus H
cpn.add_dataset(
        name="wph_htt_sm_filtered",
        id=23100050,
        processes=[procs.wph_htt_sm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=952493,
    )

cpn.add_dataset(
        name="wph_htt_mm_filtered",
        id=23100051,
        processes=[procs.wph_htt_mm],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=952493,
    )

cpn.add_dataset(
        name="wph_htt_cpo_filtered",
        id=23100052,
        processes=[procs.wph_htt_cpo],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=952493,
    )

cpn.add_dataset(
        name="wph_htt_flat_filtered",
        id=23100053,
        processes=[procs.wph_htt_flat],
        keys=["/WplusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=3,
        n_events=952493,
    )

#Wminus H

cpn.add_dataset(
        name="wmh_htt_sm_filtered",
        id=23100054,
        processes=[procs.wmh_htt_sm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=718725,
    )

cpn.add_dataset(
        name="wmh_htt_mm_filtered",
        id=23100055,
        processes=[procs.wmh_htt_mm],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=718725,
    )

cpn.add_dataset(
        name="wmh_htt_cpo_filtered",
        id=23100056,
        processes=[procs.wmh_htt_cpo],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=718725,
    )

cpn.add_dataset(
        name="wmh_htt_flat_filtered",
        id=23100057,
        processes=[procs.wmh_htt_flat],
        keys=["/WminusHToTauTau_UncorrelatedDecay_Filtered"],
        n_files=2,
        n_events=718725,
    )


