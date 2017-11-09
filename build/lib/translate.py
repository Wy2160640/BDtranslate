# -*- coding: utf-8 -*-

# 百度翻译 API 文档：http://api.fanyi.baidu.com/api/trans/product/apidoc


import argparse
import os
import httplib 
import md5
import urllib
import json
import random

def get_opt():
	parser = argparse.ArgumentParser(
				prog = 'bdtranslate', 
				description = 'bdtranslate: 百度翻译API', 
				usage = '%(prog)s.py [options] -s Hello word.'
			)
	parser.add_argument('-f', '--fromfile', nargs='?', type=str, help="需要翻译的文件", required=False)
	parser.add_argument('-s', '--srcString', nargs='?', type=str, help="需要翻译的句子", required=False)

	args = parser.parse_args()
	return args


def translate_file(fromfile, toLang='zh'):
	file_suffix = os.path.splitext(fromfile)[1]
	file_dir = os.path.dirname(os.path.abspath(fromfile))

	tofile = fromfile.replace(file_suffix, '_' + toLang + file_suffix)

	with open(fromfile, 'r') as inputfile, open(os.path.join(file_dir, tofile), 'w') as outfile:
		buffer = inputfile.readlines()
		[outfile.write(translate(line).encode('utf8')) for line in buffer]



def translate(srcString, appid='20170221000039563', secretKey='nIyk6j2N4pOIc3PpE9tY', fromLang='en', toLang='zh'):

    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = srcString.decode('utf8')
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
    trRet = ''
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        ret =  response.read()
        jobj = json.loads(ret)
        trRet = jobj['trans_result'][0]['dst']
        
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    print trRet
    return trRet


	
if __name__ == '__main__':
	args = get_opt()
	if args.fromfile:
		translate_file(args.fromfile)
	if args.srcString:
		translate(args.srcString)