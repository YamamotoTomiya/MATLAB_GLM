from psychopy import visual,core,event
import random

win=visual.Window()
win.flip()
core.wait(30)
stopwatch1=core.Clock()
instruction=visual.TextStim(win,"+",font="Hiragino Kaku Gothic Pro W3")
letter_stim=visual.TextStim(win)
#1sttime_music
letter_list11=["思い","日数","各国","資源"
                ,"玉ねぎ","世界","路上"]
letter_stim.font="Hiragino Kaku Gothic Pro W3"
random.shuffle(letter_list11)

instruction.draw()
win.flip()
core.wait(15)

for letter in letter_list11:
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    core.wait(4)
    
instruction.draw()
win.flip()
core.wait(15)
#rest
win.flip()
core.wait(30)

#1sttime_silence
letter_list12=["小説","講座","天気","夫人"
                ,"京","勧め","条例"]
letter_stim.font="Hiragino Kaku Gothic Pro W3"
random.shuffle(letter_list12)

instruction.draw()
win.flip()
core.wait(15)

for letter in letter_list12:
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    core.wait(4)
    
instruction.draw()
win.flip()
core.wait(15)
#rest
win.flip()
core.wait(30)
#2ndtime_music
letter_list21=["終戦","衛星","一挙","不信"
                ,"順番","器","領域"]
letter_stim.font="Hiragino Kaku Gothic Pro W3"
random.shuffle(letter_list21)

instruction.draw()
win.flip()
core.wait(15)

for letter in letter_list21:
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    core.wait(4)
    
instruction.draw()
win.flip()
core.wait(12)
#rest
win.flip()
core.wait(30)
#2ndtime_silence
letter_list22=["戦力","区間","おもちゃ","精度"
                ,"生姜","局面","分子"]
letter_stim.font="Hiragino Kaku Gothic Pro W3"
random.shuffle(letter_list22)

instruction.draw()
win.flip()
core.wait(15)

for letter in letter_list22:
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    core.wait(4)
    
instruction.draw()
win.flip()
core.wait(15)
#rest
win.flip()
core.wait(30)
#3rdtime_music
letter_list31=["労務","教養","費用","比率"
                ,"うつ病","真理","都会"]
letter_stim.font="Hiragino Kaku Gothic Pro W3"
random.shuffle(letter_list31)

instruction.draw()
win.flip()
core.wait(15)

for letter in letter_list31:
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    core.wait(4)
    
instruction.draw()
win.flip()
core.wait(15)
#rest
win.flip()
core.wait(30)
#3rdtime_silence
letter_list31=["時代","室内","起源","栄養"
                ,"主婦","友達","政党"]
letter_stim.font="Hiragino Kaku Gothic Pro W3"
random.shuffle(letter_list31)

instruction.draw()
win.flip()
core.wait(15)

for letter in letter_list31:
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    core.wait(4)
    
instruction.draw()
win.flip()
core.wait(15)
#rest
win.flip()
core.wait(30)

fin = visual.TextStim(win, "実験終了です．お疲れ様でした", font = "Hiragino Kaku Gothic Pro W3")
fin.draw()
win.flip()
core.wait(3)
win.close() 