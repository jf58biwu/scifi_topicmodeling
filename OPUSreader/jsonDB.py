import json
import os
import Movie

class jsonDB(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))
            return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

if __name__ == "__main__":
    location = 'movieDB.json'
    DB = jsonDB(location)
    entry1 = Movie.Movie('peter', 1999, 'Horror', 'uganda','test.xml',1112221)
    entry2 = Movie.Movie('arnold', 1999, 'Horror', 'uganda','test.xml',1112221)
    entry3 = Movie.Movie('gunhilde', 1999, 'Horror', 'uganda','test.xml',115661)
    DB.set(entry1.getID(), entry1.toList())
    print(DB.get("1112221"))
    DB.set(entry2.getID(), entry2.toList())
    print(DB.get("1112221"))
    DB.set(entry3.getID(), entry3.toList())
    print(DB.get("115661"))
