#!/usr/bin/python3

"""Module that calculate how many square units of water
    will be retained after it rains."""


def rain(walls):
    """Return integer indicating total amount of rainwater retained."""
    water_amount = 0

    for i in range(1, len(walls) - 1):

        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        water_amount += (min(left, right) - walls[i])

    return water_amount
