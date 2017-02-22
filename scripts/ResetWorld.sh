#!/bin/sh

rm -r saves/World1
rm PythonToolScipts/*
cp -r BackUpWorld/World1 saves/
cp -r BackUpScripts/* PythonToolScipts/

LastNumOfRuns=$(<NumberOfRuns.dat)
NumOfRuns=$(( LastNumOfRuns + 1 ))
echo "$NumOfRuns" > NumberOfRuns.dat

echo "Enter Engagement Score and type Enter: "
read EngagementScore

echo $EngagementScore >> "EngagementScore.dat"
