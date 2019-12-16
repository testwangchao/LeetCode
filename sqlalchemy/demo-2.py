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

article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id"), primary_key="article_id"),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key="tag_id")

)


class User(Base):
    __tablename__ = "user"
    # ORM类的属性和表中的字段映射
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=True)

    def __repr__(self):
        return "Person：name: %s" % (self.name)


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(200))
    # 与person表id关联
    uid = Column(Integer, ForeignKey("user.id"))
    # 给People表定义一个articles的属性，给Airticle表定义一个author的属性
    author = relationship("User", backref="articles")
    tags = relationship("Tag", backref="articles", secondary="article_tag")

    def __repr__(self):
        return "Article: tag: %s, uid: %s" % (self.content, self.uid)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)


# Base.metadata.drop_all()
# Base.metadata.create_all()
# user1 = User(name="wangchao")
# article1 = Article(content="Python")
# article2 = Article(content="Java")
# tag1 = Tag(name="编程语言")
# tag2 = Tag(name="解释型语言")
# article1.tags.extend([tag for tag in [tag1, tag2]])
# article2.tags.extend([tag for tag in [tag1, tag2]])
#
# user1.articles.extend([at for at in [article1, article2]])
#
# session.add(user1)
# session.commit()
users = session.query(User).filter(User.id == 1).first()
user_articles = users.articles
for article in user_articles:
    for tag in article.tags:
        print(tag.name)