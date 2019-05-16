import pymysql
import pandas as pd
host='localhost'
usename='root'
password=''
databasename='test'
timeframes=['2015-5']
for timeframe in timeframes:
    conn = pymysql.connect(host, usename, password, databasename)
    execute = conn.cursor()
    limit=5000
    last_unix=0
    cur_length=limit
    counter=0
    test_done=False
    while cur_length==limit:
        df=pd.read_sql("select * from parent_reply where unix >{} and  parent not null and score >0 order by unix asc limit {} ".format(last_unix,limit),conn)
        last_unix=df.tail(1)['unix'].values[0]
        cur_length=len(df)
        if not test_done:
            with open("test.form","a",encoding='utf8')as f:
                for content in df['parent'].values:
                    f.write(content+'\n')
            with open("test.to", "a", encoding='utf8')as f:
                for content in df['parent'].values:
                    f.write(content + '\n')
            test_done=True
        else:
            with open("train.form","a",encoding='utf8')as f:
                for content in df['parent'].values:
                    f.write(content+'\n')
            with open("train.to", "a", encoding='utf8')as f:
                for content in df['parent'].values:
                    f.write(content + '\n')

        counter+=1
        if counter%20==0:
            print(counter*limit,'rows complete so far')