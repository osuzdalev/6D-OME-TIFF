#FROM openjdk:12.0.2-jdk
FROM phusion/baseimage

# Install Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Install OpenJDK-12
RUN apt-get update && \
    apt-get install -y tar
RUN mkdir -p /usr/java
COPY openjdk-12.0.2_linux-x64_bin.tar.gz /usr/java/openjdk-12.0.2_linux-x64_bin.tar.gz
WORKDIR /usr/java
RUN tar xvf openjdk-12.0.2_linux-x64_bin.tar.gz

WORKDIR /

# Setup JAVA_HOME -- useful for docker commandline
ENV PATH="$PATH:/usr/java/jdk-12.0.2/bin"
ENV export JAVA_HOME="/usr/java/jdk-12.0.2"

# Install bftools
COPY bftools/. /usr/local/bin

# Copy all scripts
COPY apeer_main.py apeer_main.py
COPY converter.py converter.py
COPY converter.sh converter.sh
COPY module_specification.json module_specification.json

CMD [ "sh", "./converter.sh" ]