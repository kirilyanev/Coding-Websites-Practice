queries = int(input())

for polygon in range(0, queries):
    polygon_sides = int(input())

    # Total Cycles = 2 * N – 1) + (N – 1) * (N – 2)
    total_cycles = (2 * polygon_sides - 1) + (polygon_sides - 1) * (polygon_sides - 2)

    print(total_cycles)
