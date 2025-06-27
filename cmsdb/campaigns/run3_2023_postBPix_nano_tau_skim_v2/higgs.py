
"""
SM signal datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_tau_skim_v2  import campaign_run3_2023_postBPix_nano_tau_skim_v2 as cpn


cpn.add_dataset(
        name="h_ggf_htt_filtered",
        id=20136890000,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_Filtered",],
        n_files=12,
        n_events=8056751.0,
    )

cpn.add_dataset(
        name="h_ggf_htt_unfiltered",
        id=20136890001,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered",],
        n_files=1,
        n_events=121559+77742,
    )


cpn.add_dataset(
        name="h_ggf_htt_cpo_filtered",
        id=20136890002,
        processes=[procs.h_ggf_htt_cpo],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_CPodd_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11235783,
    )

cpn.add_dataset(
        name="h_ggf_htt_mm_filtered",
        id=20136890003,
        processes=[procs.h_ggf_htt_mm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_MM_Filtered_ProdAndDecay",],
        n_files=19,
        n_events=11301507,
    )

cpn.add_dataset(
        name="h_ggf_htt_sm_filtered",
        id=20136890004,
        processes=[procs.h_ggf_htt_sm],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_SM_Filtered_ProdAndDecay",],
        n_files=18,
        n_events=10717909,
    )
