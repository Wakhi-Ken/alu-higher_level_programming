#!/bin/bash
# shows size of the body of the response
response=$(curl -sI "$1")
content_length=$(echo "$response" | sed -ne 's/Content-Length: \([0-9]*\).*/\1/p')
echo "$content_length"
