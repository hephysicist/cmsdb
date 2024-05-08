# coding: utf-8

"""
EWK-related process definitions.
"""

__all__ = [
    "dy","dy_lep","dy_z2mumu","dy_z2tautau",
    "w","wj",
    "vv","ww","wz","zz"
]

from order import Process
from scinum import Number

import cmsdb.constants as const

#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
    xsecs={13.6: Number(0.1)},
)


kfactor_dy=6282.6/5455.0 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV [https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV]
dy_lep = dy.add_process(
    name="dy_lep",
    id=51000,
    label=rf"({dy.label} $Z \rightarrow ll$",
    xsecs={13.6: Number(5455.0*kfactor_dy)},
)

dy_z2mumu = dy_lep.add_process(
    name="dy_z2mumu",
    id=51001,
    label=rf"({dy.label} $Z \rightarrow \mu (\tau \rightarrow \mu$)",
    xsecs={13.6: Number(5455.0*kfactor_dy)},
    color=(51,153,204),
)

dy_z2tautau = dy_lep.add_process(
    name="dy_z2tautau",
    id=51002,
    label=rf"({dy.label} $Z \rightarrow \tau_h (\tau \rightarrow \mu)$",
    xsecs={13.6: Number(5455.0*kfactor_dy)},
    color=(255,204,102),
)

#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    xsecs={13.6: Number(0.1)},  # TODO
)

kfactor_wj=63425.1/55300 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV
wj = w.add_process(
    name="wj",
    id=6001,
    label="W + jets",
    xsecs={ 13.6 : Number(55300.*kfactor_wj)},
)

#
# Diboson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13.6: Number(0.1)},  # TODO
)

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v9)
        13: Number(12.13),
        13.6: Number(16.91),
    },
)

wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v9)
        13: Number(25.56),
        13.6: Number(46.74),
    },
)

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v9)
        13.6: Number(118.7),
    },
)
