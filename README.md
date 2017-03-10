# Find Backdoor
Find Backdoors in websites    
Scan the files ".asp, .aspx, .php, .js"    
This scanner can trigger false positive, you should have basic programming skills to use this.

#### Features
- [x] Scan by patterns
- [x] Scan just for base 64 encoded backdoors
- [x] Can change the default .php extension to others (.asp .aspx .js)
- [x] Returns the filename and the line number of the backdoor.
- [x] Generates Scan Log file.

### Basic Usage
Needs Python 3  
Download it, then run it.  
  
#### On Windows:  
example for scanning php files in a directory: `find-backdoor.py "H:\Example\Find-Backdoor\testdir"`  
example for scanning php files base64 only: `find-backdoor.py -b "H:\Example\Find-Backdoor\testdir"`  
example for scanning aspx files in a directory: `find-backdoor.py -x "C:\inetpub"`
#### On Linux:  
example for current directory (php): `./find-backdoor.py .`    
example for other directory: `./find-backdoor.py /var/www/html`    
example for javascript files: `./find-backdoor.py -j /var/www/html`    

### Built using
* Python 3.6 - [Link](https://www.python.org/)

### Tested on:
Python 3.5 and 3.6

### TO DO
- Better Patterns
- Add more ASP and Javascript patterns

### License
MIT License

### Contact
twitter @RomelSan
