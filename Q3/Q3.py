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
    #determine the maximum length of the pattern
    tmp = population
    pattern_length = 1
    #since a number has a domain of ten and a letter has a domain of 26
    #the formula for finding the total number of plates tells us that the
    #smallest pattern for a given population will be all "L"s and the
    #largest pattern will be all "N"s
    #for this reason dividing the population repeatedly by ten will give
    #us the maximum length
    while(tmp/10>1):
        tmp /= 10
        pattern_length += 1
    
    #we store the pattern in a dictionary with the keys corresponding to
    #pattern length and the values being a list of two-tuples
    #containing the total plates and the pattern
    patterns = dict({0: [(1,"")]})
    for i in range(pattern_length):
        old = patterns[i]
        new = []
        #to determine the next pattern in the sequence we simply take the
        #old pattern and add "N" and "L" to the end of it
        new += [(total_plates(p+"N"), p+"N") for (x, p) in old]
        new += [(total_plates(p+"L"), p+"L") for (x, p) in old]
        #if you give dict() a list of two-tuples, it will build a dictionary
        #with the first value of the tuple as the key and the second as the value
        #Because of the property of dictionaries not having duplicate keys, the
        #following line will eliminate patterns that generate the same number of
        #total plates.
        new = list(dict(new).items())
        patterns[i+1] = new
    #next we want to sort the patterns by total plates.  To do this we make a list
    #out of the values in the patterns dict, make it into a dictionary with the
    #total plates as the key, sort the keys, and find the proper key/pattern pair.
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
    """Determine the total plates a given pattern will generate.
    The formula that determines how many plates a pattern will gneerate
    is pretty simple.  All you do is multiple each token's domain together,
    e.g. "NNL" = 10*10*26 = 260 plates."""
    total = 1
    for p in pattern:
        if p=="N":
            total *= 10
        if p=="L":
            total *= 26
    return total
if __name__ == "__main__":
    #We use the argparse library to get the population from the command-line
    parser = argparse.ArgumentParser(description='IGN Code-Foo Q3')
    parser.add_argument('population', type=int, help="The population to generate a pattern for")
    args = parser.parse_args()
    (pattern, total, excess, prevp, nextp) = find_pattern(args.population, 'N')
    print("Pattern: ", pattern)
    print("Total: ", total)
    print("Excess: ", excess)
    print("Previous pattern: ", prevp)
    print("Next pattern: ", nextp)
