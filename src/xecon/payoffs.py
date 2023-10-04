
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Payoff(typing.Protocol):

    def evaluate(self: Payoff, state: tuple) -> float: ...

# ---------------------------------------------------------------

# agent models of the payoff of certain choices

# where a choice just masks an element of the state

# and hence is really just the payoff of a given state of the world

# rolled forward (?)

# ---------------------------------------------------------------

# so rather a given realisation of the path of the world

# or, rather, expectation over the possible paths of the world

# from the current state

# ---------------------------------------------------------------

# so payoffs are evaluated based entirely on world path realisations

# given current state

# choices are just used to mask over that state, from which we derive the possible paths

# ---------------------------------------------------------------
