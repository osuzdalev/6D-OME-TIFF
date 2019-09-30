#!/bin/bash

docker build -t 'apeer/dimension_6' .

docker run -it --rm -v "$(pwd)"/input:/input -v "$(pwd)"/output:/output  --env-file ./wfe.env apeer/dimension_6