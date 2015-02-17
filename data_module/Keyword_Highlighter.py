#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

def format(color, style=''):
    """Return a QTextCharFormat with the given attributes.
    """
    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format

STYLES = {
    'keyword': format('blue','bold'),
    'operator': format('red'),
    'brace': format('darkGray'),
    'defclass': format('black', 'bold'),
    'string': format('magenta'),
    'string2': format('darkMagenta'),
    'comment': format('darkGreen', 'italic'),
    'self': format('black', 'italic'),
    'numbers': format('brown'),
}

class Keyword_Highlighter(QSyntaxHighlighter):
    
    NEED_TO_STRIP_STR = "\"',!.?;"

    def __init__(self, document, word_keyword_str):
        
        super(Keyword_Highlighter, self).__init__(document)
        
        tmp_list = word_keyword_str.split()
        
        word_keyword_list = [ item.strip(Keyword_Highlighter.NEED_TO_STRIP_STR) for item in tmp_list]
        print(word_keyword_list) 
        
        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword']) for w in word_keyword_list]
        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.rules :
            index = expression.indexIn(text, 0)
        
            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)


