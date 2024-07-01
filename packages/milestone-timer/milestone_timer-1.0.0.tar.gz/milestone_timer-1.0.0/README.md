# Milestone Timer

A minimalist Python package to allow you to time different sections of your code.

## Basic usage

Initialise a MilestoneTimer when you want the clock to start.

```python
mt = MilestoneTimer()
```

Then add timing points in your code.

```python
mt.add_milestone("Loaded config file")
```

## Examples

```python
import logging
from time import sleep
from milestone_timer import MilestoneTimer

log_format_string = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(
    level="DEBUG",
    format=log_format_string,
)

logger = logging.getLogger(__name__)

mt = MilestoneTimer("Let's play!")

# Code here to meet the contestants
sleep(0.1)

logger.debug(mt.add_milestone("Met the contestants"))

# Code here to rotate the board
sleep(0.2)

logger.debug(mt.add_milestone("Rotated board"))

# Code here for numberwang
sleep(0.05)

logger.debug(mt.add_milestone("That's numberwang"))

print(mt)  # Equivalently, `print(mt.milestones)`, this is the underlying dict
```

STDERR:

```text
2024-06-22 20:00:30,433 | DEBUG | __main__ | Milestone 'Met the contestants' timed at  0.105 seconds
2024-06-22 20:00:30,635 | DEBUG | __main__ | Milestone 'Rotated board' timed at  0.202 seconds
2024-06-22 20:00:30,690 | DEBUG | __main__ | Milestone 'That's numberwang' timed at  0.055 seconds
```

STDOUT:

```text
{"Let's play!": 17469.432649541, 'Met the contestants': 17469.537295625, 'Rotated board': 17469.739114875, "That's numberwang": 17469.794010833}
```