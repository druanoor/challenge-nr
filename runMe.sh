#!/bin/bash

echo ""
echo "Running program without parameters and without STDIN"
echo "--------------------------------------------"
echo ""

python3 app.py
echo "Sleeping for 5s..."
sleep 5
echo ""

echo "Running program passing one book as parameter"
echo "--------------------------------------------"
echo ""

python3 app.py text-examples/2-word-catcher.txt
echo "Sleeping for 5s..."
sleep 5
echo ""

echo "Running program passing more than one book as parameter"
echo "--------------------------------------------"
echo ""

python3 app.py text-examples/2-word-catcher.txt text-examples/alice-in-wonderland.txt text-examples/moby-dick.txt
echo "Sleeping for 5s..."
sleep 5
echo ""

echo "Running program passing one book from STDIN"
echo "--------------------------------------------"
echo ""

cat text-examples/2-word-catcher.txt | python3 app.py
echo "Sleeping for 5s..."
sleep 5
echo ""

echo "Running program ussing Docker"
echo "--------------------------------------------"
echo ""

docker build -f challenge-nr.Dockerfile -t challenge-nr .
echo "Sleeping for 5s..."
sleep 5
echo ""

echo "Running using STDIN (docker)"
echo "--------------------------------------------"
echo ""

docker run --rm -it -v ${PWD}/text-examples/moby-dick.txt:/app/moby-dick.txt  challenge-nr  cat moby-dick.txt | python3 app.py
echo "Sleeping for 5s..."
sleep 5
echo ""

echo "Running passing book as parameters"
echo "--------------------------------------------"
echo ""

docker run --rm -it -v ${PWD}/text-examples/moby-dick.txt:/app/moby-dick.txt  challenge-nr  python3 app.py moby-dick.txt