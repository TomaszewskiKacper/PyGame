import pygame
class Animation:
    def __init__(self, frames, frame_duration, frame_count):
        self.frame_duration = frame_duration    #duration of a single frame in seconds
        self.frame_count = frame_count  #how many frames in animation
        self.current_frame_index = 0    #current frame
        self.time = 0.0 #time since last frame change
        self.frames = []
        
        sheet = pygame.image.load(frames)   #load image sheet
        frame_width = sheet.get_width() // frame_count  #get width of frame
        frame_height = sheet.get_height()   #get height of frame
        
        for i in range(frame_count):    #extract frames from sheet
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height) #rectangle of a frame
            self.frames.append(sheet.subsurface(frame_rect))    #append a section from image sheet
            
            
    def update(self, delta_time):
        self.time += delta_time #add time
        if self.time >= self.frame_duration:    #if the time since last frame is > frame duration
            self.time = 0   #reset clock
            self.current_frame_index = (self.current_frame_index + 1) % self.frame_count    #update index
            
        
    def get_frame(self):
        return self.frames[self.current_frame_index]    #return current frame of animation