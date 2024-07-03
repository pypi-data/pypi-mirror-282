# 使用LdConnector定义数据集读写的抽象，指向一个数据目录
#   
# 提供抽象处理数据集目录和文件
#   connector = LDConnector(...)
#   connector.list(directory) 列出所有文件
#   connector.open(filename, mode) 打开文件
#   connector.upload(srcpath, destpath) 上传文件

import os
import shutil  
import boto3
from botocore.exceptions import ClientError
from smart_open import open as s3open
from pathlib import Path



class LdConnector(object):
    def __init__(self, prefix, type, params):
        self.id = None
        self.prefix = prefix
        self.info = {
            'type': type,
            'params': params
        }

    
    def list(self, directory = ''):
        """
            列出目录下所有对象
                directory 目录名，不传则列出顶层

            返回一个列表
                
                return [""]
        """
        raise NotImplementedError


    def open(self, filename, mode = "r", **kwargs):
        """
            打开一个文件，返回一个stream用于读写
                filename 文件名
                mode "r/w" 读或写
            返回
                类似open(filname, mode)的返回结果
        """
        raise NotImplementedError


    def upload(self, srcpath, destpath):
        """
            上传文件
                srcpath  本地文件
                destpath 远端文件
        """
        raise NotImplementedError


class S3Connector(LdConnector):
    def __init__(self, prefix, type, params):
        super().__init__(prefix, type, params)
        self.prefix = self.prefix.lstrip('/')
        self.bucketname = self.info['params']['bucketname']
        self.url = f"s3://{self.bucketname}/{self.prefix}"
        self.client = self.create_client()            
        

    def create_client(self):
        url = self.info['params']['host']
        access_key = self.info['params']['accesskey']
        access_secret = self.info['params']['secretkey']

        return boto3.client(service_name='s3', endpoint_url=url, aws_access_key_id=access_key, aws_secret_access_key=access_secret)


    def list(self, directory = ''):
        prefix = str(Path(self.prefix)/Path(directory))
        paginator = self.client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=self.bucketname, Prefix=prefix)

        all_objects = []
        prefix_len = len(self.prefix)
        for page in pages:
            all_objects.extend([x['Key'][prefix_len:].lstrip('/') for x in page['Contents']])

        return all_objects


    def open(self, filename, mode, **kwargs):
        if mode in ["r", "w"]:
            mode += "b"
        elif mode not in ["rb", "wb"]:
            raise TypeError("can't support mode type {mode}")

        if filename.startswith(self.prefix):
            filename = filename[len(self.prefix):]

        filename = filename.lstrip("/")
        url = f"{self.url}/{filename}"
        fp = s3open(url, mode, transport_params={'client': self.client})
        fp.mode = mode

        return fp


    def upload(self, srcpath, destpath):
        try:
            destpath = destpath.lstrip("/")
            object_name = str(Path(self.prefix)/Path(destpath))
            response = self.client.upload_file(srcpath, self.bucketname, object_name)
        except ClientError as e:
            print(e)
            return False

        return True


    def download(self, srcpath, destpath):
        try:
            object_name = str(Path(self.prefix)/Path(srcpath))
            with open(destpath, "wb") as fp:
                response = self.client.download_fileobj(self.bucketname, object_name, fp) 
           
        except ClientError as e:
            print(e)
            return False

        return True

       
class LocalConnector(LdConnector):
    def __init__(self, prefix, type, params):
        super().__init__(prefix, type, params)
        self.prefix = self.prefix.lstrip('/')
        self.path = str(Path(params["path"])/Path(self.prefix))
        

    def list(self, directory = ''):
        all_files = []
        target = str(Path(self.path)/Path(directory))
        prefix_len = len(self.path)
        for root, dirs, files in os.walk(target):  
            for file in files:  
                apath = os.path.join(root, file)
                all_files.append(apath[prefix_len:].lstrip('/'))

        return all_files


    def open(self, filename, mode, **kwargs):
        if filename.startswith(self.prefix):
            filename = filename[len(self.prefix):]

        filename = filename.lstrip("/")
        filepath = str(Path(self.path)/Path(filename))

        if mode in ["w", "wb"]:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

        return open(filepath, mode, **kwargs)


    def upload(self, srcpath, destpath):
        if destpath.startswith(self.prefix):
            destpath = destpath[len(self.prefix):]

        destpath = destpath.lstrip("/")
        filepath = str(Path(self.path)/Path(destpath))

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
     
        shutil.copyfile(srcpath, filepath)


    def download(self, srcpath, destpath):
        if srcpath.startswith(self.prefix):
            srcpath = srcpath[len(self.prefix):]

        srcpath = srcpath.lstrip("/")
        filepath = str(Path(self.path)/Path(srcpath))

        os.makedirs(os.path.dirname(destpath), exist_ok=True)
     
        shutil.copyfile(filepath, destpath)


def s3test():
    prefix = '/flow_data/scene_mining_data'
    params =  {
        "host": "http://10.86.14.206:80",
        "accesskey": "admin123",
        "secretkey": "admin123",
        "bucketname": "datasets",
        "region": ""
    }

    from datetime import datetime 
    import json
    s = datetime.now()
    connector = S3Connector(prefix, 's3', params)

#    connector.upload("upload.file", "this/is/a/upload.file")
    
#    import rosbag
#    with connector.open("ALT_OD_MERGE_OPP/ALT_OD_MERGE_OD_MERGE_OPP.bag", "r") as fp:
#        bag = rosbag.Bag(fp)
#        for topic, msg, t in bag.read_messages(raw=True):
#            print(msg)

    connector.download("ALT_OD_MERGE_OPP/ALT_OD_MERGE_OD_MERGE_OPP.bag", "/tmp/test/1.bag")
    return 

    with connector.open("__meta__.json", "r") as fp:
        metadata = json.load(fp)

    objects = connector.list(metadata['od'])
    for x in objects:
        print(x)

    import pandas as pd
    with connector.open(objects[2], "r") as fp:
        dataframe = pd.read_csv(fp)
    print(dataframe)        

    with connector.open("test.json", "w") as fp:
        fp.write(b"hello")
        
    #with connector.open("test.json", "a") as fp:
    #    fp.write(b"again")



def localtest():
    params = {"path": "/mnt/k8s"}
    prefix = "/pcd"

    connector = LocalConnector(prefix, 'local', params)
    result = connector.list()
    with connector.open(result[0], "rb") as fp:
        print(fp.read(1024))
        
    with connector.open("hello/test", "w") as fp:
        fp.write("hello")

    connector.upload("./__init__.py", "hello/upload") 
    connector.download("hello/upload", "/tmp/hh") 
    

def test():
    s3test()
#    localtest()


if __name__ == "__main__":
    test()
