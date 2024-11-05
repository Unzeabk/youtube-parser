import os
from dotenv import load_dotenv
from services.youtube_service import YouTubeService
from services.db_service import DatabaseService

load_dotenv()

def main():
    api_key = os.getenv('API_KEY')
    db_url = os.getenv('DATABASE_URL')

    video_ids = ["JcOWSvul2X0", "miEFm1CyjfM"]

    db_service = DatabaseService(db_url)
    youtube_service = YouTubeService(api_key)

    for video_id in video_ids:
        video_info, channel_info, comments = youtube_service.get_video_data(video_id)
        
        db_service.add_channel_if_not_exists(channel_info)
        db_service.add_video(video_info)
        db_service.add_comments(video_id, comments)

    db_service.close()

if __name__ == "__main__":
    main()