import os
file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'index.html')
with open("index.html", 'rb') as fd:
    fd.read()