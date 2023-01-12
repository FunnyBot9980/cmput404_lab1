#!/bin/bash

curl -ik https://webdocs.cs.ualberta.ca/~hindle1/1.py -o file1
curl -ik -X POST -d "X=Y" https://webdocs.cs.ualberta.ca/~hindle1/1.py -o file2
