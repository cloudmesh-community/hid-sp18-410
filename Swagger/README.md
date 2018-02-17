# Assignment: Cloud and Big Data Rest Service with Swagger

Service Descprition

Built a Timestamp service that will provide following capabilities 

* Provide creation date and time
* provide last modified date and time
* provide last access date and time

Basically i have implemented a TIMESTAMP object that takes full path name 
as the input in the form of query parameter.
The swagger code-gen generate the server stub code for us by taking the 
time.yaml as input and gives us a nice foundation to develop the main logic.
I have implemented main logic in the file timestamp_stub.py. I have tried to 
uphold the best practices of API implementation by keeping the defination 
encapsulated using a stub code.

You can download the code from the repository and start playing around.

Follow the below steps

* Clone the repository
* Navigate to "flaskConnexion" directory 
* start the service by executing the command "python -m swagger_server"

You will see something like this 
Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)


Running the service from browser

* Open any browser and request the url with fullyqualified file name

* Example1
	http://localhost:8080/api/timestamp?path=/home/algo.txt
Result - 

{
  "Timestamp": {
    "accessed_time": "Fri Feb  9 01:35:56 2018",
    "creation_time": "Wed Sep 20 22:40:24 2017",
    "modified_time": "Wed Sep 20 22:40:24 2017"
  }
}

* Example2
	
	http://localhost:8080/api/timestamp?path=/home/karan/std.py

Result -

{
  "Timestamp": {
    "accessed_time": "Wed Feb  7 21:53:02 2018",
    "creation_time": "Wed Feb  7 22:13:40 2018",
    "modified_time": "Wed Feb  7 22:13:40 2018"
  }
}
