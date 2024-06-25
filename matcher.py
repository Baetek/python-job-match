"""
The main person to job matching algorithm
"""

from typing import List, Optional, NewType
from dataclasses import dataclass

from jobs import Job
from members import Member
from processor import get_word_list_for_word


MatchScore = NewType('MatchScore', int)

@dataclass
class MatchedJob:
    """
    Used as an output formatting helper object
    combines a Job with a Match Score
    """
    job: Job
    score: MatchScore

class MemberJobs:
    """
    Output formatting helper object.
    Sorts and filters jobs matched to a member for
    display purposes
    """
    def __init__(self, member: Member, jobs: Optional[List[MatchedJob]]):
        self.member = member
        self.jobs = None
        if jobs:
            self.jobs = MemberJobs._sort_and_filter(jobs)

    def __repr__(self):
        return f"{self.member}, {self.jobs}"

    @staticmethod
    def _sort_and_filter(jobs: List[MatchedJob]):
        """
        Sorts and filters jobs based on their score
        """
        jobs = sorted(jobs, key=lambda job: job.score, reverse=True)
        highest_score = jobs[0].score

        ## If we have matches with a score higher than 1 let's just ignore lower grade matches
        if highest_score > 1:
            jobs = [job for job in jobs if job.score > 1]
        return jobs

def _score_jobs_for_member(member: Member, jobs: List[Job]) -> Optional[List[MatchedJob]]:
    """
    Given a member and a list of jobs

    Returns
    -------
    list
        A list of jobs that in any way seem relevant to the given member
        along with the total relevance match score for each job
    """
    def _get_match_score(member: Member, job: Job) -> MatchScore:
        """
        Calculates the total match score for a job and member pair
        Every word the member mensions that matches a particular job
        is worth one point.
        """
        match_score = 0
        for word in member.bio:
            for word in get_word_list_for_word(word):
                if word in job.location or word in job.title:
                    match_score += 1
                    break

        return MatchScore(match_score)

    jobs_for_member: List[MatchedJob] = []

    for job in jobs:
        match_score = _get_match_score(member, job)

        if match_score > 0:
            jobs_for_member.append(MatchedJob(job, match_score))

    return jobs_for_member if len(jobs_for_member) > 0 else None

def match_jobs_to_members(
    jobs: Optional[List[Job]],
    members: Optional[List[Member]]
) -> Optional[List[MemberJobs]]:
    """
    The main public function for matching members with relevant jobs.
    """
    matches = []
    if members:
        for member in members:
            if jobs:
                jobs_for_member: Optional[List[MatchedJob]] = _score_jobs_for_member(member, jobs)
                matches += [MemberJobs(member, jobs_for_member)]

    return matches if len(matches) > 0 else None
