class Song:

    def __init__(self, key):
        self.key = key
        self.bpm, self.tab, self.background_sounds, self.user_sounds = self.__translate()
        self.length = len(self.tab)

    def __translate(self):
        self.song_dict = {
            "metal" : (130, [["Q"], ["Q"], ["W", "R"], ["Q", "E"], [ "E"], ["Q"], ["W"], [ "E"], ["R"], ["Q"], ["W", "R"], ["Q", "E"], ["E"], ["E"], ["E"], ["E"], ["E"], ["E"], ["W"], ["W"], ["W"], ["W"], ["W"], ["W"]], ["resources\\metal_E.wav", "resources\\metal_G.wav", "resources\\metal_A.wav", "resources\\metal_B.wav"], {"Q" : "resources\\user_A.wav", "W" : "resources\\user_C.wav", "E" : "resources\\user_D.wav", "R" : "resources\\user_E.wav"}),
            "blues" : (97, [["W"], ["E"], [], ["W"], ["W"], ["E"], ["W"], ["E"], ["Q"], ["W"], ["W"], ["E"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["R"], ["R"], ["E"], ["Q"], ["Q"], ["Q"], ["E"], ["W"], ["W"], ["W"], ["E"], ["Q"], ["R"], [], [], ["R"]], ["resources\\metal_E.wav", "resources\\metal_G.wav", "resources\\metal_A.wav", "resources\\metal_B.wav"],{"Q" : "resources\\user_A.wav", "W" : "resources\\user_C.wav", "E" : "resources\\user_D.wav", "R" : "resources\\user_E.wav"})
        }
        return self.song_dict[self.key]