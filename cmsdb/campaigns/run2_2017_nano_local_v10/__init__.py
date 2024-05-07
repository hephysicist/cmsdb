# coding: utf-8

"""
Common, analysis independent definition of the 2017 data-taking campaign
with datasets at NanoAOD tier in version 9.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run2_2017_nano_local_v10 = Campaign(
    name="run2_2017_nano_local_v10",
    id=220172,
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2017,
        "version": 10,
    },
)


# trailing imports to load datasets
#import cmsdb.campaigns.run2_2017_nano_local_v10.data  # noqa
import cmsdb.campaigns.run2_2017_nano_local_v10.ewk  # noqa
import cmsdb.campaigns.run2_2017_nano_local_v10.higgs  # noqa
