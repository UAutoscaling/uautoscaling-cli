# -*- coding: utf-8 -*-
import hashlib, json, httplib
import urlparse
import urllib, copy
import sys
import requests

def _verfy_ac(private_key, params):
    items = params.items()
    items.sort()

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)

    params_data = params_data+private_key
    
    '''use sha1 to encode keys'''
    hash_new = hashlib.sha1()
    hash_new.update(params_data)
    hash_value = hash_new.hexdigest()
    return hash_value

def requestToAPI(publicKey, privateKey, projectId, params):
    toPost = copy.copy(params) 
    toPost['PublicKey'] = publicKey
    toPost['ProjectId'] = projectId
    signature = _verfy_ac(privateKey, toPost)
    toPost['Signature'] = signature
    print(toPost['Action'] + '... \n')
    r = requests.post('https://api.ucloud.cn', toPost, timeout=10)
    j = json.loads(r.text)
    if j['RetCode'] == 0:
        print(j['Action'] + ' SUCCESS \n')
    else:
        print(j['Action'] + ' ERROR \n')
        print(json.dumps(j, indent=4))
    return r.text
