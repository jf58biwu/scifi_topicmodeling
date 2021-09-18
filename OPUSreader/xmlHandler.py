from xml.dom.minidom import *

class xmlHandler():
    def __init__(self, path, filename):
        self.dom_object = parse(path)
        self.filename = filename
        self.ID = path.split('/')[-2]
        print(path)
        print(self.filename)
        print(self.ID)

    def readElement(self, elementName):
        try:
            source = self.dom_object.getElementsByTagName("source")[0]
            element = source.getElementsByTagName(str(elementName))[0]
            return element.firstChild.data
        except (IndexError, AttributeError):
            return "NULL"

    def getSubtitles(self):
        subtitles = ""
        try:
            s = self.dom_object.getElementsByTagName("s")
            for subtitle in s:
                w = subtitle.getElementsByTagName("w")
                for word in w:
                    subtitles = subtitles+' '+word.firstChild.data
            subtitles = subtitles + '\n'
        except IndexError:
            return "NULL"
        return subtitles

    def getFileName(self):
        return self.filename

#if __name__ == "__main__":
