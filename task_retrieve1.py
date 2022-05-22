from psychopy import visual,core,event,gui
import random
import pathlib

subj_info={"ParticipantID":'',"age":'',"sex":["man","woman"]}

info_dlg=gui.DlgFromDict(subj_info)
if not info_dlg.OK:
    core.quit()
ID=subj_info["ParticipantID"]
age=subj_info["age"]
sex=subj_info["sex"]

str(ID)

win=visual.Window()

letter_stim=visual.TextStim(win)
letter_stim.font="Hiragino Kaku Gothic Pro W3"
letter_list=["思い","日数","各国","資源","玉ねぎ","世界","路上"
            ,"小説","講座","天気","夫人","京","勧め","条例"
            ,"終戦","衛星","一挙","不信","順番","器","領域"
            ,"戦力","区間","おもちゃ","精度","生姜","局面","分子"
            ,"労務","教養","費用","比率","うつ病","真理","都会"
            ,"時代","室内","起源","栄養","主婦","友達","政党"
            ,"騒音","書面","課程","気分","昭","助け","液晶"
            ,"立体","近隣","気配","関税","音声","永久","公園"
            ,"県立","年金","会長","公務","財産","本線","半身"
            ,"方策","軌道","外来","食卓","片手","前方","飲み物"
            ,"家畜","住まい","県民","長官","各種","領土","様式"
            ,"負債","胡椒","両側","確率","頭","公民","頻度"]
random.shuffle(letter_list)

#ファイルを開く
current_folder=pathlib.Path(__file__).parent
new_filename="{}_data.csv".format(ID) #IDをファイル名に入れる
new_filepath=current_folder/"retrieve"/new_filename
#データをファイルに書き込み
datafile=open(new_filepath,mode='a',encoding='utf_8')
datafile.write('trialID,stim,reskey,restime\n')

trialID=0
stopwatch1=core.Clock()
timer = core.Clock()
timer.reset()
for letter in letter_list:
    letter_stim.font="Hiragino Kaku Gothic Pro W3"
    letter_stim.setText(letter)
    letter_stim.draw()
    win.flip()
    stopwatch1.reset()
    resp=event.waitKeys(keyList=['n','m','s','o'],timeStamped=stopwatch1)
    key=resp[0]
    rt=resp[0]
    data='{},{},{},{}\n'.format(trialID,letter,key,rt)
    datafile.write(data)
    trialID=trialID+1


datafile.close()
win.close
    
#変数を揃える
#type関数