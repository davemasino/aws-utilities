#!/bin/bash

for snap in $(aws ec2 describe-snapshots)
do
	echo "Processing $f"
done
