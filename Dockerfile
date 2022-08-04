FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/server
RUN apt update
RUN apt -y upgrade
RUN apt install -y php libapache2-mod-php php-mysql
RUN apt install -y sudo
COPY ./data/ .
RUN chmod +x /var/server/main.sh
RUN chmod +x /var/server/run.sh
CMD /var/server/run.sh