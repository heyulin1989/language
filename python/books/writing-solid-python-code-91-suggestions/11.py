class Seasons:
	Spring = 0
	Summer = 1
	Autumn = 2
	Winter = 3
	Spring,Summer,Autumn,Winter = range(1,5,1)

print Seasons.Spring

def enum(*posarg, **keysarg):
	return type("Enum", (object,), dict(zip(posarg, xrange(len(posarg))), **keysarg))
Seasons = enum("Spring", "Summer", "Autumn", Winter=1)
print Seasons.Spring, Seasons.Summer

from collections import namedtuple
Seasons = namedtuple('Seasons', 'Spring Summer Autumn Winter')._make(range(4))

print Seasons.Spring, Seasons.Summer

from flufl.enum import Enum
class Seasons(Enum):
	Spring = "Spring"
	Summer = 2
	Autumn = 3
	Winter = 4

