import OpenSubtitlesReader
import jsonDB

''' get movie LIst
    check if movie scifi
    save movie
'''

# def savePeriod(start, end):
#     Reader = OpenSubtitlesReader.OpenSubtitlesReader()
#     Reader.loadPeriod(start,end)
#     MovieList = Reader.filterGenre(genre)
#     print(len(MovieList))
#     for film in MovieList:
#         tmp =[film.readElement('year'),film.readElement('genre'), film.readElement('country'), film.filename]
#         DB.set(film.ID,tmp)
#         print(tmp)
#         Reader.saveSubtitleTXT(film, str(start)+'_'+str(end))

def savePeriod(start, end):
    Reader = OpenSubtitlesReader.OpenSubtitlesReader()
    Reader.loadPeriod(start,end)
    MovieList = Reader.getMovieList()
    for film in MovieList:
        print(film)
        XML = Reader.createXMLobject(film[0],film[1])
        if Reader.isGenre(XML, "Sci-Fi"):
            tmp =[XML.readElement('year'),XML.readElement('genre'), XML.readElement('country'), XML.filename]
            print(tmp)
            DB.set(XML.ID,tmp)
            Reader.saveSubtitleTXT(XML, str(start)+'_'+str(end))

DB = jsonDB.jsonDB('subtitleData/movieDB.json')
genre = "Sci-Fi"
start = 1860
end = 2018

# for i in range(start, end-5, 5):
#     S = i
#     E = i+5
#     print('savePeriod('+str(S)+', '+str(E)+')')
#     savePeriod(S,E)

savePeriod(2015,2018)

# print('savePeriod(1860,1865)')
# savePeriod(1860,1865)
#
# print('savePeriod(1865,1870)')
# savePeriod(1865,1870)
#
# print('savePeriod(1870,1875)')
# savePeriod(1870,1875)
#
# print('savePeriod(1875,1880)')
# savePeriod(1875,1880)
#
# print('savePeriod(1880,1885)')
# savePeriod(1880,1885)
#
# print('savePeriod(1885,1890)')
# savePeriod(1885,1890)
#
# print('savePeriod(1890,1895)')
# savePeriod(1890,1895)
#
# print('savePeriod(1905,1910)')
# savePeriod(1895,1900)
#
# print('savePeriod(1860,1865)')
# savePeriod(1900,1905)
#
# print('savePeriod(1860,1865)')
# savePeriod(1905,1910)
#
# print('savePeriod(1930,1935)')
# savePeriod(1910,1915)
#
# print('savePeriod(1935,1940)')
# savePeriod(1915,1920)
#
# print('savePeriod(1945,1950)')
# savePeriod(1920,1925)
#
# print('savePeriod(1955,1960)')
# savePeriod(1925,1930)
#
# print('savePeriod(1960,1965)')
# savePeriod(1930,1935)
#
# print('savePeriod(1965,1970)')
# savePeriod(1935,1940)
#
# print('savePeriod(1970,1975)')
# savePeriod(1940,1945)
#
# print('savePeriod(1975,1980)')
# savePeriod(1945,1950)
#
# print('savePeriod(1980,1985)')
# savePeriod(1950,1955)
#
# print('savePeriod(1985,1990)')
# savePeriod(1955,1960)
#
# print('savePeriod(1990,1995)')
# savePeriod(1960,1965)
#
# print('savePeriod(1995,2000)')
# savePeriod(1965,1970)
#
# print('savePeriod(2005,2010)')
# savePeriod(1970,1975)
#
# print('savePeriod(2010,2015)')
# savePeriod(1975,1980)
#
# savePeriod(1980,1985)
#
# savePeriod(1985,1990)
#
# savePeriod(1990,1995)
#
# savePeriod(1995,2000)
#
# savePeriod(2000,2005)
#
# savePeriod(2005,2010)
#
# savePeriod(2010,2015)
