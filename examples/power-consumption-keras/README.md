# Predictive Maintenance (TensorFlow/Keras version)
This is an example of simple neural network regression model in federated settings. A normal high-end laptop or a workstation should be able to sustain a few clients. The data partitions are static based on four nodes. We here assume working experience with containers, Docker and docker-compose. 

## Table of Contents
- [Power Consumption Example (Keras version)](#power-consumption-example-keras-version)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Running the example (pseudo-distributed)](#running-the-example-pseudo-distributed)
  - [Clean up](#clean-up)

## Prerequisites
- [Python 3.8, 3.9 or 3.10](https://www.python.org/downloads)
- [Docker](https://docs.docker.com/get-docker)
- [Docker Compose](https://docs.docker.com/compose/install)

## Running the example (pseudo-distributed)
Clone FEDn and locate into this directory.
```sh
git clone https://github.com/scaleoutsystems/fedn.git
cd fedn/examples/power-consumption-keras
```

### Preparing the environment, the local data, the compute package and seed model

Start by initializing a virtual enviroment with all of the required dependencies.
```sh
bin/init_venv.sh
```
### Attach clients 
Get the client.yaml file

```
 docker run -d -v $PWD/client.yaml:/app/client.yaml -v $PWD/data/p2/:/var/data -e ENTRYPOINT_OPTS=--data_path=/var/data/power.npz ghcr.io/scaleoutsystems/fedn/fedn:develop-mnist-keras run client --secure=True --force-ssl -in client.yaml
```

## Clean up
You can clean up by running `docker stop <container-ID>`.
