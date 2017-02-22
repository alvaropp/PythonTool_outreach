rmdir /S /Q saves\World1
del /F /Q PythonToolScripts\*.*
Xcopy /E /I BackUpWorld\World1 saves\World1
Xcopy /E /I /y BackUpScripts\* PythonToolScripts\

SET /P LASTNUMOFRUNS= < NumberOfRuns.dat
SET /A NUMOFRUNS=%LASTNUMOFRUNS%+1
echo %NUMOFRUNS%
> NumberOfRuns.dat echo %NUMOFRUNS%

SET /P EngagementScore="Enter Engagement Score: "
>> EngagementScore.dat echo %EngagementScore%
