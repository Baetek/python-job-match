# python-job-match

## Getting started

- Clone repo
- In the repo create a virtual environment `python -m venv .venv`
- Activate the virtual environment `source .venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`

### Running the program

`python main.py`

### Running the tests

`pytest tests.py`

## Time constraint limitations

- Logging, a production program should include logging at applicable levels, so that e.g we can see the basics of what's going at INFO level, or are able to quickly find the cause of an issue at DEBUG level even if the program doesn't crash but doesn't behave as expected

- Crash handling, while some care was taken to avoid Iterating over None situations, handling API failures, and strict typing with PyRight to ensure everything is at is should be. For real programs a decision should be made whether or not the program is allowed to crash and in what circumstances. In some environments a 500 server error might be fine while in others a program should always aim to recover and report errors softly.

- Testing, the test set is quite limited

- Docker / Runtime, a Makefile, Justfile, Dockerfile type tooling could be included to allow easy and consistent running and testing of the application.

- Diagrams, state flow diagrams should be included to allow easy reasoning about the programs behaviour

- Formatting and output presentation

- Consistency across codebase

## General approach limitations

### Matching algorithm

- Fallible to negatives e.g "Somewhere outside of London" will find London jobs
- Fallible to context e.g "Edinburgh right now but relocating to London" will
find both Edinburgh and London jobs,

This could be worked around with hacks like "ignore next matching word after
"relocating", "outside", "without", but then would fail for "relocating to
london from edinburgh". I understand the purpose of this exercise is to test code quality more than how close I can get to perfect member / job matches.

Outside of "hacky" logic, a better solution might be an NLP (Natural Language Processing) library, or since the ambiguties seem to come from user bios, this means that a single AI run through per user
bio edit, could correctly populate their desired job title and desired location
fields. Fixing the fallable example above. This could be quite cost effective since the cost would be a fraction of
a penny per bio edit. This could be cheaper than server costs for running
extensive hand written python logic.

### Efficiency

There's a large trade off between CPU time and memory on this task without a clear ideal pick. A database / persistent storage would make it clear that CPU time is more valuable than memory.

So in the real world the ideal thing to do would likely be to pre-process all the data fields, such as .lower(), .alphanumeric_with_spaces(), .split(), get_word_list_for_word(). As as I mentioned most of this only needs done once per user profile edit or job listing change. Since profile edits likely occur far less often than generating lists of matches, this would be far more efficient than doing all the processing on every match algorithm run.
