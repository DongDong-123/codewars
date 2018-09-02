import sys
import time


def progress_bar(num, total):
    rate = float(num)/total
    ratenum = int(100*rate)
    r = '\r[{}{}]{}%'.format('*'*ratenum, ' '*(100-ratenum), ratenum)
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == "__main__":
    i, n = 0, 1000
    for i in range(n):
        time.sleep(0.1)
        progress_bar(i + 1, n)