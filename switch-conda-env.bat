@ECHO OFF

set root=C:\Users\%USERNAME%\anaconda3
set env-name=integrated-announcement

echo | set /p="Trying to run conda..."
call %root%\Scripts\activate.bat %root%
echo Success !!

echo | set /p="Changing conda's environment..."
call conda activate %env-name% 2> NUL

if errorlevel 1 (
  echo Failure
  echo The %env-name% environment does not exist
  echo | set /p="Creating %env-name% environment.."
  call conda create -n %env-name% python=3.11 -y > NUL 2>&1
  echo | set /p="Creating %env-name% environment..."
  call conda activate %env-name%
)
echo Success !!

echo | set /p="Installing require python packages..."
call pip install -r requirements.txt > NUL
echo Success !!