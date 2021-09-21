#!/usr/bin/env python
import sys
import logging
import sqlite3
import json
import os
from worq import get_queue
from worq import get_broker, TaskSpace
from worq.pool.thread import WorkerPool 


db_q=None
pool_db=None
url_db="memory://"
name_db=__name__
ts_db = TaskSpace(name_db) 
db=None

class DB():
    def __init__(self):
        self.tasks=dict()
                
    def add(self,id,hash,state):
        self.tasks[id]=(hash,state)
        
    def delete(self,id):
        self.tasks.pop(id)
                                   
    def get(self,id):
        err=True
        hash=None
        if id in self.tasks:
            hash=self.tasks[id][0]
            err=False
        return hash,err
        
    def list(self):    

        data=[]
        for id in self.tasks:
                d=self.tasks[id]
                data.append({"id":id,"hash":d[0],"state":d[1]})
        result={"success":True,"data":data}
        return json.dumps(result)
 
def init_pool_db():
    global db_q,pool_db    
    broker_db = get_broker(url_db,name="0")
    broker_db.expose(ts_db)
    db_q = broker_db.queue()
 
    pool_db = WorkerPool(broker_db,  workers=1)
    pool_db.start()
    
def init_db():
    global db
    db=DB()
    init_pool_db()

def deinit_db():
    pool_db.stop()     
    
def get_db():
    return db    
    
@ts_db.task
def add(id,hash,state):
    return db.add(id,hash,state)    

@ts_db.task
def delete(id,):
    return db.delete(id)    


def get_db_q():
    return db_q    