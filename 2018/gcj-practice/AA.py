import sys

with open("logger.out", "wb") as logger:
    a = sys.stdin.readline()
    logger.write(a)
    print "3"
