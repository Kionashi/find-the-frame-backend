class FindTheFrameService():
    def next_guess(self, frame: int, low:int, high:int, too_high:bool):
        """ Depending of if the proposed frame is too high or not it will return another option """
        frame = int(frame)
        low = int(low)
        high = int(high)
        too_high = bool(too_high)
        if(too_high == True):
            return {
                'frame': (low + (frame)) // 2,
                'low': low,
                'high': frame-1, 
            }
        else: # Too low
            return {
                'frame': ((frame) + high) // 2,
                'low': frame+1,
                'high': high
            }
    
    def start(self,total:int):
        """ Set the initial frame bringing the middle of the total of frames."""
        return {
            'frame': total // 2,
            'low': 0,
            'high': total, 
        }  
    
    def get_duration(self, numerator:int, denominator:int, frame:int):
        """ Calculates the time it took to reach a certain frame given the framerate and the current frame."""
        frame_rate = numerator / denominator
        frame_interval = 1 / frame_rate
        time_to_frame = int(frame) * frame_interval
        return self.format_duration(time_to_frame)

    def format_duration(self, seconds):
        """ Makes the duration more human readable."""
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s" # Cast the values as integers

