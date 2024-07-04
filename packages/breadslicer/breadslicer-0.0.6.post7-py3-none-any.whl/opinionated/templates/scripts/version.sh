#!/bin/sh

# scripts/version.sh
BASEDIR=$(dirname "$0")
latest_version=$($BASEDIR/version_sanitized.sh  $(git describe --tags --abbrev=1))
echo $latest_version-$(git rev-list --count ${latest_version}..HEAD)