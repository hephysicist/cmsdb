from order import Campaign
#
# campaign
#

campaign_run3_2022_postEE_nano_tau_skim_2025_v1 = Campaign(
    name="run3_2022_postEE_nano_tau_skim_2025_v1",
    id=20221444,  # run 2 year 2022 ver 14 #33 is just for separation between different configss
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 14,
        "tag": "postEE",
        "custom": {
            "name": "run3_2022_postEE_nano_tau_skim_2025_v1",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2025_v1/Run3_2022EE"
        },
    },
)

import cmsdb.campaigns.run3_2022_postEE_nano_tau_skim_2025_v1.bkgs
import cmsdb.campaigns.run3_2022_postEE_nano_tau_skim_2025_v1.data
import cmsdb.campaigns.run3_2022_postEE_nano_tau_skim_2025_v1.signal

