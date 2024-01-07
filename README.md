# Replication Package for "An Approach for Schema Extraction of JSON and Extended JSON Document Collections" @ IEEE 2018

This repository provides the replication package for the ICEE 2018
*An Approach for Schema Extraction of JSON and Extended JSON Document Collections*. 

## Building the Docker image
- Clone this repository
  > git clone https://github.com/SaltyRain/repEng-JSONSchemaDiscovery.git
- Build the Docker image from scratch
  > cd repEng-JSONSchemaDiscovery

  > docker build -t repeng-jsonschemadiscovery .

  OR run the command without cache
  > docker build --no-cache -t repeng-jsonschemadiscovery .

## Running Docker container
Access the container interactively with
  > docker run -it repeng-jsonschemadiscovery

## Running scripts
Inside the docker container run the script to check, if software is installed

*NOTE:* You should be in folder home/repro to run this script (Use `ls` to check the current location)

> ./smoke.sh


## Generating the paper

Finally, we need to generate the paper.

Enter the paper directory:

> cd paper

- Apply the `Makefile`:

> make

Navigate to the output folder

> cd output
> ls
