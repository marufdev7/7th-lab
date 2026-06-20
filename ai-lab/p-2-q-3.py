# Experiment No: 03
# Experiment Name:
# Write a problem to solve Tower of hanoi Problem
# Source Code:

def tower_of_hanoi(n, src, aux, des):
    if n == 1:
        print(f"Move disk 1 from {src} to {des}")
        return
    tower_of_hanoi(n-1, src, des, aux)
    print(f"Move disk {n} from {src} to {des}")
    tower_of_hanoi(n-1, aux, src, des)

n = int(input("Enter the number of Disk = "))
tower_of_hanoi(n, 'A', 'B', 'C')

# Output:
# Enter the number of Disk = 3
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C