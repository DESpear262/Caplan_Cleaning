from tqdm import tqdm
import os

from XMLDump import *
from checkByline import *

directory_name = "D:\\Caplan\\www.econlib.org"      #Target directory
destination_file = "D:\\Caplan\\xml_export.xml"     #Destination directory

#####################
#Code for deployment#
#####################

'''
#loop through all files in directory = directory_name
for path, subdirs, files in tqdm(os.walk(directory_name)):
        for name in files:
            if "\\feed\\index.html" in f"{name}\\{path}" or "@" in f"{name}\\{path}" or ".html.1" in f"{name}\\{path}":  #feed files contain comments, which I don't need for this project, @ implies printer-friendly or otherwise redundant content
                pass
            else:
                if checkByline(name):
                    XMLDump(name, destination_file)
'''

testbed = "D:\\Caplan\\testbed"                     #Testbed for checkByline
XMLTest = "D:\\Caplan\\XMLTest"                     #Testbed for XMLDump
XMLOut = "D:\\Caplan\\out.xml"                      #Outfile for XMLDump test


#######################
#Test code for XMLDump#
#######################
'''for path, subdirs, files in os.walk(testbed):
    for name in files:
        if "\\feed\\index.html" in f"{name}\\{path}" or "@" in f"{name}\\{path}" or ".html.1" in f"{name}\\{path}":  #feed files contain comments, which I don't need for this project, @ implies printer-friendly or otherwise redundant content
            pass
        else:
            if checkByline(f"{path}\\{name}"):
                with open("D:\\Caplan\\bylinetest.txt", 'a', encoding='utf-8') as out:
                    out.write(f"{path}\\{name}\n")
'''
###########################
#Test code for checkByline#
###########################
'''for path, subdirs, files in os.walk(XMLTest):
        for name in files:
            XMLDump(f"{path}\\{name}", XMLOut)
'''