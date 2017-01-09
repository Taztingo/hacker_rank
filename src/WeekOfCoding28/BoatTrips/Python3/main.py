#!/bin/python3

import sys

def can_transport(trips, capacity, boats):
    maximum = capacity * boats
    for trip in trips:
        if trip > maximum:
            return "No"
    return "Yes"


def main():
    numberOfTrips, capacity, boats = input().strip().split(' ')
    numberOfTrips, capacity, boats = [int(numberOfTrips),int(capacity),int(boats)]
    trips = list(map(int, input().strip().split(' ')))
    print(can_transport(trips, capacity, boats))

main()