from order import Campaign
#
# campaign
#

campaign_run3_2023_preBPix_nano_tau_skim_v2 = Campaign(
    name="run3_2023_preBPix_nano_tau_skim_v2",
    id=20231401,  # run 3 year 2022 ver 12 #01 is just for separation between different configs
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2023,
        "version": 14,
        "tag": "preBPix",
        "run": 3,
        "custom": {
            "name": "run3_2023_preBPix_nano_tau_skim_v2",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023"
        },
    },
)

import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2.ewk
import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2.data
import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_v2.top

