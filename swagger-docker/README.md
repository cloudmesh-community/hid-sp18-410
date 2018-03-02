#Implementing Swagger service on a Docker container

## Goal - To implement timestamp service on docker container
## Assumption - Docker already installed on the Host OS

## Steps to run this service

* Clone the repository in a seperate directory
* Build the docker container with a tag name using below command
	sudo docker build -t dock_swag .
* After successfully compiling your Dockerfile, next we need to run the docker
	sudo docker run -v /home/:/home/ -p 80:8080 -it dock_swag
* Please note that we need to create a volume mapping so that the container can
actually communicate to the host OS file system.
* Next we can test the swagger service on a local browser 
	http://localhost/api/timestamp?path=/home/algo.txt 
* Output expected would be similar to
	{
  "Timestamp": {
    "accessed_time": "Tue Feb 27 05:05:17 2018",
    "creation_time": "Thu Sep 21 02:40:24 2017",
    "modified_time": "Thu Sep 21 02:40:24 2017"
  }
}

