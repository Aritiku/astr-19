import math
import numpy as np

def f(x):
    return math.sin(x)

def main():
    # Define range and number of entries
    x_values = np.linspace(0, 2 * math.pi, 1000)
    
    # Print header
    print(f"{'x':>10} {'sin(x)':>15}")
    
    # Print table
    for x in x_values:
        print(f"{x:10.5f} {f(x):15.5f}")

if __name__ == '__main__':
    main()