#!/usr/bin/env python
import sys

from worq import get_queue
from worq import get_broker, TaskSpace
from worq.pool.thread import WorkerPool 
from browser import get_other

other_q=None
pool_other=None

url_other="memory://"
name_other=__name__
ts_other = TaskSpace(name_other)

def init_pool_other():        
    global other_q,pool_other
    broker_other = get_broker(url_other,name="3")
    broker_other.expose(ts_other)
    other_q = broker_other.queue()
    
    pool_other = WorkerPool(broker_other,  workers=1)
    pool_other.start()


def init_other():
#    ts_other.task(start,"start")
    init_pool_other()

    
def deinit_other():
    pool_other.stop()    

@ts_other.task
def start(id,url):
    return get_other().start(id,url)        
    
def get_other_q():
    return other_q    