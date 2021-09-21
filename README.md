# screenshot-server
a flask project.
beore running it, prepare cookie json foes for jd and taobao
python mk-jd-cookies.py
python mk-tb-cookies.py

cookies for pingduoduo and other more sites can be made by writing similar python programs.
they are loaded in browser.py

to run it:
python app.py

client:
1. create a task
POST:  http://127.0.0.1/do
data: json:{id:<id>,url:<url>} 
  image file name:md5.png
  md5 is of str(id)+url
2. query status
GET: http://127.0.0.1/status
3.  delete task
GET: http://127.0.0.1/del?id=<id>
4.  download image
GET: http://127.0.0.1/dowbload/<md5>.png
  


