#!/bin/bash

flatc -b -j -o src/java/ episode.fbs
flatc -b -p -o src/python/ --force-empty-vectors episode.fbs
