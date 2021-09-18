from xml.dom.minidom import *
import Movie
class MovieDB():
    def __init__(self):
        self.Movies = []

    def newDBfile(self):
        path = 'subtitleData'
        if not os.path.exists(path):
            os.mkedirs(path)
        filename = 'SubtitleDB.xml'
        filepath = os.path.join(path, filename)
        f=open(filepath, 'w+')
        f.write('test')
        f.close()
        print("wrote: "+filename)
        return filepath

    def getEntry(self, index):
        return self.Movies[index]

    def newEntry(self, title, year, genre, country,filename ,ID):
        entry = Movie.Movie(title,year,genre,country, filename, ID)
        print(entry)
        #if ID not in self.Movies:
        # if not (filter(lambda x:ID in x, self.Movies)):
        #     print(lambda x:ID in x, self.Movies)
        #     self.Movies.append((ID, [entry]))
        # else:
        #     print(filter(lambda x:ID in x, self.Movies))
        #     self.Movies[self.Movies.index((filter(lambda x:ID in x, self.Movies)))][1].append(entry)
        if any(ID in self.movies):
            self.movies

if __name__ == "__main__":
    DB = MovieDB()
    DB.newEntry(['arnold', 1999, 'Horror', 'uganda','test.xml',1112221])
    DB.newEntry(['peter', 1999, 'Horror', 'uganda','test.xml',1112221])
    print(DB.getEntry(0)[0])
    print(DB.getEntry(1)[0])
