from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
from datetime import datetime

'''
ORM删除
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

    __mapper_args__ = {
        "order_by": creat_time
    }
    # 未设置order_by参数，默认使用__mapper_args__
    author = relationship("User", backref=backref("articles", order_by=creat_time.desc))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Article(title:%s,creatime:%s)>" % (self.content, self.creat_time)

Base.metadata.drop_all()
Base.metadata.create_all()

article1 = Article(content="Python")
article2 = Article(content="Java")
user = User(name="wangchao")
user.articles=[article1, article2]
session.add(user)
session.commit()

# 正序排序（未设置__mapper_args__）
# article1 = session.query(Article).order_by(Article.creat_time).all()
# print(article1)

# 倒序排序（未设置__mapper_args__）
# article1 = session.query(Article).order_by(Article.creat_time.desc()).all()
# print(article1)

# 设置__mapper_args__
# article1 = session.query(Article).all()
# print(article1)