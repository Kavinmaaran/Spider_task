FROM mysql:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/database
RUN apt-get update
RUN apt-get -y upgrade
COPY ./data/ .
CMD ["/usr/bin/mysqld_safe"]