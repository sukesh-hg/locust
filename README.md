# LOCUST - LOAD TESTING TOOL
Locust is an easy-to-use, distributed, user load testing tool. It is intended for load-testing web sites (or other systems) and figuring out how many concurrent users a system can handle. Locust is completely event-based, and therefore it’s possible to support thousands of concurrent users on a single machine.

This repository also has a sample python application with APIs that can be load tested. To run the application in your local, run the python app.py command. There is also a Dockerfile which can be used to package the application to run in a Kubernetes environment.

For a simple, one step build and deployment use the skaffold.yaml provided. Install Skaffold on your Kube cluster and run 'skaffold run' command. 

Locust requires python 2.7 (recommended 3.5 above). You can install locust using 'pip install locustio' command. Once locust is installed simply run 'locust' command in the subdirectory with the locustfile.py file. Access the UI on port 8089.
