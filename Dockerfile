# Replication package example for ICEE 2018
# "An Approach for Schema Extraction of JSON and Extended JSON Document Collections"

# Copyright 2024, Timur Garipov <garipo01@ads.uni-passau.de>
# SPDX-License-Identifier: GPL-2.0-only

# Start off of a long-term maintained base distribution
FROM ubuntu:20.04

LABEL org.opencontainers.image.authors="garipo01@ads.uni-passau.de"

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG="C.UTF-8"
ENV LC_ALL="C.UTF-8"

# Update system and install necessary tools
RUN apt update && apt install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    build-essential \
    # Add Python for running your script
    python3 \
    python3-pip \
    # Add LaTeX packages
    texlive \
    texlive-latex-extra \
    texlive-bibtex-extra \
    texlive-fonts-recommended \
    texlive-science \
	texlive-plain-generic \
	texlive-publishers \
    texlive-fonts-extra \ 
    biber \
    # Install individual LaTeX packages
    # might be needed for libertine
    fonts-lmodern \ 
    # might be needed for libertine
    lmodern \
    # Additional packages for general LaTeX functionality
    texlive-latex-recommended \
    texlive-xetex \
    texlive-luatex \
    texlive-pictures \
    texlive-lang-english \
    texlive-lang-german

# Install Node.js 16.x
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

RUN useradd -m -G sudo -s /bin/bash repro && echo "repro:repro" | chpasswd
USER repro
WORKDIR /home/repro

# Prepare directory structure
## git-repos/       - for external git repositories
## build/           - temporary directory for out-of-tree builds
## bin/             - for generated binary executables
RUN mkdir -p $HOME/git-repos $HOME/build $HOME/bin


# Obtain JSONSchemaDiscovery sources from a git repo
WORKDIR /home/repro/git-repos
RUN git clone https://github.com/feekosta/JSONSchemaDiscovery.git

# Apply the patch to angular.json
COPY patches/mypatch.patch /tmp

WORKDIR /home/repro/git-repos/JSONSchemaDiscovery
RUN patch angular.json < /tmp/mypatch.patch


# Install project dependencies and build the project
RUN npm install
RUN npm run build

#  Production distribution is now in the dist/ subdirectory

WORKDIR /home/repro
COPY scripts/smoke.sh .

## Clone the associated paper source so contributors can work on it from within the container 

RUN git clone https://github.com/SaltyRain/rep-eng-paper.git paper