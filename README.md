## USBorderBuddy
A Streamlit web application that allows users to select a US state and see all its neighboring states. The application uses Google BigQuery to query public geospatial data.

Features
-Simple, user-friendly interface
-Dropdown menu with all US states
-Real-time display of neighboring states
-Powered by Google's public BigQuery dataset (bigquery-public-data.geo_us_boundaries.adjacent_states)

## Prerequisites
Before running this application, you need to have:

-Python 3.7 or higher
-A Google Cloud Platform account
-Access to Google BigQuery or a similar BigQuery service
-Appropriate credentials file (JSON) for your BigQuery service

## How to run 

### **Start by cloning the repo to your local machine**
````
git clone https://github.com/nathan-lioe/USBorderBuddy.git
````
### **Download all Requirements**
````
pip install -r requirements.txt

````

Place your Google BigQuery API key file in the project directory and name it geo.json.


### **Run Streamlit**
````
streamlit run app.py

````````
