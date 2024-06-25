from typing import List, Tuple, Optional, NewType
from dataclasses import dataclass

import api
from jobs import Job
from members import Member
from processor import get_word_list_for_word


MatchScore = NewType('MatchScore', int)

@dataclass
class MatchedJob:
    job: Job
    score: MatchScore


class MemberJobs:
    def __init__(self, member: Member, jobs: Optional[List[MatchedJob]]):
        self.member = member
        self.jobs = None
        if jobs:
            self.jobs = MemberJobs._sort_and_filter(jobs)

    def __repr__(self):
        return f"{self.member}, {self.jobs}"

    @staticmethod
    def _sort_and_filter(jobs: List[MatchedJob]):
        jobs = sorted(jobs, key=lambda job: job.score, reverse=True)
        highest_score = jobs[0].score

        if highest_score > 1: ## If we have matches with a score higher than 1 let's just ignore lower grade matches
            jobs = [job for job in jobs if job.score > 1]
        return jobs


def _score_jobs_for_member(member: Member, jobs: List[Job]) -> Optional[List[MatchedJob]]:
    jobs_for_member: List[MatchedJob] = []
    for job in jobs:
        match_score = _get_match_score(member, job)
        if match_score > 0:
            jobs_for_member.append(MatchedJob(job, match_score))

    return jobs_for_member if len(jobs_for_member) > 0 else None

def _get_match_score(member: Member, job: Job) -> MatchScore:
    match_score = 0
    for word in member.bio:
        for word in get_word_list_for_word(word):
            if word in job.location:
                match_score += 1
                break

            if word in job.title:
                match_score += 1
                break

    return MatchScore(match_score)

def match_jobs_to_members(jobs: Optional[List[Job]], members: Optional[List[Member]]) -> Optional[List[MemberJobs]]:
    matches = []
    if members:
        for member in members:
            if jobs:
                jobs_for_member: Optional[List[MatchedJob]] = _score_jobs_for_member(member, jobs)
                matches += [MemberJobs(member, jobs_for_member)]

    return matches if len(matches) > 0 else None
