from psychopy import visual,core,event,gui#必要なツール
import random#ランダム
import pathlib#ファイル
subj_info={"ParticipantID":'',"age":''}#ダイアログに表示する項目と初期値を設定

info_dlg=gui.DlgFromDict(subj_info)#info_dlgという名前のダイアログを表示
if not info_dlg.OK:#ダイアログでokが押されなければ終了
    core.quit()
#ダイアログの情報を変換
ID=subj_info["ParticipantID"]
age=subj_info["age"]

str(ID)
win=visual.Window()#ウィンドウを表示

letter_stim=visual.TextStim(win)#テキストの刺激を準備
letter_list=["XX","XO","OO","OX"]#リストを作成
#リストをシャッフルする

#ファイルを開く
current_folder=pathlib.Path(__file__).parent#
new_filename="{}_data.csv".format(ID) #IDをファイル名に入れる
new_filepath=current_folder/"data"/new_filename#
#データをファイルに書き込み
datafile=open(new_filepath,mode='a')#
datafile.write('trialID,stim,reskey,restime\n')#

trialID=0#試行回数
stopwatch1=core.Clock()
timer = core.Clock()
timer.reset()
while timer.getTime()<30.0:#30秒以内で終了
    #課題
    for letter in letter_list:#letter_listから順番に要素を取り出して，ブロック内でletterという名前で使用する
        random.shuffle(letter_list)
        letter_stim.setText(letter)#取り出した要素を刺激テキストとしてセットする
        letter_stim.draw()#刺激の描画
        win.flip()#ウィンドウに表示
        stopwatch1.reset()#時間のリセット
        #s,dのどちらかのキーを押したら時間を止める
        resp=event.waitKeys(keyList=['s','d'],timeStamped=stopwatch1)
        key=resp[0]#押したキー
        rt=resp[0]#止めた時間
        data='{},{},{},{}\n'.format(trialID,letter,key,rt)#trialID,letter,key,rtをデータに記入
        datafile.write(data)#データをファイルに記入
        trialID=trialID+1
        win.flip()
        core.wait(0.2)
        

datafile.close()#
win.close#
    
