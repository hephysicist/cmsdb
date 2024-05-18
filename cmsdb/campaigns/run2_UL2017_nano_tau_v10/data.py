# coding: utf-8

"""
CMS datasets from the UL2017 data-taking campaign
Link: /eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_UL2017_nano_tau_v10 import campaign_run2_UL2017_nano_tau_v10 as cpn



###Single electron datasets###


cpn.add_dataset(
    name="data_e_b",
    id=20170102, #2017 - year, 02 -data_mu, 02 - era B
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron_Run2017B",
    ],
    n_files=6,
    n_events=14808355,
    aux={
        "era"               : "B", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=20170103, #2017 - year, 02 -data_mu, 03 - era C
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron_Run2017C",
    ],
    n_files=14,
    n_events=32631295,
    aux={
        "era"               : "C", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=20170104, #2017 - year, 02 -data_mu, 04 - era D
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron_Run2017D",
    ],
    n_files=6,
    n_events=12563381,
    aux={
        "era"               : "D", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_e_e",
    id=20170105, #2017 - year, 02 -data_mu, 05 - era E
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron_Run2017E",
    ],
    n_files=13,
    n_events=27869639,
    aux={
        "era"               : "E", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=20170106, #2017 - year, 02 -data_mu, 06 - era F
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron_Run2017F",
    ],
    n_files=17,
    n_events=37181406,
    aux={
        "era"               : "F", 
        "require_triggers"  : ["IsoMu24",]
    },
)



###Single muon datasets###



cpn.add_dataset(
    name="data_mu_b",
    id=20170202, #2017 - year, 02 -data_mu, 02 - era B
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2017B",
    ],
    n_files=9,
    n_events=21572907,
    aux={
        "era"               : "B", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=20170203, #2017 - year, 02 -data_mu, 03 - era C
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2017C",
    ],
    n_files=14,
    n_events=32021527,
    aux={
        "era"               : "C", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=20170204, #2017 - year, 02 -data_mu, 04 - era D
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2017D",
    ],
    n_files=6,
    n_events=13405476,
    aux={
        "era"               : "D", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=20170205, #2017 - year, 02 -data_mu, 05 - era E
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2017E",
    ],
    n_files=15,
    n_events=33008071,
    aux={
        "era"               : "E", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=20170206, #2017 - year, 02 -data_mu, 06 - era F
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon_Run2017F",
    ],
    n_files=26,
    n_events=54333809,
    aux={
        "era"               : "F", 
        "require_triggers"  : ["IsoMu24",]
    },
)


###Tau datasets###


cpn.add_dataset(
    name="data_tau_b",
    id=20170302, #2017 - year, 03 -data_tau, 02 - era B
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2017B",
    ],
    n_files=6,
    n_events=11646232,
    aux={
        "era"               : "B", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=20170303, #2017 - year, 03 -data_tau, 03 - era C
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2017C",
    ],
    n_files=9,
    n_events=18525566,
    aux={
        "era"               : "C", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=20170304, #2017 - year, 03 -data_tau, 04 - era D
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2017D",
    ],
    n_files=4,
    n_events=7388733,
    aux={
        "era"               : "D", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_tau_e",
    id=20170305, #2017 - year, 03 -data_tau, 05 - era E
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2017E",
    ],
    n_files=9,
    n_events=15967428,
    aux={
        "era"               : "E", 
        "require_triggers"  : ["IsoMu24",]
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=20170306, #2017 - year, 03 -data_tau, 06 - era F
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau_Run2017F",
    ],
    n_files=15,
    n_events=27278347,
    aux={
        "era"               : "F", 
        "require_triggers"  : ["IsoMu24",]
    },
)


