#!/bin/bash

########################################################
# Script to launch the docker container with a bash    #
# terminal                                             #
# Author: tridivb                                      #
########################################################

source ../config/cfg.conf

docker run --rm --gpus "device=1" \
	--name detectron \
    --workdir "/home/$USER/Object_Feature_Extractor_with_Detectron" \
	-v $code_repo:"/home/$USER/Object_Feature_Extractor_with_Detectron" \
	-v $epic_kitchens_path:"/home/$USER/epic_kitchens" \
	-v $output_path:"/home/$USER/detections" \
	-it detectron:py2-caffe2-cuda9 \
	python infer_epic_kitchens.py
