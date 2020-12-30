import subprocess
import json
import re

#patern za pronalazak sekcije portova
port_pattern = '[0-9]*\/[a-zA-Z]+ +[open|close]+  +[a-zA-Z\-]*'
#patern za pronalazak ip adrese
ip_pattern='\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

#citanje fajla i razdvajanje na dve nove linije, vidi ip_raw_info
with open('ip_raw_info', 'r') as file:
    lines = file.read().split('\n\n')



#for i in range(len(lines)):
#    print(re.findall(ip_pattern,lines[i]))
#    print(re.findall(port_pattern,lines[i]))
    

    
    print(re.findall(ip_pattern,lines[2]))
    print(re.findall(port_pattern,lines[2])[0])

node = {
'host': '',
'ports': [
    { 'port_num':'',
      'status': '',
      'service':''    
    }
    ]
}
node['host']=re.findall(ip_pattern,lines[2])[0]
node['port_num']= re.findall(port_pattern,lines[2])[0].split()[0]


print(node)