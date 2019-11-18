#*encoding=utf-8
import schedule
import time
from datetime import  datetime
import requests

def job():
    base_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9bd2996b-b679-43bf-bbb5-a988214d08ac"
    body = {
        "msgtype": "text",
        "text": {"content": "(｡･∀･)ﾉﾞ~：抬头转颈，🔄左三圈，🔄右三圈....."}
    }
    r = requests.post(url=base_url, json=body)
    # print(r.request.headers)
    # print(r.json())
    if r.status_code==200:
        print(time.strftime('%Y-%m-%d %H:%M:%S') , "发送成功")
        print(int(time.time()))
    # print(r.status_code)

#schedule.every().day.at(9:05).do(job)
#schedule.every(1).minute.do(job)
#schedule.every(3).seconds.do(job)

if __name__ == "__main__":
    schedule.every().day.at("15:00").do(job)
    schedule.every().day.at("17:00").do(job)
    schedule.every().day.at("20:00").do(job)
    schedule.every().day.at("22:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)




