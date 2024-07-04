#!/bin/sh

# scripts/version_sanitized.sh
# This script returns from input a version that it is sanitized from everything
# except major, minor and patch. It ignores characters in front of the major and
# minor versions, such that:
#
# input: v.1.2.3-4
# output: v.1.2.3

echo "$1" | sed -E 's/^([^0-9]*[0-9]+\.[0-9]+\.[0-9]+).*/\1/'