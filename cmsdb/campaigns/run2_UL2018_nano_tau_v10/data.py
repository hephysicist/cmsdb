# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2018_nano_tau_v10 import campaign_run2_UL2018_nano_tau_v10 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_ul2018_a_tau",
    id=1813, # year and era A - 1, B - 2, C - 3, D - 4, 3-tau
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2018A",
    ],
    n_files=8,
    n_events=34165680,
    aux={
        "location"          : "root://eoscms.cern.ch/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2018/",
        "era"               : "a", 
        "require_triggers"  : ["IsoMu24", "IsoMu27"],      
    },
)

cpn.add_dataset(
    name="data_ul2018_a_single_mu",
    id=181, # year and era A - 1, B - 2, C - 3, D - 4
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2018A",
    ],
    n_files=36,
    n_events=193788896,
    aux={
        "location"          : "root://eoscms.cern.ch/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2018/",
        "era"               : "a", 
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1"],      
    },
)

cpn.add_dataset(
    name="data_ul2018_b_single_mu",
    id=182, # year and era A - 1, B - 2, C - 3, D - 4
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2018B",
    ],
    n_files=19,
    n_events=100489023,
    aux={
        "location"          : "root://eoscms.cern.ch/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2018/",
        "era"               : "b", 
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1"],      
    },
)

cpn.add_dataset(
    name="data_ul2018_c_single_mu",
    id=183, # year and era A - 1, B - 2, C - 3, D - 4
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2018C",
    ],
    n_files=17,
    n_events=92661577,
    aux={
        "location"          : "root://eoscms.cern.ch/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2018/",
        "era"               : "c", 
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1"],      
    },
)

cpn.add_dataset(
    name="data_ul2018_d_single_mu",
    id=184, # year and era A - 1, B - 2, C - 3, D - 4
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2018D",
    ],
    n_files=78,
    n_events=432873375,
    aux={
        "location"          : "root://eoscms.cern.ch/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2018/",
        "era"               : "D", 
        "require_triggers"  : ["IsoMu24", "IsoMu27",
                               "IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1",],      
    },
)