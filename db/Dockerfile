FROM mysql:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/database
COPY ./data/ .
CMD ["/usr/bin/mysqld_safe"]