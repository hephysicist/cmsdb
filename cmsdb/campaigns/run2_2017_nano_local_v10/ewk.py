# coding: utf-8

"""
Electroweak datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_local_v10 import campaign_run2_2017_nano_local_v10 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14242969,
    processes=[procs.dy],
    keys=[
        #"/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",
        "/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2017/DY2JetsToLL_M-50-madgraphMLM",
    ],
    n_files=45,
    n_events=66096393,
)
