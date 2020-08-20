import pyttsx3
import os

pyttsx3.speak("hello welcome in my program")

print()
print("press 1 for chrome ")
print("press 2 for notepad ")
print("press 3 for media player ")

print()
print("enter your choice: ",end="")

p=input()
if int(p)==1 :
	system.os("chrome")
elif int(p)==2 :
	system.os("notepad")
elif int(p)==3 :
	system.os("wmplayer")
else:
	print("not support")

