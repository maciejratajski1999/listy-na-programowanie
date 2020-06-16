import json
class Score:

    def __init__(self):
        self.file = open("resources\\highscore.json", "r")
        self.record = json.load(self.file)
        self.metal, self.blues = self.record["metal"], self.record["blues"]
        self.file.close()

    def save(self, score, key):
        if score > self.record[key]:
            self.record[key] = score
            self.file = open("resources\\highscore.json", "w")
            json.dump(self.record, self.file)
            self.file.close()
