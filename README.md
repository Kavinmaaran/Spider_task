# Spider_task

### Commands to be executed for docker-compose

``docker-compose build``   
``docker-compose up`` 

to stop containers: ``docker-compose down``   

Add a host to your local machine:   
      1. Windows : add ``127.0.0.1 ecorpcredit`` to **c:\Windows\System32\Drivers\etc\hosts** file    
      2. Linux : add ``127.0.0.1  ecorpcredit``  to **/etc/hosts** file
#### URL :
adminer : localhost:8080    
server : http://ecorpcredit 

sign in as root in adminer and import the database.  

import file name: "__migrations.sql"  

to sign in adminer for mysql:
for root   
username:root     
password:example
