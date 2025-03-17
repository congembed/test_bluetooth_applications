Project guideline

## How to push into SilabsSandbox repo
1. Force repo which you want to working on.

2. Use git to push your code
At your local machine:
git add ./
git commit -m "Commit messages"
git push

## CI-Bot checking
Github repos with use CI/CD system to automatic checking your pull request:
Check coding style, README.md file, build firmware and check coding quality use SonarQube tool.

If any Github check status fail, please click *Details* to know and fix it.

1. Coding style
Using Uncrustify tool to check coding style.

If checking Fail, click "Details" to show the details.


2. Check README.md file
Please add all necessary title on your README.md file



The list of title need to be added into README.md file

Overview/Summary
SDK Version
Hardware Required
Connections Required/Hardware Connection
Setup
How It Works

Refer to this project: https://github.com/SiliconLabs/bluetooth_applications/tree/master/bluetooth_air_quality_monitor

If all sections existing on README.md file it will be Pass.

SDK version: Please follow format if you use Gecko Sdk or Simplicity SDK

NOTE: Gsdk or SiSDK version is right version on github repo



Check URL Links & Files Path: This section will check all website link, image PATH in README file. If it not existing then Failed.

NOTE: Don't use private link in README file like github _staging or silabs private url. When it be public on github, viewer could not be access into it.

3. Build Firmware
It will build project and verify that there are no error and no warning in your projects.

4. Check SonarQube
