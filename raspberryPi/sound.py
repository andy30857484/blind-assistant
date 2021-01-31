#///////////////////////////////////import library/////////////////////////////////

import pygame
#///////////////////////////////////subroutine/////////////////////////////////

def sound(file,playing):
    playingg=playing
    if file != "/home/pi/sound/503none.mp3" and playingg==0:
        termination=0
        pygame.mixer.init(frequency=27050)
        pygame.mixer.music.load(file)
        v=pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play()
        pygame.time.delay(100)
        pygame.mixer.music.set_volume(v)
        pygame.time.delay(1000*5)
        pygame.mixer.init()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("sound off")
        end=0
        return end
    
    
    
    
    