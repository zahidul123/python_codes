import pymysql
import json
from datetime import datetime
timeframe='2015-5'
sql_transaction=[]
host='localhost'
username='root'
password=''
dbname='test'

conn=pymysql.connect(host,username,password,dbname)
executesd=conn.cursor()

def tablecreate():
    sql="""create table if not exists test.parent_reply (parent_id varchar(150) primary key,comment_id varchar(150) unique,parent text,comment text,subreddit text,unix int,score int)"""
    executesd.execute(sql)


def format_data(data):
    data=data.replace("\n","newlinechar").replace("\r","newlinechar").replace('"',"'")
    return data

def find_parent(pid):
    try:
        squl="select comment from parent_reply where comment_id='{}' limit 1".format(pid)
        executesd.execute(squl)
        result=executesd.fetchone()

        if result!=None:
           return result[0]
        else: return False
    except Exception as e:
        print("find parent",e)
        return False


def find_existing_score(pid):
    try:
        squl="select score from parent_reply where parent_id='{}' limit 1".format(pid)
        executesd.execute(squl)
        result=executesd.fetchone()

        if result!=None:
           return result[0]
        else: return False
    except Exception as e:
        print("find parent",e)
        return False

def acceptable(data):
    if len(data.split(''))>50 or len(data)<1:
        return False
    elif len(data)>1000:
        return False
    elif data=="[deleted]" or data=="[removed]":
        return False
    else:
        return True


def sql_insert_replace_comment(comment_id,comment, parent_id, parent_data,subreddit, create_utc, score):
    try:
        squl="""update parent_reply set parent_id=?,comment_id=?,parent=?,comment=?,subreddit=?,unix=?,score=? where parent_id=?;""".format(parent_id,comment_id,parent_data,comment,subreddit,create_utc,score,parent_id)
        transaction_bldr(squl)
    except Exception as e:
        print("replace_comment ",str(e))

def sql_insert_has_parent(comment_id, parent_id, parent_data,comment,subreddit, create_utc, score):
    try:
        squl="""insert into parent_reply (parent_id,comment_id,parent,comment,subreddit,unix,score) values("{}","{}","{}","{}","{}","{}","{}");""".format(parent_id,comment_id,parent_data,comment,subreddit,create_utc,score)
        transaction_bldr(squl)
    except Exception as e:
        print("parent insertion ",str(e))


def transaction_bldr(squl):
    global sql_transaction
    sql_transaction.append(squl)
    if len(sql_transaction)>1000:
        executesd.execute('connection begening')
        for s in sql_transaction:
            try:
              executesd.execute(s)
            except:
                pass
        conn.comit()
        sql_transaction=[]


def sql_insert_no_parent(comment_id,comment, parent_id,subreddit, create_utc, score):
    try:
        squl="""insert into parent_reply (parent_id,comment_id,comment,subreddit,unix,score) values("{}","{}","{}","{}","{}","{}","{}");""".format(parent_id,comment_id,comment,subreddit,create_utc,score)
        transaction_bldr(squl)
    except Exception as e:
        print("no parent insertion ",str(e))


if __name__=="__main__":
    tablecreate()
    row_counter=0
    paired_row=0
    with open("J:/chatdata/ridditdata/{}/RC_{}".format(timeframe.split("-")[0],timeframe),buffering=1000) as f:
        for row in f:
            print(row)
            row_counter +=1
            row=json.loads(row)
            parent_id=row["parent_id"]
            comment_id=row['name']
            body=format_data(row['body'])
            create_utc=row['create_utc']
            score=row['score']
            subreddit=row['subreddit']
            parent_data=find_parent(parent_id)
            if  score>=2:
                if acceptable(body):
                   existing_comment_score=find_existing_score(parent_id)
                   if existing_comment_score:
                       if score>existing_comment_score:
                           sql_insert_replace_comment(comment_id,parent_id,parent_data,body,subreddit,create_utc,score)
                       else:
                           if parent_data:
                               sql_insert_has_parent(comment_id,parent_id,parent_data,body,subreddit,create_utc,score)
                               paired_row+=1
                           else:
                               sql_insert_no_parent(comment_id,parent_id,body,subreddit,create_utc,score)

            if row_counter %100000==0:
                print("total rows read:{},paired rows:{},time:{}",format(row_counter,paired_row,str(datetime.now())))







