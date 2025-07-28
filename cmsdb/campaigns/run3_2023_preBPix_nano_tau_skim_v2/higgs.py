
"""
SM signal datasets for the 2023 preBPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2  import campaign_run3_2023_preBPix_nano_tau_skim_v2 as cpn

cpn.add_dataset(
        name="h_ggf_htt_filtered",
        id=220136890000,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_Filtered",],
        n_files=12,
        n_events=8056751.0,
    )

cpn.add_dataset(
        name="h_ggf_htt_unfiltered",
        id=220136890001,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered",],
        n_files=1,
        n_events=121559+77742,
    )


cpn.add_dataset(
        name="h_ggf_htt_cpo_filtered",
        id=220136890002,
        processes=[procs.h_ggf_htt_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=33,
        n_events=20252897,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_filtered",
        id=220136890003,
        processes=[procs.h_ggf_htt_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=37,
        n_events=22449164,
    )

cpn.add_dataset(
        name="h_ggf_htt_sm_filtered",
        id=220136890004,
        processes=[procs.h_ggf_htt_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=35,
        n_events=21456982,
    )

#VBF signal samples 
cpn.add_dataset(
        name="h_vbf_htt_filtered",
        id=220136890005,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )
cpn.add_dataset(
        name="h_vbf_htt_sm_filtered",
        id=220136890006,
        processes=[procs.h_vbf_htt_sm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )

cpn.add_dataset(
        name="h_vbf_htt_cpo_filtered",
        id=220136890007,
        processes=[procs.h_vbf_htt_cpo],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )

cpn.add_dataset(
        name="h_vbf_htt_mm_filtered",
        id=220136890008,
        processes=[procs.h_vbf_htt_mm],
        keys=["/VBFHToTauTau_UncorrelatedDecay_Filtered",],
        n_files=24,
        n_events=12453012,
    )
