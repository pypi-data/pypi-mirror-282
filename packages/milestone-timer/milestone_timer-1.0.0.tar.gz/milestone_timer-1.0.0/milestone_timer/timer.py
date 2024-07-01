"""Provides the MilestoneTimer."""

from time import perf_counter

import milestone_timer


class MilestoneTimer:
    """Timer that prints the time since the previous milestone.

    Parameters
    -------
    first_milestone
        Name to be used for the first milestone

    """

    def __init__(self, first_milestone: str = "timer initialised"):
        self.milestones = {first_milestone: perf_counter()}
        self.last_milestone = first_milestone

    def __str__(self):
        return str(self.milestones)

    def add_milestone(self, name: str) -> str:
        """Add a new milestone and return a time string since the last one.

        Parameters
        ----------
        name
            Name to be used for the milestone

        Returns
        -------
        str
            Message including the name of the milestone and the time since the previous one

        """
        self.milestones.update({name: perf_counter()})
        time_since_prev = self.milestones[name] - self.milestones[self.last_milestone]
        self.last_milestone = name
        return f"Milestone '{name}' timed at {time_since_prev: .3f} seconds"
