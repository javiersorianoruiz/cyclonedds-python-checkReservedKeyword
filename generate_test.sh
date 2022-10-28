#!/bin/bash

usage()
{
    echo
    echo "USAGE: $0 test_folder]"
    echo "Params List";
    echo "    test_folder  : folder where files for the test are located" 
    echo "    --help or -h : Show this info"
    echo
}

echo $1

if [ -z $1 ]; then
    echo "ERROR: Parameters expected"
    usage
    exit
fi

if [ $1 == "--help" || $1 == "-h" ]; then
    usage
    exit
fi