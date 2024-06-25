from typing import List, Any, Dict

class Job:
    def __init__(self, title, location):
        self.title: List[str] = title
        self.location: List[str] = location

    def __repr__(self):
        return f"{" ".join(self.title)}, {" ".join(self.location)})"

    @classmethod
    def new_from_list(cls, jobs_list: List[Dict[str, str]]) -> List['Job']:
        return [cls(job['title'].lower().split(), job['location'].lower().split()) for job in jobs_list]
