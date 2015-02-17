# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Englist_Practise_Main_Window.ui'
#
# Created: Sun May 19 14:33:08 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_English_Practise_Main_Widget(object):
    def setupUi(self, English_Practise_Main_Widget):
        English_Practise_Main_Widget.setObjectName(_fromUtf8("English_Practise_Main_Widget"))
        English_Practise_Main_Widget.resize(535, 469)
        self.gridLayout_2 = QtGui.QGridLayout(English_Practise_Main_Widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pb_load_test = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_load_test.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_load_test.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_load_test.setObjectName(_fromUtf8("pb_load_test"))
        self.verticalLayout.addWidget(self.pb_load_test)
        self.pb_start_test = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_start_test.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_start_test.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_start_test.setObjectName(_fromUtf8("pb_start_test"))
        self.verticalLayout.addWidget(self.pb_start_test)
        self.pb_hints_chinese = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_hints_chinese.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_hints_chinese.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_hints_chinese.setObjectName(_fromUtf8("pb_hints_chinese"))
        self.verticalLayout.addWidget(self.pb_hints_chinese)
        self.pb_hint_english = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_hint_english.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_hint_english.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_hint_english.setObjectName(_fromUtf8("pb_hint_english"))
        self.verticalLayout.addWidget(self.pb_hint_english)
        self.pb_next_test = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_next_test.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_next_test.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_next_test.setObjectName(_fromUtf8("pb_next_test"))
        self.verticalLayout.addWidget(self.pb_next_test)
        self.pb_prev_test = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_prev_test.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_prev_test.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_prev_test.setObjectName(_fromUtf8("pb_prev_test"))
        self.verticalLayout.addWidget(self.pb_prev_test)
        self.pb_follow_teacher = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_follow_teacher.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_follow_teacher.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_follow_teacher.setObjectName(_fromUtf8("pb_follow_teacher"))
        self.verticalLayout.addWidget(self.pb_follow_teacher)
        self.pb_setting = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_setting.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_setting.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_setting.setObjectName(_fromUtf8("pb_setting"))
        self.verticalLayout.addWidget(self.pb_setting)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 3, 1)
        self.groupBox = QtGui.QGroupBox(English_Practise_Main_Widget)
        self.groupBox.setMinimumSize(QtCore.QSize(371, 431))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.text_edit_for_user_answer = QtGui.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        self.text_edit_for_user_answer.setFont(font)
        self.text_edit_for_user_answer.setObjectName(_fromUtf8("text_edit_for_user_answer"))
        self.text_edit_for_hints = QtGui.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        self.text_edit_for_hints.setFont(font)
        self.text_edit_for_hints.setObjectName(_fromUtf8("text_edit_for_hints"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 3, 1)
        spacerItem = QtGui.QSpacerItem(20, 329, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.pb_check_test_ans = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_check_test_ans.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_check_test_ans.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_check_test_ans.setObjectName(_fromUtf8("pb_check_test_ans"))
        self.gridLayout_2.addWidget(self.pb_check_test_ans, 2, 2, 1, 1)
        self.pb_voice_play = QtGui.QPushButton(English_Practise_Main_Widget)
        self.pb_voice_play.setMinimumSize(QtCore.QSize(48, 48))
        self.pb_voice_play.setMaximumSize(QtCore.QSize(48, 48))
        self.pb_voice_play.setObjectName(_fromUtf8("pb_voice_play"))
        self.gridLayout_2.addWidget(self.pb_voice_play, 1, 2, 1, 1)

        self.retranslateUi(English_Practise_Main_Widget)
        QtCore.QMetaObject.connectSlotsByName(English_Practise_Main_Widget)

    def retranslateUi(self, English_Practise_Main_Widget):
        English_Practise_Main_Widget.setWindowTitle(_translate("English_Practise_Main_Widget", "English Practse Project", None))
        self.pb_load_test.setText(_translate("English_Practise_Main_Widget", "Load", None))
        self.pb_start_test.setText(_translate("English_Practise_Main_Widget", "Start", None))
        self.pb_hints_chinese.setText(_translate("English_Practise_Main_Widget", "Hints", None))
        self.pb_hint_english.setText(_translate("English_Practise_Main_Widget", "HintsE", None))
        self.pb_next_test.setText(_translate("English_Practise_Main_Widget", "Next", None))
        self.pb_prev_test.setText(_translate("English_Practise_Main_Widget", "Prev", None))
        self.pb_follow_teacher.setText(_translate("English_Practise_Main_Widget", "Teacher", None))
        self.pb_setting.setText(_translate("English_Practise_Main_Widget", "Setting", None))
        self.pb_check_test_ans.setText(_translate("English_Practise_Main_Widget", "Check", None))
        self.pb_voice_play.setText(_translate("English_Practise_Main_Widget", "Voice", None))

