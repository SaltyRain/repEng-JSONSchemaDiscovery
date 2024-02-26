# Replication package example for ICEE 2018
# "An Approach for Schema Extraction of JSON and Extended JSON Document Collections"

# Copyright 2024, Timur Garipov <garipo01@ads.uni-passau.de>
# SPDX-License-Identifier: GPL-2.0-only

# Start off of a long-term maintained base distribution
FROM ubuntu:22.04

LABEL org.opencontainers.image.authors="garipo01@ads.uni-passau.de"

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG="C.UTF-8"
ENV LC_ALL="C.UTF-8"

# Update system and install necessary tools
RUN apt update && apt install -y --no-install-recommends \
    nano \
    ca-certificates \
    curl \
    git \
    sudo \
    build-essential \
    # Add Python for running scripts
    python3 \
    python3-pip \
    # Add LaTeX packages
    texlive-base \
    texlive-bibtex-extra \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-plain-generic \
    texlive-latex-extra \
    texlive-publishers

# Install Node.js 16.x
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

RUN useradd -m -G sudo -s /bin/bash repro \
        && echo "repro:repro" | chpasswd \
        && usermod -a -G staff repro

WORKDIR /home/repro

# Clone the JSONSchemaDiscovery repository
RUN git clone https://github.com/feekosta/JSONSchemaDiscovery.git

# Change to the JSONSchemaDiscovery directory
WORKDIR /home/repro/JSONSchemaDiscovery

# Copy patches and all necessary files
COPY --chown=repro:repro ./patches patches
COPY --chown=repro:repro ./scripts scripts
COPY --chown=repro:repro ./csv csv
COPY --chown=repro:repro ./doAll.sh .
COPY --chown=repro:repro ./Makefile .

# Apply patches
RUN patch angular.json < patches/angular.patch

#install global dependencies
RUN npm install -g @angular/cli@13.3.11 && \
    npm install -g typescript@4.6.3

# Install project dependencies and build the project
RUN npm install

## Clone the associated paper  
RUN git clone https://github.com/SaltyRain/rep-eng-paper.git

# Clone datasets for the experiment
RUN git clone https://github.com/feekosta/datasets.git

# Install Python dependencies
RUN pip3 install pymongo python-dotenv requests

# make doAll.sh script executable
RUN chmod +x doAll.sh

EXPOSE 4200