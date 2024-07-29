# coding: utf-8

"""
Top quark datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_tau_v12 import campaign_run3_2022_preEE_nano_tau_v12 as cpn
### SINGLE TOP ###
#TBbarQ
cpn.add_dataset(
    name='st_tchannel_t',
    id=22120118,
    is_data=False,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=2,
    n_events=2737505.0,
    aux=None
)

#TbarBQ_t
cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22120119,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=1,
    n_events=1325389.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_sl',
    id=22120120,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=8,
    n_events=9643983.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_dl',
    id=22120121,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=6,
    n_events=4886868.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_fh',
    id=22120122,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=2,
    n_events=3861851.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_sl',
    id=22120123,
    is_data=False,
    processes=[procs.st_twchannel_tbar_sl],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=8,
    n_events=9224089.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_dl',
    id=22120124,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=3+3,
    n_events=2465884.0+2435657.0,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_fh',
    id=22120125,
    is_data=False,
    processes=[procs.st_twchannel_tbar_fh],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=5,
    n_events=7762668.0,
    aux=None
)

### TT SAMPLES ###
cpn.add_dataset(
    name='tt_sl',
    id=22120115,
    is_data=False,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=82+71,
    n_events= 88730729.0+76380270.0,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=22120116,
    is_data=False,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=24+24,
    n_events=23610071.0+23890314.0,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=22120117,
    is_data=False,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=33+32,
    n_events=53042730.0+52146535.0,
    aux=None
)

