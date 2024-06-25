"""
Model and functions relating strictly to Jobs
"""

from typing import List, Dict

class Job:
    """
    To make working with this data easier than strictly in dictionaries
    """
    def __init__(self, title, location):
        self.title: List[str] = title
        self.location: List[str] = location

    def __repr__(self):
        return f"{' '.join(self.title)}, {' '.join(self.location)})"

    @classmethod
    def new_from_list(cls, jobs_list: List[Dict[str, str]]) -> List['Job']:
        """
        Processes raw jobs data into a list of Job objects.
        The fields are pre-processed at this stage to improve performance
        """
        return [
            cls(
                job['title'].lower().split(),
                job['location'].lower().split()
            )
            for job in jobs_list
        ]
