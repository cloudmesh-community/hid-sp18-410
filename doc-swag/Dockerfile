FROM ubuntu:16.04
MAINTAINER Karan Kamatgi <krkamatg@iu.edu>

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    libssl-dev \
    pandoc \
    wget \
    curl \
    git-core \
    default-jre \
    software-properties-common -y


RUN git clone https://github.com/cloudmesh-community/hid-sp18-410.git

WORKDIR /hid-sp18-410/doc-swag

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

EXPOSE 8080

RUN make service

CMD ["make", "start"]
