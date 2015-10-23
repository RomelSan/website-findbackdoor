#!/usr/bin/python
# Name: find-backdoor.py
# Description: Utility to scan a file path for encrypted and obfuscated files (PHP)
# Author: Romel Vera Cadena (romel.vera.cadena@gmail.com) ( https://github.com/RomelSan?tab=repositories )
# Python: v3.4 , v3.5
# Date: 10/23/2015

# Library imports
import re
import os
import glob
import sys
import time
from optparse import OptionParser

#globals
pattern = '(eval\(|file_put_contents|base64_decode|python_eval|exec\(|passthru|popen|proc_open|pcntl|assert\(|system\(|shell)' #default pattern, this line is not used at all
file_extension = '.php' #default extension

#def
def searchbackdoor(fullpath, pattern):
    
    webfile = open(fullpath, "r", encoding='utf-8')
    line_num = 0
    hit_count = 0
    for line in webfile:
        line_num += 1
        if re.search(pattern, line):  
            hit_count = hit_count + 1 
            print("Filename: " + str(fullpath))
            print("Pattern Word: " + str(line))
            print("Line Number: " + str(line_num) + "\n")
    print("Total Backdoors: " + str(hit_count) + "\n")
    webfile.close()
	
def matchbackdoor(fullpath, pattern, encoding='utf-8'):
    
    webfile = open(fullpath, "r")
    line_num = 0
    hit_count = 0
    for line in webfile:
        line_num += 1
        if re.match(pattern, line):  
            hit_count = hit_count + 1 
            print("Filename: " + str(fullpath))
            print("Pattern Word: " + str(line))
            print("Line Number: " + str(line_num) + "\n")
    print("Total Backdoors: " + str(hit_count) + "\n")
    webfile.close()
#code
print("""
  __ _           _       _                _       _
 / _(_)_ __   __| |     | |__   __ _  ___| | ____| | ___   ___  _ __
| |_| | '_ \ / _` |_____| '_ \ / _` |/ __| |/ / _` |/ _ \ / _ \| '__|
|  _| | | | | (_| |_____| |_) | (_| | (__|   < (_| | (_) | (_) | |
|_| |_|_| |_|\__,_|     |_.__/ \__,_|\___|_|\_\__,_|\___/ \___/|_|
By @RomelSan
""")

parser = OptionParser(usage="usage: %prog [option] <start directory>\nDefault extension is .php you can change this with options",
                         version="%prog 1.0")

parser.add_option("-b", "--base64",
                     action="store_true",
                     dest="is_base64",
                     default=False,
                     help="Find \"base 64 encodings\" only",)						 
					 
parser.add_option("-m", "--match",
                     action="store_true",
                     dest="is_match",
                     default=False,
                     help="Find exactly pattern matches",)		
					 
parser.add_option("-a", "--asp",
                     action="store_true",
                     dest="is_asp",
                     default=False,
                     help="Search for Backdoors in .asp",)	
					 
parser.add_option("-x", "--aspx",
                     action="store_true",
                     dest="is_aspx",
                     default=False,
                     help="Search for Backdoors in .aspx",)	

parser.add_option("-j", "--javascript",
                     action="store_true",
                     dest="is_javascript",
                     default=False,
                     help="Search for Backdoors in javascript .js files",)	

(options, args) = parser.parse_args()

# Manage conflicts
if options.is_base64 and options.is_match:
    parser.error("You must select a single option, -b or -m")

if ((options.is_asp or options.is_aspx) and (options.is_javascript)):
    parser.error("You must select a single option, -a or -x or -j")
	
if options.is_asp and options.is_aspx:
    parser.error("You must select a single option, -a or -x")
	
#Set Extension
if options.is_asp:
    file_extension = '.asp'
	
if options.is_aspx:
    file_extension = '.aspx'
	
if options.is_javascript:
    file_extension = '.js'
	
# Error on invalid number of arguments
if len(args) < 1:
    parser.print_help()
    sys.exit()
	
# Error on an invalid path
if os.path.exists(args[0]) == False:
    parser.error("Invalid path")
    sys.exit()

#Set Path
yourpath = args[0]

print("\nSearching Directory for Backdoors...\n")

for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        #PHP
        if name.endswith(file_extension):
            currentpath = os.path.join(root, name)
            if options.is_base64:
                pattern = 'base64_decode'
                searchbackdoor(currentpath,pattern)
				
            elif options.is_match:
                pattern = '(eval\(|file_put_contents|base64_decode|unescape|python_eval|exec\(|passthru|popen|proc_open|pcntl|assert\(|system\(|shell)'
                matchbackdoor(currentpath,pattern)
            
            else:
                pattern = '(eval\(|file_put_contents|base64_decode|unescape|python_eval|exec\(|passthru|popen|proc_open|pcntl|assert\(|system\(|shell)'
                searchbackdoor(currentpath,pattern)
