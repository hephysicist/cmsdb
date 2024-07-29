# coding: utf-8

"""
TBU
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_nano_tau_v12 = Campaign(
    name="run3_2022_preEE_nano_tau_v12",
    id=20221233,  # run 2 year 2022 ver 12 #33 is just for separation between different configs
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2022,
        "version": 12,
        "custom": {
            "name": "run3_2022_preEE_nano_tau_v12",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022"
        },
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_tau_v12.data
import cmsdb.campaigns.run3_2022_preEE_nano_tau_v12.top
import cmsdb.campaigns.run3_2022_preEE_nano_tau_v12.ewk
import cmsdb.campaigns.run3_2022_preEE_nano_tau_v12.signal
