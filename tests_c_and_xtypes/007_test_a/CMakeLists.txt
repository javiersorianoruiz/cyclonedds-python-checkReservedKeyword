#
# Copyright(c) 2019 to 2022 ZettaScale Technology and others
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v. 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Eclipse Distribution License
# v. 1.0 which is available at
# http://www.eclipse.org/org/documents/edl-v10.php.
#
# SPDX-License-Identifier: EPL-2.0 OR BSD-3-Clause
#
project(helloword LANGUAGES C)
cmake_minimum_required(VERSION 3.16)
#IDL_FILE declaration with info to show if it is used cmake .. -LAH
SET(IDL_FILE "test.idl" CACHE STRING
              "Name of the IDL file which has to be in the folder ${TEST_NAME}.")


#TEST_NAME
if(NOT DEFINED TEST_NAME)
  message(FATAL_ERROR  "TEST_NAME has to be indicated. By example: \ncmake .. -DTEST_NAME=007_test_a")
endif(NOT DEFINED TEST_NAME)
message(STATUS "TEST_NAME=${TEST_NAME}")

#TEST_FULL_NAME
set(TEST_FULL_NAME  "${CMAKE_HOME_DIRECTORY}/../../tests/${TEST_NAME}/")
message(STATUS "TEST_FULL_NAME=${TEST_FULL_NAME}")

#IDL_FILE_FULL_NAME
set(IDL_FILE_FULL_NAME  "${TEST_FULL_NAME}${IDL_FILE}")
message(STATUS "IDL_FILE_FULL_NAME=${IDL_FILE_FULL_NAME}")

#TO DO
set(CMAKE_PREFIX_PATH "/usr/local/lib/cyclonedds/lib/cmake/CycloneDDS/")

if(NOT TARGET CycloneDDS::ddsc)
  # Find the CycloneDDS package.
  find_package(CycloneDDS REQUIRED)
endif()

# This is a convenience function, provided by the CycloneDDS package,
# that will supply a library target related the the given idl file.
# In short, it takes the idl file, generates the source files with
# the proper data types and compiles them into a library.

#Autogeneration C files from IDL file using IDLC Compiler
idlc_generate(TARGET ${TEST_NAME}_idl_generated_lib FILES ${IDL_FILE_FULL_NAME} WARNINGS no-implicit-extensibility)

# Both executables have only one related source file.
add_executable(Publisher${TEST_NAME} publisher.c)
add_executable(Subscriber${TEST_NAME} subscriber.c)

# Both executables need to be linked to the idl data type library and
# the ddsc API library.
target_link_libraries(Publisher${TEST_NAME} ${TEST_NAME}_idl_generated_lib CycloneDDS::ddsc)
target_link_libraries(Subscriber${TEST_NAME} ${TEST_NAME}_idl_generated_lib CycloneDDS::ddsc)
