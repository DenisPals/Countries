# Countries - A web application that displays economic indicators
## Complexity:
 This is a web application that uses [Tradingeconomics](https://tradingeconomics.com/) free API to display economic indicators. The value will be green, red or grey, depending if an indicator appreciated, depreciated or did not change in comparison to the previous day.

Some of the greater challenges were:
* Caching the data
* The processing of the values on the front-end using JavaScript
* The layout of the table, as it is not the normal table of the Bootstrap framework.

The test-version of Tradingeconomics API let's the developer access indicator data for 5 countries, therefore the user experience is limited when using Countries.

## Files

**main.py** &rarr; contains the route functions for the web application and also the credentials to connect the MySQL database. A test API key from tradingeconomics is provided that is limited request for the five countries I used. 

**calculate_values.js** &rarr; contains the javaScript fot the project and performs the color assignment to the values in the Table.

**helpers.py** &rarr; contains a decorater function and check_connection, a functio that pings the database to ensure connection and returns an error if no connection can be made.

## How to run
The web application can be viewed [here](https://countriesdp.herokuapp.com/). There may be a longer loading time when logging in because the API is limited to a certain number of request and multiple request are being send to fetch the economic data. Feel free to sign up using fake credentials, you won't receive any emails.
