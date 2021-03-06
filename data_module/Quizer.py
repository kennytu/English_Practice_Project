#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import codecs

# for pyw debug use
#from PyQt4 import QtCore, QtGui
#QtGui.QMessageBox.warning(None, "EPP Warning", "<b>Q5<\b>")

from Quiz import Quiz

class Quizer(object):
    
    def __init__(self):
        super(Quizer, self).__init__()
        
        self.quiz_list = []
        self.quiz_list_index = 0
        self.dir_name = None 

    def load_english_project(self, file_name):
        
        self.quiz_list = []
        self.quiz_list_index = 0
        self.dir_name = None 

        self.dir_name = os.path.dirname(str(file_name))

        project_file = self.check_and_open_utf8_file(file_name)
        
        
        pf_bs = project_file.read()
        lines = pf_bs.split("\r\n")

        self.process_file(lines)
        #for ix in lines:
        #    print ix
        
        project_file.close()
    
    def process_file(self, lines):
        
        #pid = None
        #eng_s = None
        #chi_s = None
        #book_s = None
        tmp_list = []

        for line in lines:
            #ignore empty line
            if not line.strip():
                continue
        
            line = line.strip()
            
            if line.startswith("#"): #it's comment
                continue

            if line.upper().startswith("P:") is True:
                t = line[2:].strip()
                tmp_list.append(t)
                #print t

            elif line.upper().startswith("E:") is True:
                t = line[2:].strip()
                tmp_list.append(t)
                #print t
                
            elif line.upper().startswith("C:") is True:
                t = line[2:].strip()
                tmp_list.append(t)
                #print t
                
            elif line.upper().startswith("B:") is True:
                t = line[2:].strip()
                tmp_list.append(t)
                #print t

            elif line.upper().startswith("V:") is True: #voice start
                t = line[2:].strip()
                if t == "" or t is None:
                    tmp_list.append(None)
                else:
                    tmp_list.append(t)
            
            elif line.upper().startswith("VS:") is True: #voice start
                t = line[3:].strip()
                if t == "" or t is None:
                    tmp_list.append(None)
                else:
                    tmp_list.append(t)
                #print t
                
            elif line.upper().startswith("VE:") is True: #voice end
                t = line[3:].strip()
                if t == "" or t is None:
                    tmp_list.append(None)
                else:
                    tmp_list.append(t)
                #print t

            elif line.upper().startswith("TTS:") is True: #voice end
                t = line[4:].strip()
                if t == "" or t is None:
                    tmp_list.append(None)
                else:
                    tmp_list.append(t)
                #print t
            
        print ("tmp list len:%d"%(len(tmp_list)))
        
        
        for ix in range(0, len(tmp_list), 8):
            #print "----%s---"%ix
            x1 = tmp_list[ix]       #P
            x2 = tmp_list[ix+1]     #E
            x3 = tmp_list[ix+2]     #C
            x4 = tmp_list[ix+3]     #B
            x5 = tmp_list[ix+4]     #V
            x6 = tmp_list[ix+5]     #VS
            x7 = tmp_list[ix+6]     #VE
            x8 = tmp_list[ix+7]     #TTS
           
            tmp_quiz = Quiz(x1, x2, x3, x4, x5, x6, x7, x8, self.dir_name)
            self.quiz_list.append(tmp_quiz)
            
        
        
        #if it's pyw window, don't print this
        #print self.quiz_list[0].get_english_statement()
        #print self.quiz_list[0].get_chinese_statement()
       
        
        
        """ 
        self.quiz_list[0].play_audio()
        self.quiz_list[1].play_audio()
        self.quiz_list[2].play_audio()
        self.quiz_list[3].play_audio()
        """
    
    def get_head_quiz(self):
        return self.quiz_list[0]

    def get_next_quiz(self):

        self.quiz_list_index = (self.quiz_list_index+1) % len(self.quiz_list)
        quiz = self.quiz_list[self.quiz_list_index]
        return quiz

    def get_previous_quiz(self):
        self.quiz_list_index = (self.quiz_list_index-1) % len(self.quiz_list)
        quiz = self.quiz_list[self.quiz_list_index]
        return quiz

    def check_and_open_utf8_file(self,filename, mode='r', encoding = 'utf-8'):
        """
        1. check the file name is a file type
        2. read this file by "binary" mode and get the 4 bytes from head of file
        3. close this file
        4. check utf-8 type
        5. open this file again, but this time it used codecs object to open
        6. and open parameter is read only, and string format(not binary)
        7. if this file has bom, read 1 byte and return this file desp
        6. if this file doesn't has bom, just return
        """
        
        hasBOM = False
        if os.path.isfile(filename):
            #print("file name:{}".format(filename))
            f = open(filename,'rb')
            header = f.read(4)
            f.close()
            
            # Don't change this to a map, because it is ordered
            
            encodings = [ ( codecs.BOM_UTF32, 'utf-32' ),
                ( codecs.BOM_UTF16, 'utf-16' ),
                ( codecs.BOM_UTF8, 'utf-8' ) ]
            
            for h, e in encodings:
                if header.startswith(h):
                    encoding = e
                    hasBOM = True
                    break
            
        f = codecs.open(filename,mode,encoding)
        # Eat the byte order mark
        if hasBOM:
            print("Has Born")
            f.read(1)
        return f
    




if __name__ == "__main__":
    
    my_quizer = Quizer()
    
    my_quizer.load_english_project("./kenny_book.txt")




