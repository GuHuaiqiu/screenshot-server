# screenshot-server
a flask project.
to run it:
python app.py

client:
1. create a task
POST:  http://127.0.0.1/do
data: json:{id:<id>,url:<url>} 
2. query status
GET: http://127.0.0.1/status
3.  delete task
GET: http://127.0.0.1/del?id=<id>
  


