#!/bin/sh

rm -r saves/World1
rm PythonToolScipts/*
cp -r BackUpWorld/World1 saves/
cp -r BackUpScripts/* PythonToolScipts/

LastNumOfRuns=$(<NumberOfRuns.dat)
NumOfRuns=$(( LastNumOfRuns + 1 ))
echo "$NumOfRuns" > NumberOfRuns.dat
