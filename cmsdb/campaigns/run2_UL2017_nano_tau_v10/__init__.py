# coding: utf-8

"""
TBU
"""

from order import Campaign


#
# campaign
#

campaign_run2_UL2017_nano_tau_v10 = Campaign(
    name="run2_UL2017_nano_tau_v10",
    id=20171033,  # year 2017 ver 10, 33 is just for separation between different configs
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2017,
        "version": 10,
        "custom": {
            "name": "run2_UL2017_nano_tau_v10",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/HTT_skim_v1/Run2_2017"
        },
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run2_UL2017_nano_tau_v10.data
import cmsdb.campaigns.run2_UL2017_nano_tau_v10.h_ggf_tautau
import cmsdb.campaigns.run2_UL2017_nano_tau_v10.ewk

