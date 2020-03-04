#!/bin/bash

# current Git branch
branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')


# establish branch and tag name variables
devBranch=develop
masterBranch=master
releaseBranch=release-$versionLabel
 

# create the release branch from the -develop branch
git checkout -b $releaseBranch $devBranch

DATE=$(date)

# commit version number increment
git commit -am "changes made on $DATE"

git checkout $masterBranch
git merge --no-ff $releaseBranch


