@echo off
pip install -r requirements.txt

echo [91mNow install MySQL Workbench from https://dev.mysql.com/downloads/workbench/[0m
echo [94mAfter it's installed, create a new schema named "redsnakes" and run the create_tables .sql script on it[0m
echo [95mAfter that is done, run the program from inside PyCharm and check if any exceptions occur or if you can access the default web page at http://127.0.0.1:8000/[0m

pause