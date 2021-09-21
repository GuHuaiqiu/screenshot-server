from flask import Flask, flash, redirect, render_template, request, session, abort, send_file
import os
import json
import logging
from flask.helpers import flash, url_for
from urllib.parse import urlparse
from task_tb import tb_q,init_tb,deinit_tb,get_tb_q
from task_jd import jd_q,init_jd,deinit_jd,get_jd_q
from task_other import other_q,init_other,deinit_other,get_other_q
from browser import init_browser,deinit_browser
from db import init_db,deinit_db,get_db,get_db_q
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/del")
def delete():
    id = request.args.get('id')
    h,err = get_db().get(id)
    if not err :
         os.remove(h+'.png'   )
    result=get_db_q().db.delete(id)
    return '{"result":"%s"}'%(result)

@app.route("/status")
def status():
    return  get_db().list()


@app.route('/start', methods=["POST"]) # Allowing Post requests
def start():
    data = json.loads(request.data)
    id = data["id"]
    url = data["url"]
    print(data)
    tt= urlparse(url)
#    print(tt)
    t=tt.netloc
    
    if t.endswith( "taobao.com") or t.endswith("tmall.com"):
        result = get_tb_q().task_tb.start(id,url)
    elif t.endswith("jd.com"): 
        result = get_jd_q().task_jd.start(id,url)    
    else:
        result = get_other_q().task_other.start(id,url)    
        
    # wait for the final result
    #result.wait(timeout=30)
    #print(result)
    
    return '{"status":0}'

@app.route("/download/<path>", methods = ['GET'])
def DownloadLogFile (path = None):
#    file_path = UPLOAD_FOLDER + filename
    return send_file(path, as_attachment=True, attachment_filename='')
        
if __name__ == "__main__":
    init_db()
    init_tb()
    init_jd()    
    init_other() 
    init_browser()    
    app.run(host='0.0.0.0', port=80)
    deinit_tb()
    deinit_jd()    
    deinit_other()        
    deinit_browser()
    deinit_db()