# Skeptic Scanner

[![](https://img.shields.io/badge/Category-Static%20Code%20Analysis-E5A505?style=flat-square)]() [![](https://img.shields.io/badge/Language-Python-green?style=flat-square)]()


------------
[![Logo](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/logo.png "Logo")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/logo.png "Logo")

------------


**Skeptic Scanner** is an open-source automation tool it means to analyze the source code (HTML and PHP) and check if it contains some important elements such as ( File Upload and Forms with Input Password ), which maybe represent a significant risk. It also retrieves important pages like Admin, Rules, etc. 

The tool will help Application Security teams included ( Penetration Testers, Code Reviewers, and SOC teams) to find some important places to be its starting point and get more attention to these functions, which is often desirable for attackers.

As the tool is written in **Python**, it can be used in both Windows and Linux.

## Installation


```python
git clone https://github.com/TamkeenCyber/Skeptic-Scanner.git
cd Skeptic-Scanner/
python3 -m pip install -r requirements.txt
```

## Usage



```python
root@kali:~/Skeptic-Scanner# python3 Skeptic-Scanner.py
   _____ __              __  _         _____                                 
  / ___// /_____  ____  / /_(_)____   / ___/_________ _____  ____  ___  _____
  \__ \/ //_/ _ \/ __ \/ __/ / ___/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 ___/ / ,< /  __/ /_/ / /_/ / /__    ___/ / /__/ /_/ / / / / / / /  __/ /
/____/_/|_|\___/ .___/\__/_/\___/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/
              /_/


usage: Skeptic-Scanner.py [-h] -r [-c CLONE]

Skeptic Scanner

optional arguments:
  -h, --help            show this help message and exit
  -r, --run             Run Scan
  -c CLONE, --clone CLONE
                        Clone a git repo to src folder
Example:

Please, move your source code inside the { ~/Skeptic-Scanner/src } folder 
OR use ( -c URL ) for clone from git repo. 

python3 Skeptic-Scanner.py -r

Use Skeptic-Scanner.py With clone from remote repo:

python3 Skeptic-Scanner.py -r -c https://github.com/TamkeenCyber/Skeptic-Scanner.git

```

------------

- ### Scan from local folder: 
Kindly, move your source code inside the `$ ~/Skeptic-Scanner/src ` folder
Run the Scan 
```
root@kali:~/Skeptic-Scanner# python3 Skeptic-Scanner.py -r 
```
##### After the scan is finished, the HTML report will be opened in the browser automatically.
  
&nbsp;

- ### Clone remote Git Repository and run scan
use ` -c  Your_ Repository_URL.git` to clone Git Repository. 
```python
root@kali:~/Skeptic-Scanner# python3 Skeptic-Scanner.py -r  -c https://github.com/OWASP/Vulnerable-Web-Application.git
```
##### After the scan is finished, the HTML report will be opened in the browser automatically.  

## Output 

- #### Beautiful HTML report
The generated report contains multiple functions like search and sort. 
[![Html-Report](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/output-HTML-Report.png "Html-Report")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/output-HTML-Report.png "Html-Report")


- #### JSON
[![json](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/output-JSON.png "json")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/output-JSON.png "json")

- ####  Command output  
To print the full paths in the command output, un-comment the following codes in Skeptic-Scanner.py:
```
    pd.set_option('display.max_columns', None)  
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', -1)
```
[![CLI](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/output-CLI.png "CLI")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/output-CLI.png "CLI")



## Example
For getting in touch with the tool, we want to try the following: 
- ###### Clone a remote repository from Github and Run a Scan.
- ###### We want to know the Admin pages.
- ###### Pages containing upload files.

------------

- ##### Clone the remote repository from Github and Run the Scan
[![E1](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-1.png "E1")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-1.png "E1")
&nbsp;
[![E2](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-2.png "E2")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-2.png "E2")
&nbsp;

------------
- #####  We want to know the Admin pages
[![E3](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-3.png "E3")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-3.png "E3")
&nbsp;
[![E4](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-4.png "E4")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-4.png "E4")

------------

- #####  Pages containing upload files
As we see **the file path:**  `/root/Skeptic-Scanner/src/Vulnerable-Web-Application-master/FileUpload/fileupload3.php ` in **Source Line** `15`
[![E5](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-5.png "E5")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-5.png "E5")
&nbsp;
[![E6](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-6.png "E6")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-6.png "E6")
&nbsp;
[![E7](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-7.png "E7")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources/E-7.png "E7")

------------

 -  **Here are the HTML report and the JSON file.**
[![E8](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources//E-8-Results.png "E8")](https://raw.githubusercontent.com/TamkeenCyber/Skeptic-Scanner/master/resources//E-8-Results.png "E8")


## Author
- ##### Mohammed Aljuhani   [![](https://img.shields.io/badge/twitter-@MohammedJuh-00aced?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/MohammedJuh)

&nbsp;

------------


### Note
> Your advice, suggestions, or comments will be much appreciated and welcomed. Thank you.
