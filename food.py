
import os,random,time,requests,json
f=open(os.getcwd()+r"/food.txt","r",encoding="utf-8")
foodlist=f.readlines()
food=[]
for aa in foodlist:
    food.append(aa.strip())
output=("命运的选择是："+random.choice(food))
data = {
    "msgtype":"text",
    "text":{
        "content":output,
        "mentioned_list":"[@all]"
        }
    }
json_str = json.dumps(data,ensure_ascii=False).encode('utf-8')
headers = {'Content-Type': 'application/json'}
print(json_str)
print(output)
response = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4bb3356c-7dac-4406-981c-c4a01d916f10', headers=headers, data=json_str)
