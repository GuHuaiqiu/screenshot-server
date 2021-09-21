import hashlib

import requests

def download(id,url):
    md5_hash = hashlib.md5()
    md5_hash.update(bytes(id, encoding='ascii'))
    md5_hash.update(bytes(url, encoding='ascii'))        
    md5 = md5_hash.hexdigest()  
    fn=md5+'.png'
    local_file_path='dn_'+fn
    url='http://127.0.0.1/download/'+fn
    
    response = requests.get(url)
    # If the HTTP GET request can be served
    if response.status_code == 200:
         
        # Write the file contents in the response to a file specified by local_file_path
        with open(local_file_path, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=128):
                local_file.write(chunk)
    
id=0
with open("test.txt","r") as f:
    for line in f:        
       download(str(id),line.strip())
       id=id+1
       