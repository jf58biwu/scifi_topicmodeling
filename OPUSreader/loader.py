import os

class loader():

	def __init__(self):
		# The extension to search for
		self.exten = '.xml'
		# The top argument for walk
		self.topdir = '/home/fill/Desktop/DigPhil_Projekt/OpenSubtitles_en/OpenSubtitles/xml/en'
		self.Movies = []

	def loadTimeSpan(self, start, end):
		self.Movies = []
		years = range (start, end)
		for year in years:
			for dirpath, dirnames, files in os.walk(self.topdir+'/'+str(year)):
				for name in files:
					path = dirpath+'/'+name
					if name.lower().endswith(self.exten):
						movie = (path, name)
						print(movie)
						self.Movies.append(movie)

	def getMovieList(self):
		return self.Movies

if __name__ == "__main__":

	XMLloader = loader()
	XMLloader.loadTimeSpan(1945,1950)
	print(len(XMLloader.Movies))
