#!/bin/bash

echo "Content-type: text"
echo
ping -c 1 $QUERY_STRING
