#!/bin/bash

envs=$(eval "conda env list | cut -d ' ' -f1 | cut -d '#' -f1")

exists=false
cmd="conda env create -f environment.yml"

for env_name in $envs
do
	if [ "$env_name" == "tesco-scrap" ]
	then
		cmd="conda activate tesco-scrap"
		exists=true
	fi
done

eval $cmd

if [ $exists != True ]
then
	conda activate tesco-scrap
fi

# conda activate tesco-scrap
