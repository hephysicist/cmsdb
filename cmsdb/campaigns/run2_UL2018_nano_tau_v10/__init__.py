# coding: utf-8

"""
TBU
"""

from order import Campaign


#
# campaign
#

campaign_run2_UL2018_nano_tau_v10 = Campaign(
    name="run2_UL2018_nano_tau_v10",
    id=20181033,  # run 2 year 2022 ver 12 #33 is just for separation between different configs
    ecm=13,
    bx=25, #???
    aux={
        "tier": "NanoAOD",
        "year": 2018,
        "version": 10,
        "custom": {
            "name": "run2_UL2018_nano_tau_v10",
            "creator": "desy",
            "location": "root://eoscms.cern.ch/eos/cms/store/group/phys_tau/TauFW/nanoV10/Run2_2018/",  
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_UL2018_nano_tau_v10.data
