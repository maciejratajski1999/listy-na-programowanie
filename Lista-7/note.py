
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
        pos_translation = {"Q": 70, "W": 310, "E": 550, "R": 790}
        return image_translation[self.key], pos_translation[self.key]