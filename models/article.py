from . import *


# 定义User对象:
class Article(Base, ModelMixin):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author_id = Column(Integer)
    ct = Column(Integer)
    content = Column(Text)