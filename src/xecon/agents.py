
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Agent(typing.Protocol):
    pass

# ---------------------------------------------------------------


@xt.nTuple.decorate()
class Bank(typing.NamedTuple):
    pass


@xt.nTuple.decorate()
class Consumer(typing.NamedTuple):
    pass


@xt.nTuple.decorate()
class Business(typing.NamedTuple):
    pass


@xt.nTuple.decorate()
class Government(typing.NamedTuple):
    pass


# ---------------------------------------------------------------
