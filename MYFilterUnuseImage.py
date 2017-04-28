#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:20:11 2017

@author: mayu
"""
import os
import re

imageNameSets = set()
sourcePathList = []

def traverse(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        name, ext = os.path.splitext(path)
        if ext == '.imageset':
            fileNameList = name.split('/')
            fileName = fileNameList[-1]
            imageNameSets.add(fileName)
        elif os.path.isdir(path):
            traverse(path)
        else:
            name, ext = os.path.splitext(path)
            if ext == '.m' or ext == '.h' or ext == '.storyboard' or ext == '.xib' or ext == '.plist' or ext == '.mm':
                sourcePathList.append(path)
rootPatch = '/Users/apple/Desktop/Lianjia_iOS_Shell_Project'                
traverse(rootPatch)

imageNameList = list(imageNameSets)

def fileContainKeyword(fileList):
    for pertFile in fileList:
        dataSource = open(pertFile).read()
        for imageName in imageNameList:
            if imageName in dataSource:
                if imageName in imageNameSets:
                    imageNameSets.remove(imageName)
                    
fileContainKeyword(sourcePathList)

resultList = list(imageNameSets)
pattern = re.compile(r'.*\d+')
for imageName in imageNameSets:
    if pattern.match(imageName):
        resultList.remove(imageName)
        
#print resultList       
#print len(resultList)

resultPath = '/Users/apple/Desktop/unuse_image_sets_result'
f = open(resultPath, 'w')
for result in resultList:
    print result
    f.write(result + '\n')