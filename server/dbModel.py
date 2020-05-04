# Begining on my Database model
import datetime
from sqlalchemy import  create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///theData.sqlite', echo = True)

Base = declarative_base()


##### Database models #####

class Chat_session (Base):
    __tablename__ = 'chat_sessions'

    id = Column(Integer, primary_key = True )
    client_name = Column(String)
    operator_name = Column(String)
    chat_hist = relationship("Chat_history")
    def __repr__(self):
        return "<User(id='%s', client_name='%s', operator_name='%s')>" % (
                            self.client_name, self.operator_name, self.id)

class Chat_history(Base):
    __tablename__ = 'chat_history'

    id = Column(Integer, primary_key = True )
    Chat_session_id = Column(Integer, ForeignKey(Chat_session.id))
    message = Column(String)
    time_stamp = Column(DateTime, default=datetime.datetime.utcnow)
    #chat_session = relationship("Chat_session", back_populates="chat_history")

### Setup of the Database
Base.metadata.create_all(engine)
