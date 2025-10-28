#!/bin/bash
# Instructions to push to your GitHub
git init
git add .
git commit -m "Initial commit: AIIS-WH2 scaffold"
git branch -M main
git remote add origin https://github.com/benchen1981/AIIS-WH2.git
git push -u origin main
# Note: you must have permission to push to this repo. Create the repo on GitHub first or run:
# gh repo create benchen1981/AIIS-WH2 --public --source=. --remote=origin
