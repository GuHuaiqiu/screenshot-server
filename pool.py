#!/usr/bin/env python
import sys
from worq.pool.process import WorkerPool
from tasks import init

def main(url, **kw):
    broker = init(url)
    pool = WorkerPool(broker, init, workers=2)
    pool.start(**kw)
    return pool

if __name__ == '__main__':
    main(sys.argv[-1])