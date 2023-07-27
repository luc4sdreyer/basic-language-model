@echo off

set THIS_PATH_WITH_SLASH=%~dp0
set THIS_PATH=%THIS_PATH_WITH_SLASH:~0,-1%

python -m venv venv
set PYTHON=%THIS_PATH%/venv/Scripts/python
@REM echo %THIS_PATH_WITH_SLASH%
@REM echo %THIS_PATH%
@REM echo %PYTHON%
%PYTHON% -m pip install -r requirements.txt
ipython kernel install --user --name=venv
