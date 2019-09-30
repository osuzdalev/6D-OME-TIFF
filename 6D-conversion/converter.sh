#!/usr/bin/env bash
# Allow for 3GB of RAM
export _JAVA_OPTIONS="-Xmx3g"
export JVM_ARGS="-Xms3g -Xmx3g"
export BF_MAX_MEM="3g"

ls -a
# run main script
python3 apeer_main.py