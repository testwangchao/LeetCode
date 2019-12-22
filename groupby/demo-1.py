from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
from datetime import datetime

'''
groupby、having
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
    age = Column(Integer, nullable=False)
    sex = Column(Enum("male", "female", "secret"), default="secret")


# Base.metadata.drop_all()
# Base.metadata.create_all()

# user1 = User(name="wangchao", age=18, sex="male")
# user2 = User(name="zhangsan", age=28, sex="female")
# user3 = User(name="Lisa", age=15, sex="male")
# user4 = User(name="Zhoujielun", age=30, sex="male")
# session.add_all([user1, user2, user3, user4])
# session.commit()

# male的人数
# result = session.query(User.sex, func.count(User.id)).group_by(User.sex).all()
# print(result)

# male中年龄大于18岁的人数
count = session.query(User.sex, func.count(User.id)).group_by(User.sex, User.age).having(User.age > 18).all()
print(count)