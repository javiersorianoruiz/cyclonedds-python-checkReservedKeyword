#!/bin/bash

FILE_TEST="test.idl"

#Example execution to save a file output console including errors
#rm -f output-9-nov-22.txt && ./launch_tests.sh -a 2>&1 > output-9-nov-22.txt

usage()
{
    echo
    echo "USAGE: $0 [--iterative|--automatic(default)]"
    echo "Params List";
    echo "    --iterative or -i : After each test execution a press key is required to continue tests execution" 
    echo "    --automatic or -a : All tests are executed without any interruption" 
    echo "    --help or -h : Show this info"
    echo
}

iterative=true

#set mode iterative or automatic
#if not indicated mode, default mode automatic is set
if [ -z $1 ]; then
    iterative=false
    elif [ $1 == "--iterative" ] || [ $1 == "-i" ]; then
        iterative=true
    elif [ $1 == "--automatic" ] || [ $1 == "-a" ]; then
        iterative=false
    elif [ $1 == "--help" ] || [ $1 == "-h" ]; then
        #show help info if the first param is -h or --help
        usage
        exit
    else
        #Unknown parameter
        usage
        exit
fi


function ProgressBar {
# Process data
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done
# Build progressbar string lengths
    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

# 1.2 Build progressbar strings and print the ProgressBar line
# 1.2.1 Output example:                           
# 1.2.1.1 Progress : [########################################] 100%
printf "\rProgress : [${_fill// /#}${_empty// /-}] ${_progress}%%"

}

#execute a test for each directory that it is found
tests=`ls -d */ | sort -n`
number_total_tests=`echo ${tests[@]} | wc -w`
number_test=1
echo "Number total of tests to be excecuted: " $number_total_tests
for test in $tests
do
    #if mode is iterative, before each test, the screen is cleaned.
    if [ "$iterative" = true ] ; then
        clear
    fi
    #delete caracter / at the end of name folder
    testName=`echo $test | sed 's/.$//g'`
    echo "------------------------------------------------------------"
    echo "Executing test $number_test of $number_total_tests with Name: $testName"
    ProgressBar $number_test $number_total_tests
    #show IDL for test
    idl_test_file=$test$FILE_TEST
    echo -e "\n\tShow content IDL test file: $idl_test_file"
    echo "------------------------------------------------------------"
    cat $idl_test_file
    echo "------------------------------------------------------------"

    ./generate_test.sh $testName

    #if mode is iterative wait user press key
    if [ "$iterative" = true ] ; then
        if [ "$number_test" -lt "$number_total_tests" ] ; then
            echo "Press any key to continue with the following test ..."
            read -n 1 -s
        fi
    fi

    let "number_test++"
done
