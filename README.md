# Countries - A web application that displays economic indicators
## Complexity:
 This is a web application that uses Trading Economics API to display economic indicators. The value will be green, red or grey, depending if an indicator appreciated, depreciated or did not change in respect to the previous day.

Challenging problems were:
* Caching the data
* The processing of the values on the front-end using JavaScript
* The layout of the table, as it is not the normal table of the Bootstrap framework.


## Files

**main.py** contains the route functions for the web application and also the credentials to connect the MySQL database. A test API key from tradingeconomics is provided that is limited request for the five countries I used. 
**app.yaml** serves the web applications on Google Cloud.
**helpers.py** contains a decorater function and check_connection, a functio that pings the database to ensure connection and returns an error if no connection can be achieved.

## Where to find
The web application can be viewed [here](https://countriesdp.herokuapp.com/). There may be a longer loading time when logging in because the API is limited to a certain number of request and multiple request are being send to fetch the economic data. 
