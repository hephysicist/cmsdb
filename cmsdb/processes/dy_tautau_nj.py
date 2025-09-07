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


dy_tautau_m50toinf_0j = Process(
    name="dy_tautau_m50toinf_0j",
    id=51650,
    xsecs={
        13.6: Number(1664.684),
    },
    aux={
        "lep_id": 15,
        "mll": (50.0, const.inf),
    },
)

dy_tautau_m50toinf_1j = Process(
    name="dy_tautau_m50toinf_1j",
    id=51651,
    xsecs={
        13.6: Number(316.240),
    },
    aux={
        "lep_id": 15,
        "mll": (50.0, const.inf),
    },
)

dy_tautau_m50toinf_2j = Process(
    name="dy_tautau_m50toinf_2j",
    id=51652,
    xsecs={
        13.6: Number(116.472),
    },
    aux={
        "lep_id": 15,
        "mll": (50.0, const.inf),
    },
)