import time
import math

# least trouble getting the audio to work
import pygame

alert_sound = "alert.mp3"

def timer(seconds):
    pygame.mixer.init()
    print(f"Timer started for {seconds} seconds.")
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < seconds:
        elapsed_time = time.time() - start_time

        if math.floor(elapsed_time) % 5 == 0:
            print(f"Elapsed Time: {math.floor(elapsed_time)}")

        time.sleep(1)

    print("Times up!")

    pygame.mixer.music.load(alert_sound)
    pygame.mixer.music.play()
    
    time.sleep(5)

if __name__ == "__main__":
    timer(3)
