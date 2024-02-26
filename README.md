
# Replication Package for "An Approach for Schema Extraction of JSON and Extended JSON Document Collections" @ IEEE 2018

This repository provides the replication package for the IEEE 2018 paper "An Approach for Schema Extraction of JSON and Extended JSON Document Collections".

## Prerequisites

Ensure that `docker-compose` is installed and Docker is running on your local machine.

You can verify this by executing:
```
docker-compose version
```
and
```
docker ps
```

## Build the Image and Run Containers

First, navigate to the repository folder, open the terminal, and execute the following command:

```
docker-compose up -d
```

This command pulls the required images and starts two containers in detached mode: `mongodb` for the database and `jsonschemadiscovery` for the JSONSchemaDiscovery tool.

## Run the Experiment

After the containers are up and running, enter the `jsonschemadiscovery` container in interactive mode:

```
docker exec -it jsonschemadiscovery /bin/bash
```

Next, execute the following command:

```
./doAll.sh
```

This script performs an initial smoke test to ensure the environment is set up correctly. It then runs a Python script that creates a user for API interaction, extracts data from .tar files, and inserts them into the database. Finally, it extracts the JSON schema, compares the reproduced results with the original paper's data, and generates a paper.pdf file containing the report of this reproduction package.

### Issue: Error Code 504 during Raw Schema Extraction

During the execution of the project, you might encounter the following error:

`Error Code: 504
Error occurred while trying to proxy: localhost:4200/api/batch/rawschema/steps/all`


This error indicates a timeout issue typically related to the server-side processing taking longer than expected. If you see this error, particularly during raw schema extraction for any dataset (e.g., drugs, companies, movies), please follow the steps below:

- Ensure that your server and all services are running correctly.
- Check if there is any network issue or server overload that might be causing the delay.
- Retry the operation by running the `./doAll.sh` script again. Often, re-initiating the process resolves the issue.

## Copy and View the Resulting Paper

To copy the directory with the resulting paper, run the following command in another terminal from the folder where you want to save the results:

```
docker cp jsonschemadiscovery:/home/repro/JSONSchemaDiscovery/rep-eng-paper .
```
