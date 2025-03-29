@echo off
:: Navigate to the project directory
cd D:\KoooraBroadcastTracker

:: Activate the virtual environment
call env\Scripts\activate

:: Run the scheduler script
python scheduler.py

:: Deactivate the virtual environment (optional)
deactivate

:: Pause to allow viewing of any errors (optional)
pause