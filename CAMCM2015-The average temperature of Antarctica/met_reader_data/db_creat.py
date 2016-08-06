# -*- coding:utf-8 -*-

if __name__ == '__main__':
    from models import Base, engine

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
