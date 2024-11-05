from sqlalchemy.exc import IntegrityError
from models import Channel, Video, Comment
from database import Database

class DatabaseService:
    def __init__(self, db_url):
        self.db = Database(db_url)
        self.session = self.db.get_session()

    def add_channel(self, channel_info):
        channel = self.session.query(Channel).filter_by(channel_id=channel_info["channel_id"]).first()
        if not channel:
            channel = Channel(**channel_info)
            self.session.add(channel)
            self.session.commit()
        else:
            for key, value in channel_info.items():
                setattr(channel, key, value)
            self.session.commit()

    def add_video(self, video_info):
        video = self.session.query(Video).filter_by(video_id=video_info["video_id"]).first()
        if not video:
            video = Video(**video_info)
            self.session.add(video)
            self.session.commit()
        else:
            for key, value in video_info.items():
                setattr(video, key, value)
            self.session.commit()

    def add_comments(self, video_id, comments):
        for comment_info in comments:
            comment = self.session.query(Comment).filter_by(comment_id=comment_info["comment_id"]).first()
            if not comment:
                comment = Comment(**comment_info)
                self.session.add(comment)
            else:
                for key, value in comment_info.items():
                    setattr(comment, key, value)
        self.session.commit()

    def close(self):
        self.session.close()