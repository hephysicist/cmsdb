"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2 import campaign_run3_2022_preEE_nano_tau_skim_v2 as cpn


cpn.add_dataset(
        name="h_ggf_htt_filtered",
        id=22013689000,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_Filtered",],
        n_files=12,
        n_events=8056751.0,
    )

cpn.add_dataset(
        name="h_ggf_htt_unfiltered",
        id=220178223,
        processes=[procs.h_ggf_htt],
        keys=["/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered",],
        n_files=1,
        n_events=121559+77742,
    )