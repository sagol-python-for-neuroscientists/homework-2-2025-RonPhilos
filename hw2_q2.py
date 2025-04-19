from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    def pairs (agent1, agent2):
        if agent1 is None or agent2 is None:
            return [a for a in (agent1, agent2) if a]
        a, b = agent1, agent2
        a_cat, b_cat = a.category, b.category
    #positive meetings#
        if a_cat == Condition.CURE:
            if b_cat == Condition.SICK:
                b = b._replace(category=Condition.HEALTHY)
            elif b_cat == Condition.DYING:
                b = b._replace(category=Condition.SICK)
        if b_cat == Condition.CURE:
            if a_cat == Condition.SICK:
                a = a._replace(category=Condition.HEALTHY)
            elif a_cat == Condition.DYING:
                a = a._replace(category=Condition.SICK)
    #negative meetings#
        if a_cat == Condition.SICK and b_cat ==Condition.SICK:
                a = a._replace(category=Condition.DYING)
                b = b._replace(category=Condition.DYING)
        elif a_cat == Condition.SICK and b_cat ==Condition.DYING:
                a = a._replace(category=Condition.DYING)
                b = b._replace(category=Condition.DEAD)
        elif a_cat == Condition.DYING and b_cat ==Condition.SICK:
                a = a._replace(category=Condition.DEAD)
                b = b._replace(category=Condition.DYING)
        elif a_cat == Condition.DYING and b_cat ==Condition.DYING:
                a = a._replace(category=Condition.DEAD)
                b = b._replace(category=Condition.DEAD)

        return [a,b]
    
    meeting_agents = [agent for agent in agent_listing if agent.category not in (Condition.HEALTHY, Condition.DEAD)]
    updated = []
    i = 0
    while i < len(meeting_agents):
        agent1 = meeting_agents[i]
        if i + 1 < len(meeting_agents):
            agent2 = meeting_agents[i + 1]
            updated.extend(pairs(agent1, agent2))
            i += 2
        else:
            updated.append(agent1)
            i += 1

    untouched = [agent for agent in agent_listing if agent.category in (Condition.HEALTHY, Condition.DEAD)]
    return updated + untouched