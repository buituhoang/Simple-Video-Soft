from PyQt5 import QtWidgets, QtGui, QtCore
from GUI import MainWindow
from pathlib import Path

import ffmpeg
import os
import time
import urllib

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.MainScreen = MainWindow()  
        self.MainScreen.setupUi(self)

        self.MainScreen.choose_file_type_output_video.addItems([
            'Select output file type','.avi','.flv', '.m4a', 
            '.m4b', '.mkv','.mp3', '.mp4', '.mpeg', '.wma', '.wmv'
            ])
        self.MainScreen.choose_speed_video.addItems([
            'ultrafast', 'superfast', 'veryfast', 'fast', 
            'medium', 'slow', 'veryslow'
            ])
        self.MainScreen.tabWidget.setCurrentIndex(0)
        self.MainScreen.CancelFileButton.setVisible(False)
        self.MainScreen.CancelImageButton.setVisible(False)
        self.MainScreen.ButtonConvert.setEnabled(False)
        self.MainScreen.AddressBroadcast.setEnabled(False)
        self.MainScreen.label_Progress.setVisible(False)

        self.OutputType ='.mp4'
        self.ConverSpeed = '-preset ultrafast'
        self.CRF = '-crf 23'
        self.OutputFileName = 'F_' + time.strftime("%H_%M_%S", time.localtime())
        self.OutputFullNameWithType = self.OutputFileName + self.OutputType
        self.SavingPath = ''
        self.FilePathString = ''
        self.OutputFilePathString = ''
        self.AddImageString = ''
        self.ImagePathString = ''
        self.OpacityString = ''
        self.ImagePosition = ''
        self.RotateDegree = 0
        self.hFlip = 0
        self.vFlip = 0
        self.TransposeString = ''
        self.flipString = ''
        self.AddressBroadcastString = ''
        self.StreamingAddress = ''

        self.MainScreen.tabWidget.currentChanged.connect(self.clearData)
        self.MainScreen.BrowseButton.clicked.connect(self.handle_open_file)
        self.MainScreen.BrowseImageButton.clicked.connect(self.handle_open_image)
        self.MainScreen.CancelFileButton.clicked.connect(self.cancle_chosen_file)
        self.MainScreen.CancelImageButton.clicked.connect(self.cancle_chosen_image)
        self.MainScreen.BrowseSavingButton.clicked.connect(self.handle_saving_folder)
        self.MainScreen.choose_file_type_output_video.currentIndexChanged.connect(self.fileTypeVideoChange)
        self.MainScreen.choose_speed_video.currentIndexChanged.connect(self.speedChangeVideo)
        self.MainScreen.spinBoxCFRVideo.valueChanged.connect(self.CFRchangeVideo)
        self.MainScreen.ButtonConvert.clicked.connect(self.ConvertVideo)
        self.MainScreen.OutPutFileNameEdit.textChanged.connect(self.setOutputFileName)
        self.MainScreen.AddressBroadcast.textChanged.connect(self.setAddressBroadcasting)
        self.MainScreen.Centered.toggled.connect(self.putImageCentered)
        self.MainScreen.CenteredLeft.toggled.connect(self.putImageCenteredLeft)
        self.MainScreen.CenteredRight.toggled.connect(self.putImageCenteredRight)
        self.MainScreen.CenteredTop.toggled.connect(self.putImageCenteredTop)
        self.MainScreen.CenteredBottom.toggled.connect(self.putImageCenteredBottom)
        self.MainScreen.TopLeft.toggled.connect(self.putImageTopLeft)
        self.MainScreen.TopRight.toggled.connect(self.putImageTopRight)
        self.MainScreen.BottomLeft.toggled.connect(self.putImageBottomLeft)
        self.MainScreen.BottomRight.toggled.connect(self.putImageBottomRight)
        self.MainScreen.OpacitySlider.valueChanged['int'].connect(self.changeOpacity)
        self.MainScreen.CounterClockwise.clicked.connect(self.rotateCounterClockwise)
        self.MainScreen.Clockwise.clicked.connect(self.rotateClockwise)
        self.MainScreen.Horizontal.clicked.connect(self.flipHorizontal)
        self.MainScreen.Vertical.clicked.connect(self.flipVertical)
        self.MainScreen.checkBoxBroadcast.stateChanged.connect(self.setBroadcastEnable)
        
    def setAddressBroadcasting(self):
        self.StreamingAddress = self.MainScreen.AddressBroadcast.text()
        self.AddressBroadcastString = '-f rtp_mpegts ' + self.StreamingAddress 
        self.setCommand()

    def clearData(self):
        self.AddImageString = ''
        self.MainScreen.command_box.clear()
        self.TransposeString = ''
        self.TransposeCommand = ''
        self.OpacityString = ''
        self.OutputType = '.mp4'
        self.SavingPath = ''
        self.OutputFilePathString = ''
        self.OutputFileName = 'F_' + time.strftime("%H_%M_%S", time.localtime())
        self.OutputFullNameWithType = self.OutputFileName + self.OutputType
        self.RotateDegree = 0
        self.hFlip = 0
        self.vFlip = 0
        self.TransposeString = ''
        self.flipString = ''

    def setBroadcastEnable(self):
        if self.MainScreen.checkBoxBroadcast.isChecked():
            self.MainScreen.AddressBroadcast.setEnabled(True)
        else:
            self.MainScreen.AddressBroadcast.setEnabled(False)
            self.MainScreen.AddressBroadcast.clear()
            self.AddressBroadcastString = ''

    def changeOpacity(self):
        self.MainScreen.OpacityValue.setNum(self.MainScreen.OpacitySlider.value())
        self.setOpacityString()

    def rotateCounterClockwise(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        t = QtGui.QTransform()
        t.rotate(270)
        rotateTmpPic = tmpPic.transformed(t)
        self.TempNewThumbnail = QtGui.QPixmap(rotateTmpPic)
        self.MainScreen.newThumbnail.setPixmap(rotateTmpPic)
        self.RotateDegree += 270
        self.checkRotation()
        
    def rotateClockwise(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        t = QtGui.QTransform()
        t.rotate(90)
        rotateTmpPic = tmpPic.transformed(t)
        self.TempNewThumbnail = QtGui.QPixmap(rotateTmpPic)
        self.MainScreen.newThumbnail.setPixmap(rotateTmpPic)
        self.RotateDegree += 90
        self.checkRotation()

    def flipHorizontal(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        flipTmpPic = tmpPic.transformed(QtGui.QTransform().scale(-1, 1))
        self.TempNewThumbnail = QtGui.QPixmap(flipTmpPic)
        self.MainScreen.newThumbnail.setPixmap(flipTmpPic)
        self.hFlip += 1
        self.checkRotation()

    def flipVertical(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        flipTmpPic = tmpPic.transformed(QtGui.QTransform().scale(1, -1))
        self.TempNewThumbnail = QtGui.QPixmap(flipTmpPic)
        self.MainScreen.newThumbnail.setPixmap(flipTmpPic)
        self.vFlip += 1
        self.checkRotation()

    def checkRotation(self):
        if self.RotateDegree != 0:
            mod = self.RotateDegree % 360
            if mod == 90:
                self.TransposeString = 'transpose=1'
            elif mod == 180:
                self.TransposeString = 'transpose=1, transpose=1'
            elif mod == 270:
                self.TransposeString = 'transpose=2'
            else:
                self.TransposeString = ''
        if self.hFlip % 2 == 1 and self.vFlip % 2 == 0:
            self.flipString = 'hflip'
        if self.hFlip % 2 == 0 and self.vFlip % 2 == 1:
            self.flipString = 'vflip'
        if self.hFlip % 2 == 1 and self.vFlip % 2 == 1:
            self.flipString = "'hflip', 'vflip'"
        self.setTransposeCommand()

    def setTransposeCommand(self):
        if self.TransposeString != '' and self.flipString == '':
            self.TransposeCommand = self.TransposeString 
        
        if self.TransposeString == '' and self.flipString != '':
            self.TransposeCommand = self.flipString 

        if self.TransposeString != '' and self.flipString != '':
            self.TransposeCommand = [self.TransposeString, self.flipString]
        self.setCommand()

    def putImageCentered(self):
        if self.MainScreen.Centered.isChecked():
            self.MainScreen.label_Position.setText("Centered")
            self.ImagePosition = 'overlay=(W-w)/2:(H-h)/2'
            self.setAddImageString()
            self.setCommand

    def putImageCenteredLeft(self):
        if self.MainScreen.CenteredLeft.isChecked():
            self.MainScreen.label_Position.setText("Centered Left")
            self.ImagePosition = 'overlay=5:(H-h)/2'
            self.setAddImageString()
            self.setCommand

    def putImageCenteredRight(self):
        if self.MainScreen.CenteredRight.isChecked():
            self.MainScreen.label_Position.setText("Centered Right")
            self.ImagePosition = 'overlay=W-w-5:(H-h)/2'
            self.setAddImageString()
            self.setCommand

    def putImageCenteredTop(self):
        if self.MainScreen.CenteredTop.isChecked():
            self.MainScreen.label_Position.setText("Centered Top")
            self.ImagePosition = 'overlay=(W-w)/2:5'
            self.setAddImageString()
            self.setCommand

    def putImageCenteredBottom(self):
        if self.MainScreen.CenteredBottom.isChecked():
            self.MainScreen.label_Position.setText("Centered Bottom")
            self.ImagePosition = 'overlay=(W-w)/2:H-h-5'
            self.setAddImageString()
            self.setCommand

    def putImageTopLeft(self):
        if self.MainScreen.TopLeft.isChecked():
            self.MainScreen.label_Position.setText("Top Left")
            self.ImagePosition = 'overlay=5:5'
            self.setAddImageString()
            self.setCommand

    def putImageTopRight(self):
        if self.MainScreen.TopRight.isChecked():
            self.MainScreen.label_Position.setText("Top Right")
            self.ImagePosition = 'overlay=W-w-5:5'
            self.setAddImageString()
            self.setCommand

    def putImageBottomLeft(self):
        if self.MainScreen.BottomLeft.isChecked():
            self.MainScreen.label_Position.setText("Bottom Left")
            self.ImagePosition = 'overlay=5:H-h-5'
            self.setAddImageString()
            self.setCommand

    def putImageBottomRight(self):
        if self.MainScreen.BottomRight.isChecked():
            self.MainScreen.label_Position.setText("Bottom Right")
            self.ImagePosition = 'overlay=W-w-5:H-h-5'
            self.setAddImageString()
            self.setCommand

    def setAddImageString(self):
        if self.OpacityString != '':
            self.FilterString = self.OpacityString + '[0][fg]' + self.ImagePosition 
        else:
            self.FilterString = self.ImagePosition
        self.AddImageString = '-i ' + self.ImagePathString + ' -filter_complex ' + self.FilterString
        if self.ImagePosition != '':
            self.setCommand()

    def setOpacityString(self):
        self.OpacityString = '[1:v]format=rgba,colorchannelmixer=aa=' + str(float(self.MainScreen.OpacityValue.text()) / float(100)) + '[fg];'
        self.setAddImageString()
        if self.ImagePosition != '':
            self.setCommand()

    def setOutputFileName(self):
        self.OutputFileName = self.MainScreen.OutPutFileNameEdit.text()
        if self.OutputFileName == '':
            self.OutputFileName = 'F_' + time.strftime("%H:%M:%S", time.localtime())
        self.OutputFullNameWithType = self.OutputFileName + self.OutputType
        self.setSavingPath()
        self.setCommand()

    def ConvertVideo(self):
        text = self.MainScreen.command_box.toPlainText()
        if text != '':
            self.MainScreen.command_box.clear()
            self.MainScreen.label_Progress.setVisible(True)
            if os.path.exists(self.SavingPath):
                os.remove(self.SavingPath)
            self.Run()
        else: 
            self.MainScreen.ButtonConvert.setEnabled(False)
            self.MainScreen.label_Progress.setText("No Command")
            self.MainScreen.label_Progress.setVisible(True)

    def Run(self):
        print("Wait")
        process = QtCore.QProcess(self)
        process.start('ffmpeg', self.CommandArgument)

    def CFRchangeVideo(self):
        self.CRF = '-crf ' + str(self.MainScreen.spinBoxCFRVideo.value())
        self.setCommand()
        
    def fileTypeVideoChange(self):
        if self.MainScreen.choose_file_type_output_video.currentText() != 'Select output file type':
            self.OutputType = self.MainScreen.choose_file_type_output_video.currentText()
            self.OutputFullNameWithType = self.OutputFileName + self.OutputType
            self.setSavingPath()
            self.setCommand()

    def speedChangeVideo(self):
        self.ConverSpeed = '-preset ' + self.MainScreen.choose_speed_video.currentText()
        self.setCommand()

    def handle_saving_folder(self):
        self.OutputFilePathString = QtWidgets.QFileDialog.getExistingDirectory()
        print(self.OutputFilePathString)
        self.FolderPath.setText(self.OutputFilePathString)
        self.setSavingPath()
        self.setCommand()
        if self.FilePathString != '':
            self.MainScreen.ButtonConvert.setEnabled(True)

    def handle_open_file(self):
        self.MainScreen.ButtonConvert.setEnabled(False)
        self.FilePathString = ''
        self.MainScreen.FilePath.clear()
        self.MainScreen.FileName.clear()
        self.MainScreen.InputThumbnail.clear()
        self.MainScreen.command_box.clear()
        self.MainScreen.CancelFileButton.setVisible(False)
        if os.path.exists(r'.\Temp\\thumbnail.png'):
            os.remove(r'.\Temp\\thumbnail.png')
        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "", "*.3gp *.amv *.avi *.flv *.gif *.mkv *.mp4 *.mpeg *.mpg *.ts *wmv")
        if filename[0] == '':
            return None
        self.FilePathString = filename[0]
        self.MainScreen.FilePath.setText(self.FilePathString)
        self.MainScreen.FileName.setText("Chosen file: " + Path(self.FilePathString).parts[len(Path(self.FilePathString).parts) - 1])
        if os.path.exists(r'.\Temp\\thumbnail.png'):
            os.remove(r'.\Temp\\thumbnail.png')

        (
            ffmpeg
            .input(self.FilePathString, ss=1)
            .filter('scale', 175, -1)
            .output(r'.\Temp\\thumbnail.png', vframes=1)
            .run()
        )
        if not os.path.exists(r'.\Temp\\thumbnail.png'):
            self.FilePathString = ''
            self.MainScreen.FileName.setText('The file format is not valid. Please select another file')
            return None
        else:
            self.MainScreen.CancelFileButton.setVisible(True)
            self.MainScreen.InputThumbnail.setPixmap(QtGui.QPixmap(r'.\Temp\\thumbnail.png'))
            self.MainScreen.oldThumbnail.setPixmap(QtGui.QPixmap(r'.\Temp\\thumbnail.png'))
            self.MainScreen.newThumbnail.setPixmap(QtGui.QPixmap(r'.\Temp\\thumbnail.png'))
            self.TempNewThumbnail = QtGui.QPixmap(r'.\Temp\\thumbnail.png')
            self.setCommand()
            self.MainScreen.CounterClockwise.setEnabled(True)
            self.MainScreen.Clockwise.setEnabled(True)
            self.MainScreen.Horizontal.setEnabled(True)
            self.MainScreen.Vertical.setEnabled(True)
            self.MainScreen.ButtonConvert.setEnabled(True)

    def handle_open_image(self):
        self.MainScreen.ImagePath.clear()
        self.MainScreen.ImageThumbnailName.clear()
        self.MainScreen.ImageThumbnail.clear()
        self.MainScreen.CancelImageButton.setVisible(False)

        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "*.jpeg *.png")
        if filename[0] == '':
            return None
        self.ImagePathString = filename[0]
        self.MainScreen.ImagePath.setText(self.ImagePathString)
        self.MainScreen.ImageThumbnailName.setText(Path(self.ImagePathString).parts[len(Path(self.ImagePathString).parts) - 1])
        self.MainScreen.CancelImageButton.setVisible(True)
        pixmap = QtGui.QPixmap(self.ImagePathString)
        self.MainScreen.ImageThumbnail.setPixmap(pixmap.scaledToWidth(100))

    def setCommand(self):
        self.MainScreen.command_box.clear()
        if self.SavingPath == '':
            self.SavingPath = '.\\' + self.OutputFullNameWithType
        if self.MainScreen.checkBoxBroadcast.isChecked():
            if self.AddressBroadcastString != '':
                if self.MainScreen.tabWidget.currentIndex() == 2:
                    self.MainScreen.command_box.insertPlainText(f'-i {self.FilePathString} -vf {self.TransposeCommand} -c:v libx264 -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.AddressBroadcastString}')
                    self.CommandArgument = ['-i', self.FilePathString, '-threads', '1', '-vf', self.TransposeCommand, '-c:v', 'libx264', '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-f', 'rtp_mpegts', self.StreamingAddress]
                elif self.MainScreen.tabWidget.currentIndex() == 1:
                    self.MainScreen.command_box.insertPlainText(f'-i {self.FilePathString} {self.AddImageString} -c:v libx264 -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.AddressBroadcastString}')
                    if self.ImagePathString != '' and self.FilterString != '':
                        self.CommandArgument = ['-i', self.FilePathString, '-i', self.ImagePathString, '-filter_complex', self.FilterString , '-threads', '1', '-c:v', 'libx264', '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2','-f', 'rtp_mpegts', self.StreamingAddress]
                else:
                    self.MainScreen.command_box.insertPlainText(f'-i {self.FilePathString} -c:v libx264 -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.AddressBroadcastString}')
                    self.CommandArgument = ['-i', self.FilePathString, '-threads', '1', '-c:v', 'libx264', '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-f', 'rtp_mpegts', self.StreamingAddress]
        else:
            if self.MainScreen.tabWidget.currentIndex() == 2:
                self.MainScreen.command_box.insertPlainText(f'-i {self.FilePathString} -vf {self.TransposeCommand} -c:v libx264 {self.ConverSpeed} -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.CRF} {self.SavingPath}')
                self.CommandArgument = ['-i', self.FilePathString, '-threads', '1', '-vf', self.TransposeCommand, '-c:v', 'libx264', '-preset', self.MainScreen.choose_speed_video.currentText(), '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-crf', str(self.MainScreen.spinBoxCFRVideo.value()), self.SavingPath]
            elif self.MainScreen.tabWidget.currentIndex() == 1:
                self.MainScreen.command_box.insertPlainText(f'-i {self.FilePathString} {self.AddImageString} -c:v libx264 {self.ConverSpeed} -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.CRF} {self.SavingPath}')
                if self.ImagePathString != '' and self.FilterString != '':
                    self.CommandArgument = ['-i', self.FilePathString, '-i', self.ImagePathString, '-filter_complex', self.FilterString , '-threads', '1', '-c:v', 'libx264', '-preset', self.MainScreen.choose_speed_video.currentText(), '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-crf', str(self.MainScreen.spinBoxCFRVideo.value()), self.SavingPath]
            else:
                self.MainScreen.command_box.insertPlainText(f'-i {self.FilePathString} -c:v libx264 {self.ConverSpeed} -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.CRF} {self.SavingPath}')
                self.CommandArgument = ['-i', self.FilePathString, '-threads', '1', '-c:v', 'libx264', '-preset', self.MainScreen.choose_speed_video.currentText(), '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-crf', str(self.MainScreen.spinBoxCFRVideo.value()), self.SavingPath]
            
    def setSavingPath(self):
        if self.OutputFilePathString == '':
            self.SavingPath = '.\\' + self.OutputFullNameWithType 
        else:
            self.SavingPath = self.OutputFilePathString + '\\' + self.OutputFullNameWithType 

    def cancle_chosen_file(self):
        self.MainScreen.ButtonConvert.setEnabled(False)
        self.FilePathString = ''
        self.MainScreen.FilePath.clear()
        self.MainScreen.FileName.clear()
        self.MainScreen.InputThumbnail.clear()
        self.MainScreen.oldThumbnail.clear()
        self.MainScreen.newThumbnail.clear()
        self.MainScreen.command_box.clear()
        self.MainScreen.CancelFileButton.setVisible(False)
        self.MainScreen.CounterClockwise.setEnabled(False)
        self.MainScreen.Clockwise.setEnabled(False)
        self.MainScreen.Horizontal.setEnabled(False)
        self.MainScreen.Vertical.setEnabled(False)
        if os.path.exists(r'.\Temp\\thumbnail.png'):
            os.remove(r'.\Temp\\thumbnail.png')

    def cancle_chosen_image(self):
        self.MainScreen.ImagePath.clear()
        self.MainScreen.ImageThumbnailName.clear()
        self.MainScreen.ImageThumbnail.clear()
        self.MainScreen.command_box.clear()
        self.MainScreen.ButtonConvert.setEnabled(False)
        self.MainScreen.CancelImageButton.setVisible(False)

    