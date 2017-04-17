#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:48:34 2017

@author: mayu
"""

from hashlib import md5
import os
import shutil
 


dic = {}

def getMD5WithPath(path):
    m = md5()
    a_file = open(path, 'rb') 
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def updateDicWithPath(filename):
    fileMd5 = getMD5WithPath(filename)
    if (dic.has_key(fileMd5)): 
        dic[fileMd5].append(filename)
    else:
        dic[fileMd5] = [filename]

def traverse(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        if os.path.isdir(path): 
            traverse(path)
        else:
            name, ext = os.path.splitext(path)
            if ext == '.png':
                updateDicWithPath(path)
rootPatch = '/Users/apple/Desktop/Lianjia_iOS_Shell_Project'                
traverse(rootPatch)

bakPath = '/Users/apple/Desktop/same_image_sets'
for (k,v) in  dic.items(): 
    if len(v) > 1:
        path = os.path.join(bakPath, k) 
        os.mkdir(path)
        
        for imagePath in v:
            curStr = imagePath.replace('/','_') 
            
            tempPath = os.path.join(path, curStr)
            shutil.copyfile(imagePath, tempPath)
            print curStr
        
        print 'xxxxxxxxxxxxxxxxxxxxx'

        
        


