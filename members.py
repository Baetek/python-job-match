from typing import List, Any, Dict
from processor import get_alphanumeric_with_spaces

class Member:
    def __init__(self, name, bio):
        self.name: str = name
        self.bio: List[str] = bio

    def __repr__(self):
        return f"Person(name={self.name}, bio={self.bio})"

    @classmethod
    def new_from_list(cls, member_list: List[Dict[str, str]]) -> List['Member']:
        return [cls(member['name'].lower(), get_alphanumeric_with_spaces(member['bio']).lower().split(" ")) for member in member_list]

