#!/usr/bin/env bash

#
# mini release maker for kmlcircle
#
export VERSION=1
export DIR="kmlcircle-${VERSION"
svn export http://kmlcircle.googlecode.com/svn/trunk/ $DIR

rm -rf ${DIR}/images
rm -rf ${DIR}/makerelease.sh

tar -xzvf ${DIR}.tar.gz ${DIR}
