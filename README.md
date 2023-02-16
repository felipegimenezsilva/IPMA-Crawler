# IPMA-Crawler

### IPMA Open-Data Crawler

IPMA Open API refers to the open data service provided by the Portuguese Institute for the Sea and the Atmosphere (IPMA). IPMA is a government agency responsible for weather and sea conditions forecasting, and provides a range of meteorological and oceanographic services to the public, including data on temperature, precipitation, wind, and wave conditions, among others.

The IPMA Open API is a programming interface that allows developers to access and retrieve real-time weather and sea information, as well as historical data, for any location in Portugal. The API provides data in various formats, including JSON and XML, and can be used to develop weather and oceanography applications, as well as integrate weather data into other services and systems.

The IPMA Open API is free to use, and developers are encouraged to use the service to create innovative weather applications, products, and services. However, there are some terms and conditions for using the API, which can be found on the IPMA website.

### Project Description

This algorithm crawls through the IPMA Open Data API to search and process information, collecting the file name, file URL, and the date/time of the last update for each file. It returns a pandas dataframe and functions as a web crawler. This project aims to create a list of content and streamline the process of checking for updates to the content available in the API.

Please note that this program is available for anyone to use, but it should be used with caution and used in accordance with the permissions provided by IPMA.

### Example of usage:

install the dependencies;
```
pip install -r requirements.txt
```
Running the algorithm: 
```
python3 crawler_ipma.py
```
