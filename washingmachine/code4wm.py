#http://sh2.ipyy.com/smsJson.aspx 对应UTF-8(返回值为json格式) 

#http://sh2.ipyy.com/sms.aspx?action=send&userid=&account=账号&password=密码&mobile=15023239810,13527576163&content=内容&sendTime=&extno=

'''
成功的返回json
{"returnstatus":"Success",
"message":"操作成功",
"remainpoint":"-4",
"taskID":"1504080852350206",
"successCounts":"1"}
'''

import urllib.request
#userid为企业id不需要验证
mobile = '18550035274' #目标手机号
code = '8427'
content = urllib.parse.quote('您的验证码为'+ code +'，有效期3分钟，请速去填写。【宜叁集】') #中文需要先转码
url = 'http://sh2.ipyy.com/smsJson.aspx?action=send&userid=eoncci&account=jlf60&password=ab1256022&mobile='+ mobile +'&content='+ content +'&sendTime=&extno='
req = urllib.request.urlopen(url)
res = req.read()
print( res.decode())
