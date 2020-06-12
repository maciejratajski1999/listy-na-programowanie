
class Note:

    def __init__(self, key):
        self.key = key
        self.image, self.pos = self.__translate()

    def __str__(self):
        return self.key + " " + self.image + " " +  str(self.pos)

    def __translate(self):
        image_translation = {"Q": "resources\\Q.png",
                                  "W": "resources\\W.png",
                                  "E": "resources\\E.png",
                                  "R": "resources\\R.png"}
        pos_translation = {"Q": 190, "W": 350, "E": 510, "R": 660}
        return image_translation[self.key], pos_translation[self.key]