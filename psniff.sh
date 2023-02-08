#!/bin/bash

if [ "$1" == "start" ]; then
  pktmon start -c --comp 14 -m real-time
elif [ "$1" == "etl2txt" ]; then
  pktmon etl2txt C:\Windows\system32\PktMon.etl
elif [ "$1" == "list" ]; then
  pktmon list
else
  echo "Invalid argument."
fi