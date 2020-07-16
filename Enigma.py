# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:35:52 2020

@author: sphill98

code for Enigma
"""

class Enigma():
    def __init__(self, mode):
        self.mode = mode
        self.ref_disk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.DISK = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                     "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                     "VZBRGITYUPSDNHLXAWMJQOFECK", "JPGVOUMFYQBENHZRDKASXLICTW",
                     "NZJHGRCXMYSWBOUFAIVLPEKQDT", "FKQHTLXOCBJSPDZRAMEWNIUYGV"]
        
    def setDisk(self, n_lst):
        self.dsk = []
        for n in n_lst:
            self.dsk.append(self.DISK[n-1])
    
    def setInit(self, init_cond):
        self.init_cond = init_cond
        self.count = 0
        self.counter = [] #to rotate disk
        self.disk_counter = 1
        self.init_counter = [] #to check rotation
        for i in range(len(self.init_cond)):
            self.counter.append(self.dsk[i].find(self.init_cond[i]))  
            self.init_counter.append(self.dsk[i].find(self.init_cond[i]))
    
    def setFile(self):
        if self.mode == "E":
            self.e_file = open("Encode.txt")
        else:
            self.d_file = open("Decode.txt")
    
    def reflect(self, alph):
        self.ref = self.ref_disk[-(self.ref_disk.index(alph)+1)]
        return self.ref
    
    def rotate_init(self):
        for i in range(len(self.counter)):
            if self.counter[i] != self.init_counter[i]:
                return False
        return True
    
    def rotate_disk(self):
        self.counter[0] = (self.counter[0] + 1) % 26
        for i in range(self.disk_counter):
            if (self.counter[i] == self.init_counter[i]):
                self.counter[i + 1] = (self.counter[i + 1] + 1) % 26
        if self.rotate_init():
            self.disk_counter = ((self.disk_counter + 1) % (len(self.dsk)-1)) + 1
    
    def modifier(self, ch):
        self.ch = ch
        self.ch_ind = (self.dsk[0].index(self.ch) - self.counter[0] + 26) % 26
        for i in range(len(self.dsk)):
            self.ch = self.dsk[i][(self.counter[i] + self.ch_ind) % 26]
        self.ch = self.reflect(self.ch)
        self.ch_ind = (self.dsk[len(self.dsk) - 1].index(self.ch) - self.counter[len(self.dsk) - 1] + 26) % 26
        for i in range(len(self.dsk)):
            self.ch = self.dsk[len(self.dsk) - (1 + i)][(self.counter[len(self.dsk) - (1 + i)] + self.ch_ind) % 26]
        self.rotate_disk()
        return self.ch
    
    def enigma(self):
        self.text = input()
        while self.text != "":
            print(self.modifier(self.text))
            self.text = input()
        print("End")
        
    def printSetting(self):
        for d in self.dsk:
            print(d)
        print(self.init_counter)    
        

aa = Enigma("E")
aa.setDisk([4, 1, 5])
aa.setInit("EKV")
aa.enigma()
