# Find Backdoor
Find Backdoors in websites    
Scan the files ".asp, .aspx, .php, .js"    
This scanner can trigger false positive, you should have basic programming skills to use this.

#### Features
- [x] Scan complete pattern
- [x] Scan just for base 64 encoded backdoors
- [x] Can change the default .php extension to others (.asp .aspx .js)
- [x] Returns the filename and the number of the line of the backdoor.

### Basic Usage
Download it, then run it    
example for current directory (php): ./find-backdoor.py .    
example for other directory: ./find-backdoor.py /var/www/html    
example for javascript file: ./find-backdoor.py -j /var/www/html    
example for aspx file: ./find-backdoor.py -x C:\inetpub

### Built using
* Python 3.5 - [Link](https://www.python.org/)

### Tested on:
Python 3.4 and 3.5

### TO DO
- Nothing yet...

### License
MIT License

### Contact
twitter @RomelSan