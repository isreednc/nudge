import time
import math
import sys
import threading
import asyncio

# least trouble getting the audio to work
import pygame

pygame.mixer.init()
alert_sound = "alert.mp3"
running_event = threading.Event()

async def main():
    time.sleep(1)
    print("---------------------------------\n")

    seconds = 0
    label = ''
    repeats = 5
    if len(sys.argv) < 2:
        print("Usage: python nudge.py <seconds> <label> <repeats>")
        pygame.quit()
        sys.exit(1)

    try:
        seconds = int(sys.argv[1])
    except:
        print("Invalid argument. <seconds> must be an int.\nUsage: python nudge.py <seconds> <label> <repeats>") 
        pygame.quit()
        sys.exit(1)

    if len(sys.argv) == 2:
        await start_threads(seconds, label, repeats)
        sys.exit(2)

    label = sys.argv[2]

    if len(sys.argv) == 3:
        await start_threads(seconds, label, repeats)

    try:
        repeats = int(sys.argv[3])
    except:
        print("Invalid argument. <repeats> must be an int.\nUsage: python nudge.py <seconds> <label> <repeats>") 
        pygame.quit()
        sys.exit(1)

    if len(sys.argv) == 4:
        await start_threads(seconds, label, repeats)
        
    print("Too many arguments.\nUsage: python nudge.py <seconds> <label> <repeats>")


def handle_input():
    try:
        while True:
            user_input = input()
            if user_input.lower() == "quit":
                print("Quitting the program...")
                pygame.quit()
                sys.exit(1)
    except KeyboardInterrupt:
        print("Turning off any timer and exiting...")       
    finally:
        running_event.set()
    running_event.set()


def timer(seconds, label, repeats):
    if repeats + 1 <= 0:
        print("No repeats, exiting program")
        running_event.set()
        time.sleep(5)

    if label == '':
        print(f"Timer started for {seconds} seconds.")
    else:
        print(f"Timer: {label}\n{seconds} seconds\n{repeats} repeats left")
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < seconds:
        elapsed_time = time.time() - start_time

        if math.floor(elapsed_time) % 5 == 0:
            print(f"Elapsed Time: {math.floor(elapsed_time)}")

        time.sleep(1)

    print("\nTimes up!")

    pygame.mixer.music.load(alert_sound)
    pygame.mixer.music.play()
    
    time.sleep(5)

    repeats -= 1
    if repeats >= 0:
        print(f"Resetting timer. {repeats} repeats left\n")
    timer(seconds, label, repeats)

async def start_threads(seconds, label, repeats):
    timer_thread = threading.Thread(target=timer, args=(seconds, label, repeats), daemon=True)
    input_thread = threading.Thread(target=handle_input, daemon=True)

    timer_thread.start()
    input_thread.start()

    while not running_event.is_set():
        time.sleep(1)

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())
