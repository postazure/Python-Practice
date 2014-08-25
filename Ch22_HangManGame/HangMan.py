import random
import sys
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("hangman.ui")[0]



def wrong(self):
    self.pieces_shown += 1
    for i in range(self.pieces_shown):
        self.pieces[i].setHidden(False)
    if self.pieces_shown == len(self.pieces):
        message = "You Lose. The word was " + self.currentword
        QtGui.QMessageBox.warning(self, "Hangman", message)
        self.new_game()

def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != 1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations

def replace_letters(string, location, letter):
    new_string = ''
    for i in range(0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string


f = open("words.txt",'r')
self.lines = f.readlines()
for lin in self.lines:
    line.strip() #remove whitespace ie. /n
f.close

self.currentword = random.choice(self.lines)


if len(guess) == 1:
    if guess in self.currentword:
        locations = find_letters(guess, self.currentword)
        self.word.setText(replace_letters(str(self.word.text()), locations, guess))
        if str(self.word.text()) == self.currentword:
            self.win()
    else:
        self.wrong()

