#!/bin/bash

if [ -d './deploy' ]; then
	rm -rf './deploy'
fi

mkdir './deploy'

cp 'index.html' './deploy'
cp -r 'stylesheets' './deploy'
cp -r 'js' './deploy'
cp -r 'bower_components' './deploy'

git subtree push --prefix deploy origin gh-pages