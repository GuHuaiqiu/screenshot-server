#!/usr/bin/env python
import sys
from worq import get_queue
from worq import get_broker, TaskSpace
from worq.pool.thread import WorkerPool 
from browser import get_jd

jd_q=None
pool_jd=None
url_jd="memory://"
name_jd=__name__
ts_jd = TaskSpace(name_jd)   
def init_pool_jd():
    global jd_q,pool_jd    
    broker_jd = get_broker(url_jd,name="2")
    broker_jd.expose(ts_jd)
    jd_q = broker_jd.queue()
 
    pool_jd = WorkerPool(broker_jd,  workers=1)
    pool_jd.start()
    
def init_jd():
#    ts_jd.task(start,"start")
    init_pool_jd()

    
def deinit_jd():
    pool_jd.stop()
    
@ts_jd.task
def start(id,url):
    return get_jd().start(id,url)    

def get_jd_q():
    return jd_q