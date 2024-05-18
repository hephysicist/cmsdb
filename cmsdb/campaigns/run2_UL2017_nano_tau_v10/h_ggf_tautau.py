# coding: utf-8

"""
CMS datasets from the UL2017 data-taking campaign
Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v10 import campaign_run2_UL2017_nano_tau_v10 as cpn


#
# Muon
#

cpn.add_dataset(
    name="h_ggf_tautau",
    processes=[procs.h_ggf_tautau],
    id=11100,
    keys=[
        "/GluGluHToTauTau_M125",
    ],
    n_files=6,
    n_events=6772374.0,
    aux={
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="h_ggf_tautau_cp_odd_filtered",
    processes=[procs.h_ggf_tautau],
    id=11101,
    keys=[
        "/GluGluHToTauTau_UncorrelatedDecay_CPodd_Filtered",
    ],
    n_files=20,
    n_events=22474426.0,
    aux={
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="h_ggf_tautau_cp_odd_unfiltered",
    processes=[procs.h_ggf_tautau],
    id=11102,
    keys=[
        "/GluGluHToTauTau_UncorrelatedDecay_CPodd_Filtered",
    ],
    n_files=1,
    n_events=322913.0,
    aux={
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1"],      
    },
)