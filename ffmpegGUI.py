from PyQt5 import QtCore, QtGui, QtWidgets
import ffmpeg
import ffmpy
import os
from pathlib import Path
import time
import subprocess
import urllib
import sys

class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Input = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Input.setFont(font)
        self.label_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Input.setObjectName("label_Input")
        self.verticalLayout.addWidget(self.label_Input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_File = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_File.sizePolicy().hasHeightForWidth())
        self.label_File.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_File.setFont(font)
        self.label_File.setObjectName("label_File")
        self.horizontalLayout.addWidget(self.label_File)
        self.FilePath = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FilePath.setFont(font)
        self.FilePath.setObjectName("FilePath")
        self.horizontalLayout.addWidget(self.FilePath)
        self.BrowseButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.BrowseButton.setFont(font)
        self.BrowseButton.setObjectName("BrowseButton")
        self.horizontalLayout.addWidget(self.BrowseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.InputThumbnail = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputThumbnail.sizePolicy().hasHeightForWidth())
        self.InputThumbnail.setSizePolicy(sizePolicy)
        self.InputThumbnail.setObjectName("InputThumbnail")
        self.horizontalLayout_2.addWidget(self.InputThumbnail)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.FileName = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileName.sizePolicy().hasHeightForWidth())
        self.FileName.setSizePolicy(sizePolicy)
        self.FileName.setText("")
        self.FileName.setObjectName("FileName")
        self.horizontalLayout_2.addWidget(self.FileName)
        self.CancelFileButton = QtWidgets.QToolButton(self.frame)
        self.CancelFileButton.setObjectName("CancelFileButton")
        self.horizontalLayout_2.addWidget(self.CancelFileButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_14.addWidget(self.frame)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_8)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_CRF_Video = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_CRF_Video.sizePolicy().hasHeightForWidth())
        self.label_CRF_Video.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_CRF_Video.setFont(font)
        self.label_CRF_Video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CRF_Video.setObjectName("label_CRF_Video")
        self.verticalLayout_6.addWidget(self.label_CRF_Video)
        self.spinBoxCFRVideo = QtWidgets.QSpinBox(self.frame_7)
        self.spinBoxCFRVideo.setProperty("value", 23)
        self.spinBoxCFRVideo.setObjectName("spinBoxCFRVideo")
        self.verticalLayout_6.addWidget(self.spinBoxCFRVideo)
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_8)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_Speed_Video = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Speed_Video.sizePolicy().hasHeightForWidth())
        self.label_Speed_Video.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Speed_Video.setFont(font)
        self.label_Speed_Video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Speed_Video.setObjectName("label_Speed_Video")
        self.verticalLayout_5.addWidget(self.label_Speed_Video)
        self.choose_speed_video = QtWidgets.QComboBox(self.frame_6)
        self.choose_speed_video.setObjectName("choose_speed_video")
        self.verticalLayout_5.addWidget(self.choose_speed_video)
        self.horizontalLayout_8.addWidget(self.frame_6)
        self.frame_14 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.checkBoxBroadcast = QtWidgets.QCheckBox(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxBroadcast.setFont(font)
        self.checkBoxBroadcast.setObjectName("checkBoxBroadcast")
        self.verticalLayout_12.addWidget(self.checkBoxBroadcast)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_broadcast = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_broadcast.sizePolicy().hasHeightForWidth())
        self.label_broadcast.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_broadcast.setFont(font)
        self.label_broadcast.setObjectName("label_broadcast")
        self.horizontalLayout_14.addWidget(self.label_broadcast)
        self.AddressBroadcast = QtWidgets.QLineEdit(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddressBroadcast.sizePolicy().hasHeightForWidth())
        self.AddressBroadcast.setSizePolicy(sizePolicy)
        self.AddressBroadcast.setObjectName("AddressBroadcast")
        self.horizontalLayout_14.addWidget(self.AddressBroadcast)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_8.addWidget(self.frame_14)
        self.verticalLayout_14.addWidget(self.frame_8)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.VideoConversionTab = QtWidgets.QWidget()
        self.VideoConversionTab.setObjectName("VideoConversionTab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.VideoConversionTab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.VideoConversionTab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_Video_Convert_to = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Video_Convert_to.sizePolicy().hasHeightForWidth())
        self.label_Video_Convert_to.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Video_Convert_to.setFont(font)
        self.label_Video_Convert_to.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Video_Convert_to.setObjectName("label_Video_Convert_to")
        self.verticalLayout_4.addWidget(self.label_Video_Convert_to)
        self.choose_file_type_output_video = QtWidgets.QComboBox(self.frame_5)
        self.choose_file_type_output_video.setObjectName("choose_file_type_output_video")
        self.verticalLayout_4.addWidget(self.choose_file_type_output_video)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_7.addWidget(self.frame_5)
        self.tabWidget.addTab(self.VideoConversionTab, "")
        self.WatermarkAddingTab = QtWidgets.QWidget()
        self.WatermarkAddingTab.setObjectName("WatermarkAddingTab")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.WatermarkAddingTab)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_11 = QtWidgets.QFrame(self.WatermarkAddingTab)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_Image = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Image.sizePolicy().hasHeightForWidth())
        self.label_Image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Image.setFont(font)
        self.label_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Image.setObjectName("label_Image")
        self.verticalLayout_11.addWidget(self.label_Image)
        self.frame_15 = QtWidgets.QFrame(self.frame_11)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Image_File = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Image_File.sizePolicy().hasHeightForWidth())
        self.label_Image_File.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Image_File.setFont(font)
        self.label_Image_File.setObjectName("label_Image_File")
        self.horizontalLayout_10.addWidget(self.label_Image_File)
        self.ImagePath = QtWidgets.QLineEdit(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ImagePath.setFont(font)
        self.ImagePath.setObjectName("ImagePath")
        self.horizontalLayout_10.addWidget(self.ImagePath)
        self.BrowseImageButton = QtWidgets.QPushButton(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.BrowseImageButton.setFont(font)
        self.BrowseImageButton.setObjectName("BrowseImageButton")
        self.horizontalLayout_10.addWidget(self.BrowseImageButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ImageThumbnail = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageThumbnail.sizePolicy().hasHeightForWidth())
        self.ImageThumbnail.setSizePolicy(sizePolicy)
        self.ImageThumbnail.setText("")
        self.ImageThumbnail.setObjectName("ImageThumbnail")
        self.horizontalLayout_9.addWidget(self.ImageThumbnail)
        self.ImageThumbnailName = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageThumbnailName.sizePolicy().hasHeightForWidth())
        self.ImageThumbnailName.setSizePolicy(sizePolicy)
        self.ImageThumbnailName.setText("")
        self.ImageThumbnailName.setObjectName("ImageThumbnailName")
        self.horizontalLayout_9.addWidget(self.ImageThumbnailName)
        self.CancelImageButton = QtWidgets.QToolButton(self.frame_15)
        self.CancelImageButton.setObjectName("CancelImageButton")
        self.horizontalLayout_9.addWidget(self.CancelImageButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_11.addWidget(self.frame_15)
        self.horizontalLayout_15.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.WatermarkAddingTab)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_Image_Position = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Image_Position.sizePolicy().hasHeightForWidth())
        self.label_Image_Position.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Image_Position.setFont(font)
        self.label_Image_Position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Image_Position.setObjectName("label_Image_Position")
        self.verticalLayout_13.addWidget(self.label_Image_Position)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_16 = QtWidgets.QFrame(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.TopLeft = QtWidgets.QRadioButton(self.frame_16)
        self.TopLeft.setText("")
        self.TopLeft.setObjectName("TopLeft")
        self.gridLayout.addWidget(self.TopLeft, 0, 0, 1, 1)
        self.CenteredTop = QtWidgets.QRadioButton(self.frame_16)
        self.CenteredTop.setText("")
        self.CenteredTop.setObjectName("CenteredTop")
        self.gridLayout.addWidget(self.CenteredTop, 0, 1, 1, 1)
        self.TopRight = QtWidgets.QRadioButton(self.frame_16)
        self.TopRight.setText("")
        self.TopRight.setObjectName("TopRight")
        self.gridLayout.addWidget(self.TopRight, 0, 2, 1, 1)
        self.CenteredLeft = QtWidgets.QRadioButton(self.frame_16)
        self.CenteredLeft.setText("")
        self.CenteredLeft.setObjectName("CenteredLeft")
        self.gridLayout.addWidget(self.CenteredLeft, 1, 0, 1, 1)
        self.Centered = QtWidgets.QRadioButton(self.frame_16)
        self.Centered.setText("")
        self.Centered.setObjectName("Centered")
        self.gridLayout.addWidget(self.Centered, 1, 1, 1, 1)
        self.CenteredRight = QtWidgets.QRadioButton(self.frame_16)
        self.CenteredRight.setText("")
        self.CenteredRight.setObjectName("CenteredRight")
        self.gridLayout.addWidget(self.CenteredRight, 1, 2, 1, 1)
        self.BottomLeft = QtWidgets.QRadioButton(self.frame_16)
        self.BottomLeft.setText("")
        self.BottomLeft.setObjectName("BottomLeft")
        self.gridLayout.addWidget(self.BottomLeft, 2, 0, 1, 1)
        self.CenteredBottom = QtWidgets.QRadioButton(self.frame_16)
        self.CenteredBottom.setText("")
        self.CenteredBottom.setObjectName("CenteredBottom")
        self.gridLayout.addWidget(self.CenteredBottom, 2, 1, 1, 1)
        self.BottomRight = QtWidgets.QRadioButton(self.frame_16)
        self.BottomRight.setText("")
        self.BottomRight.setObjectName("BottomRight")
        self.gridLayout.addWidget(self.BottomRight, 2, 2, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.verticalLayout_9.addWidget(self.frame_16)
        self.label_Position = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Position.sizePolicy().hasHeightForWidth())
        self.label_Position.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Position.setFont(font)
        self.label_Position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Position.setObjectName("label_Position")
        self.verticalLayout_9.addWidget(self.label_Position)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        self.horizontalLayout_15.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.WatermarkAddingTab)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_Opacity = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Opacity.sizePolicy().hasHeightForWidth())
        self.label_Opacity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Opacity.setFont(font)
        self.label_Opacity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Opacity.setObjectName("label_Opacity")
        self.verticalLayout_8.addWidget(self.label_Opacity)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.OpacityValue = QtWidgets.QLabel(self.frame_13)
        self.OpacityValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OpacityValue.setObjectName("OpacityValue")
        self.horizontalLayout_12.addWidget(self.OpacityValue)
        self.label_percent = QtWidgets.QLabel(self.frame_13)
        self.label_percent.setObjectName("label_percent")
        self.horizontalLayout_12.addWidget(self.label_percent)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.OpacitySlider = QtWidgets.QSlider(self.frame_13)
        self.OpacitySlider.setMaximum(100)
        self.OpacitySlider.setProperty("value", 100)
        self.OpacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.OpacitySlider.setObjectName("OpacitySlider")
        self.verticalLayout_8.addWidget(self.OpacitySlider)
        self.horizontalLayout_15.addWidget(self.frame_13)
        self.tabWidget.addTab(self.WatermarkAddingTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.CounterClockwise = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CounterClockwise.sizePolicy().hasHeightForWidth())
        self.CounterClockwise.setSizePolicy(sizePolicy)
        self.CounterClockwise.setObjectName("CounterClockwise")
        self.horizontalLayout_11.addWidget(self.CounterClockwise)
        self.Horizontal = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Horizontal.sizePolicy().hasHeightForWidth())
        self.Horizontal.setSizePolicy(sizePolicy)
        self.Horizontal.setObjectName("Horizontal")
        self.horizontalLayout_11.addWidget(self.Horizontal)
        self.Vertical = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vertical.sizePolicy().hasHeightForWidth())
        self.Vertical.setSizePolicy(sizePolicy)
        self.Vertical.setObjectName("Vertical")
        self.horizontalLayout_11.addWidget(self.Vertical)
        self.Clockwise = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clockwise.sizePolicy().hasHeightForWidth())
        self.Clockwise.setSizePolicy(sizePolicy)
        self.Clockwise.setObjectName("Clockwise")
        self.horizontalLayout_11.addWidget(self.Clockwise)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.tab)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.oldThumbnail = QtWidgets.QLabel(self.frame_10)
        self.oldThumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.oldThumbnail.setObjectName("oldThumbnail")
        self.horizontalLayout_16.addWidget(self.oldThumbnail)
        self.arrow = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrow.sizePolicy().hasHeightForWidth())
        self.arrow.setSizePolicy(sizePolicy)
        self.arrow.setAlignment(QtCore.Qt.AlignCenter)
        self.arrow.setObjectName("arrow")
        self.horizontalLayout_16.addWidget(self.arrow)
        self.newThumbnail = QtWidgets.QLabel(self.frame_10)
        self.newThumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.newThumbnail.setObjectName("newThumbnail")
        self.horizontalLayout_16.addWidget(self.newThumbnail)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_14.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Output = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Output.setFont(font)
        self.label_Output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Output.setObjectName("label_Output")
        self.verticalLayout_2.addWidget(self.label_Output)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Output_file_name = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Output_file_name.sizePolicy().hasHeightForWidth())
        self.label_Output_file_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Output_file_name.setFont(font)
        self.label_Output_file_name.setObjectName("label_Output_file_name")
        self.horizontalLayout_4.addWidget(self.label_Output_file_name)
        spacerItem9 = QtWidgets.QSpacerItem(28, 19, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.OutPutFileNameEdit = QtWidgets.QLineEdit(self.frame_2)
        self.OutPutFileNameEdit.setObjectName("OutPutFileNameEdit")
        self.horizontalLayout_4.addWidget(self.OutPutFileNameEdit)
        spacerItem10 = QtWidgets.QSpacerItem(98, 19, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SavingFolder = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SavingFolder.sizePolicy().hasHeightForWidth())
        self.SavingFolder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SavingFolder.setFont(font)
        self.SavingFolder.setObjectName("SavingFolder")
        self.horizontalLayout_3.addWidget(self.SavingFolder)
        self.FolderPath = QtWidgets.QLineEdit(self.frame_2)
        self.FolderPath.setObjectName("FolderPath")
        self.horizontalLayout_3.addWidget(self.FolderPath)
        self.BrowseSavingButton = QtWidgets.QPushButton(self.frame_2)
        self.BrowseSavingButton.setObjectName("BrowseSavingButton")
        self.horizontalLayout_3.addWidget(self.BrowseSavingButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_Command = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Command.setFont(font)
        self.label_Command.setObjectName("label_Command")
        self.horizontalLayout_6.addWidget(self.label_Command)
        self.command_box = QtWidgets.QTextEdit(self.frame_3)
        self.command_box.setObjectName("command_box")
        self.horizontalLayout_6.addWidget(self.command_box)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_14.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Progress = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Progress.setFont(font)
        self.label_Progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Progress.setObjectName("label_Progress")
        self.verticalLayout_3.addWidget(self.label_Progress)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.ButtonConvert = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonConvert.setFont(font)
        self.ButtonConvert.setObjectName("ButtonConvert")
        self.horizontalLayout_5.addWidget(self.ButtonConvert)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_14.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.clearData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.BrowseButton.clicked.connect(self.handle_open_file)
        self.BrowseImageButton.clicked.connect(self.handle_open_image)
        self.CancelFileButton.clicked.connect(self.cancle_chosen_file)
        self.CancelFileButton.setVisible(False)
        self.CancelImageButton.setVisible(False)
        self.CancelImageButton.clicked.connect(self.cancle_chosen_image)
        self.BrowseSavingButton.clicked.connect(self.handle_saving_folder)
        self.choose_file_type_output_video.addItems(['Select output file type','.avi','.flv', '.m4a', '.m4b', '.mkv','.mp3', '.mp4', '.mpeg', '.wma', '.wmv'])
        self.choose_speed_video.addItems(['ultrafast', 'superfast', 'veryfast', 'fast', 'medium', 'slow', 'veryslow'])
        self.choose_file_type_output_video.currentIndexChanged.connect(self.fileTypeVideoChange)
        self.choose_speed_video.currentIndexChanged.connect(self.speedChangeVideo)
        self.spinBoxCFRVideo.valueChanged.connect(self.CFRchangeVideo)
        self.ButtonConvert.setEnabled(False)
        self.ButtonConvert.clicked.connect(self.ConvertVideo)
        self.OutPutFileNameEdit.textChanged.connect(self.setOutputFileName)
        self.AddressBroadcast.textChanged.connect(self.setAddressBroadcasting)
        self.Centered.toggled.connect(self.putImageCentered)
        self.CenteredLeft.toggled.connect(self.putImageCenteredLeft)
        self.CenteredRight.toggled.connect(self.putImageCenteredRight)
        self.CenteredTop.toggled.connect(self.putImageCenteredTop)
        self.CenteredBottom.toggled.connect(self.putImageCenteredBottom)
        self.TopLeft.toggled.connect(self.putImageTopLeft)
        self.TopRight.toggled.connect(self.putImageTopRight)
        self.BottomLeft.toggled.connect(self.putImageBottomLeft)
        self.BottomRight.toggled.connect(self.putImageBottomRight)
        self.OpacitySlider.valueChanged['int'].connect(self.changeOpacity)
        self.CounterClockwise.clicked.connect(self.rotateCounterClockwise)
        self.Clockwise.clicked.connect(self.rotateClockwise)
        self.Horizontal.clicked.connect(self.flipHorizontal)
        self.Vertical.clicked.connect(self.flipVertical)
        self.AddressBroadcast.setEnabled(False)
        self.checkBoxBroadcast.stateChanged.connect(self.setBroadcastEnable)
        self.OutputType ='.mp4'
        self.ConverSpeed = '-preset ultrafast'
        self.CRF = '-crf 23'
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        self.OutputFileName = 'F_' + current_time
        self.OutputFullNameWithType = self.OutputFileName + self.OutputType
        self.SavingPath = ''
        self.FilePathString = ''
        self.OutputFilePathString = ''
        self.label_Progress.setVisible(False)
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

    def setAddressBroadcasting(self):
        self.StreamingAddress = self.AddressBroadcast.text()
        # print(self.StreamingAddress)
        self.AddressBroadcastString = '-f rtp_mpegts ' + self.StreamingAddress 
        print(self.AddressBroadcastString)
        self.setCommand()

    def clearData(self):
        self.AddImageString = ''
        self.command_box.clear()
        self.TransposeString = ''
        self.TransposeCommand = ''
        self.OpacityString = ''
        self.OutputType = '.mp4'
        self.SavingPath = ''
        self.OutputFilePathString = ''
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        self.OutputFileName = 'F_' + current_time
        self.OutputFullNameWithType = self.OutputFileName + self.OutputType
        self.RotateDegree = 0
        self.hFlip = 0
        self.vFlip = 0
        self.TransposeString = ''
        self.flipString = ''

    def setBroadcastEnable(self):
        if self.checkBoxBroadcast.isChecked():
            self.AddressBroadcast.setEnabled(True)
        else:
            self.AddressBroadcast.setEnabled(False)
            self.AddressBroadcast.clear()
            self.AddressBroadcastString = ''

    def changeOpacity(self):
        self.OpacityValue.setNum(self.OpacitySlider.value())
        self.setOpacityString()

    def rotateCounterClockwise(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        t = QtGui.QTransform()
        t.rotate(270)
        rotateTmpPic = tmpPic.transformed(t)
        self.TempNewThumbnail = QtGui.QPixmap(rotateTmpPic)
        self.newThumbnail.setPixmap(rotateTmpPic)
        self.RotateDegree += 270
        self.checkRotation()
        
    def rotateClockwise(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        t = QtGui.QTransform()
        t.rotate(90)
        rotateTmpPic = tmpPic.transformed(t)
        self.TempNewThumbnail = QtGui.QPixmap(rotateTmpPic)
        self.newThumbnail.setPixmap(rotateTmpPic)
        self.RotateDegree += 90
        self.checkRotation()

    def flipHorizontal(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        flipTmpPic = tmpPic.transformed(QtGui.QTransform().scale(-1, 1))
        self.TempNewThumbnail = QtGui.QPixmap(flipTmpPic)
        self.newThumbnail.setPixmap(flipTmpPic)
        self.hFlip += 1
        self.checkRotation()

    def flipVertical(self):
        tmpPic = QtGui.QPixmap(self.TempNewThumbnail)
        flipTmpPic = tmpPic.transformed(QtGui.QTransform().scale(1, -1))
        self.TempNewThumbnail = QtGui.QPixmap(flipTmpPic)
        self.newThumbnail.setPixmap(flipTmpPic)
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
        if self.Centered.isChecked():
            print("Centered")
            self.label_Position.setText("Centered")
            self.ImagePosition = 'overlay=(W-w)/2:(H-h)/2'
            self.setAddImageString()
            self.setCommand

    def putImageCenteredLeft(self):
        if self.CenteredLeft.isChecked():
            print("CenteredLeft")
            self.label_Position.setText("Centered Left")
            self.ImagePosition = 'overlay=5:(H-h)/2'
            self.setAddImageString()
            self.setCommand


    def putImageCenteredRight(self):
        if self.CenteredRight.isChecked():
            print("CenteredRight")
            self.label_Position.setText("Centered Right")
            self.ImagePosition = 'overlay=W-w-5:(H-h)/2'
            self.setAddImageString()
            self.setCommand


    def putImageCenteredTop(self):
        if self.CenteredTop.isChecked():
            print("CenteredTop")
            self.label_Position.setText("Centered Top")
            self.ImagePosition = 'overlay=(W-w)/2:5'
            self.setAddImageString()
            self.setCommand


    def putImageCenteredBottom(self):
        if self.CenteredBottom.isChecked():
            print("CenteredBottom")
            self.label_Position.setText("Centered Bottom")
            self.ImagePosition = 'overlay=(W-w)/2:H-h-5'
            self.setAddImageString()
            self.setCommand


    def putImageTopLeft(self):
        if self.TopLeft.isChecked():
            print("TopLeft")
            self.label_Position.setText("Top Left")
            self.ImagePosition = 'overlay=5:5'
            self.setAddImageString()
            self.setCommand


    def putImageTopRight(self):
        if self.TopRight.isChecked():
            print("TopRight")
            self.label_Position.setText("Top Right")
            self.ImagePosition = 'overlay=W-w-5:5'
            self.setAddImageString()
            self.setCommand


    def putImageBottomLeft(self):
        if self.BottomLeft.isChecked():
            print("BottomLeft")
            self.label_Position.setText("Bottom Left")
            self.ImagePosition = 'overlay=5:H-h-5'
            self.setAddImageString()
            self.setCommand


    def putImageBottomRight(self):
        if self.BottomRight.isChecked():
            print("BottomRight")
            self.label_Position.setText("Bottom Right")
            self.ImagePosition = 'overlay=W-w-5:H-h-5'
            self.setAddImageString()
            self.setCommand


    def setAddImageString(self):
        if self.OpacityString != '':
            self.FilterString = self.OpacityString + '[0][fg]' + self.ImagePosition 
        else:
            self.FilterString = self.ImagePosition
        self.AddImageString = '-i ' + self.ImagePathString + ' -filter_complex ' + self.FilterString
        print(self.AddImageString)
        if self.ImagePosition != '':
            self.setCommand()

    def setOpacityString(self):
        self.OpacityString = '[1:v]format=rgba,colorchannelmixer=aa=' + str(float(self.OpacityValue.text()) / float(100)) + '[fg];'
        # print(self.OpacityString)
        self.setAddImageString()
        if self.ImagePosition != '':
            self.setCommand()

    def setOutputFileName(self):
        self.OutputFileName = self.OutPutFileNameEdit.text()
        print(self.OutputFileName)
        if self.OutputFileName == '':
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            self.OutputFileName = 'F_' + current_time
        self.OutputFullNameWithType = self.OutputFileName + self.OutputType
        print(self.OutputFullNameWithType)
        self.setSavingPath()
        self.setCommand()

    def ConvertVideo(self):
        text = self.command_box.toPlainText()
        print(text)
        # print(text.split())
        if text != '':
            self.command_box.clear()
            self.label_Progress.setVisible(True)
            if os.path.exists(self.SavingPath):
                os.remove(self.SavingPath)
            self.Run()
        else: 
            self.ButtonConvert.setEnabled(False)
            self.label_Progress.setText("No Command")
            self.label_Progress.setVisible(True)

    def Run(self):
        try:
            process = QtCore.QProcess(app)
            # process.start(r'F:\ffmpeg\Temp\dummy.bat')
            process.start('ffmpeg', self.CommandArgument)
            if process.waitForStarted():
                self.label_Progress.setVisible(True)
            if process.waitForFinished():
                self.label_Progress.setText("Done")
                time.sleep(3)
                self.label_Progress.setVisible(False)
                self.label_Progress.setText("Please wait ...")
        except KeyboardInterrupt:
            raise

    def CFRchangeVideo(self):
        self.CRF = '-crf ' + str(self.spinBoxCFRVideo.value())
        self.setCommand()
        
    def fileTypeVideoChange(self):
        if self.choose_file_type_output_video.currentText() != 'Select output file type':
            self.OutputType = self.choose_file_type_output_video.currentText()
            self.OutputFullNameWithType = self.OutputFileName + self.OutputType
            print(self.OutputFullNameWithType)
            self.setSavingPath()
            self.setCommand()

    def speedChangeVideo(self):
        self.ConverSpeed = '-preset ' + self.choose_speed_video.currentText()
        self.setCommand()

    def handle_saving_folder(self):
        self.OutputFilePathString = QtWidgets.QFileDialog.getExistingDirectory()
        print(self.OutputFilePathString)
        self.FolderPath.setText(self.OutputFilePathString)
        self.setSavingPath()
        self.setCommand()
        if self.FilePathString != '':
            self.ButtonConvert.setEnabled(True)

    def handle_open_file(self):
        self.ButtonConvert.setEnabled(False)
        self.FilePathString = ''
        self.FilePath.clear()
        self.FileName.clear()
        self.InputThumbnail.clear()
        self.command_box.clear()
        self.CancelFileButton.setVisible(False)
        if os.path.exists(r'.\Temp\\thumbnail.png'):
            os.remove(r'.\Temp\\thumbnail.png')
        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "", "*.3gp *.amv *.avi *.flv *.gif *.mkv *.mp4 *.mpeg *.mpg *.ts *wmv")
        if filename[0] == '':
            return None
        print(filename)
        self.FilePathString = filename[0]
        print(self.FilePathString)
        self.FilePath.setText(self.FilePathString)
        self.FileName.setText("Chosen file: " + Path(self.FilePathString).parts[len(Path(self.FilePathString).parts) - 1])
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
            self.FileName.setText('The file format is not valid. Please select another file')
            return None
        else:
            self.CancelFileButton.setVisible(True)
            self.InputThumbnail.setPixmap(QtGui.QPixmap(r'.\Temp\\thumbnail.png'))
            self.oldThumbnail.setPixmap(QtGui.QPixmap(r'.\Temp\\thumbnail.png'))
            self.newThumbnail.setPixmap(QtGui.QPixmap(r'.\Temp\\thumbnail.png'))
            self.TempNewThumbnail = QtGui.QPixmap(r'.\Temp\\thumbnail.png')
            self.setCommand()
            self.CounterClockwise.setEnabled(True)
            self.Clockwise.setEnabled(True)
            self.Horizontal.setEnabled(True)
            self.Vertical.setEnabled(True)
            self.ButtonConvert.setEnabled(True)

    def handle_open_image(self):
        self.ImagePath.clear()
        self.ImageThumbnailName.clear()
        self.ImageThumbnail.clear()
        self.CancelImageButton.setVisible(False)

        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "*.jpeg *.png")
        if filename[0] == '':
            return None
        self.ImagePathString = filename[0]
        print(self.ImagePathString)
        self.ImagePath.setText(self.ImagePathString)
        self.ImageThumbnailName.setText(Path(self.ImagePathString).parts[len(Path(self.ImagePathString).parts) - 1])
        self.CancelImageButton.setVisible(True)
        pixmap = QtGui.QPixmap(self.ImagePathString)
        self.ImageThumbnail.setPixmap(pixmap.scaledToWidth(100))

    def setCommand(self):
        self.command_box.clear()
        if self.SavingPath == '':
            self.SavingPath = '.\\' + self.OutputFullNameWithType
        if self.checkBoxBroadcast.isChecked():
            if self.AddressBroadcastString != '':
                if self.tabWidget.currentIndex() == 2:
                    self.command_box.insertPlainText(f'-i {self.FilePathString} -vf {self.TransposeCommand} -c:v libx264 -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.AddressBroadcastString}')
                    self.CommandArgument = ['-i', self.FilePathString, '-vf', self.TransposeCommand, '-c:v', 'libx264', '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-f', 'rtp_mpegts', self.StreamingAddress]
                    print(self.CommandArgument)
                elif self.tabWidget.currentIndex() == 1:
                    self.command_box.insertPlainText(f'-i {self.FilePathString} {self.AddImageString} -c:v libx264 -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.AddressBroadcastString}')
                    if self.ImagePathString != '' and self.FilterString != '':
                        self.CommandArgument = ['-i', self.FilePathString, '-i', self.ImagePathString, '-filter_complex', self.FilterString , '-c:v', 'libx264', '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2','-f', 'rtp_mpegts', self.StreamingAddress]
                        print(self.CommandArgument)
                else:
                    self.command_box.insertPlainText(f'-i {self.FilePathString} -c:v libx264 -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.AddressBroadcastString}')
                    print(self.StreamingAddress)
                    self.CommandArgument = ['-i', self.FilePathString, '-c:v', 'libx264', '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-f', 'rtp_mpegts', self.StreamingAddress]
                    print(self.CommandArgument)
        else:
            if self.tabWidget.currentIndex() == 2:
                self.command_box.insertPlainText(f'-i {self.FilePathString} -vf {self.TransposeCommand} -c:v libx264 {self.ConverSpeed} -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.CRF} {self.SavingPath}')
                self.CommandArgument = ['-i', self.FilePathString, '-vf', self.TransposeCommand, '-c:v', 'libx264', '-preset', self.choose_speed_video.currentText(), '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-crf', str(self.spinBoxCFRVideo.value()), self.SavingPath]
                print(self.CommandArgument)
            elif self.tabWidget.currentIndex() == 1:
                self.command_box.insertPlainText(f'-i {self.FilePathString} {self.AddImageString} -c:v libx264 {self.ConverSpeed} -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.CRF} {self.SavingPath}')
                if self.ImagePathString != '' and self.FilterString != '':
                    self.CommandArgument = ['-i', self.FilePathString, '-i', self.ImagePathString, '-filter_complex', self.FilterString , '-c:v', 'libx264', '-preset', self.choose_speed_video.currentText(), '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-crf', str(self.spinBoxCFRVideo.value()), self.SavingPath]
                    print(self.CommandArgument)
            else:
                self.command_box.insertPlainText(f'-i {self.FilePathString} -c:v libx264 {self.ConverSpeed} -b:v 6M -maxrate 6M -bufsize 2M -c:a aac -ac 2 {self.CRF} {self.SavingPath}')
                print(self.StreamingAddress)
                self.CommandArgument = ['-i', self.FilePathString, '-c:v', 'libx264', '-preset', self.choose_speed_video.currentText(), '-b:v', '6M', '-maxrate', '6M', '-bufsize', '2M', '-c:a', 'aac', '-ac', '2', '-crf', str(self.spinBoxCFRVideo.value()), self.SavingPath]
                print(self.CommandArgument)

            
    def setSavingPath(self):
        if self.OutputFilePathString == '':
            self.SavingPath = '.\\' + self.OutputFullNameWithType 
        else:
            self.SavingPath = self.OutputFilePathString + '\\' + self.OutputFullNameWithType 

    def cancle_chosen_file(self):
        self.ButtonConvert.setEnabled(False)
        self.FilePathString = ''
        self.FilePath.clear()
        self.FileName.clear()
        self.InputThumbnail.clear()
        self.oldThumbnail.clear()
        self.newThumbnail.clear()
        self.command_box.clear()
        self.CancelFileButton.setVisible(False)
        self.CounterClockwise.setEnabled(False)
        self.Clockwise.setEnabled(False)
        self.Horizontal.setEnabled(False)
        self.Vertical.setEnabled(False)
        if os.path.exists(r'.\Temp\\thumbnail.png'):
            os.remove(r'.\Temp\\thumbnail.png')

    def cancle_chosen_image(self):
        self.ImagePath.clear()
        self.ImageThumbnailName.clear()
        self.ImageThumbnail.clear()
        self.command_box.clear()
        self.ButtonConvert.setEnabled(False)
        self.CancelImageButton.setVisible(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Video Soft"))
        self.label_Input.setText(_translate("MainWindow", "Input"))
        self.label_File.setText(_translate("MainWindow", "File"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.label_Video_Convert_to.setText(_translate("MainWindow", "Convert to"))
        self.label_Speed_Video.setText(_translate("MainWindow", "Speed"))
        self.label_CRF_Video.setText(_translate("MainWindow", "Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VideoConversionTab), _translate("MainWindow", "Video Conversion"))
        self.label_Image.setText(_translate("MainWindow", "Image"))
        self.label_Image_File.setText(_translate("MainWindow", "File"))
        self.BrowseImageButton.setText(_translate("MainWindow", "Browse"))
        self.label_Image_Position.setText(_translate("MainWindow", "Image position"))
        self.label_Opacity.setText(_translate("MainWindow", "Opacity"))
        self.OpacityValue.setText(_translate("MainWindow", "100"))
        self.label_percent.setText(_translate("MainWindow", "%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WatermarkAddingTab), _translate("MainWindow", "Watermark Adding"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Video Rotation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WatermarkAddingTab), _translate("MainWindow", "Watermark Adding"))
        self.label_Output.setText(_translate("MainWindow", "Output"))
        self.label_Output_file_name.setText(_translate("MainWindow", "File Name"))
        self.SavingFolder.setText(_translate("MainWindow", "Saving Folder"))
        self.BrowseSavingButton.setText(_translate("MainWindow", "Browse"))
        self.label_Command.setText(_translate("MainWindow", "Command"))
        self.label_Progress.setText(_translate("MainWindow", "Please wait ..."))
        self.ButtonConvert.setText(_translate("MainWindow", "Run"))
        self.checkBoxBroadcast.setText(_translate("MainWindow", "Broadcast"))
        self.label_broadcast.setText(_translate("MainWindow", "Address"))
        self.CancelFileButton.setToolTip(_translate("MainWindow", "Cancel file"))
        self.CancelImageButton.setToolTip(_translate("MainWindow", "Cancel image"))
        self.CancelImageButton.setText(_translate("MainWindow", "X"))
        self.CancelFileButton.setText(_translate("MainWindow", "X"))
        self.CounterClockwise.setIcon(QtGui.QIcon(r'.\Temp\counterclockwise.png'))
        self.CounterClockwise.setIconSize(QtCore.QSize(20, 20))
        self.Clockwise.setIcon(QtGui.QIcon(r'.\Temp\clockwise.png'))
        self.Clockwise.setIconSize(QtCore.QSize(20, 20))
        self.Horizontal.setIcon(QtGui.QIcon(r'.\Temp\horizontal.png'))
        self.Horizontal.setIconSize(QtCore.QSize(20, 20))
        self.Vertical.setIcon(QtGui.QIcon(r'.\Temp\vertical.png'))
        self.Vertical.setIconSize(QtCore.QSize(20, 20))
        self.CounterClockwise.setEnabled(False)
        self.Clockwise.setEnabled(False)
        self.Horizontal.setEnabled(False)
        self.Vertical.setEnabled(False)

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = MainWindow()  
        self.ui.setupUi(self)
    
app = QtWidgets.QApplication(sys.argv)
myapp = MainScreen()
myapp.show()   
sys.exit(app.exec_())
