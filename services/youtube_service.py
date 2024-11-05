import requests

class YouTubeService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def get_video_data(self, video_id):
        video_info = self.get_video_info(video_id)
        channel_info = self.get_channel_info(video_info['channel_id'])
        comments = self.get_comments(video_id)
        return video_info, channel_info, comments

    def get_video_info(self, video_id):
        url = f"{self.base_url}/videos?part=snippet,statistics&id={video_id}&key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['items'][0]

        return {
            "video_id": video_id,
            "title": data['snippet']['title'],
            "description": data['snippet']['description'],
            "view_count": data['statistics'].get('viewCount'),
            "like_count": data['statistics'].get('likeCount'),
            "comment_count": data['statistics'].get('commentCount'),
            "uploaded_at": data['snippet']['publishedAt'],
            "channel_id": data['snippet']['channelId']
        }

    def get_channel_info(self, channel_id):
        url = f"{self.base_url}/channels?part=snippet,statistics&id={channel_id}&key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['items'][0]

        return {
            "channel_id": channel_id,
            "username": data['snippet']['customUrl'],
            "title": data['snippet']['title'],
            "description": data['snippet']['description'],
            "subscriber_count": data['statistics'].get('subscriberCount'),
            "view_count": data['statistics'].get('viewCount'),
            "date_joined": data['snippet']['publishedAt']
        }

    def get_comments(self, video_id, max_results=100):
        url = f"{self.base_url}/commentThreads?part=snippet&videoId={video_id}&maxResults={max_results}&key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        comments_data = response.json()['items']

        comments = []
        for item in comments_data:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                "comment_id": item['id'],
                "video_id": video_id,
                "username": comment['authorDisplayName'],
                "text": comment['textDisplay'],
                "like_count": comment.get('likeCount', 0),
                "uploaded_at": comment['publishedAt'],
                "channel_id": comment.get('authorChannelId', {}).get('value')
            })
        return comments