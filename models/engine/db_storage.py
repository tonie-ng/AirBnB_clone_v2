#!/usr/bin/python3
"""Database engine setup module"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Setup new database"""

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        host = os.getenv("HBNB_MYSQL_HOST")
        env = os.getenv("HBNB_ENV"))

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(user, pwd, host, db),
                pool_pre_ping=True
                )
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """this method must return a dictionary"""

        result = {}
        if cls:
           temp = self.__session.query(cls)
           for obj in temp:
               obj_key = "{}.{}".format(type(obj).__name__, obj.id)
               result[obj_key] = obj
        else:
            all_cls = [State, City, User, Place, Review, Amenity]
            for item in all_cls:
                temp = self.__session.query(item)
                for obj in temp:
                    obj_key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[obj_key] = obj
        return result

    def new(self, obj):
        """add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""

        if obj:
            self.session.delete(obj)

    def reload(self):
        """"""
        
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
