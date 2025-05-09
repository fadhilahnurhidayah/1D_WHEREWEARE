import os
import time
import threading
from pygame import mixer
import sys

MP3_FILE = "One Direction - Where We Are (Official Audio).mp3"  
LYRICS = [
    (3.0, "Remember when we would stay out to late"),
    (7.5, "We were young, having fun, made mistakes"),
    (10.56, "Did we ever know?"),
    (12.58, "Did we ever know?????"),
    (14.56, "Did we ever know? Yeah..."),
    (19.01, "All the things we just think out the same"),
    (23.02, "Never wrong, always right, not afraid"),
    (26.23, "Did we ever know??????"),
    (28.20, "Did we ever know??"),
    (30.02, "Did we ever know???"),
    (34.02, "Is it all inside of my head?"),
    (37.19, "Maybe you still think I don't care"),
    (41.53, "But all I need is you"),
    (44.51, "Yeah, you know it's true,"),
    (46.23, "Yeah, you know it's true"),
    (48.08, "Forget about where we are"),
    (52.03, "And let go, we're so close"),
    (56.00, "If you don't know where to start"),
    (59.58, "Just hold on and don't run"),
    (64.02, "No..."),
    (65.31, "We're looking back"),
    (67.56, "We're messing around"),
    (69.57, "But that was then"),
    (71.50, "And this is now"),
    (72.49, "All we need is enough love"),
    (77.01, "To hold us"),
    (79.01, "Where we are")
    (79.01, "dah malas ulang la")

]

def animate_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class MusicPlayer:
    def __init__(self):
        mixer.init()
        self.current_time = 0
        self.is_playing = False

    def play(self):
        if not os.path.exists(MP3_FILE):
            return

        mixer.music.load(MP3_FILE)
        mixer.music.play()
        self.is_playing = True
        
        threading.Thread(target=self.update_time, daemon=True).start()
        
        self.display_lyrics()

    def update_time(self):
        while self.is_playing:
            self.current_time = mixer.music.get_pos() / 1000  
            time.sleep(0.1)

    def display_lyrics(self):
        displayed = set()
        
        while self.is_playing:
            for timestamp, lyric in LYRICS:
                if (timestamp <= self.current_time < timestamp + 3 and 
                    lyric not in displayed):
                    
                    sys.stdout.write("\r" + " " * 100 + "\r")  
                    
                    mins, secs = divmod(timestamp, 60)
                    print(f"[{int(mins)}:{int(secs):02d}] ", end="")
                    
                    animate_text(lyric, speed=0.10)
                    
                    displayed.add(lyric)
            
            time.sleep(0.1)
            
            if not mixer.music.get_busy():
                self.is_playing = False
                
        print("\nLagu selesai ges")

    def stop(self):
        mixer.music.stop()
        self.is_playing = False

if __name__ == "__main__":
    player = MusicPlayer()
    
    try:
        player.play()
        while player.is_playing:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nstop cpe")
    finally:
        player.stop()