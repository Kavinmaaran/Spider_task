#! /bin/bash
file="/var/server"

cd ${file}
cd Server

php -S localhost:8000 >/dev/null 2>&1 &
