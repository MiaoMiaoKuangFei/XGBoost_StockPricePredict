# Date,Open,High,Low,Close,Adj Close,Volume
import pandas as pd
from jqdatasdk import *
if __name__ == '__main__':
    security = ['600460.XSHG']
    print("请输入用户名")
    usn = input()
    print("请输入密码")
    psw = input()
    auth(usn, psw)
    spd:pd.DataFrame = get_price(security=security,
                    start_date="2010-01-01 00:00:00",
                    end_date="2021-08-04 23:59:59",
                    frequency='daily',
                    fields=['open', 'close', 'high', 'low', 'volume'],  # 以每个时段的开始价格作为当前时段的价格
                    skip_paused=True,
                    fq='pre',
                    count=None).drop(['code'], axis=1)
    spd.to_csv("slv.csv",index=False)
    print("写入成功")