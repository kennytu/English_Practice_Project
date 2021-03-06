#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
sys.path.append("./data_module")

from PyQt4 import QtCore, QtGui

#for pyw debug
#QtGui.QMessageBox.warning(None, "EPP Warning", "<b>3<\b>")

from Quizer import Quizer
from Keyword_Highlighter import Keyword_Highlighter

class Englist_Practise_Handler(object):
    
    def __init__(self, parent, view_obj):
        
        super(Englist_Practise_Handler,self).__init__()

        self.parent = parent
        self.view_obj = view_obj
        #self.quizer = Quizer()
        self.quizer = None
        
        self.view_obj.pb_load_test.pressed.connect(self.handle_pb_load_test)
        self.view_obj.pb_start_test.pressed.connect(self.handle_pb_start_test)
        self.view_obj.pb_voice_play.pressed.connect(self.handle_pb_voice_play)
        self.view_obj.pb_hints_chinese.pressed.connect(self.handle_pb_hints_chinese)
        self.view_obj.pb_next_test.pressed.connect(self.handle_pb_next_test)
        self.view_obj.pb_prev_test.pressed.connect(self.handle_pb_prev_test)
        self.view_obj.pb_follow_teacher.pressed.connect(self.handle_pb_follow_teacher)
        self.view_obj.pb_setting.pressed.connect(self.handle_pb_setting)
        self.view_obj.pb_hint_english.pressed.connect(self.handle_pb_hint_english)
        self.view_obj.pb_check_test_ans.pressed.connect(self.handle_pb_check_test_ans)
        
        self.view_obj.text_edit_for_user_answer.textChanged.connect(self.process_user_input_window)

        #self.load_new_file_and_start_flag = False
        #self.send_msg_to_hint_window("GUIDE", "中文按鍵KEY測試")
    
        self.current_quiz = None
        self.current_audio_player = None
        
        self.timer = QtCore.QTimer(self.parent)
        self.timer.timeout.connect(self.enable_pb_voice_palay)
        self.reset_pb_enabled_status("INIT")

        
        self.string_guide_hint = ""
        self.string_chinese_hint = ""
        self.string_english_hint = ""
        self.string_ans_hint = ""
    

        self.flag_chinese_hint = False
        self.flag_english_hint = False
        self.flag_ans_hint = False
        

        #Teacher Mode
        self.teacher_timer = QtCore.QTimer(self.parent)
        self.teacher_timer.timeout.connect(self.teacher_routine)
        self.teacher_flag = False
        self.teacher_delay_time = 1
    
        #short cut setting
        self.set_short_cut()

    def set_short_cut(self):
        self.sh_cut_audio = QtGui.QShortcut(self.parent)
        self.sh_cut_audio.setKey("Ctrl+P") 
        self.sh_cut_audio.activated.connect(self.handle_pb_voice_play)
        
        self.sh_cut_next = QtGui.QShortcut(self.parent)
        self.sh_cut_next.setKey("Ctrl+]")
        self.sh_cut_next.activated.connect(self.handle_pb_next_test)

        self.sh_cut_prev = QtGui.QShortcut(self.parent)
        self.sh_cut_prev.setKey("Ctrl+[")
        self.sh_cut_prev.activated.connect(self.handle_pb_prev_test)
    
        self.sh_cut_chi = QtGui.QShortcut(self.parent)
        self.sh_cut_chi.setKey("Ctrl+U")
        self.sh_cut_chi.activated.connect(self.handle_pb_hints_chinese)

        self.sh_cut_eng = QtGui.QShortcut(self.parent)
        self.sh_cut_eng.setKey("Ctrl+I")
        self.sh_cut_eng.activated.connect(self.handle_pb_hint_english)
    
        self.sh_cut_ans = QtGui.QShortcut(self.parent)
        self.sh_cut_ans.setKey("Ctrl+O")
        self.sh_cut_ans.activated.connect(self.handle_pb_check_test_ans)

    def reset_pb_enabled_status(self, status = "INIT"):
        if status == "INIT":
            self.view_obj.pb_load_test.setEnabled(True)
            self.view_obj.pb_start_test.setEnabled(False)
            self.view_obj.pb_voice_play.setEnabled(False)
            self.view_obj.pb_hints_chinese.setEnabled(False)
            self.view_obj.pb_next_test.setEnabled(False)
            self.view_obj.pb_prev_test.setEnabled(False)
            self.view_obj.pb_follow_teacher.setEnabled(False)
            self.view_obj.pb_setting.setEnabled(False)
            self.view_obj.pb_hint_english.setEnabled(False)
            self.view_obj.pb_check_test_ans.setEnabled(False)
        elif status == "LOAD":
            self.view_obj.pb_load_test.setEnabled(True)
            self.view_obj.pb_start_test.setEnabled(True)
            self.view_obj.pb_voice_play.setEnabled(False)
            self.view_obj.pb_hints_chinese.setEnabled(False)
            self.view_obj.pb_next_test.setEnabled(False)
            self.view_obj.pb_prev_test.setEnabled(False)
            self.view_obj.pb_follow_teacher.setEnabled(False)
            self.view_obj.pb_setting.setEnabled(False)
            self.view_obj.pb_hint_english.setEnabled(False)
            self.view_obj.pb_check_test_ans.setEnabled(False)
        elif status == "START":
            self.view_obj.pb_load_test.setEnabled(True)
            self.view_obj.pb_start_test.setEnabled(False)
            self.view_obj.pb_voice_play.setEnabled(True)
            self.view_obj.pb_hints_chinese.setEnabled(True)
            self.view_obj.pb_next_test.setEnabled(True)
            self.view_obj.pb_prev_test.setEnabled(True)
            self.view_obj.pb_follow_teacher.setEnabled(True)
            self.view_obj.pb_setting.setEnabled(True)
            self.view_obj.pb_hint_english.setEnabled(True)
            self.view_obj.pb_check_test_ans.setEnabled(True)

    def handle_pb_load_test(self):
        print ("PB LOAD TEST!")
        
        prevoius_user_path = ''
        try:
            previous_path_file = open("./previous_user_path.txt", "r")
            prevoius_user_path = previous_path_file.readline()
        except IOError as err:
            print "previous information for file doesn't exist "
            prevoius_user_path = ''

        if prevoius_user_path != '':
            previous_path_file.close()
            print("previous user path:")
            print(prevoius_user_path) 
            #check path is exist or not
            if os.path.exists(prevoius_user_path) is False:
                prevoius_user_path = ''

        files_types = "English Practise Machine Format(*.txt);; (*.*)"
        #file_name = QtGui.QFileDialog.getOpenFileNames(self.parent, 'Select one file to open', '', files_types)
        file_name = QtGui.QFileDialog.getOpenFileNames(self.parent, 'Select one file to open', prevoius_user_path, files_types)
        print(file_name)
        

        if file_name == []:
            print ("NO FILE SELECT!")
            return
        
        previous_path_file = open("./previous_user_path.txt", "w")
        previous_path_file.write(file_name[0])
        previous_path_file.close()
        
        self.quizer = Quizer()
        #print (file_name[0])
        print (os.path.basename(str(file_name[0])))
        print (os.path.dirname(str(file_name[0])))
        self.quizer.load_english_project(file_name[0])
        #self.load_new_file_and_start_flag = True
        
        self.reset_all_hint_string_and_flag()
        self.reset_all_user_input_window()
        

        self.reset_pb_enabled_status("LOAD")
        self.send_msg_to_hint_window("GUIDE","按下Start就可以開始嚕!")
        
    def handle_pb_start_test(self):
        print ("PB START!")
        self.current_quiz = self.quizer.get_head_quiz()
        self.reset_pb_enabled_status("START")
        msg = "Please Press Audio Button to Play Sound! \n"
        msg += self.get_current_quiz_total_and_right_word_str()

        self.send_msg_to_hint_window("GUIDE", msg)
        self.reset_all_user_input_window()
        self.set_user_answer_keyword_highlight() 
        
    def handle_pb_voice_play(self):
        print ("PB VOICE PLAY")
        self.current_audio_player =  self.current_quiz.get_audio_player()
        self.view_obj.pb_voice_play.setEnabled(False)
        mp3_time = None
        mp3_time = self.current_quiz.get_mp3_track_time()
        if mp3_time != None:
            self.current_audio_player.play(mp3_time[0],mp3_time[1])
            self.timer.start(mp3_time[2] + 100)
        else:
            self.current_audio_player.play()
            self.timer.start(self.current_audio_player.seconds()*1000 + 200)
        
        msg = self.get_current_quiz_total_and_right_word_str()
        self.send_msg_to_hint_window("GUIDE", msg)
        
        """
        print ("PB VOICE PLAY")
        self.current_audio_player =  self.current_quiz.get_audio_player()
        self.view_obj.pb_voice_play.setEnabled(False)
        self.current_audio_player.play()
        mp3_time = self.current_audio_player.seconds()+0.2
        self.timer.start(mp3_time*1000)
        
        msg = self.get_current_quiz_total_and_right_word_str()
        self.send_msg_to_hint_window("GUIDE", msg)
        """
    def handle_pb_hints_chinese(self):
        print ("PB HINTS CHINESE")
        self.flag_chinese_hint = not self.flag_chinese_hint
        self.send_msg_to_hint_window("CHINESE", self.current_quiz.get_chinese_statement())

    def handle_pb_next_test(self):
        print ("PB NEXT TEST")
        
        self.enable_pb_voice_palay()
        
        self.reset_all_hint_string_and_flag()
        self.current_quiz = self.quizer.get_next_quiz()
        
        msg = "Please Press Audio Button to Play Sound! \n"
        msg += self.get_current_quiz_total_and_right_word_str()
        self.send_msg_to_hint_window("GUIDE", msg)
        
        self.reset_all_user_input_window()
        self.set_user_answer_keyword_highlight() 
        
    def handle_pb_prev_test(self):
        print ("PB PREV TEST")
        self.enable_pb_voice_palay()
        self.reset_all_hint_string_and_flag()
        self.current_quiz = self.quizer.get_previous_quiz()
        
        msg = "Please Press Audio Button to Play Sound! \n"
        msg += self.get_current_quiz_total_and_right_word_str()
        self.send_msg_to_hint_window("GUIDE", msg)
        
        self.reset_all_user_input_window()
        self.set_user_answer_keyword_highlight() 

    def handle_pb_follow_teacher(self):
        print ("PB FOLLOW TEACHER")
        if self.teacher_flag is False:
            self.teacher_flag = True
            self.view_obj.text_edit_for_user_answer.setEnabled(False)
            self.teacher_hint_string()
            self.current_audio_player =  self.current_quiz.get_audio_player()
            mp3_time = self.current_quiz.get_mp3_track_time()
            if mp3_time != None:
                self.current_audio_player.play(mp3_time[0],mp3_time[1])
                self.teacher_timer.start(mp3_time[2]+(500*self.teacher_delay_time))
            else:
                self.current_audio_player.play()
                self.teacher_timer.start(self.current_audio_player.seconds()*1000 + (500*self.teacher_delay_time))
            
            #self.current_audio_player.play()
            #mp3_time = self.current_audio_player.seconds() + self.teacher_delay_time
            #self.teacher_timer.start(mp3_time * 1000)
        
        elif self.teacher_flag is True:
            self.teacher_flag = False
            self.view_obj.text_edit_for_user_answer.setEnabled(True)
            if self.teacher_timer.isActive() is True:
                self.teacher_timer.stop()
                self.view_obj.text_edit_for_hints.setText("")
                self.current_audio_player.stop()


    def handle_pb_setting(self):
        print ("PB SETTING")
    
    def handle_pb_hint_english(self):
        print ("PB HINT ENGLISH")
        #self.flag_english_hint = True
        self.flag_english_hint = not self.flag_english_hint
        print("self.flag_english_hint:")
        print(self.flag_english_hint)
        self.send_msg_to_hint_window("ENGLISH", self.current_quiz.get_hint_statement())

    def handle_pb_check_test_ans(self):
        print ("PB CHECK TEST ANS")
        user_msg = self.view_obj.text_edit_for_user_answer.toPlainText()
        ans = self.current_quiz.is_correct_english(str(user_msg))
        
        #check user englishe sentence
        msg = self.get_current_quiz_total_and_right_word_str()
        self.send_msg_to_hint_window("GUIDE", msg)

        self.send_msg_to_hint_window("ENGLISH", self.current_quiz.get_hint_statement())
        
        self.flag_ans_hint = True
        if ans == "YES":
            #self.send_msg_to_hint_window("ANS", "RIGHT ANSWER !!! GO NEXT QUIZ !")
            #QtGui.QApplication.beep()
            self.handle_pb_next_test()
        else:
            result_msg = "WRONG!\n"
            result_msg += "Solution is:\n%s"%self.current_quiz.get_english_statement()
            self.send_msg_to_hint_window("ANS", result_msg)
            self.flag_ans_hint = False

    def enable_pb_voice_palay(self):
        if self.timer.isActive() is True:
            self.timer.stop()
            self.view_obj.pb_voice_play.setEnabled(True)
            self.current_audio_player.stop()

    def reset_all_hint_string_and_flag(self):
        self.string_guide_hint = ""
        self.string_chinese_hint = ""
        self.string_english_hint = ""
        self.string_ans_hint = ""

        self.flag_chinese_hint = False
        self.flag_english_hint = False
        self.flag_ans_hint = False
        
        self.view_obj.text_edit_for_hints.setText("")
    
    def reset_all_user_input_window(self):
        self.view_obj.text_edit_for_user_answer.setText("")

    def get_current_quiz_total_and_right_word_str(self):
        
        quiz_pid = self.current_quiz.get_id()
        total_num = self.current_quiz.get_total_word_number()
        right_num = self.current_quiz.get_right_now_correct_word_number()

        return "%s: This sentence has %d words, you got %d words"%(quiz_pid,total_num, right_num)
        #return "This sentence has %d words, you got %d words"%(total_num, right_num)
    
    def set_user_answer_keyword_highlight(self):
       
        if self.current_quiz != None:
            user_edit_text =  self.view_obj.text_edit_for_user_answer
            english_str = self.current_quiz.get_english_statement()
         
            print(user_edit_text)
            print (english_str)
            
            highlight = Keyword_Highlighter(user_edit_text, english_str) 
    
    def send_msg_to_hint_window(self, msg_type=None, msg=""):

        total_msg_list = []
        
        if msg_type == "GUIDE":
            self.string_guide_hint = msg

        if msg_type == "CHINESE" and self.flag_chinese_hint is True:
            self.string_chinese_hint = "Chinese Hint : \n" + msg
            #self.string_chinese_hint = msg

        elif msg_type == "ENGLISH" and self.flag_english_hint is True:
            self.string_english_hint = "English Hint : \n" + msg

        elif msg_type == "ANS" and self.flag_ans_hint is True:
            self.string_ans_hint = msg
        
        if self.string_guide_hint != "":
            total_msg_list.append(self.string_guide_hint)
        
        if self.string_chinese_hint != "" and self.flag_chinese_hint is True:
            total_msg_list.append(self.string_chinese_hint)
        
        if self.string_english_hint != "" and self.flag_english_hint:
            total_msg_list.append(self.string_english_hint)
        
        if self.string_ans_hint != "":
            total_msg_list.append(self.string_ans_hint)
        
        total_msg = "\n\n".join(total_msg_list)
        self.view_obj.text_edit_for_hints.setText(QtCore.QString.fromUtf8(total_msg))

    
    def process_user_input_window(self):
        
        if self.current_quiz is None:
            print("CURRENT QUIZ IS NONE!!!")
            return

        user_msg = self.view_obj.text_edit_for_user_answer.toPlainText()
        
        ans = self.current_quiz.is_correct_english(str(user_msg))
      
        msg = self.get_current_quiz_total_and_right_word_str()
       
        self.send_msg_to_hint_window("GUIDE", msg)

        self.send_msg_to_hint_window("ENGLISH", self.current_quiz.get_hint_statement())
        
        if ans == "YES":
            self.flag_ans_hint = True
            self.send_msg_to_hint_window("ANS", "RIGHT ANSWER !!! GO NEXT QUIZ !")
            QtGui.QApplication.beep()
        else:
            self.send_msg_to_hint_window("ANS", "")
            self.flag_ans_hint = False

    def teacher_routine(self): 
        self.current_audio_player.stop()
        self.current_quiz = self.quizer.get_next_quiz()
        self.teacher_hint_string()
        self.current_audio_player =  self.current_quiz.get_audio_player()
        mp3_time = self.current_quiz.get_mp3_track_time()
        if mp3_time != None:
            self.current_audio_player.play(mp3_time[0],mp3_time[1])
            self.teacher_timer.setInterval(mp3_time[2]+(500*self.teacher_delay_time))
        else:
            self.current_audio_player.play()
            self.teacher_timer.setInterval(self.current_audio_player.seconds()*1000 + (500*self.teacher_delay_time))
        
         
    def teacher_hint_string(self):
        self.view_obj.text_edit_for_hints.setText("")
        
        tmp_list = []
        tmp_list.append(str(self.current_quiz.get_id()))
        tmp_list.append(self.current_quiz.get_chinese_statement())
        tmp_list.append(self.current_quiz.get_english_statement())
        
        tmp_str = "\n\n".join(tmp_list)

        self.view_obj.text_edit_for_hints.setText(tmp_str)










