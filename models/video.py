from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True)
    video_id = Column(String, unique=True)
    title = Column(String)
    description = Column(String)
    view_count = Column(Integer)
    like_count = Column(Integer)
    comment_count = Column(Integer)
    uploaded_at = Column(DateTime)
    channel_id = Column(String, ForeignKey('channels.channel_id'))

    channel = relationship("Channel")

    def __repr__(self):
        return f"<Video(id={self.id}, title={self.title}, views={self.view_count})>"