def tower_of_hanoi(n, from_r, to_r, aux_r):
    if n == 0:
        return
    tower_of_hanoi(n - 1, from_r, aux_r, to_r)
    print("move circle", n, "from r", from_r, "to r", to_r)
    tower_of_hanoi(n - 1, aux_r, to_r, from_r)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
