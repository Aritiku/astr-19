import numpy as np

#defines function
def f(x):
    return x**3 + 8

#tells to find at x=9
def main():
    x = 9
    result = f(x)
    print("f(9) =", result)

    if result > 27:
        print("YAY!")


if __name__ == '__main__':
    main()