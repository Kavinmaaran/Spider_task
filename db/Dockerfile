FROM mysql:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/database
RUN apt update
RUN apt -y upgrade
COPY ./data/ .
CMD ["/usr/bin/mysqld_safe"]