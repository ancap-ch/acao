#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from io import TextIOWrapper
sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

modelos = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/modelos'
fontes = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/fontes'
ufontes = u'C:/Users/Thiago/Desktop/ancap.ch/artigos/fontes'
saidas = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/pdfs'
main_tex = 'C:/Users/Thiago/Desktop/ancap.ch/artigos/main/main.tex'

import argparse
import os
import subprocess
import shutil


import unicodedata
path = fontes.encode('utf-8').strip()
#dirs = [unicodedata.normalize('NFC', f) for f in os.listdir(ufontes)]
dirs = os.listdir(path)
l = open('lista.txt','w', encoding='UTF-8')
for index, d in enumerate(dirs, 1):
	sys.stdout.write(str(index))
	sys.stdout.write(": ")
	# sys.stdout.flush()	
	dd = d.decode('utf-8')
	ds = dd.replace("_", " ")
	print(ds)
	l.write(str(index))
	l.write(": ")
	l.write(ds + '\n')
l.close()
