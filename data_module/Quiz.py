#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import urllib2
import time
import mp3play
import math
import random

class Quiz(object):
    
    STRIP_STR = "\"',!.?;"

    def __init__(self, pid, 
                       eng_statement, 
                       che_statement, 
                       book_name,
                       voice_file,
                       voice_start=None,
                       voice_end=None,
                       is_tts=False,
                       dir_name=None):
        
        super(Quiz, self).__init__()
        
        self.pid = pid
        self.eng_statement = eng_statement
        self.eng_statement_for_slice = eng_statement
        self.book_name = book_name
        self.voice_file = voice_file
        self.voice_start = voice_start
        self.voice_end = voice_end
        self.is_tts = False if is_tts == "NO" else True
        self.dir_name = dir_name

        self.total_correct_word_number = 0 
        self.right_now_correct_word_number = 0
        
  
        self.eng_statement = self.eng_statement.replace("#","\n")

        #the english statement will be SPLIT and then strpit,
        #each word will be save to this variable
        #for example
        # I, am, Kenny. will be split to
        # 1: I, 2: am, 3: Kenny.
        # then strip result: [ I am Kenny ]
        self.eng_each_word_list = []
        
        #temporary save user word when update is_correct_english
        self.right_now_user_eng_each_word_list = []

        #chinese statement
        self.che_statement = che_statement.replace("#","\n")
        #self.che_statement = che_statement
        

        self.private_process_english_statement()
        
        self.tmp_hint_word_list = None
        self.debug()

    def debug(self):
        print("==>pid: ", self.pid)
        print("==>eng_statement: ", self.eng_statement)
        print("==>book_name: ", self.book_name)
        print("==>voice_file: ", self.voice_file)
        print("==>voice_start:", self.voice_start)
        print("==>voice_end: ", self.voice_end)
        print("==>is_tts: ", self.is_tts)
        print("==>dir_name: ", self.dir_name)

    def private_process_english_statement(self):
        
        tmp_list = self.eng_statement.split()
        self.eng_each_word_list = [ item.strip(Quiz.STRIP_STR) for item in tmp_list ]
        
        self.total_correct_word_number = len(self.eng_each_word_list)
        #print (self.eng_each_word_list)
   
    def get_id(self):
        return self.pid

    def get_english_statement(self):
        return self.eng_statement
    
    def get_chinese_statement(self):
        return self.che_statement


    def is_correct_english(self, user_eng_statement):
        
        ret = "YES"

        tmp_list = user_eng_statement.split()

        self.right_now_user_eng_each_word_list = \
                [ item.strip(Quiz.STRIP_STR) for item in tmp_list ]
        

        self.right_now_correct_word_number = 0
        
        i_min = min(len(self.right_now_user_eng_each_word_list), self.total_correct_word_number)
        
        if i_min <= 0:
            return "NO"

        for ix in range(0, i_min):
            if self.right_now_user_eng_each_word_list[ix].lower() == self.eng_each_word_list[ix].lower():
                self.right_now_correct_word_number += 1
            else :
                ret = "NO"
                
        """
        #enumerate index always from 0 start
        for index, word in enumerate(self.right_now_user_eng_each_word_list):
            if index >= self.total_correct_word_number:
                print("user input length large than correct answer!, break")
                break

            if word.lower() == self.eng_each_word_list[index].lower():
                self.right_now_correct_word_number +=1
            else :
                ret = "NO"
        """

        if self.right_now_correct_word_number != self.total_correct_word_number:
            return "NO"
        
        return "YES"
    
    def get_right_now_correct_word_number(self):
            return self.right_now_correct_word_number

    def get_total_word_number(self):
            return self.total_correct_word_number
    
    def get_hint_statement(self):
        
        tmp = []
        #print(self.right_now_user_eng_each_word_list) 
        for ix in range(0, self.total_correct_word_number):
            #print(ix) 
            #print(" " + self.right_now_user_eng_each_word_list[ix].lower())
            #print(" " + self.eng_each_word_list[ix].lower())
            #if ix < self.right_now_correct_word_number: 
            if ix < len(self.right_now_user_eng_each_word_list):
                if self.right_now_user_eng_each_word_list[ix].lower() == self.eng_each_word_list[ix].lower():
                    tmp.append(self.eng_each_word_list[ix])
                else :
                    if self.tmp_hint_word_list != None:
                        tmp.append(self.tmp_hint_word_list[ix])
                    else:
                        tmp.append(self.private_get_hint_word(self.eng_each_word_list[ix]))
            else :
                if self.tmp_hint_word_list != None:
                    tmp.append(self.tmp_hint_word_list[ix])
                else:
                    tmp.append(self.private_get_hint_word(self.eng_each_word_list[ix]))
        
        if self.tmp_hint_word_list == None:
            self.tmp_hint_word_list = tmp
            
        return " ".join(tmp)
    
    def private_get_hint_word(self, word):
        hint_word = word
        
        #if show_word_flag is 1:
        #    return hint_word
        #else:
        if len(hint_word) <= 2:
            return "_" * len(hint_word)
        else :
            show_word_flag = random.randint(0,1)
            if show_word_flag is 1:
                return hint_word
                
            tmp_str_list = []
            for index, letter in enumerate(word):
                if index == 0:
                    tmp_str_list.append(letter)
                else :
                    tmp_str_list.append("_")
            return "".join(tmp_str_list)
    
    def prepare_audio_file(self):
        """
            OK, first, we get the voice name from setting
            then, we check the is_tts file is true or False
            if is_tts is false, then we just get the fully voice path
            else, we need to generate the tts file and save to tts folder for next use.
        """
        dir_name = "." if self.dir_name is None else self.dir_name

        fully_voice_file_name = None

        #fully_voice_level_list = [dir_name, self.book_name, self.voice_file] if self.is_tts is False else [dir_name, self.book_name, "tts_voice", self.voice_file]

        if not self.is_tts:
            fully_voice_level_list = [dir_name, self.book_name, self.voice_file]
        else:
            fully_voice_level_list = [dir_name, self.book_name, "tts_voice", self.voice_file]
            #create the tts folder
            tmp_tts_path = os.path.sep.join(fully_voice_level_list[:-1])
            if os.path.exists(tmp_tts_path) is False:
                #create
                os.mkdir(tmp_tts_path)

        fully_voice_file_name = os.path.sep.join(fully_voice_level_list)
        
        print("xxxx===> fully_voice_file_name:")
        print(fully_voice_file_name)
        #check the file exist or not
        if not os.path.exists(fully_voice_file_name):
            # need create the tts voice and save to the file
            self._create_tts_voice(fully_voice_file_name)
        
        return fully_voice_file_name

    def _create_tts_voice(self, file_name):
        #check eng statment has ## mark or not
            eng_slice_list = [item.strip() for item in self.eng_statement_for_slice.split("##")]
            slice_count = len(eng_slice_list)

            if slice_count == 1:
                self.tts_from_google(file_name, eng_slice_list[0])
            else :
                tmp_list = []
                for ix in range(0, slice_count):
                    tmp_name = "tts_voice" + "-tmp-" +str(ix) + ".mp3"
                    self.tts_from_google(tmp_name, eng_slice_list[ix])
                    tmp_list.append(tmp_name)
                
                t1 = [ "\""+ item+"\"/B" for item in tmp_list]
                t2 = " + ".join(t1)
                t3 = "COPY %s \"%s\""%(t2, file_name)
                os.system(t3) # merge many voice files to one file
            
                #clean the tmp_voice-tmp-ix.mp3 files    
                for ix in tmp_list:
                    cmd = "del \"%s\""%ix
                    os.system(cmd) 

    
    def tts_from_google(self, tts_voice_file_name, eng):
            print("Connect to Google TTS Server")
            tmp_list = eng.split()
            tmp_str = "+".join(tmp_list)
            url = "http://translate.google.com/translate_tts?tl=en&q=" + tmp_str
            print url
            request = urllib2.Request(url)
            request.add_header('User-agent', 'Mozilla/5.0')
            opener = urllib2.build_opener()
            
            file_error_flag = False
            f = open(tts_voice_file_name, "wb")
            
            try :
                f.write(opener.open(request).read())
            except urllib2.URLError as err :
                print err
                file_error_flag = True
            
            f.close()
            
            if file_error_flag is True:
                os.remove(tts_voice_file_name) 

    def play_audio(self):
        
        mp3_file_name = self.prepare_audio_file()

        if os.path.exists(mp3_file_name) is True: 
            print("Play Voice!!")
            clip = mp3play.load(mp3_file_name)
            clip.play()
            time.sleep(min(30, clip.seconds()+0.5))
            clip.stop()
    
    def get_audio_player(self):
        mp3_file_name = self.prepare_audio_file()

        if os.path.exists(mp3_file_name) is True: 
            print("Play Voice!!")
            clip = mp3play.load(mp3_file_name)
            return clip
            #clip.play()
            #time.sleep(min(30, clip.seconds()+0.5))
            #clip.stop()

        return None
    
    def get_mp3_track_time(self):
        if self.voice_start is None or self.voice_end is None:
            return None
        else:
            print "self.voice_start:", self.voice_start
            print "self.voice_end", self.voice_end
            m_start = int(self.voice_start)
            m_end = int(self.voice_end)
            
            dur_time = math.ceil(m_end - m_start)   #ms
            #print("m_start:%d\n"%(m_start))
            #print("m_end  :%d\n"%(m_end))
            #print("dur_time:%d\n"%(dur_time))
            
            return (m_start, m_end, dur_time)
    
    
if __name__ == "__main__" :

    vs = 5680
    ve = 9589
    clip = mp3play.load("./train_basic_english_30min_everyday/01-03.mp3")
    clip.play(vs, ve)
    time.sleep(((ve-vs)/1000)+1)

    """
    test_quiz = Quiz("03-06", 
                     "I was wondering, if you help me this afternoon", 
                     "我在想說你下午是否可以幫我一個忙?", 
                     "kenny_123")
    print (test_quiz.get_english_statement())
    print (test_quiz.get_chinese_statement())

    print (test_quiz.is_correct_english("I am kenny, Who are ff"))
    print (test_quiz.get_right_now_correct_word_number())
    print (test_quiz.get_hint_statement())
    
    test_quiz.play_audio()
    """




