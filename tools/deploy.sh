#!/bin/sh

FROM='front-end'
TO='gh-pages'

# Check
if [ -f 'NOT_BUILD' ]; then
    exit 0
fi

git config --global user.name 'anonymous'
git config --global user.email 'anonymous'

git fetch

# Build stati pages
git checkout $FROM
npm install
npm run build
git checkout -- package-lock.json

# Remove old pages
git checkout $TO
ls | grep -E -v 'static|dist|CNAME' | xargs -I {} rm -rf {}
mv ./dist/* .
rm -rf ./dist
touch .nojekyll
rm -rf dist node_modules

# Push changes
git add -A
git commit -m ':seedling: Pages updated.'
git push