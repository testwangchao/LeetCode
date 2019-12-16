from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
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

# 判断是否连接成功
# conn = engine.connect()

Base = declarative_base(engine)


# 创建ORM模型，必须继承自sqlclchemy给我们提供好的基类
class Person(Base):
    __tablename__ = "person"
    # ORM类的属性和表中的字段映射
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=True)
    age = Column(Integer)

    def __repr__(self):
        return "Person：name: %s, age: %s" % (self.name, self.age)


class PersonExtend(Base):
    __tablename__ = "person_extend"
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50), nullable=True)
    uid = Column(Integer, ForeignKey("person.id"))
    # uselist置为false
    person = relationship("Person", backref=backref(name="extend", uselist=False))

# 将创建好的ORM模型映射到数据库中
# Base.metadata.create_all()
session = sessionmaker(engine)()

'''添加数据'''
# 创建对象，也是创建一条数据
# person1 = Person(name="wangchao", age=27)
# 将对象添加到session会话中
# session.add(person1)

# 一次性添加多条数据
# person2 = Person(name="Tom", age=18)
# person3 = Person(name="Ami", age=25)

# session.add_all([person2, person3])
# 提交
# session.commit()
'''查改对象'''
# 查找某个模型对应的那个表中所有的数据:
# all_person = session.query(Person).all()
# for p in all_person:
#     print(p)

# 指定筛选
# filter_person = session.query(Person).filter_by(name="wangchao")
# for p in filter_person:
#     print(p)


class Airticle(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(200))
    # 与person表id关联
    uid = Column(Integer, ForeignKey("person.id"))
    # 给People表定义一个articles的属性，给Airticle表定义一个author的属性
    author = relationship("Person", backref="articles")

    def __repr__(self):
        return "Airticle: tag: %s, uid: %s" % (self.content, self.uid)


# Base.metadata.drop_all()
# Base.metadata.create_all()


# article = session.query(Person).filter(Airticle.uid == Person.id).all()
# for data in article:
#     print(data.articles)

# 通过Airticle的articles属性查出people关联的Airticl的数据
# a1 = session.query(Airticle).filter(Airticle.id == 5).first()
# print(a1.author)
# 通过Person的articles属性查出people关联的Airticl的数据
# p1 = session.query(Person).filter(Person.id ==3).first()
# print(p1.articles)
p1 = Person(name="wangchao")
a1 = Airticle(content="Python")
a2 = Airticle(content="Java")
a3 = Airticle(content="PHP")
a = lambda x: x.extend([a1, a2, a3])
a(p1.articles)
session.add(p1)
session.commit()