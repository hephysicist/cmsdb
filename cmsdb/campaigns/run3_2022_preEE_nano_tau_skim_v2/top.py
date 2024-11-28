
"""
Top quark datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2 import campaign_run3_2022_preEE_nano_tau_skim_v2 as cpn

### SINGLE TOP ###
#TBbarQ
cpn.add_dataset(
    name='st_tchannel_t',
    id=22120118,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t_channel_top_4f_InclusiveDecays'],
    n_files=3,
    n_events=2737505.0,
    aux=None
)

#TbarBQ_t
cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22120119,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t_channel_antitop_4f_InclusiveDecays'],
    n_files=2,
    n_events=1325389.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_sl',
    id=22120120,
    processes=[procs.st_twchannel_t_sl],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=9+9,
    n_events=4743805+4900178,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_dl',
    id=22120121,
    processes=[procs.st_twchannel_t_dl],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=5+5,
    n_events=2386952+2499916,
    aux=None
)


cpn.add_dataset(
    name='st_twchannel_t_fh',
    id=22120122,
    processes=[procs.st_twchannel_t_fh],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=5+5,
    n_events=3861851+3909424,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_sl',
    id=22120123,
    processes=[procs.st_twchannel_tbar_sl],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=8+9,
    n_events=4366325+4816386,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_dl',
    id=22120124,
    processes=[procs.st_twchannel_tbar_dl],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=5+5,
    n_events=2327604+2435657,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_fh',
    id=22120125,
    processes=[procs.st_twchannel_tbar_fh],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=5+5,
    n_events=3762818+3999850,
    aux=None
)
cpn.add_dataset(
    name="st_schannel_t_lep",
    id=22120126,
    processes=[procs.st_schannel_t_lep],
    keys=['/ST_s_channel_top_4f_leptonDecays'],
    n_files=2,
    n_events=781538,
)
cpn.add_dataset(
    name="st_schannel_tbar_lep",
    id=22120127,
    processes=[procs.st_schannel_tbar_lep],
    keys=['/ST_s_channel_antitop_4f_leptonDecays'],
    n_files=1,
    n_events=484738,
)
### TT SAMPLES ###

cpn.add_dataset(
    name='tt_sl',
    id=22120115,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=179+155,
    n_events= 78965882+76380270,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=22120116,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=53+53,
    n_events=23610071+23890314,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=22120117,
    processes=[procs.tt_fh],
    keys=['/TTto4Q'],
    n_files=71,
    n_events=52883494.0,
    aux=None
)



# cpn.add_dataset(
#     name="dataset_40",
#     id=40,
#     processes=[procs.process_40],
#     keys=['ST_t_channel_antitop_4f_InclusiveDecays'],
#     n_files=2,
#     n_events=1325389.0,
# )



# cpn.add_dataset(
#     name="dataset_70",
#     id=70,
#     processes=[procs.process_70],
#     keys=['TT'],
#     n_files=14,
#     n_events=7398738.0,
# )

# cpn.add_dataset(
#     name="dataset_71",
#     id=71,
#     processes=[procs.process_71],
#     keys=['TT_ext1'],
#     n_files=13,
#     n_events=7301650.0,
# )








