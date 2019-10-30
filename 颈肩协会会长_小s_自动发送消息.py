#*encoding=utf-8
import schedule
import time
import requests

def job():
    base_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9bd2996b-b679-43bf-bbb5-a988214d08ac"
    body = {
        "msgtype": "text",
        "text": {"content": "嗨：抬头转颈，🔄左三圈，🔄右三圈....."}
    }
    r = requests.post(url=base_url, json=body)
    print(r.request.headers)
    print(r.json())
    print(r.status_code)

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



