# !/usr/bin/env python3
# encoding: utf-8

"""
    Find all circular (clockwise) tours a truck can take to visit all petrol pumps arranged in a circle. Assume:
        c[] has distance from each petrol pump to next.
        p[] has amount of petrol at every pump.
        The truck has to stop at and use all petrol at each pump. The truck has infinite capacity.
        For 1 unit petrol, the truck can go 1 unit of distance.

    @author: Mohammed Ataaur Rahaman
"""


def path1(ditances, fuel, tank, travelled, current_city, visited):
    if current_city is None:
        for i in range(len(distances)):
            path1(distances, fuel, tank + fuel[i], distances[i], (i + 1)%len(distances), visited + 1)
        return

    if visited == len(ditances):
        return print(current_city)

    if tank - travelled < 0:
        return

    path1(distances, fuel, tank - travelled + fuel[current_city], distances[current_city], (current_city + 1)%len(distances), visited + 1)


def path2(distances, fuel, cities_left, current_city, tank):
    if current_city is None:
        for i in range(cities_left):
            path2(distances, fuel, cities_left, i, 0)
        return

    if not cities_left:
        return print(current_city)

    fuel_left = tank + fuel[current_city] - distances[current_city]
    if fuel_left >= 0:
        path2(distances, fuel, cities_left -1, (current_city + 1)%len(distances), fuel_left)


if __name__ == '__main__':
    distances = [4, 3, 9, 5]
    fuel = [1, 2, 10, 8]

    print(f"Cities to start from (algo I): ")
    path1(distances, fuel, 0, 0, None, 0)

    print(f"Cities to start from (algo II): ")
    path2(distances, fuel, len(distances), None, 0)