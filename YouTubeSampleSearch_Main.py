import sys
from YouTubeSampleSearch_Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog
import random
from selenium import webdriver
from pytube import YouTube
import os

# YouTube Sample Search - randomized search terms challenge producers to sample obscure music. Users can also convert whatever YouTube video they want to the highest bitrate available via copying and pasting the video's URL into the URL bar.


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('YouTube Sample Search')
        self.downloadButton.setAutoDefault(True)
        self.searchButton.clicked.connect(self.searchButtonPushed)
        self.browseButton.clicked.connect(self.browseButtonPushed)
        self.youTubeURLTextEdit
        self.downloadButton.clicked.connect(self.downloadButtonPushed)
        self.dlComplete = self.downloadCompleteLabel.setText("")

    def timePeriodGroup(self):

        # randomizes time periods available for search

        timePeriod = ('50s', '60s', '70s', '80s',
                      '90s', '00s', '2010s', '2020s')

        timePeriodResult = random.choice(timePeriod)

        self.timePeriodSearch = str(
            self.timePeriodLineEdit.setText(timePeriodResult))

        return self.timePeriodSearch

    def regionGroup(self):

        # randomizes regions available for search

        region = ('Ghanaian', 'Chinese', 'Japanese', 'Indian', 'South African',      'American', 'Mexican', 'Canadian', 'Nigerian', 'Haitian',
                  'West Indian', 'Jamaican', 'Russian', 'Turkish', 'English',
                  'French', 'Spanish', 'Angolan', 'Antiguan', 'Caribbean',
                  'Jamaican', 'Puerto Rican', 'Cuban', 'German', 'Polish',
                  'Brazilian', 'Polish', 'Italian', 'Korean', 'Thai', 'Egyptian'
                  'Malaysian', 'African', 'Asian', 'North American', 'Somalian'
                  'South American', 'European', 'Australian', 'Kiwi',
                  'Sudanese', 'Ethiopian', 'Polynesian', 'Tongan', 'Dominican',
                  'Costa Rican', 'Colombian', 'Gambian', 'Kenyan')

        regionResult = random.choice(region)

        self.regionSearch = str(
            self.regionLineEdit.setText(regionResult))

        return self.regionSearch

    def genreGroup(self):

        # randomizes genres available for search

        genre = ('Rap', 'Rock', 'Salsa', 'Kompa', 'Roots', 'R&B', 'Soul', 'Pop',     'Dancehall', 'Metal', 'Reggae', 'Classical', 'Merengue',
                 'Hardcore Techno', 'High Life', 'EDM', 'Country', 'Funk',
                 'OST', 'TV theme', 'Movie Theme', 'Acid House', 'Commercial',
                 'Movie Soundtrack', 'Techno', 'House', 'Country',
                 'Electronic', 'Yacht Rock', 'Hard Rock', 'Hardcore', 'Folk',
                 'Indie Rock', 'Indie', 'Bluegrass', 'Psychedelic Rock',
                 'Rave', 'Dance', 'Breakbeat')

        genreResult = random.choice(genre)

        self.genreSearch = str(self.genreLineEdit.setText(genreResult))

        return self.genreSearch

    def searchButtonPushed(self):

        # automates a YouTube search of the aforementioned terms into a new browser window

        self.dlComplete

        browser = webdriver.Chrome(
            'C:\\Users\\Sam\\Downloads\\chromedriver.exe')

        self.timePeriodGroup()
        self.regionGroup()
        self.genreGroup()

        browser.get(
            f'https://www.youtube.com/results?search_query={self.timePeriodLineEdit.text()}+{self.regionLineEdit.text()}+{self.genreLineEdit.text()}+music')

    def browseButtonPushed(self):

        # lets the user decide the destination for the audio they want to download

        self.dlComplete

        self.filename = QFileDialog.getExistingDirectory(self, 'Save File')

        if self.filename:
            self.fileLocationTextEdit.setText(str(self.filename))

    def downloadButtonPushed(self):

        # Converts the youtube video in the YouTube URL bar into an mp4 and then an mp3, also gives a prompt when the download's complete

        self.dlComplete

        audioLink = YouTube(str(self.youTubeURLTextEdit.text()))
        audioFile = audioLink.streams.get_audio_only()
        output = audioFile.download(output_path=self.filename)

        file, ext = os.path.splitext(output)
        mp3File = file + '.mp3'
        os.rename(output, mp3File)

        self.dlComplete = self.downloadCompleteLabel.setText(
            "Download Complete!")


if __name__ == '__main__':
    app = qtw.QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()
    sys.exit(app.exec_())
