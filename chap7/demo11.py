# 姓名：fmm
# 开发时间：2022/4/20 11:32
import schedule
import time

def job():
    print('哈哈')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)