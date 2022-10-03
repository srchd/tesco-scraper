@echo off
setlocal enabledelayedexpansion
set ENV=""
set NEEDED_ENV=tesco-scrap

for /f %%e in ('conda info --envs') do (
	if %%e==%NEEDED_ENV% (
		set ENV=%%e
		echo !ENV!
	)
)

if !ENV!=="" (
	echo anyad
	call conda env create -f environment.yml
)
@echo on