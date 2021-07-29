import os

directory = os.path.join("c:\\","path")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f=open(file, 'r')
           #  perform calculation
           f.close()

