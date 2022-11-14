IDLC generation for python:
IMPORTANT: Go to the path where the idl is located and executed (it doesn't work in other path):
cd /app/helloworld_topic
rm -rf module_test/* && /usr/local/lib/cyclonedds/bin/idlc -l/usr/local/lib/python3.8/dist-packages/cyclonedds/_idlpy.cpython-38-x86_64-linux-gnu.so -Wno-implicit-extensibility -o /home/jasorian/cyclonedds-python-checkReservedKeyword/tests/001_test /home/jasorian/cyclonedds-python-checkReservedKeyword/tests/001_test/test.idl

In a second terminal, (don't reuse the previous terminal used for the IDL generation for python) 
compile and update lib idlpy (plugin python idlc)
export CYCLONEDDS_HOME=/usr/local/lib/cyclonedds/

#New way to compile and install (recommended)
    python3 setup.py build
    pip3 install .
########################

#Old way (manually, not recommended)
    rm -f ./build/lib.linux-x86_64-3.8/cyclonedds/_idlpy.cpython-38-x86_64-linux-gnu.so
    python3 setup.py build
    ll ./build/lib.linux-x86_64-3.8/cyclonedds/_idlpy.cpython-38-x86_64-linux-gnu.so
    cp -f ./build/lib.linux-x86_64-3.8/cyclonedds/_idlpy.cpython-38-x86_64-linux-gnu.so /usr/local/lib/python3.8/dist-packages/cyclonedds/_idlpy.cpython-38-x86_64-linux-gnu.so
    Update python files from cyclonedds-python
    cp -f /app/cyclonedds-python/cyclonedds/idl/annotations.py /usr/local/lib/python3.8/dist-packages/cyclonedds/idl/annotations.py
    cp -f /app/cyclonedds-python/cyclonedds/idl/_xt_builder.py /usr/local/lib/python3.8/dist-packages/cyclonedds/idl/_xt_builder.py
########################