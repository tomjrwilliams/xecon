
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Asset(typing.Protocol):
    
    # at time? given state of the world?
    def value(self: Asset, currency: str) -> float: ...

# ---------------------------------------------------------------


@xt.nTuple.decorate()
class Account(typing.NamedTuple):
    # ie. the closest we have to cash
    # but always with the two parties explicit
    # (at least one a bank (?))
    pass


@xt.nTuple.decorate()
class Bond(typing.NamedTuple):
    pass


@xt.nTuple.decorate()
class Loan(typing.NamedTuple):
    pass


# ---------------------------------------------------------------
