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
    "dy","dy_lep",#"dy_z2mumu","dy_z2ee","dy_z2tautau",
    "dy_ll_m50","dy_ll_m50_0j","dy_ll_m50_1j","dy_ll_m50_2j",
    "dy_tt_m50","dy_tt_m50_0j","dy_tt_m50_1j","dy_tt_m50_2j",
    "w","w_lnu","wj",""
    "w","w_lnu","wj","wj_1j","wj_2j","wj_3j","wj_4j",
    "vv","ww","wz","zz"
]


from order import Process
from scinum import Number
#from scripts.get_x_secs import get_xsec_values,save_xsecs_to_file
import cmsdb.constants as const


#[https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV]
kfactor_dy_lo=6282.6/5455.0 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV

kfactor_dy_nlo=6282.6/6748.0 # NLO->NNLO+NLO_EW k-factor computed for 13.6 TeV
kfactor_dy_nlo_powheg=6282.6/6731.99 # NLO->NNLO+NLO_EW k-factor computed for 13.6 TeV

kfactor_wj=63425.1/55300 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV
kfactor_ww=1.524 # LO->NNLO+NLO_EW computed for 13.6 TeV
kfactor_zz=1.524 # LO->NNLO+NLO_EW computed for 13.6 TeV
kfactor_wz=1.414 # LO->NNLO+NLO_EW computed for 13.6 TeV


kfactor_dy = kfactor_dy_nlo

#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
)

dy_lep = dy.add_process(
    name="dy_lep",
    id=51000,
    label=rf"$Z \rightarrow ll$",
    xsecs={13.6: Number(0.1)},
)


### DY to LL incl bagged taus ###
dy_ll_m50 = dy_lep.add_process(
    name="dy_ll_m50",
    label=rf"$Z \rightarrow \ell\ell$",
    id=51100,
    xsecs={13.6: Number(6747, {"tot": 30.85})* kfactor_dy},
    color="#3399cc",
)

dy_ll_m50_0j = dy_ll_m50.add_process(
    name="dy_ll_m50_0j",
    id=51110,
    xsecs={
        # NLO xsec taken from https://xsdb-temp.app.cern.ch/xsdb/?columns=39911424&currentPage=0&pageSize=10&searchQuery=DAS%3DDYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  # noqa
        13.6: Number(5378, {"tot": 8.007}) * kfactor_dy
    },
)

dy_ll_m50_1j = dy_ll_m50.add_process(
    name="dy_ll_m50_1j",
    id=51111,
    xsecs={
        13.6: Number(1017, {"tot": 6.264}) * kfactor_dy,
    },
) 

dy_ll_m50_2j = dy_ll_m50.add_process(
    name="dy_ll_m50_2j",
    id=51112,
    xsecs={
        13.6: Number(385.5, {"tot": 3.858}) * kfactor_dy,
    },
)

### DY to TauTau ###

dy_tt_m50 = dy_lep.add_process(
    name="dy_tt_m50",
    id=51650,
    label=rf"$Z \rightarrow \tau\tau$+jet fakes",
    color="#a172bd",
)

dy_tt_m50_0j = dy_tt_m50.add_process(
    name="dy_tt_m50_0j",
    id=51651,
    xsecs={
        13.6: Number(5377,{"tot": 15.09}) * kfactor_dy /3.,
    },
)

dy_tt_m50_1j = dy_tt_m50.add_process(
    name="dy_tt_m50_1j",
    id=51652,
    xsecs={
        13.6: Number(1036, {"tot": 63.32}) * kfactor_dy /3., 
    },
)

dy_tt_m50_2j = dy_tt_m50.add_process(
    name="dy_tt_m50_2j",
    id=51653,
    xsecs={
        13.6: Number(375.8, {"tot": 6.895}) * kfactor_dy /3., 
    },
)
# dy_z2ee = dy_lep.add_process(
#     name="dy_z2ee",
#     id=51001,
#     label=rf"$Z \rightarrow ee$",
#     xsecs={13.6: Number(5455.0*kfactor_dy)},
#     color="#b9ac70",
# )
# dy_z2mumu = dy_lep.add_process(
#     name="dy_z2mumu",
#     id=51004,
#     label=rf"$Z \rightarrow \mu\mu$",
#     xsecs={13.6: Number(5455.0*kfactor_dy)},
#    color="#3399cc",
# )

# dy_z2tautau = dy_lep.add_process(
#     name="dy_z2tautau",
#     id=51005,
#     label=rf"$Z \rightarrow \tau\tau$+jet fakes",
#     xsecs={13.6: Number(5455.0*kfactor_dy)},
#     color="#a172bd",
# )





