from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
from datetime import datetime

'''
懒加载
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


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=True)


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(200), nullable=False)
    creat_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref=backref("articles", lazy="dynamic"))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Article(title:%s,creatime:%s)>" % (self.content, self.creat_time)

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(content="Python")
# article2 = Article(content="Java")
# user = User(name="wangchao")
# for i in range(1,100):
#     article = Article(content="Python-article-%s" % i)
#     user.articles.append(article)
# session.add(user)
# session.commit()

user = session.query(User).first()
# type(articles) >> AppenderQuery
# articles1 = user.articles.filter(Article.id > 50).all()
# for data in articles1:
#     print(data)

article3 = Article(content="Php")
user.articles.append(article3)
session.add(user)
session.commit()