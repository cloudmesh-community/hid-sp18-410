FROM openjdk:7
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -P /usr/src/app
COPY time.yaml /usr/src/app/

RUN java -jar swagger-codegen-cli-2.3.1.jar generate \
-i /usr/src/app/time.yaml \
-l python-flask \
-o /usr/src/app/flaskConnexion \
-D supportPython2=true




#WORKDIR /usr/src/app/flaskConnexion

FROM python:3-alpine


#RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/flaskConnexion
COPY default_controller.py /usr/src/app/flaskConnexion/swagger_server/controllers
COPY timestamp_stub.py /usr/src/app/flaskConnexion/swagger_server/controllers 
COPY swagger.yaml /usr/src/app/flaskConnexion/swagger_server/swagger

WORKDIR /usr/src/app/flaskConnexion

EXPOSE 8080



ENTRYPOINT ["python"]

CMD ["-m", "swagger_server"]
