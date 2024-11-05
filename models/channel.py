from sqlalchemy import Column, String, Integer, DateTime
from database import Base

class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)
    channel_id = Column(String, unique=True)
    username = Column(String)
    title = Column(String)
    description = Column(String)
    subscriber_count = Column(Integer)
    view_count = Column(Integer)
    date_joined = Column(DateTime)

    def __repr__(self):
        return f"<Channel(id={self.id}, title={self.title}, subscribers={self.subscriber_count})>"