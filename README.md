# ants.py

This is my entry for the [2011 Google AI Challenge](http://aichallenge.org/) in which I reimplemented the ants-protocol layer to solve the problem of friendly ants stepping on each other at a low level. In the end I made it to the 77th percentile.

## Usage

If you have the official [tools](http://aichallenge.org/using_the_tools.php) you can play a game with one of my bots via *MyBot.py* or one of the decider-specific _bot*.py_ files. 

* ```$ python2 botBrownian.py``` moves each ant randomly. Since ants cannot step on eachother, they diffuse outward from the anthills.
* ```$ python2 botNavigator.py``` assigns each idle ant to a goal. Ants' goals persist between turns, and unassigned ants diffuse randomly.
* ```$ python2 botKMeans.py``` finds *k* goals and assigns ants to each of *k* clusters. Goals have associated *too close* and *too far* radii, so ants behave differently for different goals.
* ```$ python2 botHedge.py``` runs 13 simplistic strategies and probabalistically applies them. Then it judges ant behavior based on who collected food without dying and learns to trust or distrust each of the 13 strategies. *See the **metadecider** directory.*

## More Info

* These bots were part of a [project](http://www.ccs.neu.edu/home/jaa/CS6140.11F/Homeworks/finalProject.html) for my Fall 2011 [machine learning class](http://www.ccs.neu.edu/home/jaa/CS6140.11F/).
* I wrote [a report](https://docs.google.com/document/d/1MB0IAFvgE2BEx4_PUJ1wvHeEERwt_C9YSU4E4FY2gHA/edit) which explains how I attempted to adapt a hedge learner to the ants competition.
* You can [watch games](http://aichallenge.org/profile.php?user=2184) my bots played in the competition.

---

Requires Python 2.7