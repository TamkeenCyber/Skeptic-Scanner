import os
import re
from bs4 import BeautifulSoup
import json
import pyfiglet
import pandas as pd
import jinja2
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime
import argparse
import webbrowser
import dload
import sys

current_dir = str(Path(__file__).resolve().parent)+ "\\"
path= '/'.join(current_dir.split('\\'))
src_dir =path + 'src'
content = []
start_scan =''
end_scan =''


# Banner 
def banner():
    os.system("")
    ascii_banner = pyfiglet.figlet_format("Skeptic Scanner", font="slant")
    CGREEN  = '\33[32m'
    CEND = '\033[0m'
    CBOLD     = '\33[1m'
    print(CBOLD + CGREEN + ascii_banner + CEND)
    print()


# Usage
example_text = '''

Example:

Please, move your source code inside the { ~/Skeptic-Scanner/src } folder OR use ( -c URL ) for clone from git repo. 

python3 Skeptic-Scanner.py -r

Use Skeptic-Scanner.py With clone from remote repo:

python3 Skeptic-Scanner.py -r -c https://github.com/TamkeenCyber/Skeptic-Scanner.git

 '''
parser = argparse.ArgumentParser(description='''Skeptic Scanner is an open-source automation tool. 
It means to analyze the source code (HTML and PHP) and check if it contains some important elements 
such as ( File Upload and Forms with Input Password ), which maybe represent a significant risk.
It also retrieves important pages like Admin, Rules, etc.''',
                                 epilog=example_text,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-r",'--run', help="Run Scan", action="store_true",required=True)
parser.add_argument("-c",'--clone', help="Clone a git repo to src folder")
banner()
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

# Scan
def scan():    
    global start_scan
    start_scan= datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    print('Start Scan at ' + start_scan)
               
    for subdir, dirs, files in os.walk(src_dir):
        for file in files:        

            filepath = subdir + os.sep + file
            filepath ='/'.join(filepath.split('\\'))

            if filepath.lower().endswith(".html") or  filepath.lower().endswith(".php") :
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    soup = BeautifulSoup(f.read(),'html.parser')

                    search_keyword =['admin','rule','pass','user']
                    
                    for title in search_keyword:
                        result = soup.find_all('title', text=re.compile(title, re.I))
                        for t in result:
                            info = {"sourceline": t.sourceline, "path":filepath,  "tag": str(t),'type':'Page'}                    
                            content.append(info)                          
                                         
                    tag_upload = soup.find_all('input',{'type':"file"}) 
                    tag_password = soup.find_all('input',{'type':"password"}) 
                    for u in tag_upload:                    
                        info = {"sourceline": u.sourceline, "path":filepath,  "tag": str(u),'type':'Upload'}                    
                        content.append(info)                    
                    for p in tag_password:                    
                        info = { "sourceline": p.sourceline, "path":filepath,  "tag": str(p),'type':'Password'}                    
                        content.append(info)
    global end_scan
    end_scan= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('End Scan at ' + end_scan) 


def export_to_JSON(data):    
    filename = 'Skeptic-Report.json'
    with open(path+filename, 'w') as f:
        json.dump(data, f)
    
def export_to_HTML(data):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))
    filename = 'Skeptic-Report.html'
    template = env.get_template('template.html')
    html = template.render(content=data,date=datetime.now().strftime("%Y-%m-%d"),startdate=start_scan,enddate=end_scan)
    with open(path+filename, 'w') as f:
        f.write(html)
    webbrowser.open_new_tab(path+filename)

if args.run:    
    if args.clone:
        if not os.path.exists(src_dir):
            os.makedirs(src_dir)
        print('\33[33m' + 'Cloning "' + args.clone +  '" into "' + src_dir + '"' +'\33[0m')
        print()
        dload.git_clone(args.clone,src_dir)
    scan()
    print()    
    print("We have found the following tag(s): ")
    
    export_to_JSON(content)
    export_to_HTML(content)

    df = pd.DataFrame.from_dict(content, orient='columns')
    #pd.set_option('display.max_columns', None)  
    #pd.set_option('display.expand_frame_repr', False)
    #pd.set_option('max_colwidth', -1)
    print(df)