#!/bin/bash



directory="/path/to/directory"



if [ ! -d "$directory" ]; then
  echo "404 : $directory"
  exit 1
fi
rm -f "$directory"/*
echo "deleted"



