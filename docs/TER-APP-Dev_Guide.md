# TER-APP-Dev-Guide
This document describes the architecture and API exposed by TER app, and provides a developer's guide to starting and monitoring activity. 

A core feature of the application is support for the openADR protocol, which is not explained here.

# Modules
The TER app is composed of several conceptual modules (not necessarily python modules).
* API - the app exposes admin, prices, meters, and devices APIs, with web views, via Django
* VTN - an OpenADR server communicates to OpenADR clients aka VENs. Integrates with TER logic to acquire priceing data to send events to VENs and respond to usage and status reports from VENs
* TER app, including event poll - a python scheduled job that polls the prices API for current price schedules and calls the VTN, and updates external MDM service with usage reports
    to generate an OpenADR event for VENs
* Test VEN - a simple OpenADR VEN used to validate VTN functionality.

# Start up
1) Setup terminal windows on local and remote systems
    - On local machine, open cmd prompt, git clone nhec_ter repo and cd nhec_ter
    - Ssh into dev or staging
2) populate prices API
    * edit assets/prices.json to set schedule.date to today's date, and set all prices.datetime date values to tomorrow's date, e.g. 
        "schedule": {
        "date":"2022-04-27",
        "prices": [
            {"datetime":"2022-04-28T0:0:0+0000","price":"23.45"},
            ...
    * Post updated prices, e.g. 
        - curl -X POST -u admin:StagingTER -H 'Content-Type: application/json' -d @assets/prices.json http://staging.nhecter.com/prices/
3) populate prices API
    * view /meters/ to ensure contains entry for test VEN, e.g.
            "meters":[
                { "meter_id": "TER0001", "ven_id": "NHEC_test_01", "device_id": "DEVICEABS123DCN8889999" },
    * edit assets/meters.json and POST to /meters/ if need be, e.g. 
        - curl -X POST -H 'Content-Type: application/json' -d @assets/meters.json http://staging.nhecter.com/meters/
4) Start TER
    * on dev or staging, cd nhec_ter, start TER
        - sudo docker-compose -f staging.docker-compose.yml up -d
    * view VTN logs
        - sudo docker logs -f nhec_ter_vtn_1
5) on local machine, start VEN
    * python openadr/ven.py -i NHEC_test_01 -d DEVICEABS123DCN8889999 -v staging.nhecter.com  -s 242
6) Monitor behavior via logs on local and remote terminals, sequence of events should be
    * VEN registers with VTN
    * VEN registers status and realEnergy (usage) reports with VTN
    * TER periodically adds events to VTN
        - this involves TER poller to read from /prices/ API and create events
    * VEN periodically pulls events from VTN
    * VTN periodically recieves status and usage reports from VEN
        - on receipt of status report, VTN hands report to TER app which updates /devices/ API
        - on receipt of usage reports, VTN hands report to TER app which updates /devices/ API and sends a CMEP reports tp MDM endpoint



