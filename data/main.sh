#! /bin/bash
cp your_domain.conf /etc/apache2/sites-available/.
a2ensite your_domain
service apache2 reload
/var/server/run.sh
/usr/sbin/apache2ctl -D FOREGROUND