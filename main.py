"""
Implementation of an exercise of matching
people with jobs that may suit them

Calls external API's to retrieve a list of people and a list of jobs
and finds people suitable jobs
"""

from typing import List

import api
from jobs import Job
from members import Member
from matcher import match_jobs_to_members


if __name__ == '__main__':
    jobs: List[Job] = Job.new_from_list(api.get_jobs())
    members: List[Member] = Member.new_from_list(api.get_members())

    matches = match_jobs_to_members(jobs, members)

    if matches:
        for match in matches:
            print(f"Member: {match.member}\nMatching Jobs: {match.jobs}\n")
