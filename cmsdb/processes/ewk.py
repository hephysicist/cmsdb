# coding: utf-8

"""
EWK-related process definitions.

Some DY processes contain phasespace ranges in auxiliary fields. Each each is inclusive in the lower
bound and exclusive in the upper bound, i.e. (a, b) means a <= x < b:

- mll: dilepton invariant mass range
- ptll: dilepton pt range
- njets: number of extra jets on generator level (mostly NLO)
"""

__all__ = [
    "dy","dy_lep","dy_z2mumu","dy_z2ee", #,"dy_z2tautau","dy_lep_m10to50""dy_lowmass"
    "w","wj",
    "vv","ww","wz","zz"
]


from order import Process
from scinum import Number
#from scripts.get_x_secs import get_xsec_values,save_xsecs_to_file
import cmsdb.constants as const


#[https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV]
kfactor_dy=6282.6/5455.0 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV
kfactor_wj=63425.1/55300 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV
kfactor_ww=1.524 # LO->NNLO+NLO_EW computed for 13.6 TeV
kfactor_zz=1.524 # LO->NNLO+NLO_EW computed for 13.6 TeV
kfactor_wz=1.414 # LO->NNLO+NLO_EW computed for 13.6 TeV


#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
    xsecs={13.6: Number(0.1)},
)

dy_lep = dy.add_process(
    name="dy_lep",
    id=51000,
    label=rf"{dy.label} $Z \rightarrow ll$",
    xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
        13.6: Number(5455.0*kfactor_dy)},
)

# dy_lep_m10to50 = dy.add_process(
#     name="dy_lep_m10to50",
#     id=50001,
#     label=rf"{dy.label} $Z \rightarrow ll$",
#     xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#         13.6: Number(5455.0*kfactor_dy)},
# )


dy_z2mumu = dy_lep.add_process(
    name="dy_z2mumu",
    id=51001,
    label=rf"$Z \rightarrow \mu (\tau \rightarrow \mu$)",
    # xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
    #        13.6: Number(5455.0*kfactor_dy)},
    color="#94a4a2",
)

# dy_z2tautau = dy_lep.add_process(
#     name="dy_z2tautau",
#     id=51002,
#     label=rf"$Z \rightarrow \ell \tau_h$",
#     xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#            13.6: Number(5455.0*kfactor_dy)},
#     #color="#e76300",
# )

dy_z2ee = dy_lep.add_process(
    name="dy_z2ee",
    id=51003,
    label=rf"$Z \rightarrow e (\tau \rightarrow e)$",
    # xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
    #        13.6: Number(5455.0*kfactor_dy)},
    color="#b9ac70",
)

dy_z2ll = dy_lep.add_process(
    name="dy_z2ll",
    id=51004,
    label=rf"$Z \rightarrow \tau \tau$",
    # xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
    #        13.6: Number(5455.0*kfactor_dy)},
   color="#832db6",
)

# dy_lowmass = dy_lep_m10to50.add_process(
#     name="dy_lowmass",
#     id=51005,
#     label=rf"$Z \rightarrow \tau \tau (M-10to50)$",
#     # xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#     #        13.6: Number(5455.0*kfactor_dy)},
#      color="#b9ac70",
# )


#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    xsecs={13.6: Number(0.1)},  # TODO
)

wm_lnu_xs_13p6 = const.n_leps * Number(9009.5, {
    "scale": (0.014j, 0.012j),
    "pdf": 0.008j,
})
wp_lnu_xs_13p6 = const.n_leps * Number(12122.5, {
    "scale": (0.011j, 0.014),
    "pdf": 0.007j,
})

#kfactor_wj=63425.1/55300 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV
wj = w.add_process(
    name="wj",
    id=6001,
    label="W + jets",
        xsecs={
        13: const.n_leps * Number(20508.9, {
            "scale": (165.7, 88.2),
            "pdf": 770.9,
        }),
        # addition necessary due to absence of combined value
        13.6: 55300.*kfactor_wj, 
            #wm_lnu_xs_13p6 + wp_lnu_xs_13p6,
    },
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

# ZZ 13 TeV xsec values at nNNLO from
zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v9)
        13: Number(12.13),
        13.6: Number(12.75*kfactor_zz),
    },
)

wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v9)
        13: Number(25.56),
        13.6: Number(29.1*kfactor_wz),
    },
)

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v9)
        13   : Number(118.7),
        13.6 : Number(80.23*kfactor_ww),
    },
)
# List of top-level processes
processes = [ww,zz,wz,dy_lep,wj]

# Save the xsec values to 'top.txt' for energy 13.6 TeV
save_xsecs_to_file(processes, 'wj.txt', 13.6)