# dy_lep_m10to50 = dy.add_process(
#     name="dy_lep_m10to50",
#     id=50001,
#     label=rf"{dy.label} $Z \rightarrow ll$",
#     xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#         13.6: Number(5455.0*kfactor_dy)},
# )


# dy_z2mumu = dy_lep.add_process(
#     name="dy_z2mumu",
#     id=51001,
#     label=rf"$Z \rightarrow \mu (\tau \rightarrow \mu$)",
#     # xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#     #        13.6: Number(5455.0*kfactor_dy)},
#     #color="#94a4a2",
# )

# dy_z2tautau = dy_lep.add_process(
#     name="dy_z2tautau",
#     id=51002,
#     label=rf"$Z \rightarrow \ell \tau_h$",
#     xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#            13.6: Number(5455.0*kfactor_dy)},
#     #color="#e76300",
# )


# dy_z2tautau = dy_lep.add_process(
#     name="dy_z2tautau",
#     id=51002,
#     label=rf"({dy.label} $Z \rightarrow \tau_h (\tau \rightarrow \mu)$",
#     xsecs={13.6: Number(5455.0*kfactor_dy)},
#     color=(255,204,102),
# )


# dy_z2ee = dy_lep.add_process(
#     name="dy_z2ee",
#     id=51003,
#     label=rf"$Z \rightarrow e (\tau \rightarrow e)$",
#     # xsecs={13: Number(5455.0*kfactor_dy), #FIXME Add proper number for 13TeV
#     #        13.6: Number(5455.0*kfactor_dy)},
#     color="#b9ac70",
# )



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
# xsec taken from: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=process_name%3DWtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8
w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
    label=rf"{w.label} ($W \rightarrow l\nu$)",
    xsecs={
        13: const.n_leps * Number(20508.9, {
            "scale": (165.7, 88.2),
            "pdf": 770.9,
        }),
        13.6: Number(67710.0, {"total": 834},)
    },
    color="#c95954"
)


#x-secs are taken from xsec analyser:
#https://cms-generators.docs.cern.ch/useful-tools-and-links/HowToGenXSecAnalyzer/#during-the-production-of-mc-samples
#curl https://raw.githubusercontent.com/cms-sw/genproductions/master/Utilities/calculateXSectionAndFilterEfficiency/genXsec_cfg.py -o ana.py
#cmsRun ana.py inputFiles="/store/mc/Run3Summer22MiniAODv4/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/40000/87f20e33-c9b5-4a40-9056-532c201980bb.root" maxEvents=-1
wj = w.add_process(
    name="wj",
    id=6001,
    label="W + jets",
        xsecs={
        13: const.n_leps * Number(20508.9, {
            "scale": (165.7, 88.2),
            "pdf": 770.9,
        }),
        13.6:  Number(54250, {"total":  106.9},)*kfactor_wj, 
    },
    color="#c95954"
)
#cmsRun ana.py inputFiles="/store/mc/Run3Summer22MiniAODv4/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v1/60000/7614f956-d7d5-4d09-a8e5-f00bcd329ea5.root" maxEvents=-1
wj_1j = w.add_process(
    name="wj_1j",
    id=6011,
    label="W + 1 jet",
        xsecs={13.6: Number(9166, {"total":  26.90},)*kfactor_wj, 
    },

    color="#c95954"
)
#cmsRun ana.py inputFiles="/store/mc/Run3Summer22MiniAODv4/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v1/60000/cce5ebfd-1e6b-4958-b686-1e2e9c48f78f.root" maxEvents=-1
wj_2j = w.add_process(
    name="wj_2j",
    id=6021,
    label="W + 2 jet",
        xsecs={13.6:  Number(2942, {"total": 9.558},)*kfactor_wj, 
    },
    color="#c95954"
)
#cmsRun ana.py inputFiles="/store/mc/Run3Summer22MiniAODv4/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/50000/a4d4296e-8fd8-48bb-9a69-d353bce82c28.root" maxEvents=-1
wj_3j = w.add_process(
    name="wj_3j",
    id=6031,
    label="W + 3 jets",
        xsecs={13.6: Number(864.4, {"total": 3.037},) * kfactor_wj, 
    },
    color="#c95954"
)

#cmsRun ana.py inputFiles="/store/mc/Run3Summer22MiniAODv4/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/MINIAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/e35e9a14-7946-4369-b311-50ac6ab209cb.root" maxEvents=-1
wj_4j = w.add_process(
    name="wj_4j",
    id=6041,
    label="W + 4 jets",
        xsecs={13.6: Number(419.0, {"total": 1.6},)*kfactor_wj, 
    },
    color="#c95954"
)


#
# Diboson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13.6: Number(0.1)},  # TODO
    color="#7aee7a"
)

from cmsdb.processes.combined_procs import vvt

vv.add_parent_process(vvt)

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


