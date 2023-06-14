#!/bin/bash
/home/jason/anaconda3/etc/profile.d/conda.sh init bash
/home/jason/anaconda3/etc/profile.d/conda.sh create -y --name test_env5 pandas
exec $SHELL
