#! /bin/bash
file="/var/server"

cd ${file}
cd Server

php -S localhost:80 >/dev/null 2>&1 &
