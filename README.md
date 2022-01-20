# Nseindia parser
____
## This is data parser via selenium on the site https://www.nseindia.com/

The parser contains human imitation and fake activity.

Parser save data into __TotalCost.csv__ with format: name:final_price

For the starting work python 3 is required.

## PRE-setup

1. fill in the proxy data in **.env** file
```
    PROXY_IP= "Proxy ip"
    PROXY_PORT= "Proxy port"
    PROXY_LOGIN= "Proxy login"
    PROXY_PASSWORD= "Proxy password"
    PROXY_TYPE="http or https"
```
2. download [chromedriver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) and put it into the path

## Starting project
```
1. pip install -r requirements.txt
2. python nseindia_parser.py
```