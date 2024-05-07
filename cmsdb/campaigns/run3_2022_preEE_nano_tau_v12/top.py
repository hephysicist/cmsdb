# coding: utf-8

"""
Top quark datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v12 import campaign_run3_2022_preEE_nano_tau_v12 as cpn


#
# ttbar
#
# semileptonic
cpn.add_dataset(
    name="tt_sl",
    id=41,
    processes=[procs.tt_sl],
    keys=[
        "/TTtoLNu2Q",
    ],
    n_files=43,
    n_events=79946100.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)
# leptionic
cpn.add_dataset(
    name="tt_dl",
    id=42,
    processes=[procs.tt_dl],
    keys=[
        "/TTTo2L2Nu",
    ],
    n_files=16,
    n_events=23657213.0,
    aux={
        "require_triggers"  : ["IsoMu24"]     
    },
)

cpn.add_dataset(
    name="tt_fh",
    id=43,
    processes=[procs.tt_fh],
    keys=[
        "/TTto4Q",
    ],
    n_files=11,
    n_events=53489658.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

# single top

cpn.add_dataset(
    name="st_t_bbarq",
    id=44,
    processes=[procs.st_tchannel_t],
    keys=[
        "/TBbarQ_t-channel",
    ],
    n_files=1,
    n_events=2737505.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

cpn.add_dataset(
    name="st_tbar_bq",
    id=45,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/TbarBQ_t-channel",
    ],
    n_files=1,
    n_events=1376732.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

# single top tW channel

cpn.add_dataset(
    name="st_t_wminus_to_lnu2q",
    id=46,
    processes=[procs.st_twchannel],
    keys=[
        "/TWminustoLNu2Q",
    ],
    n_files=3,
    n_events=4755214.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

cpn.add_dataset(
    name="st_t_wminus_to_2l2nu",
    id=47,
    processes=[procs.st_twchannel],
    keys=[
        "/TWminusto2L2Nu",
    ],
    n_files=2,
    n_events=2435456.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

cpn.add_dataset(
    name="st_tbar_wplus_to_lnu2q",
    id=48,
    processes=[procs.st_twchannel],
    keys=[
        "/TbarWplustoLNu2Q",
    ],
    n_files=3,
    n_events=4490649.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

cpn.add_dataset(
    name="st_tbar_wplus_to_2l2nu",
    id=49,
    processes=[procs.st_twchannel],
    keys=[
        "/TbarWplusto2L2Nu",
    ],
    n_files=2,
    n_events=2401448.0,
    aux={
        "require_triggers"  : ["IsoMu24"]
    },
)

