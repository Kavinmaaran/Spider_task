FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/server
RUN apt update
RUN apt -y upgrade
RUN apt install -y php libapache2-mod-php php-mysql
COPY ./data/ .
EXPOSE 80
CMD [ "php", "-S", "0.0.0.0:80" ]