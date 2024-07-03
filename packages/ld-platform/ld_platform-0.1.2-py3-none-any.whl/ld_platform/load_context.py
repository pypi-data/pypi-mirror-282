# 根据当前环境设定 context, 目前运行环境为airflow

import os, json
from airflow.operators.python import get_current_context

def load_json_api(params):
    """
    "global":{
        "models_url":"http://dms-jsonapi:8000/api/ca_dms/models/"
    """
    os.environ["DEFAULT_JSONAPI_URL"] = params['global']['models_url']


def load_db(params):
    """
    "global":{
        "mongo_uri":"ld-mongo:27017/LiangdaoDMS"
    }
    """
    uri = params['global']['mongo_uri']
    uri, database = uri.rsplit('/', 1)
    os.environ["DEFAULT_MONGO_URI"] = f"mongodb://{uri}"
    os.environ["DEFAULT_MONGO_DATABASE"] = database


def load_writer(params):
    """
    "global":{
        "connector_params":{
            "params":{
                "accesskey":"changan-test"
                "bucketname":"changan-test"
                "host":"http://10.86.14.206:80"
                "region":""
                "secretkey":"changan-test"
            }
            "type":"s3"
        }
        "tempdata_path_prefix":"/auto/mining"
    }
    """
    
    params = get_current_context()['params']
    connector_params = params['global']['connector_params']
    writer = connector_params
    writer['prefix'] = params['global']['tempdata_path_prefix']
    os.environ["DEFAULT_WRITER"] = json.dumps(writer) 
    os.environ["DEFAULT_WRITER_ID"] = params['global']['tempdata_connector']
        

def load_context():
    params = get_current_context()['params']

    load_json_api(params)
    load_db(params)
    load_writer(params)

    os.environ["CTX_DAG_RUN_ID"] = os.getenv("AIRFLOW_CTX_DAG_RUN_ID")
    os.environ["CTX_TASK_ID"] = os.getenv("AIRFLOW_CTX_TASK_ID")
    
    os.environ["CTX_PROJECT"] = params['global']['project']
    os.environ["CTX_FLOW"] = params['global']['flow']
    os.environ["CTX_INPUTS"] = json.dumps(params['inputs'])
