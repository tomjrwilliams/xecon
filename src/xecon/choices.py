
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Choice(typing.Protocol):

    def mask(self: Choice, state: tuple) -> float: ...

# ---------------------------------------------------------------

class Discrete(Choice):

    pass

# ---------------------------------------------------------------

class Continuous(Choice):

    pass

# ---------------------------------------------------------------

# payoff is calculated given a certain model of the world from the agent?

# so is a function
# that takes a fucntion - the model

# and passes in the relevant choice variable?

# ---------------------------------------------------------------

# or takes a model (function from state to payoff)

# and a state variable

# and a choice value (given by the decision?)

# and masks the state with the choice value

# and then calls the model on the state

# to return the payoff

# ---------------------------------------------------------------

# then at the decision layer

# for each choice

# for each possible value of the choice

# we can generate payoff samples, given the state and payoff model per choice

# and then (naive solution?) simply take the max payoff (and thus choice and value)

# for each in the relevant decision tree, given any decision consequences

# ---------------------------------------------------------------

# we don't even need any backprop yet?

# but where that presuambly comes in on the basis of

# how we fit those models, presuming the agents learn

# if we then have an actual payoff, we can use some kind of rl

# to fit against the payoff estimates of the payoff-models

# ---------------------------------------------------------------

# so in fact, contra the above

# the payoff is not a function of the choice at all

# the choice just masks the state

# from which we derive possible (agent models of) the potential world paths

# and then from the world paths, we have a per agent payoff function

# ---------------------------------------------------------------


# so choices don't have individual payoff functions


# but they do have indivudla models

# which are how we generate possible paths?


# or even not? the model is also per agent?

# with the masking by the choices done at state level


# which the model then evolves into paths

# which is then fed to the payoff function



# ---------------------------------------------------------------

