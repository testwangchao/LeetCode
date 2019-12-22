from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref


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
    # 与person表id关联
    uid = Column(Integer, ForeignKey("user.id"))
    #
    author = relationship("User", backref=backref(name="articles", cascade="save-update,delete"), cascade="save-update,delete")


# Base.metadata.drop_all()
# Base.metadata.create_all()
# user = User(name="wangchao")
# article1 = Article(content="Python")
# article1.author = user
# session.add(article1)
# session.commit()
user1 = session.query(User).filter(User.id == 1).first()
session.delete(user1)
session.commit()
