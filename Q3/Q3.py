#!/usr/bin python3
"""IGN Code-Foo Question 3
You own a license plate manufacturing company. Given a population, determine the simplest pattern that will produce enough unique plates. Since all the plates that match the pattern will be generated, find the pattern that produces the least excess plates. Use a combination of letters (A-Z) and numbers (0-9).

EXAMPLE 1
Population: 10
Pattern: 1 number
Total Plates: 10
Excess Plates: 0

EXAMPLE 2
Population: 25
Pattern: 1 letter
Total Plates: 26
Excess Plates: 1

Example 3
Population: 12          Population: 12
Pattern: 2 numbers      Pattern: 1 letter
Total Plates: 100       Total Plates: 26
Excess Plates: 88       Excess Plates: 14

To find the total plates you simply multiply each token's set size together, e.g. 1 number, 2 letters = 10*26*26.
"""

import argparse
import math

def find_pattern(population, pattern):
    """Determines the correct pattern to use for the population"""
    tmp = population
    pattern_length = 1
    while(tmp/10>1):
        tmp /= 10
        pattern_length += 1

    """patterns = [[""]]
    #generate the patterns
    for i in range(pattern_length):
        for p in patterns[i]:
            patterns.append([p+"N", p+"L"])
            #patterns.append([p+"N"])
            #patterns.append([p+"L"])"""
    patterns = dict({0: [(1,"")]})
    for i in range(pattern_length):
        old = patterns[i]
        new = []
        new += [(total_plates(p+"N"), p+"N") for (x, p) in old]
        new += [(total_plates(p+"L"), p+"L") for (x, p) in old]
        new = list(dict(new).items())
        patterns[i+1] = new
    tps = []
    for tp in patterns.values():
        tps += [(t, p) for (t, p) in tp]
    patterns = dict(tps)
    sortedpatterns = dict()
    sortedkeys = sorted(list(patterns.keys()))
    for t in sortedkeys:
        if t<population:
            continue
        else:
            prevp = patterns[sortedkeys[sortedkeys.index(t)-1]]
            nextp = patterns[sortedkeys[sortedkeys.index(t)+1]]
            return (patterns[t], t, (t-population), prevp, nextp)

def total_plates(pattern):
    """Determine the total plates a given pattern will generate"""
    total = 1
    for p in pattern:
        if p=="N":
            total *= 10
        if p=="L":
            total *= 26
    return total
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='IGN Code-Foo Q3')
    parser.add_argument('population', type=int, help="The population to generate a pattern for")
    args = parser.parse_args()
    (pattern, total, excess, prevp, nextp) = find_pattern(args.population, 'N')
    print("Pattern: ", pattern)
    print("Total: ", total)
    print("Excess: ", excess)
    print("Previous pattern: ", prevp)
    print("Next pattern: ", nextp)
