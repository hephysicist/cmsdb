# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2  import campaign_run3_2023_preBPix_nano_tau_skim_v2 as cpn


####################################################################################################
#
# Drell-Yan
#
####################################################################################################


cpn.add_dataset(
    name='dy_lep_madgraph', #DYto2L_M-50
    id=2212013,
    processes=[procs.dy_lep],
    keys=['/DYto2L_M_50_madgraphMLM'],
    n_files=128,
    n_events=130559088,
    aux=None
)

cpn.add_dataset(
    name='wj_incl_madgraph',
    id=414,
    processes=[procs.wj],
    keys=['/WtoLNu_madgraphMLM'],
    n_files=104,
    n_events=191075090,
    aux=None,
)

cpn.add_dataset(
    name='ww',
    id=22120112,
    processes=[procs.ww,],
    keys=['/WW'],
    n_files=24,
    n_events=33507000,
    aux=None
)

cpn.add_dataset(
    name='wz',
    id=22120113,
    processes=[procs.wz,],
    keys=['/WZ'],
    n_files=12,
    n_events=16770000,
    aux=None
)

cpn.add_dataset(
    name='zz',
    id=22120114,
    processes=[procs.zz,],
    keys=['/ZZ'],
    n_files=2,
    n_events=2517000,
    aux=None
)



