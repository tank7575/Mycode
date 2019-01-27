class Songbird:
    def __init__(self, name, song):
        self.name = name
        self.song = song
        print("^^^ name")
        print(self.name, 'Is Born...')

    def sing(self):
        print(">>>> sing")
        print(self.name, 'Sings:', self.song)

    def __del__(self):
        print("<<<< __del__")
        print(self.name, 'Flew Away!\n')
