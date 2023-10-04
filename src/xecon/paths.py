
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Path(typing.Protocol):

    pass


# ---------------------------------------------------------------


# states reprsent the world at a given point

# we then mask elements of the state with different possible choice trees

# under a given decision

# from which we can calcualte the payoffs per possible path of the masked state from each set of choices

# to evaluate what the agent does


# ---------------------------------------------------------------
