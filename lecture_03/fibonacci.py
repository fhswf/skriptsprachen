""" Test module providing the fib() function"""

def fib(n: int) -> int: 
    """Calculate the nth Fibonacci number"""
    if n < 2:
        return [0, 1][n]
    else:
        return fib(n-1) + fib(n-2)  

if __name__ == "__main__":
    import sys
    print(fib(int(sys.argv[1])))