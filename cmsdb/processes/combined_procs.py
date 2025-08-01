# coding: utf-8

"""
Top-related process definitions.
"""

__all__ = [
    "vvt",
]

from order import Process
#
# single top + 2 vector bosons
#
#
vvt = Process(
    name="vvt",
    id=4400,
    label=f"top + VV",
)