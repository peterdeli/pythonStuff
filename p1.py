'''
Created on Jan 19, 2019
@author: dad
'''

if __name__ == '__main__':
    pass
import os
# get environment
from os import environ

env_items = environ.items()

env_values={(k,v) for (k,v) in environ.items()}

import io
from sys import argv

with open('somefile.txt', 'rb') as inf:
    txtdata = inf.read()

if txtdata.startswith(b'\xff\xd8'):
    text = u'This is a Text file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(txtdata))

    
env_filtered = [ env_item for env_item in environ.items() if 'python' in env_item[0].lower() or 'python' in env_item[1].lower()]
global visited_dirs
visited_dirs = []

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    ldir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], ldir)
        parent[folders[-1]] = subdir
    return ldir

def walk_dir( top, walk_type ):
    global visited_dirs
    if walk_type == 'new': 
        visited_dirs = []
    try:
        for root, dirs, files in os.walk(top):
            if root in visited_dirs: 
                break
            else:
                visited_dirs.append(root)
            print "->>> " + str(root)
            dirlen = len(dirs)
            print "[" + str(dirlen )  + "] subdirs under " + root
            print "[" + str(len(files)) + "] of files under "  + root
            for sdir in dirs: 
                sdirpath = os.path.join( root, sdir )
                if ( os.path.isdir( sdirpath ) ): 
                        walk_dir( sdirpath, 'recursion' )
                        continue
                else:
                    print "Skipping non-dir " | str(sdir)
                    continue
    except Exception as ex:
        print str(ex) 
        return 

for k,v in env_values:
        print "Key: " + k + " Value: " + v

keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {k:v for k, v in zip(keys, values)}

# system
import socket
print socket.gethostname()

# hash
# {'a': 1, 'c': 3, 'b': 2}

# get dirs
fn='p1.py'

# todo: try/except

print( "File " + fn + " ? " + str(os.path.isfile(fn)))
# True
# False
print(  "Dir " + fn + " ? " + str(os.path.isdir(fn)))
#False
print( "Path to " + fn + ": " + str(os.path.abspath(fn)))



# recurse directories

#basedir=environ.get('HOME')
basedir="/var"
# for root, dirs, files in os.walk(basedir):
#     print('Searching:', root)
#     print('All directories', dirs)
#     print('All files:', files)
#     print('----------------------')

dirlist = {}
shortest_dir = 0
longest_dir = 0
print "Getting subdirs and file lists for " + str(basedir)
for root, dirs, files in os.walk(basedir):
    path = root.split(os.sep)
    flen = len(files)
    dirlist[root] = flen 
    shortest_dir = flen if flen < shortest_dir else shortest_dir
    longest_dir = flen if flen > longest_dir else longest_dir
    
    
    #print str( root )
    #print str(os.path.basename(root))
    #print str( len( files )) + " files "
    
print "done. " + str( len(dirlist)) + " dirs."
print "Shortest: " + str(shortest_dir)
print "Longest: " + str(longest_dir)

paths = environ.get('PYTHONPATH')
pdicts = {}
for path in paths.split(':'):
    pdict = get_directory_structure( path ) 
    pdicts[path] = pdict

#dirlist_dict = [ pdict for pdict in get_directory_structure( path ) for path in paths.split(':') ]
print "Done"
#print "Recurse basedir "
#walk_dir(basedir, 'new')
# for root, dirs, files in os.walk(basedir):
#     print str(root)
#     dirs.sort()
#     dirlen=len(dirs)
#     print str(dirlen)  + " # of subdirs"
#     print str(files.length) + " # of files"

        
        
        


# get users
import getpass
print "User: " + getpass.getuser()
#qry=raw_input("Builtin name: ")
qry='clob'
index=-1
import sys
try:
    index=dir(__builtins__).index(qry)
    print(  "Query for builtin " + qry + " found at index " +  str(index) )
except ValueError:
    print "Error determining builtin: " + str(sys.exc_info())
    index=-1
    print(  "Query for builtin " + qry + " failed." ) 
    
# try:
#     someFunction()
# except Exception as ex:
#     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#     message = template.format(type(ex).__name__, ex.args)
#     print message


# import pip
#sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])

import pkg_resources
installed_packages = pkg_resources.working_set
try:
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    for p in installed_packages_list:
        if p.type != 'NoneType': 
            print str(p)
except Exception as ex:
    print "Something didn't work"

print "Done"
       
# wildcard / glob
import glob
# get file lists by date, extension, etc
# like ls -l or ls -lR



# get processes
#### 
