# Countries
#### Description:
 
 **This Web Application was a project for my applicationa s a web developer at Trading Economics.**
 **Using Trading Economics API I was able to implement a program that lets the user see major economic indicators
 for the countries available in the free tier and if they appreciated or depreciated in value.**

**For API calls I used Python on the back-end that calls the API and passes specific data foramtted as a dictionary into the HTML template**.
The data is then displayed in a table and if the indicator appreciated the value is in green color while when then indicator value depreciated,
the color will be red. 

If there was no recent change in value the color will be grey. The color is based on JavaScript processing the current and previous value of
the indicator which I have set within the id and class names of each row/column.

JavaScript reads the value and then assigns adds a class to the class list. **Up, neutral or down**. Using CSS The color of the value changes accordingly.

Because API calls are limited to one per second, The building of the data structure on the back-end can take some time. To reduce latency
I cached the data in a list and at request, the server will first chose the list as resource, **given the list is not empty**.  

The user can register and the credentials are stored in a MySQL database that runs on a web server. For more security the database will use the built in Flask Werkzeug module and store a hash instead of password characters. When logging in this hash is passed again into a Werkzeug function and then validates if the password is valid or not.

**app.py**
App.py contains all the necessary routes and functions for the web application. There is also a global list to store the fetched data in case the user refreshes the page. Instead of fetching the entire data again, the server will serve the data stored in the list. 

**helpers.py**
Helpers.py contains two functions. The first is called login_required and is a wrapper that will ensure that only logged in users have access to the main page. The other function is called check_connection and it's goal is to ping the MySQL database to ensure that there is an connection. If there is no connection it will repeat this process with a minor delay inbetween, else it will render an error.

**calculate_values.js**
Calculate_values.js is the JavaScript file that computes if a indicator depreciated or appreciated. The indicators that appreciate if the decline in value are stored in an array and upon reading the algorithm will check if the current indicator is negatively positiv and vise versa. 
The algorithm will then automatically add an additional class to the class list. This class is delcared in the CSS to carry a certain color.
Green for increase, Red for decrease or Grey if no change happened.

**index.html**
Index.html is the main page that carries the table with the data. I order to feed all the data into my html, I stored the data via Jinja syntax in IDs and the inner HTML. JS will then go through assigned classes, get the elements id and innter HTML, which are the latest value and the previous value for each indicator. 

This were the main files worthy of an extra explenation. Otherwise there is a standard CSS file that carries the color classes for the values in the table and a register and login page containing forms for user authentication. 

To run the app (on windows) use 
**python -m flask run** or else try **python flask run**
