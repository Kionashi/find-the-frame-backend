from abc import ABC, abstractmethod
class ImageSourceService(ABC):

    @abstractmethod
    def get_video(self, video_name: str):
        pass    

    @abstractmethod
    def get_frame(self, frame: int, video_name:str):
        pass

    @abstractmethod
    def get_all_videos(self):
        pass

    @abstractmethod
    def get_all_videos():
        pass