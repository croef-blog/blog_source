import os
import argparse
import time
import hashlib
import json
import datetime
from qiniu import Auth, put_file, etag

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
CONIFG_NAME = os.path.join(SRC_DIR, 'qn_conf.json')


def get_upload_file_name(path):
    file_name = os.path.basename(path)
    name, ext = os.path.splitext(file_name)
    hash_name = hashlib.md5(str(time.time()).encode('utf-8') + path.encode('utf-8')).hexdigest()
    path_name = hash_name + ext
    return datetime.datetime.now().strftime("%Y/%m/%d") + '/' + path_name


def upload(header, path, conf):
    if not os.path.exists(path):
        print('upload error, path not exist' + path)
        return False
    key = header + '/' + get_upload_file_name(path)
    print("key: " + key)
    auth = Auth(conf['access_key'], conf['secret_key'])
    token = auth.upload_token(conf['bucket_name'], key, 3600)
    ret, info = put_file(token, key, path)
    assert ret['key'] == key
    assert ret['hash'] == etag(path)
    print("url: " + conf['host'] + '/' + key)


def prepare_key(access_key='', secret_key='', bucket_name='', host=''):
    conf = {}
    if os.path.exists(CONIFG_NAME):
        with open(CONIFG_NAME, mode='r', encoding='utf-8') as f:
            conf = json.load(f)
    if access_key and len(access_key) > 0:
        conf['access_key'] = access_key
    if secret_key and len(secret_key) > 0:
        conf['secret_key'] = secret_key
    if bucket_name and len(bucket_name) > 0:
        conf['bucket_name'] = bucket_name
    if host and len(host) > 0:
        conf['host'] = host
    with open(CONIFG_NAME, mode='w', encoding='utf-8') as f:
        json.dump(conf, f)
    return conf


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--header', action='store', required=True, dest='header', help='key header for nos')
    parser.add_argument('--path', action='store', required=True, dest='path', help='file path')
    parser.add_argument('--ak', action='store', required=False, dest='access_key', help='access key')
    parser.add_argument('--sk', action='store', required=False, dest='secret_key', help='secret key')
    parser.add_argument('--bk', action='store', required=False, dest='bucket_name', help='bucket key')
    parser.add_argument('--host', action='store', required=False, dest='host', help='host')
    args = parser.parse_args()
    upload(args.header, args.path, prepare_key(args.access_key, args.secret_key, args.bucket_name, args.host))
