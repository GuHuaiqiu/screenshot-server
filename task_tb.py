#!/usr/bin/env python
import sys
from worq import get_queue
from worq import get_broker, TaskSpace
from worq.pool.thread import WorkerPool 
from browser import get_tb
tb_q=None
pool_tb=None


url_tb="memory://"
name_tb=__name__

ts_tb = TaskSpace(name_tb)
def init_pool_tb():   
    global pool_tb,tb_q    
    broker_tb = get_broker(url_tb,name="1")
    broker_tb.expose(ts_tb)
    tb_q = broker_tb.queue()

    pool_tb = WorkerPool(broker_tb,  workers=1)
    pool_tb.start()
   


def init_tb():
#    ts_tb.task(start,"start")
    init_pool_tb()
    
    
def deinit_tb():
    pool_tb.stop()
        
    
@ts_tb.task
def start(id,url):
    return get_tb().start(id,url)    
    
def get_tb_q():
    return tb_q