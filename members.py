"""
Model and functions relating strictly to Members
"""

from typing import List, Dict
from processor import get_alphanumeric_with_spaces

class Member:
    """
    To make working with this data easier than strictly in dictionaries
    """
    def __init__(self, name, bio):
        self.name: str = name
        self.bio: List[str] = bio

    def __repr__(self):
        return f"Person(name={self.name}, bio={self.bio})"

    @classmethod
    def new_from_list(cls, member_list: List[Dict[str, str]]) -> List['Member']:
        """
        Processes raw member data into a list of Member objects.
        The fields are pre-processed at this stage to improve performance
        """
        return [
            cls(
                member['name'].lower(),
                get_alphanumeric_with_spaces(member['bio']).lower().split(" ")
            )
            for member in member_list
        ]
