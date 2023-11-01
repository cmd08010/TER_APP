# nhec-ter
Transactive Energy Rate application, including OpenADR support

# TBD: DEFINE A LICENSE  

# About The Project
The TER application sends hourly pricing data to NHEC member's devices to allow those devices to schedule their 
electrical consumption at optimal times. Usage data is reported back from those devices and passed to an NHEC
settlement engine to calculate monthly bills based on usage and hourly TER prices.

The TER app integrates with other systems to 
* acquire daily TER pricing data (next day's hourly prices). Integration with NHEC PRAIS system via TER REST API
* acquire 'dummy' meter data from NISC to associate telemetry to an account. Integration with NISC agent via TER API
* send usage reports for billing reconciliation. Integration with NISC MDM system via CMEP formatted REST requests
* invoke OpenADR VTN component to send pricing data to OpenADR VENs representing member devices
* acquire usage data from VTN, which in turn has acquired OpenADR reports from VENs

A detailed design document is maintained on Bellwatt's Google drive.

# Getting Started
The TER and its backend database are launched as docker containers via 'docker compose up' at the cmd line at the project
root. Once running, configuration of the database and users is performed as so:

Now let's open a new cmd prompt to run the following commands:
```
cmd prompt> docker exec -it nhec_ter_web_1 /bin/bash
container prompt> python manage.py makemigrations prices
container prompt> python manage.py makemigrations meters
container prompt> python manage.py migrate
container prompt> python manage.py createsuperuser // enter un/pswd eg: admin adminPswd123
```

Open the browser then navigate to: http://127.0.01:8000/admin <br/>
Enter the superuser credentials as we created above (eg: admin adminPswd123)

create group named 'prices' with permissions to access prices API (4 permissions)<br/>
create group named 'meters' with permissions to access meters API (4 permissions)<br/>

create user named prais, provide a pswd, e.g. prPswd123, associated with group 'prices'<br/>
create user named nisc, provide a pswd, e.g. niPswd123, associated with group 'meters'<br/>

One can navigate the prices and meters APIs as superuser in the browser, 

> http://127.0.0.1/prices/

> http://127.0.0.1/meters/

or can access it programmatically via curl or
other, e.g.

> cmd prompt> curl -u prais:prPswd123* http://127.0.0.1:8000/prices/

> cmd prompt> curl -X POST  -u nisc:niPswd123* -H 'Content-Type: application/json' \\
-d '{ "meters": { "meterID": "0001", "VEN_ID": "999", "device_id": "47" } }' http://127.0.0.1:8000/meters/
