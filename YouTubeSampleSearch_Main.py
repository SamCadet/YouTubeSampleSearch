import sys
from YouTubeSampleSearch_Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot
import random
from pytube import YouTube
import os
import webbrowser

# YouTube Sample Search - randomized search terms challenge producers to sample obscure music. Users can also convert whatever YouTube video they want to the highest bitrate available via copying and pasting the video's URL into the URL bar.


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('YouTube Sample Search')
        self.downloadButton.setAutoDefault(True)
        self.searchButton.clicked.connect(self.searchButtonPushed)
        self.browseButton.clicked.connect(self.browseButtonPushed)
        self.downloadButton.clicked.connect(self.downloadButtonPushed)
        self.youTubeURLTextEdit
        self.dlComplete = self.downloadCompleteLabel.setText("")

    def timePeriodGroup(self):

        # randomizes time periods available for search

        timePeriod = ('50s', '60s', '70s', '80s',
                      '90s', '00s', '2010s', '2020s')

        timePeriodResult = random.choice(timePeriod)

        self.timePeriodSearch = str(
            self.randomTimePeriodLabel.setText(timePeriodResult))

        return self.timePeriodSearch

    def regionGroup(self):

        # randomizes regions available for search

        region = ('Ghanaian', 'Chinese', 'Japanese', 'Indian', 'South African',      'American', 'Mexican', 'Canadian', 'Nigerian', 'Haitian',
                  'West Indian', 'Jamaican', 'Russian', 'Turkish', 'English',
                  'French', 'Spanish', 'Angolan', 'Antiguan', 'Caribbean',
                  'Jamaican', 'Puerto Rican', 'Cuban', 'German', 'Polish',
                  'Brazilian', 'Polish', 'Italian', 'Korean', 'Thai',
                  'Egyptian', 'Malaysian', 'African', 'Asian',
                  'North American', 'Somalian', 'South American', 'European',
                  'Australian', 'Kiwi', 'Sudanese', 'Ethiopian', 'Polynesian',
                  'Tongan', 'Dominican', 'Costa Rican', 'Colombian',
                  'Gambian', 'Kenyan')

        regionResult = random.choice(region)

        self.regionSearch = str(
            self.randomRegionLabel.setText(regionResult))

        return self.regionSearch

    def genreGroup(self):

        # randomizes genres available for search

        genre = ('Rap', 'Rock', 'Salsa', 'Kompa', 'Roots', 'RNB', 'Soul', 'Pop',     'Dancehall', 'Metal', 'Reggae', 'Classical', 'Merengue',
                 'Hardcore Techno', 'High Life', 'EDM', 'Country', 'Funk',
                 'Movie OST', 'Game OST', 'TV theme', 'Movie Theme',
                 'Acid House', 'Commercial', 'Movie Soundtrack', 'Techno',
                 'House', 'Country', 'Electronic', 'Yacht Rock', 'Hard Rock',
                 'Hardcore', 'Folk', 'Indie Rock', 'Indie', 'Bluegrass',
                 'Psychedelic Rock', 'Rave', 'Dance', 'Breakbeat')

        genreResult = random.choice(genre)

        self.genreSearch = str(self.randomGenreLabel.setText(genreResult))

        return self.genreSearch

    def searchButtonPushed(self):

        # automates a YouTube search of the aforementioned terms into a new browser tab

        self.dlComplete

        self.timePeriodGroup()
        self.regionGroup()
        self.genreGroup()

        webbrowser.open_new_tab(
            f'https://www.youtube.com/results?search_query={self.randomTimePeriodLabel.text()}+{self.randomRegionLabel.text()}+{self.randomGenreLabel.text()}')

    def removeReservedChars(self, youTubeURL):

        reservedChars = {'<', '>', ':', '"', '/', '\\', '|', '?', '*'}

        for char in youTubeURL:
            if char in reservedChars:
                youTubeURL = youTubeURL.replace(char, '_')

        return youTubeURL

    def browseButtonPushed(self):

        # lets the user decide the destination for the audio they want to download

        self.linkString = self.youTubeURLTextEdit.text()
        self.YouTubeURL = YouTube(self.linkString)

        self.fileLocation = QFileDialog.getExistingDirectory(self, 'Save File')
        self.fileName = self.removeReservedChars(str(self.YouTubeURL.title))
        print(self.fileName)

        if self.fileLocation:
            self.fileLocationTextEdit.setText(
                f'{self.fileLocation}/{self.fileName}')

    @pyqtSlot()
    def downloadButtonPushed(self):

        # Converts the youtube video in the YouTube URL bar into an mp4 and then an mp3, also gives a prompt when the download's complete

        audioLink = YouTube(self.youTubeURLTextEdit.text())
        audioFile = audioLink.streams.get_audio_only()
        output = audioFile.download(
            output_path=self.fileLocation, filename=self.fileName)

        self.linkString.register_on_progress_callback(self.fileProgress)

        file, ext = os.path.splitext(output)
        mp3File = file + '.mp3'
        os.rename(output, mp3File)

        self.dlComplete = self.downloadCompleteLabel.setText(
            "Download Complete!")

    def fileProgress(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = int((abs(bytes_remaining - size) / size)) * 100
        self.progressBar.setValue(progress)


if __name__ == '__main__':
    app = qtw.QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()
    sys.exit(app.exec_())
