from order import Campaign
#
# campaign
#

campaign_run3_2023_preBPix_nano_tau_skim_2025_v1 = Campaign(
    name="run3_2023_preBPix_nano_tau_skim_2025_v1",
    id=320231201, 
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2023,
        "version": 14,
        "tag": "preBPix",
        "postfix" : "",
        "custom": {
            "name": "run3_2023_preBPix_nano_tau_skim_2025_v1",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2025_v1/Run3_2023"
        },
    },
)

import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1.bkgs
import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1.data
import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1.signal
import cmsdb.campaigns.run3_2023_preBPix_nano_tau_skim_2025_v1.cp_signal
