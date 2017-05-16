# mover para a pasta que contém as pastas que devem ser renomeadas

import os

path = "."

[os.rename(f, f.replace(" ".encode('utf-8'), "_".encode('utf-8').strip())) for f in os.listdir(path.encode('utf-8').strip())]

#print(os.listdir(".".encode('utf-8').strip()))
#for d in os.listdir(".".encode('utf-8').strip()):
#  print(d.replace(" ".encode('utf-8'), "_".encode('utf-8').strip()))
#  print(d)


