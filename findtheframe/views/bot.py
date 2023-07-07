from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from ..services.framex import FrameXService
from ..services.findtheframe import FindTheFrameService
from rest_framework import status

class BotView(viewsets.ViewSet):

    image_service = FrameXService() 
    find_the_frame_service = FindTheFrameService()

    @action(detail=False, methods=['GET'], url_path='video/(?P<video_name>[^/.]+)/start')
    def start(self,request, video_name):
        video = self.image_service.get_video(video_name) 
        response = self.find_the_frame_service.start(video['frames'])
        frame_url = self.image_service.get_frame(response['frame'],video_name) 
        response['frame_url'] = frame_url
        return Response(response, status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'], url_path='video/(?P<video_name>[^/.]+)/frame/(?P<frame>\d+)/low/(?P<low>\d+)/high/(?P<high>\d+)/input/(?P<input>\w+)')
    def get_new_frame(self, request,video_name, frame,low,high,input):
        """ Get a new frame for the given video depending of the input is high or low"""
        match input:
            case 'high':
                too_high = True
            case 'low':
                too_high = False
            case _:
                return Response('Invalid input',status.HTTP_400_BAD_REQUEST)
        response = self.find_the_frame_service.next_guess(frame,low,high,too_high)
        frame_url = self.image_service.get_frame(response['frame'],video_name) 
        response['frame_url'] = frame_url # Set the frame url in the response object
        return Response(response,status.HTTP_200_OK)


    @action(detail=False, methods=['GET'], url_path='videos')
    def list_videos(self, request):
        """ List all videos"""
        response = self.image_service.get_all_videos()
        return Response(response,status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='video/(?P<video_name>[^/.]+)/finish/(?P<frame>\d+)')
    def finish(self,request, video_name,frame):
        """ Given a frame and a video name, return the timestamp of the frame."""
        video = self.image_service.get_video(video_name)
        duration = self.find_the_frame_service.get_duration(numerator=video['frame_rate'][0], denominator=video['frame_rate'][1], frame=frame) 
        return Response(duration, status.HTTP_200_OK)