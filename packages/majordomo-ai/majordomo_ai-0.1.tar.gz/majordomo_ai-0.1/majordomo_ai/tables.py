import requests
import os
import json
from pathlib import Path

def create_table_from_csv(client_url, 
                          database, 
                          table_name, 
                          input_device, 
                          input_file, 
                          **kwargs
                          ):
    debug_on = False

    json_input = {}
    azure_credentials = {}
    azure_blob = {}

    json_input['database'] = database
    json_input['table_name'] = table_name
    json_input['input_file'] = input_file
    json_input['input_device'] = input_device

    # Fill the default values.
    json_input['append'] = False

    # Parse the user overrides.
    for key, value in kwargs.items():
        match key:
            case "debug_on":
                debug_on = value
            case "append":
                append = value
            case default:
                pass

    if input_device == "local":
        my_file = Path(input_file)
        if not my_file.is_file():
            raise ValueError("Input file not found")

        file = {'file': open(input_file, 'rb')}

        resp  = requests.post(client_url + '/file_upload', files=file)
        if debug_on:
            print(resp.json())

    elif input_device == "azure_blob":
        json_input['azure_credentials'] = azure_credentials
        json_input['azure_blob'] = azure_blob

    try:
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(json_input)
        result = requests.post(client_url + '/csv_ingestion', data=json_data, headers=headers)
        if debug_on:
            print(result.content)
    except Exception as e: raise

    return result

def tables_query(client_uri, 
                 user_token, 
                 embedding_model, 
                 llm_model, 
                 database, 
                 table_names, 
                 query_str,
                 **kwargs
                 ):
    debug_on = False

    json_input = {}

    json_input['user_token'] = user_token

    # Fill the default values.
    json_input['embedding_model'] = embedding_model
    json_input['llm_model'] = llm_model
    json_input['database'] = database
    json_input['table_names'] = table_names
    json_input['query'] = query_str
    json_input['temperature'] = 1.0
    json_input['top_k'] = 2

    # Parse the user overrides.
    for key, value in kwargs.items():
        match key:
            case "debug_on":
                debug_on = value
            case "temperature":
                json_input['temperature'] = value
            case "top_k":
                json_input['top_k'] = value
            case default:
                pass

    try:
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(json_input)
        result = requests.post(client_uri + '/sql_query', data=json_data, headers=headers)
        if debug_on:
            print(result.content)
    except Exception as e: raise

    return result

#create_table_from_csv("http://127.0.0.1:8000",
#                      "stock",
#                      "table1",
#                      "local",
#                      "/home/azureuser/Stock Price.csv",
#                      debug_on=True
#                      )
#
#tables = ["table1"]
#tables_query("http://127.0.0.1:8000",
#          "md-02c52fd6-a17c-4169-aebb-1cb4fa7ee60c", 
#          "text-embedding-3-large",
#          "gpt-3.5-turbo",
#          "stock",
#          tables,
#          "Which is the best performing stock in last 3 months in percentage terms?"
#          )
