"""
Basic semi-integration testing
"""

from typing import List

from test_fixtures import MEMBERS, JOBS

from jobs import Job
from members import Member
from matcher import match_jobs_to_members

def test_match_jobs_to_members():
    """
    Given an example list of jobs and members,
    ensure decent matches are provided
    """
    jobs: List[Job] = Job.new_from_list(JOBS)
    members: List[Member] = Member.new_from_list(MEMBERS)

    matches = match_jobs_to_members(jobs, members)

    assert str(matches) == """
        [Person(name=joe, bio=['im', 'a', 'designer', 'from', 'london', 'uk']), [MatchedJob(job=ux designer, london), score=2)], Person(name=marta, bio=['im', 'looking', 'for', 'an', 'internship', 'in', 'london']), [MatchedJob(job=legal internship, london), score=2), MatchedJob(job=sales internship, london), score=2)], Person(name=hassan, bio=['im', 'looking', 'for', 'a', 'design', 'job']), [MatchedJob(job=ux designer, london), score=1)], Person(name=grace, bio=['im', 'looking', 'for', 'a', 'job', 'in', 'marketing', 'outside', 'of', 'london']), [MatchedJob(job=software developer, london), score=1), MatchedJob(job=marketing internship, york), score=1), MatchedJob(job=data scientist, london), score=1), MatchedJob(job=legal internship, london), score=1), MatchedJob(job=sales internship, london), score=1), MatchedJob(job=ux designer, london), score=1)], Person(name=daisy, bio=['im', 'a', 'software', 'developer', 'currently', 'in', 'edinburgh', 'but', 'looking', 'to', 'relocate', 'to', 'london']), [MatchedJob(job=software developer, london), score=3), MatchedJob(job=software developer, edinburgh), score=3)]]
    """.strip()

def test_match_jobs_to_members_no_jobs_no_members():
    """
    Ensure no matches are found if no members or jobs are provided
    """
    matches = match_jobs_to_members(None, None)

    assert matches is None

def test_match_jobs_to_members_no_jobs():
    """
    Ensure no matches are found if only members are provided
    """
    members: List[Member] = Member.new_from_list(MEMBERS)

    matches = match_jobs_to_members(None, members)

    assert matches is None

def test_match_jobs_to_members_no_members():
    """
    Ensure no matches are found if only jobs are provided
    """
    jobs: List[Job] = Job.new_from_list(JOBS)

    matches = match_jobs_to_members(jobs, None)

    assert matches is None
