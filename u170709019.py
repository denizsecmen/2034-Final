import os
import hashlib
import requests
import uuid
import urllib.request
from urllib.parse import urlparse
import threading 
import queue
import multiprocessing
fga=queue.Queue()
url =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg"
,"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg"]
h=queue.Queue()
sa=list()
def control(file_name):
  g=hashlib.md5()
  sg=open(file_name,'rb')
  g.update(sg.read())
  vg=g.hexdigest()
  if vg in sa:
    print("File is already exsist"+str(file_name))
  sa.append(vg) 
  sg.close()
def download_file(url, file_name=None):
  r = requests.get(url, allow_redirects=True)
  file = file_name if file_name else str(uuid.uuid4())
  open(file, 'wb').write(r.content) 
  sa.append(file)
def process(url):
  byb=os.fork()
  if byb==0:
    print("Child process PID:"+str(os.getpid()))
    child=os.getpid()
    for g in url:
       f=threading.Thread(download_file(g))
       f.start()
    f.join()
    for i in range(0,len(sa)):
       fa=threading.Thread(control(sa[i]))
       fa.start()
    print("Child Progess Ended!")
  elif byb<0:
    print("Error happened!")
  else:
    os.wait()
    print("Parent process PID:"+str(os.getpid()))
    print("Parent process Ended!")
process(url)
