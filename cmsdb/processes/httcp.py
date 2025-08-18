# coding: utf-8

"""
Single Higgs process duplications needed to implment different cp hypotheses.

"""

from __future__ import annotations

__all__ = [
    "h_ggf_htt_sm",
    "h_ggf_htt_sm_prod_sm","h_ggf_htt_sm_prod_mm","h_ggf_htt_sm_prod_cpo",
    "h_ggf_htt_mm",
    "h_ggf_htt_mm_prod_sm","h_ggf_htt_mm_prod_mm","h_ggf_htt_mm_prod_cpo",
    "h_ggf_htt_cpo",
    "h_ggf_htt_cpo_prod_sm","h_ggf_htt_cpo_prod_mm","h_ggf_htt_cpo_prod_cpo",
    "h_ggf_htt_flat",
    "h_ggf_htt_flat_prod_sm","h_ggf_htt_flat_prod_mm","h_ggf_htt_flat_prod_cpo", 

    "h_vbf_htt_cpo", "h_vbf_htt_sm","h_vbf_htt_mm","h_vbf_htt_flat",
    
    "zh_htt_cpo","zh_htt_sm","zh_htt_mm","zh_htt_flat",
    "wh_htt_cpo","wh_htt_sm","wh_htt_mm","wh_htt_flat",
    
    "wph_htt_cpo","wph_htt_sm","wph_htt_mm","wph_htt_flat",
    "wmh_htt_cpo","wmh_htt_sm","wmh_htt_mm","wmh_htt_flat",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import add_xsecs, DotDict, add_decay_process, add_sub_decay_process

from cmsdb.processes.higgs import h_ggf_htt, h_vbf_htt, wh_htt, zh_htt

h_ggf_htt_xsecs = {
        ecm: h_ggf_htt.get_xsec(ecm) 
        for ecm in h_ggf_htt.xsecs.keys()
}

### ggH CP-even decays ###
h_ggf_htt_sm = h_ggf_htt.add_process(
    name="h_ggf_htt_sm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-even",
    id=11110,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_sm_prod_sm = h_ggf_htt_sm.add_process(
    name="h_ggf_htt_sm_prod_sm",
    label=r"$H_{ggf}\rightarrow\tau\tau$)",
    id=11111,
    xsecs = h_ggf_htt_xsecs,
)
h_ggf_htt_sm_prod_mm = h_ggf_htt_sm.add_process(
    name="h_ggf_htt_sm_prod_mm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-even (prod max. mix)",
    id=11112,
    xsecs = h_ggf_htt_xsecs,
)
h_ggf_htt_sm_prod_cpo = h_ggf_htt_sm.add_process(
    name="h_ggf_htt_sm_prod_cpo",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-even (prod CP-odd)",
    id=11113,
    xsecs = h_ggf_htt_xsecs,
)

### ggH Max mixing decays ###

h_ggf_htt_mm = h_ggf_htt.add_process(
    name="h_ggf_htt_mm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, max. mix",
    id=11120,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_mm_prod_sm = h_ggf_htt_mm.add_process(
    name="h_ggf_htt_mm_prod_sm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, max. mix (prod CP-even)",
    id=11121,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_mm_prod_mm = h_ggf_htt_mm.add_process(
    name="h_ggf_htt_mm_prod_mm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, max. mix (prod max. mix)",
    id=11122,
    xsecs = h_ggf_htt_xsecs,
)
h_ggf_htt_mm_prod_cpo = h_ggf_htt_mm.add_process(
    name="h_ggf_htt_mm_prod_cpo",
    label=r"$H_{ggf}\rightarrow\tau\tau$, max. mix (prod CP-odd)",
    id=11123,
    xsecs = h_ggf_htt_xsecs,
)

### ggH CP-odd decays ###

h_ggf_htt_cpo = h_ggf_htt.add_process(
    name="h_ggf_htt_cpo",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-odd",
    id=11130,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_cpo_prod_sm = h_ggf_htt_cpo.add_process(
    name="h_ggf_htt_cpo_prod_sm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-odd (prod CP-even)",
    id=11131,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_cpo_prod_mm = h_ggf_htt_cpo.add_process(
    name="h_ggf_htt_cpo_prod_mm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-odd (prod max. mix)",
    id=11132,
    xsecs = h_ggf_htt_xsecs,
)
h_ggf_htt_cpo_prod_cpo = h_ggf_htt_cpo.add_process(
    name="h_ggf_htt_cpo_prod_cpo",
    label=r"$H_{ggf}\rightarrow\tau\tau$, CP-odd (prod CP-odd)",
    id=11133,
    xsecs = h_ggf_htt_xsecs,
)

### ggH no CP hypothesis on decays###

h_ggf_htt_flat = h_ggf_htt.add_process(
    name="h_ggf_htt_flat",
    label=r"$H_{ggf}\rightarrow\tau\tau$, flat",
    id=11140,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_flat_prod_sm = h_ggf_htt_flat.add_process(
    name="h_ggf_htt_flat_prod_sm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, flat (prod CP-even)",
    id=11141,
    xsecs = h_ggf_htt_xsecs,
)

h_ggf_htt_flat_prod_mm = h_ggf_htt_flat.add_process(
    name="h_ggf_htt_flat_prod_mm",
    label=r"$H_{ggf}\rightarrow\tau\tau$, flat (prod max. mix)",
    id=11142,
    xsecs = h_ggf_htt_xsecs,
)
h_ggf_htt_flat_prod_cpo = h_ggf_htt_flat.add_process(
    name="h_ggf_htt_flat_prod_cpo",
    label=r"$H_{ggf}\rightarrow\tau\tau$, flat (prod CP-odd)",
    id=11143,
    xsecs = h_ggf_htt_xsecs,
)

### VBF processes ###    
h_vbf_htt_xsecs = {
        ecm: h_vbf_htt.get_xsec(ecm) 
        for ecm in h_vbf_htt.xsecs.keys()
}

h_vbf_htt_cpo = h_vbf_htt.add_process(
    name="h_vbf_htt_cpo",
    label=r"$H_{VBF}\rightarrow\tau\tau, CP-odd$",
    id=12101,
    xsecs = h_vbf_htt_xsecs,
)

h_vbf_htt_sm = h_vbf_htt.add_process(
    name="h_vbf_htt_sm",
    label=r"$H_{VBF}\rightarrow\tau\tau$",
    id=12102,
    xsecs = h_vbf_htt_xsecs,
)

h_vbf_htt_mm = h_vbf_htt.add_process(
    name="h_vbf_htt_mm",
    label=r"$H_{VBF}\rightarrow\tau\tau$, max. mix",
    id=12103,
    xsecs = h_vbf_htt_xsecs,
)

h_vbf_htt_flat = h_vbf_htt.add_process(
    name="h_vbf_htt_flat",
    label=r"$H_{VBF}\rightarrow\tau\tau$, flat",
    id=12104,
    xsecs = h_vbf_htt_xsecs,
)

### WH processes ###       
#W^+ H

wh_htt_cpo = wh_htt.add_process(
    name="wh_htt_cpo",
    label=r"$W(H\rightarrow\tau\tau), CP-odd$",
    id=16989,
)

wh_htt_sm = wh_htt.add_process(
    name="wh_htt_sm",
    label=r"$W(H\rightarrow\tau\tau), CP-even$",
    id=16988,
)

wh_htt_mm = wh_htt.add_process(
    name="wh_htt_mm",
    label=r"$W(H\rightarrow\tau\tau), max. mix$",
    id=16987,
)

wh_htt_flat = wh_htt.add_process(
    name="wh_htt_flat",
    label=r"$W(H\rightarrow\tau\tau), flat$",
    id=16986,
)
#W^- H


wph_htt_xsecs = { 
        13.6: Number(0.8889, {  # value for mH=125 GeV
            "scale": (0.004j, 0.007j),
            "pdf": 0.018j,
        }),  #https://arxiv.org/pdf/2402.09955
}

wph_htt_cpo = wh_htt_cpo.add_process(
    name="wph_htt_cpo",
    label=r"$W^{+}(H\rightarrow\tau\tau), CP-odd$",
    id=16999,
    xsecs = wph_htt_xsecs,
)

wph_htt_sm = wh_htt_sm.add_process(
    name="wph_htt_sm",
    label=r"$W^{+}(H\rightarrow\tau\tau), CP-even$",
    id=16998,
    xsecs = wph_htt_xsecs,
)

wph_htt_mm = wh_htt_mm.add_process(
    name="wph_htt_mm",
    label=r"$W^{+}(H\rightarrow\tau\tau), max. mix$",
    id=16997,
    xsecs = wph_htt_xsecs,
)

wph_htt_flat = wh_htt_flat.add_process(
    name="wph_htt_flat",
    label=r"$W^{+}(H\rightarrow\tau\tau), flat$",
    id=16996,
    xsecs = wph_htt_xsecs,
)
#W^- H

wmh_htt_xsecs = { 
        13.6: Number(0.5677, {  # value for mH=125 GeV
            "scale": (0.004j, 0.007j),
            "pdf": 0.018j,
        }),  #https://arxiv.org/pdf/2402.09955
}

wmh_htt_cpo = wh_htt_cpo.add_process(
    name="wmh_htt_cpo",
    label=r"$W^{-}(H\rightarrow\tau\tau), CP-odd$",
    id=16995,
    xsecs = wmh_htt_xsecs,
)

wmh_htt_sm = wh_htt_sm.add_process(
    name="wmh_htt_sm",
    label=r"$W^{-}(H\rightarrow\tau\tau), CP-even$",
    id=16994,
    xsecs = wmh_htt_xsecs,
)

wmh_htt_mm = wh_htt_mm.add_process(
    name="wmh_htt_mm",
    label=r"$W^{-}(H\rightarrow\tau\tau), max. mix$",
    id=16993,
    xsecs = wmh_htt_xsecs,
)

wmh_htt_flat = wh_htt_flat.add_process(
    name="wmh_htt_flat",
    label=r"$W^{-}(H\rightarrow\tau\tau), flat$",
    id=16992,
    xsecs = wmh_htt_xsecs,
)

### ZH processes ###       
zh_htt_xsecs = {
        ecm: zh_htt.get_xsec(ecm) 
        for ecm in zh_htt.xsecs.keys()
}#https://arxiv.org/pdf/2402.09955

zh_htt_cpo = zh_htt.add_process(
    name="zh_htt_cpo",
    label=r"$Z(H\rightarrow\tau\tau), CP-odd$",
    id=14999,
    xsecs = zh_htt_xsecs,
)

zh_htt_sm = zh_htt.add_process(
    name="zh_htt_sm",
    label=r"$Z(H\rightarrow\tau\tau)$",
    id=14998,
    xsecs = zh_htt_xsecs,
)

zh_htt_mm = zh_htt.add_process(
    name="zh_htt_mm",
    label=r"$Z(H\rightarrow\tau\tau), max. mix$",
    id=14997,
    xsecs = zh_htt_xsecs,
)

zh_htt_flat = zh_htt.add_process(
    name="zh_htt_flat",
    label=r"$Z(H\rightarrow\tau\tau), flat$",
    id=14996,
    xsecs = zh_htt_xsecs,
)





