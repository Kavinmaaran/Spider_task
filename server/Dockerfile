FROM ubuntu/apache2:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/server
RUN apt update
RUN apt -y upgrade
RUN apt install -y php libapache2-mod-php php-mysql
RUN apt install -y sudo
COPY ./data/ .
RUN chmod +x /var/server/main.sh
RUN chmod +x /var/server/run.sh
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_balancer
RUN a2enmod lbmethod_byrequests
RUN a2enmod headers
RUN service apache2 restart
CMD /var/server/main.sh