# coding: utf-8

"""
Higgs datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_local_v10 import campaign_run2_2017_nano_local_v10 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14230587,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017/GluGluHToTauTau_M125",  # noqa
    ],
    n_files=6,
    n_events=12974000,
)
