from order import Campaign
#
# campaign
#

campaign_run3_2022_postEE_v1_nano_tau_v14 = Campaign(
    name="run3_2022_postEE_v1_nano_tau_v14",
    id=20221434,  # run 2 year 2022 ver 14 #33 is just for separation between different configs
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2022,
        "version": 14,
        "tag": "postEE",
        "custom": {
            "name": "run3_2022_postEE_v1_nano_tau_v14",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v1/Run3_2022EE"
        },
    },
)

import cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14.ewk
import cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14.data
import cmsdb.campaigns.run3_2022_postEE_v1_nano_tau_v14.top
#import cmsdb.campaigns.run3_2022_preEE_nano_tau_v12.signal
