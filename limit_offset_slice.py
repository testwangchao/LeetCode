from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.query import Query
from datetime import datetime


'''
limit、offset、切片
1. limit：可以限制每次查询的时候只查询几条数据。
2. offset：可以限制查找数据的时候过滤掉前面多少条。
3. 切片：可以对Query对象使用切片操作，来获取想要的数据。可以使用`slice(start,stop)`方法来做切片操作。也可以使用`[start:stop]`的方式来进行切片操作。一般在实际开发中，中括号的形式是用得比较多的。
'''
HOSTNAME = "127.0.0.1"
PORT = 3306
DB = "flask_db"
USER = "root"
PASSWD = "123456"

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USER, password=PASSWD,
                                                                                       host=HOSTNAME, port=PORT, db=DB)
engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(200))
    creat_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Article(title:%s,creatime:%s)>" % (self.content, self.creat_time)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# for i in range(1,101):
#     content = "test %s" % i
#     article = Article(content=content)
#     session.add(article)
#     session.commit()
#     time.sleep(0.5)

# limit
# aricels = session.query(Article).limit(10).all()
# for article in aricels:
#     print(article)

# offset 从第十条数据开始
# aricels = session.query(Article).offset(10).all()
# print(aricels)

# 显示最新加入的文章slice、切片
# recent_articles = session.query(Article).order_by(Article.creat_time.desc()).slice(1,10)
recent_articles = session.query(Article).order_by(Article.creat_time.desc())[0:10]
for article in recent_articles:
    print(article)
