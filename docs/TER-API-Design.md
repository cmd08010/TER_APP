# TER-API-Design
This document describes the API exposed by TER app. 

# API

The API supports several consumers:
* PRAIS application which sends TER pricing information to TER, at /prices/
* NISC process which sends TER meter info to TER, at /meters/
* Admin users observing devices operational status at /devices/
* Admin users via admin portal, at /admin

The API is currently hosted on Azure, without an associated domain name. The IP address may change during development and will
be distrubuted via email. The API is acccessible on port 8000.

## Prices API
The prices API accepts requests from PRAIS to add pricing schedules to TER, and to read the history of pricing schedules. 
A price schedule has a date value understood to represent the day on which the schedule is provided, containing a list of 
hourly prices for the following day. Any number of schedules can be provided for a given day - only the most recently added 
up to the close of the day will be processed. A price schedule is expected to be received at least once per day by TER, to 
represent the following day's TER rates. The TER application is responsible for receiving rate schedules from PRAIS and 
passing them along to an OpenADR VTN, which in turn passes it to OpenADR VENs.

Requests to the prices API requires http basic auth username and password credentials. These will be distributed to clients via email.

To obtain list of price schedules:
GET http://<host:port>/prices/
e.g. GET http://52.255.194.193:8000/prices/

To add a price schedule:
POST http://<host:port>/prices/
e.g. POST http://52.255.194.193:8000/prices/

example payload:
{
    "schedule": {
        "date":"2022-02-22",
        "prices": [
            {"datetime":"2022-02-23T0:0:0+0000","price":"12.34"},
            {"datetime":"2022-02-23T0:1:0+0000","price":"23.45"},
            {"datetime":"2022-02-23T0:2:0+0000","price":"34.56"}
        ]
    }
}

## Meters API
The meters API accepts requests from NISC (or intermediate agent) to add meter data to TER. A meter record contains 
meter ID, VEN ID, and device ID. This allows TER to associate a usage report received from a given VEN for a given device 
to be associated with a meter, and therefore to create a usage report for the NISC billing system (MDM). NISC must become 
aware of VENs and their devices prior to populating TER with this information. This is accomplished through a registration 
process defined elsewhere. 

While there only needs to be one list of meters, the API framework used by the TER allows multiple records to exist. By convention,
user's of the API should act is if there is just one instance of the meters list, and after using an http POST operation to
create an initial instance, subsequent updates should be made to that instance using the http PUT operation with the 'id' of the resource.
A nuance is that
during development and testing multiple instances may be created and destroyed, each incrementing the instance 'id', therefore, 
users must discover the autogenersted 'id', returned in the response to the POST operation, and use that value in the path for subsequent 
PUT operations. For example:

POST response =
{"id":7,"created":"2022-02-25T18:11:48.431285Z","meters":[{"meter_id":"TER0001","ven_id":"NHEC_test_01","device_id":"device099"}]}

PUT path = http://52.255.194.193:8000/meters/7/

Requests to the meters API requires http basic auth username and password credentials. These will be distributed to clients via email. 

The API is currently hosted on Azure, without an associated domain name. As of this writing:
host:port = 52.255.194.193:8000

To obtain list of meters records:
GET http://<host:port>/meters/
e.g. GET http://52.255.194.193:8000/meters/

To add a meters record:
POST http://<host:port>/meters/
e.g. POST http://52.255.194.193:8000/meters/

example payload:
{
    "meters": [
        { "meter_id": "TER0001", "ven_id": "NHEC_test_01", "device_id": "device099" }
    ]
}

To update a meters record:
PUT http://<host:port>/meters/<id>
e.g. POST http://52.255.194.193:8000/meters/10/

example payload:
{
    "meters": [
        { "meter_id": "TER0001", "ven_id": "NHEC_test_01", "device_id": "device099" }
    ]
}

## devices API
The TER app will maintain the operational status (ON/OFF) for each according to reports provided by VENs. 

Requests to the devices API requires http basic auth username and password credentials. These will be distributed to clients via email. 

The API is currently hosted on Azure, without an associated domain name. As of this writing:
host:port = 52.255.194.193:8000

To obtain list of devices:
GET http://<host:port>/devices/
e.g. GET http://52.255.194.193:8000/devices/

Example response:
[{"id":10,"device_id":"device001","ven_id":"NHEC_test_01","statusOn":true}]


