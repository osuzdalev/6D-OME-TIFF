#!/usr/bin/env bash
docker build . -t apeer/ometiff_builder

docker run -it --rm -v "$(pwd)"/input:/input -v "$(pwd)"/output:/output --env-file ./wfe.env apeer/ometiff_builder