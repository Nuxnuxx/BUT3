FROM ubuntu

RUN apt-get update && apt-get install -y nginx vim

EXPOSE 80

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
