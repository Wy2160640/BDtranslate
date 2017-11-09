## BDtranslate

百度翻译

下载完成后，修改<div color='red'>def translate(srcString, appid='yourAppid', secretKey='yourKey', fromLang='en', toLang='zh'):</div>行

将<strong>yourAppid, yourKey</strong>修改成百度翻译申请的appid,[申请](http://api.fanyi.baidu.com/api/trans/product/apidoc)

## 用法

翻译文件

python translate.py -f file.txt

翻译句子

python translate.py -r "I love China."

