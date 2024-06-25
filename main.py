
from typing import List, Tuple, Optional

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


## We assumed the program can fail and the upstream will try again if so
## We can do some logging
## Work on error handling
## NLP ?
## There are efficiency gains to be had with the word cloud generator and the from list back to list on sentences
# Run through pydantic?
# Add comments
# Docker?
# requirements

# Fallible to negatives e.g "Somewhere outside of London" will find London jobs
# Fallible to context e.g "Edinburgh right now but relocating to London" will find both Edinburgh and London jobs,

# This could be worked around with hacks like "ignore next matching word after "relocating", "outside", "without", but then would fail for "relocating to london from edinburgh".
# natural language processing libraries or AI would be required to solve this more properly.
# Since the ambiguties seem to come from user bios, one AI run through per user bio edit, could correctly populate their desired job title and desired location fields
# And this could be quite cost effective since the cost would be a fraction of a penny per bio edit. This could be cheaper than server costs for running extensive hand written python logic.

# Trade off between processing and data storage on parsing fields like bio to alphanumerics
