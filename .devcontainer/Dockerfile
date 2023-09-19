# The base image: latest version of Ubuntu LTS
FROM ubuntu:latest

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=">=1.6,<1.7"

# Install system dependencies
RUN apt-get update -y && apt-get upgrade -y

# Toolchain 
RUN apt-get install -y curl

# Install Python
RUN apt-get install -y python3 python3-pip \
  ca-certificates \
  default-libmysqlclient-dev \
  build-essential

RUN echo "export PATH=\"$HOME/.local/bin:$PATH\"" >> ~/.bashrc
RUN echo "alias python='python3'" >> ~/.bashrc
RUN echo "alias pip='pip3'" >> ~/.bashrc

RUN pip install "poetry$POETRY_VERSION"
RUN poetry config virtualenvs.in-project true

# Install Git
RUN apt-get install -y git

# Create a working directory
WORKDIR /workspace

COPY . .

# This will be the default command that runs
# when a container is run from this image.
# You may need to customize this depending
# on your application's start-up procedure.
CMD ["bash"]
