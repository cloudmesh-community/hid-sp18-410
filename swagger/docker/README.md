# Swagger Timestamp service on Docker

## Acknowledgement 
Thanks to Pathan, Shagufta for giving us a starting point in implementing this service on docker.

## Implementation :
* The specification of the Swagger REST service is defined in the YAML file `time.yaml` file
* Timestamp generation logic has been implemented in the stub file `timestamp_stub.py`
* The server-side code was generated using Swagger Codegen

## Steps for Execution :
* Please make sure you have atleast 1 file on your host filesystem in the directory `\home\` in order to test this service. 
  The name of the file must be included in the make test section accordingly.
 
* clone the repository

* navigate to the directory 

        cd /hid-sp18-410/swagger/docker/


* Using docker to run the Timestamp swagger service :

	- make docker-all -- actually creates the docker image, starts the container and runs the service

	- make docker-build -- creates the docker image only

	- make docker-start -- starts the container and runs the REST service

	- make docker-stop -- stops the container 

	- make docker-remove -- removes the docker image

	- make docker-clean -- stops the container and remove the image
  
* Test the service :
  Include the file parameter in test section for example - `localhost:8080/api/timestamp?path=/home/<filename>`
  Please make sure to run the following command in a seperate terminal after running `make docker-all`
  
  	make docker test -- curl for the timestamp details


    
 * The yaml file is located at 

        hid-sp18-410/swagger/docker/time.yaml
    
* The default_controller is at 

        hid-sp18-410/swagger/docker/default_controller.py
    
* The timestamp related modules (which are used in the default_controller.py) are located at 

		hid-sp18-410/swagger/docker/

* To install these modules alone, please cd to the above directory and run:
		
		pip install -r requirements.txt
 		python setup.py install


## Service Descprition

This swagger REST service aims at exposing the time stamp details of 
any desired file residing on the host file system. The basic idea of
creating a docker container with all the implementation details and 
creating a volume for sharing the host file system with the docker container is very important.
Volumes helped me in realizing my timestamp service implementation.
I have exposed my service on port 8080.





