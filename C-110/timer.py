import time
def countdown_timer(seconds):
    while seconds>0:
        mins = int(seconds/60)
        sec = int(seconds%60)
        timer = f'{mins}:{sec}'
        print(timer)
        seconds -=1
        time.sleep(1)
    print("timeup")

seconds = input("Enter The Time In Seconds ")
countdown_timer(int(seconds))