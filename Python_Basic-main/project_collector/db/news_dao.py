#DAO: datavase Access object
#데이터 작업을 하는 객체

#뉴스 (제목,본문,날짜 url)저장

from db.common.connection import conn_mongodb
def add_news(data):
    pass
    conn=conn_mongodb()
    conn.insert_one(data)