import loader
import os
import xmlHandler as xml
class OpenSubtitlesReader():

    def __init__(self):
        self.XMLloader = loader.loader()

    def loadPeriod(self,start,end):
        self.XMLloader.loadTimeSpan(start,end)

    def filterGenre(self, genre):
        list = []
        for movie in self.XMLloader.getMovieList():
            xmlHandl = xml.xmlHandler(movie[0], movie[1])
            if genre in xmlHandl.readElement("genre"):
                list.append(xmlHandl)
        return list

    def getMovieList(self):
        return self.XMLloader.getMovieList()

    def isGenre(self, xmlObject,genre):
        if genre in xmlObject.readElement("genre"):
            return True
        else:
            return False

    def createXMLobject(self, filename, path):
        xmlHandl = xml.xmlHandler(filename, path)
        return xmlHandl

    def saveSubtitleTXT(self, subtitle, directory):
        path = 'subtitleData'+'/'+directory
        if not os.path.exists(path):
            os.makedirs(path)
        filename = subtitle.getFileName() + '.txt'
        f=open(os.path.join(path, filename), 'w+')
        f.write(subtitle.getSubtitles())
        f.close()
        print("wrote: "+filename)

    def saveDBentry():
        path = 'subtitleData'
        if not os.path.exists(path):
            os.mkedirs(path)
        filename = SubtitleDB

if __name__ == "__main__":
    Reader = OpenSubtitlesReader()
    Reader.loadPeriod(1920,1930)
    SciFi = Reader.filterGenre("Sci-Fi")
    print(len(SciFi))
    for film in SciFi:
        print(film.readElement('year')+' '+film.readElement('genre')+' '+film.readElement('country'))
        Reader.saveSubtitleTXT(film,'1920_1930')
