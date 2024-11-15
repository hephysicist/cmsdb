"""
CMS TAUPOG skimmed datasets from the 2022 data-taking campaign 
"""
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_v2_nano_tau_v14 import campaign_run3_2022_postEE_v2_nano_tau_v14 as cpn

cpn.add_dataset(
        name="st_schannel_tbar_lep",
        id=220177019,
        is_mc=True,
        processes=[procs.st_schannel_tbar_lep],
        keys=["/ST_s_channel_antitop_4f_leptonDecays",],
        n_files=4,
        n_events=1700756,
    )

cpn.add_dataset(
        name="st_schannel_t_lep",
        id=220194586,
        is_mc=True,
        processes=[procs.st_schannel_t_lep],
        keys=["/ST_s_channel_top_4f_leptonDecays",],
        n_files=5,
        n_events=2685976,
    )

cpn.add_dataset(
        name="st_twchannel_tbar_dl",
        id=220158817,
        is_mc=True,
        processes=[procs.st_twchannel_tbar_dl],
        keys=["/ST_tW_antitop_2L2Nu","/ST_tW_antitop_2L2Nu_ext1",],
        n_files=32,
        n_events=16782203,
    )

cpn.add_dataset(
        name="st_twchannel_tbar_fh",
        id=220179123,
        is_mc=True,
        processes=[procs.st_twchannel_tbar_fh],
        keys=["/ST_tW_antitop_4Q","/ST_tW_antitop_4Q_ext1",],
        n_files=29,
        n_events=25974756,
    )

cpn.add_dataset(
        name="st_twchannel_t_dl",
        id=220157472,
        is_mc=True,
        processes=[procs.st_twchannel_t_dl],
        keys=["/ST_tW_top_2L2Nu","/ST_tW_top_2L2Nu_ext1",],
        n_files=31,
        n_events=16575338,
    )

cpn.add_dataset(
        name="st_twchannel_t_fh",
        id=220124315,
        is_mc=True,
        processes=[procs.st_twchannel_t_fh],
        keys=["/ST_tW_top_4Q","/ST_tW_top_4Q_ext1",],
        n_files=31,
        n_events=27459158,
    )

cpn.add_dataset(
        name="st_twchannel_t_sl",
        id=220136016,
        is_mc=True,
        processes=[procs.st_twchannel_t_sl],
        keys=["/ST_tW_top_LNu2Q","/ST_tW_top_LNu2Q_ext1",],
        n_files=57,
        n_events=32511808,
    )

cpn.add_dataset(
        name="st_tchannel_tbar",
        id=220166551,
        is_mc=True,
        processes=[procs.st_tchannel_tbar],
        keys=["/ST_t_channel_antitop_4f_InclusiveDecays",],
        n_files=5,
        n_events=4794814,
    )

cpn.add_dataset(
        name="st_tchannel_t",
        id=220162147,
        is_mc=True,
        processes=[procs.st_tchannel_t],
        keys=["/ST_t_channel_top_4f_InclusiveDecays",],
        n_files=10,
        n_events=9368799,
    )

cpn.add_dataset(
        name="tt_dl",
        id=220131478,
        is_mc=True,
        processes=[procs.tt_dl],
        keys=["/TTto2L2Nu","/TTto2L2Nu_ext1",],
        n_files=369,
        n_events=167682796,
    )

cpn.add_dataset(
        name="tt_fh",
        id=220181419,
        is_mc=True,
        processes=[procs.tt_fh],
        keys=["/TTto4Q","/TTto4Q_ext1",],
        n_files=484,
        n_events=363409416,
    )

cpn.add_dataset(
        name="tt_sl",
        id=220168761,
        is_mc=True,
        processes=[procs.tt_sl],
        keys=["/TTtoLNu2Q",],
        n_files=534,
        n_events=264626088,
    )
