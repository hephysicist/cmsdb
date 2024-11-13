"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14 import campaign_run3_2022_postEE_v1_nano_tau_v14 as cpn

cpn.add_dataset(
    name="h_ggf_htt_uncor_unfiltered",
    id=14805985,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHTo2Tau_UncorrelatedDecay_UnFiltered",
            ],
            n_files=1,
            n_events=499966,
        ),
    ),
)