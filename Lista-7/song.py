class Song:

    def __init__(self, key):
        self.key = key
        self.tab = self.__translate()[1:]
        self.bpm = self.__translate()[0]

    def __translate(self):
        self.song_dict = {
            "metal" : [210, ["Q"], ["Q"], ["W", "R"], ["Q", "E"], [ "E"], ["Q"], ["W"], [ "E"], ["R"], ["Q"], ["W", "R"], ["Q", "E"], ["E"], ["E"], ["E"], ["E"], ["E"], ["E"], ["W"], ["W"], ["W"], ["W"], ["W"], ["W"]],
            "blues" : [97, ["W"], ["E"], [], ["W"], ["W"], ["E"], ["W"], ["E"], ["Q"], ["W"], ["W"], ["E"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["Q"], ["Q"], ["E"], ["W"], ["W"], ["W"], ["E"], ["Q"], ["R"], [], [], ["R"]]
        }
        return self.song_dict[self.key]