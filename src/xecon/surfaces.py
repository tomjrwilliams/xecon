
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Surface(typing.Protocol):
    
    # at time? given state of the world?
    def value(self: Surface, currency: str) -> float: ...

# ---------------------------------------------------------------

# at each point in time
# each bank maintains a loan surface
# of what they're willing to lend at
# per maturity and credit rating

# and how much?

# where presumably they start their surface

# from the (shared?) market observable (government?) bond surface

# ---------------------------------------------------------------

# similar model of government funding needs
# and business

# random arrival process of outflow requirements
# which if beyond current accounts

# are met by issuing a bond at the 'market' surface

# ---------------------------------------------------------------
