#!/bin/bash



directory="dir"  



if [ -d "$directory" ]; then
  cd "$directory"
  find . -type f -name "*.png" -delete
  echo "deleted"
else
  echo "no dir"
fi



