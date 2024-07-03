import os
import datetime
import pymongo
from json import loads, dumps
from .ld_connector import S3Connector, LocalConnector
#from ld_connector import S3Connector

test_writer = {
    "prefix": "/flow_data/writer",
    "params": {
        "host": "http://10.86.14.206:80",
        "accesskey": "admin123",
        "secretkey": "admin123",
        "bucketname": "datasets",
        "region": ""
    },
    "type": "s3"
}

def context_get_db():
    """
        获取当前上下文数据库(pymongo database)
    """
    mongouri = os.getenv("DEFAULT_MONGO_URI", "mongodb://root:example@10.86.14.34:30301")
    database = os.getenv("DEFAULT_MONGO_DATABASE", "flow")
    client = pymongo.MongoClient(mongouri)
    return client[database]


def context_get_jsonapi():
    """
        获取当前上下文jsonapi url
    """
    return os.getenv("DEFAULT_JSONAPI_URL", "http://10.86.24.63:10000/api/ca_dms/models/")


def get_connector(config):
    """
        通过配置获取连接器
    """
    if config['type'] in ["s3", "S3"]:
        return S3Connector(config["prefix"], "s3", config["params"])

    if config['type'] in ["本地"]:
        return LocalConnector(config["prefix"], "local", config["params"])


def context_get_writer():
    """
        获取当前上下文默认写连接器
    """
    writercfg = loads(os.getenv("DEFAULT_WRITER", dumps(test_writer)))

    writer = get_connector(writercfg)
    writer.id = os.getenv("DEFAULT_WRITER_ID", "IDD")

    return writer


def get_context():
    context = {
        'run_id': os.getenv("CTX_DAG_RUN_ID", datetime.datetime.now().isoformat()[:-7]),
        'task_id': os.getenv("CTX_TASK_ID", "task_id"),
        'project': os.getenv("CTX_PROJECT", "project_id"),
        'flow': os.getenv("CTX_FLOW", "flow_id"),
        'inputs': loads(os.getenv("CTX_INPUTS", dumps({'data': 'id'})))
    }

    return context

def test():
    writer = context_get_writer()
    print(writer.id)
    #with writer.open("test/haha", "w") as fp:
    #    fp.write(b"12345")
        
        
    
if __name__ == "__main__":
    test()
