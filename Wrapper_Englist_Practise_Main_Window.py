#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys 
from PyQt4 import QtCore, QtGui

from Englist_Practise_Main_Window import Ui_English_Practise_Main_Widget
from Englist_Practise_Handler import Englist_Practise_Handler

class Wrapper_Englist_Practise_Main_Window(QtGui.QWidget):

    def __init__(self):
        super(Wrapper_Englist_Practise_Main_Window, self).__init__()
        self.ui = Ui_English_Practise_Main_Widget()
        self.ui.setupUi(self)
        self.init_ui()
        self.ui.splitter.setStretchFactor(0,2)
        self.ui.splitter.setStretchFactor(1,4)
        self.view_handler = Englist_Practise_Handler(self, self.ui)
    
    def init_ui(self):
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/window_book_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)


        btn_boundary_size = QtCore.QSize(8,8)
        
        self.init_btn_icon( self.ui.pb_load_test, 
                            "Open English Practise Project",
                            "./images/open-file-icon.png",
                            btn_boundary_size)
        
        self.init_btn_icon( self.ui.pb_start_test,
                            "Start English Practise",
                            "./images/start button.png",
                            btn_boundary_size)

        self.init_btn_icon( self.ui.pb_voice_play,
                            "Play Voice of English Statement",
                            "./images/speaker-icon.png",
                            btn_boundary_size)
        
        #self.ui.pb_voice_play.setEnabled(False)

        self.init_btn_icon( self.ui.pb_hints_chinese,
                            "Chinese Hints",
                            "./images/hints.png",
                            btn_boundary_size)
        
        self.init_btn_icon( self.ui.pb_next_test,
                            "Next Quiz",
                            "./images/Button-Next-icon.png",
                            btn_boundary_size)

        self.init_btn_icon( self.ui.pb_prev_test,
                            "Previous Quiz",
                            "./images/previous.png",
                            btn_boundary_size)
        
        self.init_btn_icon( self.ui.pb_follow_teacher,
                            "Teaching Mode",
                            "./images/teaching_mode.png",
                            btn_boundary_size)

        self.init_btn_icon( self.ui.pb_setting,
                            "Setting",
                            "./images/setting.png",
                            btn_boundary_size)
        
        self.init_btn_icon( self.ui.pb_hint_english,
                            "Hints for English...",
                            "./images/hints_for_english.png",
                            btn_boundary_size)
        
        self.init_btn_icon( self.ui.pb_check_test_ans,
                            "Check your answer!!",
                            "./images/verify.png",
                            btn_boundary_size)

    def init_btn_icon(self, btn, tooltip_str, image_path, btn_boundary_size):
        btn.setText("")
        btn.setToolTip(tooltip_str)
        btn.setIcon(QtGui.QIcon(image_path))
        view_btn_size = btn.size() - btn_boundary_size
        btn.setIconSize(view_btn_size) 


      
     
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("plastique"))  # I Like!
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Windows"))
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("motif"))
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cde"))
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    
    main_win = Wrapper_Englist_Practise_Main_Window()
    main_win.show()
    sys.exit(app.exec_())









