#!/usr/bin/env bash

#
# mini release maker for kmlcircle
#
export VERSION=001
export DIR="kmlcircle-${VERSION}"
rm -rf ${DIR}
rm -rf ${DIR}.tar.gz

svn export http://kmlcircle.googlecode.com/svn/trunk/ $DIR

rm -rf ${DIR}/images
rm -rf ${DIR}/hurricanes
rm -rf ${DIR}/makerelease.sh

tar -czvf ${DIR}.tar.gz ${DIR}
