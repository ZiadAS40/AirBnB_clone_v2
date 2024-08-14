#!/usr/bin/python3
"""
difining new engine
"""


class DBStorage:
    """
    defining new class for the storage
    in the DB ("data base").
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialize the DBstorage class"""
        from sqlalchemy import create_engine
        from os import getenv
        from models.base_model import Base

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user,
                                             password,
                                             host,
                                             database), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on the current database sesion"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        """
        add an object to the current database sesion
        """
        self.__session.add(obj)
    
    def save(self):
        """
        commit all the changes
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """
        delete from the current database sesion
        """
        if obj != None:
            self.__session.delete(obj)
    
    def reload(self):
        """
        -> create all tables on the database.
        -> create the sesion.
        """
        from sqlalchemy.orm import scoped_session, sessionmaker
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def close(self):
        """call remove for the private session"""
        self.__session.remove()