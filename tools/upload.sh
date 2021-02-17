#!/bin/sh

FROM='upload'
TO='gh-pages'

# If static directory is clean, do nothing 
if [[ -z $(git status -s static) ]]; then 
    exit 0 
fi

git config --global user.name 'anonymous'
git config --global user.email 'anonymous'

git fetch

# Update resources
git checkout $TO
rm -rf static/profile.yml
git checkout $FROM -- static
git add static 
git commit -m ':seedling: Resources updated.'
git push

# Delete cache
git checkout $FROM
ls static | grep -v 'profile.yml' | xargs -I {} rm -rf static/{}
git add static
git commit -m ':wastebasket: Cache deleted.'
git push
