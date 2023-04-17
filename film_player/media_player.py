class Player:
    def __init__(self, media_name, quality='720p'):
        self.media_name = media_name  # назва медіа
        self.quality = quality  # якість відтворення за замовчуванням
        self.playing = False  # чи відтворюється медіа зараз
        self.last_time = 0  # час, на якому було призупинене відтворення

    def play(self):
        if not self.playing:
            self.playing = True
            print(f'Playing {self.media_name} at {self.quality} quality')
        else:
            print(f'{self.media_name} is already playing')

    def pause(self):
        if self.playing:
            self.playing = False
            print(f'Pausing {self.media_name} at {self.last_time} seconds')
        else:
            print(f'{self.media_name} is already paused')

    def save_last_time(self, time):
        self.last_time = time
        print(f'Saving last time for {self.media_name} at {self.last_time} seconds')

    def change_quality(self, quality):
        self.quality = quality
        print(f'Changing {self.media_name} quality to {self.quality}')
