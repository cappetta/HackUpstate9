#!/usr/bin/env bash


echo "display dispensary information"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/dispensary


echo "Display OnCall Doctors - Bob"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/meet/Bob
echo "Display OnCall Doctors - Mary"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/meet/Mary
echo "Display OnCall Doctors - Wendel"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/meet/Wendel
echo "Display OnCall Doctors - Doug"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/meet/Doug


echo "Display Doctors List "
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/doctors

echo "Display Quality Testing Results - AK-47 "
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/quality/AK-47

echo "Display Quality Testing Results - BlueLighning "
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/quality/BlueLighning

echo "Display Quality Testing Results - Gorilla"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/quality/Gorilla


echo "Display Quality Testing Results - GirlScoutCookies"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/quality/GirlScoutCookies


echo "Testing Inventory Lookup - Hybrid"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/info/hybrid

echo "Testing Inventory Lookup - Sativa"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/info/sativa

echo "Testing Inventory Lookup - Indica"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/info/indica

#sleep 10

echo "testing place 1st order"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/place/1

echo "testing place 2nd order"
http  https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/place/2

echo "testing place 3rd order"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/place/3


#sleep 10

echo "testing retrieve 1st order"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/retrieve/1

echo "testing retrieve 2nd order"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/retrieve/2

echo "testing retrieve 3rd order"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/retrieve/3



echo "testing register 1st device"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/register/Mary

echo "testing register 2nd device"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/register/John

echo "testing register 3rd device"
http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/register/Tom


echo "testing posting inventory - Mary"
echo '{"AK-47": "5g"}' |http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/add/Mary

echo "testing posting inventory - John"
echo '{"Blue Lightning": "112g"}' |http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/add/John


echo "testing posting inventory - Tom"
echo '{"Cookies": "20", "Cartridges": "10"}' |http https://54bsx6qo9l.execute-api.us-east-1.amazonaws.com/dev/add/Tom





