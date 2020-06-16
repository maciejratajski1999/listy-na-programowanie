
class Note:

    def __init__(self, key, sounds):
        self.key = key
        self.sounds = self.sound_Q, self.sound_W, self.sound_E, self.sound_R = sounds
        self.image, self.pos, self.sound = self.__translate()


    def __str__(self):
        return self.key + " " + self.image + " " +  str(self.pos)

    def __translate(self):
        image_translation = {"Q": ("resources\\Q.png", 190, self.sound_Q),
                                  "W": ("resources\\W.png", 350, self.sound_W),
                                  "E": ("resources\\E.png", 510, self.sound_E),
                                  "R": ("resources\\R.png", 670, self.sound_R),
                             None : ("resources\\placeholder.bmp", 1000, None)}
        return image_translation[self.key]