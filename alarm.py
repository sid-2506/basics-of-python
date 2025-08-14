import time
import datetime
import pygame

def setAlarm(alarm_time):
    print("Setting alarm for", alarm_time)
    sound_file = "song.mp3"
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if(current_time == alarm_time):
            print("Alarm ringing")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            for i in range(60):
                time.sleep(1)
                
            break
        time.sleep(1)
    

alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
setAlarm(alarm_time)

