# coding: utf-8

"""
TBU
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_tau_spinner = Campaign(
    name="run3_2022_preEE_tau_spinner",
    id=20221234,  # run 2 year 2022 ver 12 #33 is just for separation between different configs
    ecm=13.6,
    bx=25, #???
    aux={
        "tier"      : "NanoAOD",
        "year"      : 2022,
        "version"   : 12,
        "tag"       : "preEE",
        "custom"    : {
                      "creator": "desy",
                      "location": "/eos/cms/store/group/phys_tau/ksavva/archive/htt_skim_v1/Run3_2022",  
        },
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_tau_spinner.higgs
