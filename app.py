import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import os

st.title("US States Neighbor Finder")
st.write("Select your state to see all neighboring states")

key_path = "geo.json"

def create_bigquery():

    if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        return bigquery.Client()
    
    try:
        credentials = service_account.Credentials.from_service_account_file(
            key_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        return bigquery.Client(credentials=credentials, project=credentials.project_id)
    except Exception as e:
        st.error(f"Error setting up BigQuery client: {e}")
        st.info("Please make sure your service account key file exists and has the correct permissions.")
        return None


def get_states():
    client = create_bigquery()
    if not client:
        return []
    
    query = """
    SELECT DISTINCT state_name 
    FROM `bigquery-public-data.geo_us_boundaries.adjacent_states`
    ORDER BY state_name
    """
    query_job = client.query(query)
    results = query_job.result()
        
    s_list = []
    for row in results:
        s_list.append(row.state_name)
    return s_list

    

def get_neighbors(state_name):
    client = create_bigquery()
    if not client:
        return []
    
    query = f"""
    SELECT neighbor 
    FROM `bigquery-public-data.geo_us_boundaries.adjacent_states`,
    UNNEST(neighbors_state) AS neighbor
    WHERE state_name = '{state_name}'
    ORDER BY neighbor
    """

    n_list = []
    query_job = client.query(query)
    results = query_job.result()
    for row in results:
        n_list.append(row.neighbor)
    return n_list

all_states = get_states()

if all_states:
    home_state = st.selectbox("Select your State", all_states)

    if home_state:
        neighbors = get_neighbors(home_state)
        if neighbors:
            st.subheader(f"States bordering {home_state}:")
            for x in neighbors:
                st.write(f"{x}")


