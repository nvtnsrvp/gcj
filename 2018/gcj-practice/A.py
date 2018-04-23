import sys

def recurse_guess_number(a, b, n):
    mid = (a+b)/2
    sys.stderr.write(str(mid))
    s = sys.stdin.readline()
    if n < 0:
        raise "LIMIT_REACHED"
    if s == "CORRECT":
        return
    elif s == "TOO_BIG":
        guess_number(a, mid, n-1)
    elif s == "TOO_SMALL":
        guess_number(mid+1, b, n-1)
    else:
        raise "WRONG_ANSWER"

def guess_number(a, b, n):
    with open("logger.out", "wb") as logger:
        for i in range(n):
            mid = (a+b)/2
            print mid
            s = sys.stdin.readline()
            logger.write("Guess: "+str(mid)+ " Read: "+s)
            looger.flush()
            if s == "CORRECT":
                return
            elif s == "TOO_BIG":
                b = mid
            elif s == "TOO_SMALL":
                a = mid + 1
            else:
                raise "WRONG_ANSWER"

t = int(sys.stdin.readline().strip())
for i in range(t):
    a, b  = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().strip())
    guess_number(a, b, n)

