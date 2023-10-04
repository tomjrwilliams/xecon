
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Model(typing.Protocol):

    pass

# ---------------------------------------------------------------


#  models are how agents make decisons

# ie. they produce paths from the state outward


# interestingly mdoels only have to cover

# those variables needed for each agents payoff


# and can eg. aggregate / ignore others

# ---------------------------------------------------------------


# and don't need to be causal dynamics


# as they aren't use to iterate the step forward

# that's the dynamics



# they're each agents model of their own variables of interest

# likely highly local, specific to the agent


# but do need to be able to produce entire paths of those vairables

# out from the current masked state


# ie. local in variables, but need to be evaluated out into the future


# ---------------------------------------------------------------


# crucially there needs to be no sense in which

# the model is approximating the dynamic


# they're in some sense completely unrelated


# ---------------------------------------------------------------
