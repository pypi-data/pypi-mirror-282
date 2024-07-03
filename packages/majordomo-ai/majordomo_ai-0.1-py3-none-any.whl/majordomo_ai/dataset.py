import requests
from pathlib import Path
import os
import json
from datetime import datetime

def create_dataset_from_document(client_url, 
                                 user_token, 
                                 dataset, 
                                 input_device, 
                                 input_file, 
                                 embedding_model,
                                 **kwargs
                                 ):
    debug_on = False

    json_input = {}
    azure_credentials = {}
    azure_blob = {}

    json_input['user_token'] = user_token

    json_input['dataset'] = dataset
    json_input['input_file'] = input_file
    json_input['input_device'] = input_device

    # Fill the default values.
    json_input['index_type'] = "vector_db"
    json_input['pdf_extractor'] = "PyMuPDF"
    json_input['llm_model'] = ''
    json_input['embedding_model'] = embedding_model

    # Parse the user overrides.
    for key, value in kwargs.items():
        match key:
            case "index_type": 
                json_input['index_type'] = value
            case "debug_on":
                debug_on = value
            case "azure_client_id": 
                azure_credentials['client_id'] = value
            case "azure_tenant_id": 
                azure_credentials['tenant_id'] = value
            case "azure_client_secret": 
                azure_credentials['client_secret'] = value
            case "azure_account_url": 
                azure_blob['account_url'] = value
            case "azure_container_name": 
                azure_blob['container_name'] = value
            case "azure_blob_name": 
                azure_blob['blob_name'] = value
            case "pdf_extractor":
                json_input['pdf_extractor'] = value
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
        result = requests.post(client_url + '/doc_ingestion', data=json_data, headers=headers)
        if debug_on:
            print(result.content)
    except Exception as e: raise

    return result

def create_dataset_from_slack(client_url, 
                                 user_token, 
                                 dataset, 
                                 slack_token, 
                                 slack_channel, 
                                 embedding_model,
                                 **kwargs
                                 ):
    debug_on = False

    json_input = {}

    json_input['user_token'] = user_token

    json_input['dataset'] = dataset
    json_input['slack_token'] = slack_token
    json_input['channel_id'] = slack_channel

    # Fill the default values.
    json_input['index_type'] = "vector_db"
    json_input['llm_model'] = ''
    json_input['embedding_model'] = embedding_model
    json_input['start_date'] = "01/01/2024"
    json_input['end_date'] = "01/01/2025"

    # Parse the user overrides.
    for key, value in kwargs.items():
        match key:
            case "index_type": 
                json_input['index_type'] = value
            case "debug_on":
                debug_on = value
            case "start_date":
                json_input['start_date'] = value
            case "end_date":
                json_input['end_date'] = value
            case default:
                pass

    try:
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(json_input)
        result = requests.post(client_url + '/slack_ingestion', data=json_data, headers=headers)
        if debug_on:
            print(result.content)
    except Exception as e: raise

    return result

#create_dataset_from_slack("http://127.0.0.1:8000",
#                          "md-02c52fd6-a17c-4169-aebb-1cb4fa7ee60c", 
#                          "slackdata", 
#                          "xoxb-7192156673861-7204518115204-fqOSLMXmVX65dUTQNkHgS6MS",
#                          "C0779E23FCP",
#                          "text-embedding-3-large",
#                          debug_on=True
#                          )

#create_dataset_from_document("md-02c52fd6-a17c-4169-aebb-1cb4fa7ee60c", 
#                             "whales", 
#                             "URL", "https://gamma.tatacommunications.com/assets/wp-content/uploads/2024/06/institutional-investors-and-analysts-meet-2024-transcript.pdf",
#                             "text-embedding-3-large",
#                             debug_on=True
#                            )

#create_dataset_from_document("md-02c52fd6-a17c-4169-aebb-1cb4fa7ee60c", 
#                             "court", 
#                             "local", 
#                             "/home/azureuser/court.txt",
#                             "text-embedding-3-large",
#                             debug_on=True
#                            )


#create_dataset_from_document("md-02c52fd6-a17c-4169-aebb-1cb4fa7ee60c", 
#                             "macbeth", 
#                             "azure_blob", 
#                             "",
#                             "text-embedding-3-large",
#                             azure_client_id="2bb92ecc-e351-49a9-8616-8347e81f1ecf",
#                             azure_tenant_id="d9cfb9e9-79e6-4f78-a45e-d6d9cc78c40e",
#                             azure_client_secret="Eof8Q~uFyuAPhpaM-y53KTR~zrkkgue5QxojucbO",
#                             azure_account_url="https://anandllmops.blob.core.windows.net/",
#                             azure_container_name="rag",
#                             azure_blob_name="macbeth.pdf",
#                             debug_on=True
#                            )
