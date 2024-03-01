#!/bin/bash

rm ../../app.py
rm ../../data_access_impl.py
rm ../../data_access_interfaces.py
rm ../../nodes.py

cp app.py ../..
cp data_access_impl.py ../..
cp data_access_interfaces.py ../..
cp nodes.py ../..