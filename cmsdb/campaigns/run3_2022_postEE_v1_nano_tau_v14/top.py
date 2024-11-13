"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14 import campaign_run3_2022_postEE_v1_nano_tau_v14 as cpn
### SINGLE TOP ###

cpn.add_dataset(
    name='st_tchannel_t',
    id=22120118,
    processes=[procs.st_tchannel_t],
    keys=['/ST_t-channel_top_4f_InclusiveDecays'],
    n_files=5,
    n_events=9368799,
    aux=None
)

cpn.add_dataset(
    name='st_tchannel_tbar',
    id=22120119,
    processes=[procs.st_tchannel_tbar],
    keys=['/ST_t-channel_antitop_4f_InclusiveDecays'],
    n_files=3,
    n_events=4794814,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_sl',
    id=22120120,
    processes=[procs.st_twchannel_t_sl],
    keys=['/ST_tW_top_LNu2Q', '/ST_tW_top_LNu2Q_ext1'],
    n_files=13+13,
    n_events=16686824+15824984,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_dl',
    id=22120121,
    processes=[procs.st_twchannel_t_dl],
    keys=['/ST_tW_top_2L2Nu', '/ST_tW_top_2L2Nu_ext1'],
    n_files=7+8,
    n_events=8065066+8510272,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_t_fh',
    id=22120122,
    processes=[procs.st_twchannel_t_fh],
    keys=['/ST_tW_top_4Q', '/ST_tW_top_4Q_ext1'],
    n_files=7+7,
    n_events=13459714+13999444,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_sl',
    id=22120123,
    processes=[procs.st_twchannel_tbar_sl],
    keys=['/ST_tW_antitop_LNu2Q', '/ST_tW_antitop_LNu2Q_ext1'],
    n_files=13+14,
    n_events=16485400+17271609,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_dl',
    id=22120124,
    processes=[procs.st_twchannel_tbar_dl],
    keys=['/ST_tW_antitop_2L2Nu', '/ST_tW_antitop_2L2Nu_ext1'],
    n_files=7+8,
    n_events=8259727+8522476,
    aux=None
)

cpn.add_dataset(
    name='st_twchannel_tbar_fh',
    id=22120125,
    processes=[procs.st_twchannel_tbar_fh],
    keys=['/ST_tW_antitop_4Q', '/ST_tW_antitop_4Q_ext1'],
    n_files=7+7,
    n_events=13447400+12556124,
    aux=None
)

### TT SAMPLES ###
cpn.add_dataset(
    name='tt_sl',
    id=22120115,
    processes=[procs.tt_sl],
    keys=['/TTtoLNu2Q', '/TTtoLNu2Q_ext1'],
    n_files=82+71,
    n_events= 88730729+76380270,
    aux=None
)

cpn.add_dataset(
    name='tt_dl',
    id=22120116,
    processes=[procs.tt_dl],
    keys=['/TTto2L2Nu', '/TTto2L2Nu_ext1'],
    n_files=84+83,
    n_events=84124365+84236946,
    aux=None
)

cpn.add_dataset(
    name='tt_fh',
    id=22120117,
    processes=[procs.tt_fh],
    keys=['/TTto4Q', '/TTto4Q_ext1'],
    n_files=107+112,
    n_events=178208417.0+186029697.0,
    aux=None
)

