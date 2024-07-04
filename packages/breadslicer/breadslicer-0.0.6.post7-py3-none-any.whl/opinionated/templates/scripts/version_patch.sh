#!/bin/sh

# scripts/version_path.sh
# This script return from input a version without patch numbering. It ignores
# characters in front of the major and minor versions, such that:
#
# input: v.1.2.3-4
# output: v.1.2

echo "$1" | sed -E 's/^([^0-9]*[0-9]+\.[0-9]+)\..*/\1/'