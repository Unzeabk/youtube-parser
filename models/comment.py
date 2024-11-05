from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from database import Base

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comment_id = Column(String, unique=True)
    video_id = Column(String, ForeignKey('videos.video_id'))
    username = Column(String)
    text = Column(String)
    like_count = Column(Integer)
    uploaded_at = Column(DateTime)
    channel_id = Column(String, ForeignKey('channels.channel_id'))

    def __repr__(self):
        return f"<Comment(id={self.id}, text={self.text}, likes={self.like_count})>"