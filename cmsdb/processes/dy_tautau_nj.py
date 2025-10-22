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
"dy_tautau_m50toinf_0j", "dy_tautau_m50toinf_1j", "dy_tautau_m50toinf_2j",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import multiply_xsecs

#xsecs are taken from https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&ordDirection=-1&ordFieldName=createdOn&pageSize=10&searchQuery=process_name%3DDYto2Tau-2Jets


#[https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV]
kfactor_dy_lo=6282.6/5455.0 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV

kfactor_dy_nlo=6282.6/6748.0 # NLO->NNLO+NLO_EW k-factor computed for 13.6 TeV
kfactor_dy_nlo_powheg=6282.6/6731.99 # NLO->NNLO+NLO_EW k-factor computed for 13.6 TeV

kfactor_wj=63425.1/55300 # LO->NNLO+NLO_EW k-factor computed for 13.6 TeV
kfactor_ww=1.524 # LO->NNLO+NLO_EW computed for 13.6 TeV
kfactor_zz=1.524 # LO->NNLO+NLO_EW computed for 13.6 TeV
kfactor_wz=1.414 # LO->NNLO+NLO_EW computed for 13.6 TeV


kfactor_dy = kfactor_dy_nlo

dy_tautau_m50toinf_0j = Process(
    name="dy_tautau_m50toinf_0j",
    id=51650,
    xsecs={
        #13.6: Number(1664.684), 
        13.6: Number(5368/3. * kfactor_dy), # Factor of 1/3 from taking only taus
    },
)

dy_tautau_m50toinf_1j = Process(
    name="dy_tautau_m50toinf_1j",
    id=51651,
    xsecs={
        #13.6: Number(316.240),
        13.6: Number(1014/3. * kfactor_dy), 
    },
)

dy_tautau_m50toinf_2j = Process(
    name="dy_tautau_m50toinf_2j",
    id=51652,
    xsecs={
        #13.6: Number(116.472),
        13.6: Number(380.8/3. * kfactor_dy), 
    },
)