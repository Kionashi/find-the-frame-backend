
from typing import Final
from ..serializers.framexvideo import FrameXVideoSerializer
import requests
from rest_framework import status
from .base import ImageSourceService

class FrameXService(ImageSourceService):
    BASE_URL: Final = 'https://framex-dev.wadrid.net/api/video/'

    def test(self):
        return 'Testing'
    
    def get_video(self, video_name: str):
        """ Get video object."""
        new_url: str = f'{self.BASE_URL}{video_name}/' 
        try:
            response: requests.Response = requests.get(new_url)
            serializer = FrameXVideoSerializer(data=response.json(), many=False)
            if (serializer.is_valid()):
                return serializer.data
        except:
            print('error searching the video')
        return None

    def get_frame(self, frame: int, video_name:str= None) ->str:
        """ Returns the url of the frame """
        if not video_name: # If the video_name is not sent we use the first video in the list by default
            videos: list[FrameXVideoSerializer] = self.get_all_videos()
            video_name = videos[0]['name']
        frame_url: str = f'{self.BASE_URL}{video_name}/frame/{frame}/' 
        print(f'frame_url => {frame_url}')
        return frame_url
       
    
    # Get all videos
    def get_all_videos(self) -> list[FrameXVideoSerializer]:
        """ Returns a list with all the videos """
        try: 
            response: requests.Response = requests.get(self.BASE_URL)
            # Check the response status code 
            if response.status_code == status.HTTP_200_OK:
                serializer = FrameXVideoSerializer(data=response.json(), many=True)
                if (serializer.is_valid()):
                    return serializer.data
                else:
                    print(f'Response not valid D: ==>{serializer.errors}') 
            else:
                print(f'Request failed with status code => {response.status_code}')
        except Exception as error:
            print(f'Request failed ==>{error}')
        
        return []

