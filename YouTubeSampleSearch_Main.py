import sys
from YouTubeSampleSearch_Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog
import random
from selenium import webdriver
from pytube import YouTube
import os

# YouTube Sample Search - randomized search terms challenge producers to sample obscure music

# ytApi = os.environ['YOUTUBE_API_KEY']


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

    def timePeriodGroup(self):
        timePeriod = ('50s', '60s', '70s', '80s',
                      '90s', '00s', '2010s', '2020s')

        timePeriodResult = random.choice(timePeriod)

        self.timePeriodSearch = str(
            self.timePeriodLineEdit.setText(timePeriodResult))

        return self.timePeriodSearch

    def regionGroup(self):

        region = ('Ghanaian', 'Chinese', 'Japanese', 'Indian', 'South African', 'American', 'Mexican', 'Canadian', 'Nigerian', 'Haitian',
                  'Jamaican', 'English', 'French', 'Spanish', 'Puerto Rican', 'Cuban', 'German')

        regionResult = random.choice(region)

        self.regionSearch = str(
            self.regionLineEdit.setText(regionResult))

        return self.regionSearch

    def genreGroup(self):

        genre = ('Rap', 'Rock', 'Salsa', 'R&B', 'Soul', 'Pop', 'Dancehall', 'Metal', 'Reggae', 'Classical', 'Merengue',
                 'Country', 'Funk', 'OST', 'TV themes', 'Movie Themes', 'Commercials', 'Movie Soundtracks', 'Techno', 'House', 'Country', 'Electronic', 'Yacht Rock', 'Hard Rock', 'Hardcore')

        genreResult = random.choice(genre)

        self.genreSearch = str(self.genreLineEdit.setText(genreResult))

        return self.genreSearch

    def searchButtonPushed(self):

        browser = webdriver.Chrome(
            'C:\\Users\\Sam\\Downloads\\chromedriver.exe')

        self.timePeriodGroup()
        self.regionGroup()
        self.genreGroup()

        browser.get(
            f'https://www.youtube.com/results?search_query={self.timePeriodLineEdit.text()}+{self.regionLineEdit.text()}+{self.genreLineEdit.text()}+music')

    def browseButtonPushed(self):

        self.filename = QFileDialog.getExistingDirectory(self, 'Save File')

        if self.filename:
            self.fileLocationTextEdit.setText(str(self.filename))

        self.dlComplete = self.downloadCompleteLabel.setText("")

    def downloadButtonPushed(self):

        audioLink = YouTube(str(self.youTubeURLTextEdit.text()))
        audioFile = audioLink.streams.filter(only_audio=True).first()
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
