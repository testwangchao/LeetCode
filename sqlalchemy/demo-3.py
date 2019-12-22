from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref

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
    content = Column(String(200))
    '''
    ORM层面的删除，会无视mysql级别的外键约束，直接会将对应的数据删除，
    然后将从表中外键设置为null，如果想要避免这种行为，应该将从表中的外键的"nullable"置为false
    '''
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)

    author = relationship("User", backref="articles")


# Base.metadata.drop_all()
# Base.metadata.create_all()

# user1 = User(name="wangchao")
# article1 = Article(content="学习Flask")
# article1.author = user1
# session.add(article1)
# session.commit()
user1 = session.query(User).filter(User.id == 1).first()
session.delete(user1)
session.commit()
