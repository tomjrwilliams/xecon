
from __future__ import annotations

import typing

import xtuples as xt

# ---------------------------------------------------------------

class Decision(typing.Protocol):
    
    # decisions are equipped with a number of choices

    # each with a differentiable payoff function
    # of either a boolean
    # or continuous variable (s?)

    # where the agent then picks the max decision choice
    # given the max point of the relevant choices 
    
    pass

class Consequence(typing.Protocol):

    # consequences are tree shaped relationships between decision-choices and other decisions

    # where choosing choice A from decision 1

    # means having to make decision 2

    # and so on
    # with the final payoff then evaluated per possible path through
    # the tree

    # ie. we pass the masked state through the decision tree
    # with the payoff decided as the sum over the branches?

    # or no - the payoff is then calculated from the possible paths

    # given a certain decision-masked state representation

    # where we have one such decision masked state per final leaf node in the decision tree
    
    pass

# ---------------------------------------------------------------

# loans are then consumer driven
# given funding needs, they're matched to the right point on the curve
# and take the best of the banks available to them?

# presumably balanced against the neg-payoff from not taking the loan?
# or we assume for now they have no decision

# ---------------------------------------------------------------

# alternative decision is bankruptcy?

# ie. so eventually cost given credit rating raises beyond the point
# it makes sense not to default?

# but investment can always be cut back
# so it does make sense to have a neg payoff for new investment

# ie. that's an optimisation decision
# bankruptcy is more likely from existing debt maturing

# ---------------------------------------------------------------

# so the outflow arrival process

# needs to come equipped with some kind of return on capital estimate
# an expected profit / in a certain time (?) related to the flow

# or a knock-on cost from not paying it

# ---------------------------------------------------------------

# ie. they're decisions?

# always represented as (at least?) two choices

# even a continuous range of values

# so presumably where the decision of one
# eg. the price quote response from locating the consumer on surface

# can feed into the parametrisation of the other agent

# ---------------------------------------------------------------

# where presumably there has to be some linkage

# constraints

# such that choosing to invest cash you don't have, means also choosing to take out a loan

# sort of conditional action trees

# where taking it has consquences and you recursively explore the tree

# until no more consequences, and then compare between the potential nodes

# for their expected payoffs

# ---------------------------------------------------------------

# the ideal case is that we have a completely closed form

# payoff max decision, rather than any kind of optimisation

# though as soon as we allow continuous values
# we need a generic way of picking the optimal point on whatever surface that is

# per decision, and then optimsing between them

# ---------------------------------------------------------------
