f5_home_assigment:

My solution for the next home assignment.

Functional requirements:
1. Set up a docker-compose file for these two docker containers, and two two docker files that build:
1.Build an image with Nginx, using a dockerfile, that starts from the Ubuntu image as the base image.
   In the nginx image, configure at least 2 servers, on 2 different ports, one that responds with a custom html response, and one that responds with an HTTP error code.
2. Build another image, to be used as a testing image, with a go/python script to check each one of the Nginx servers.
3. Set up a docker-compose file for these 2 docker containers.
2.Set up a Github repo:
1. The Github should contain all of the above files and run the docker build, and docker compose as part of Github actions.
2. If the test passed, publish to an artifact as a file with the name "succeeded", if not, a file with the name "fail".

Non-functional requirements:
1. Try to comment and document what you think will be useful for us to know, or do you want to explain?
2. Try to keep the image size as small as you can

