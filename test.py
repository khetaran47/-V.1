from tkinter import *
import random
import time
import tkinter
from tkinter import font
window= Tk()
window.title('Game Tai Kum')
window.geometry('700x840')
game_finished= False #เริ่มมาเกมไม่จบ
score = 0
lives = 3

status_str = StringVar()
status_str.set('คะแนนตอนนี้คือ: '+ str(score)+'|'+'❤️'*lives) 
show_status=Label(window, textvariable=status_str,font=('Arial',28))
show_status.pack(pady=20)

#dict

word_dict={
    'luffy':
    {'category':'ตัวการ์ตูน', 'hint':['เป็นโจรสลัด','ใส่หมวกฟาง','เป็นพระเอกในเรื่อง']
    },
    'messi':
    {'category':'นักฟุตบอล', 'hint':['นักฟุตบอลทีมชาติอาร์เจนติน่า','เคยอยู่บาร์เซโลน่า','ตอนนี้อยู่ทีม psg']
    },
    'doraemon':
    {'category':'ตัวการ์ตูน', 'hint':['มาจากโลกอนาคต','เป็นแมว','มีกระเป๋าใส่ของวิเศษ']
    },
    'goku':
    {'category':'ตัวการ์ตูน', 'hint':['เป็นชาวไซย่า','เป็นตัวดี','เป็นพระเอกในเรื่อง']
    },
    'popeye':
    {'category':'ตัวการ์ตูน', 'hint':['เป็นกะลาสีเรือ','กินผักโขม','สู้กับพลูโต']
    },
    'jerry':
    {'category':'ตัวการ์ตูน', 'hint':['เป็นหนู','ชอบกินชีส','โดนตีกี่ทีก็ไม่เป็นอะไร']
    },
}

word=list(word_dict.keys())

def get_new_secret_word():
    random.shuffle(word)
    secret_word = word.pop()
    clue = list('?'*len(secret_word))
    return secret_word, clue
secret_word, clue= get_new_secret_word()   

clue_str= StringVar()
clue_str.set(' | '.join(clue))
show_clue= Label(window, textvariable=clue_str, font=('Arial',50))
show_clue.pack(padx=10, pady=30)

category_str = StringVar()
category_str.set(word_dict[secret_word]['category'])
show_category= Label(window, textvariable=category_str, font=('Arial', 50))
show_category.pack(padx=10, pady=30)


hint= word_dict[secret_word]['hint']
hint_text = StringVar()
hint_text.set('Hint')
hint_str = StringVar()
hint_str.set('\n'.join(hint)) #\n เหมือน enter
show_hint_text=Label(window, textvariable=hint_text, font=('Arial Bold',28))
show_hint_text.pack()
show_hint = Label(window, textvariable=hint_str, font=('Arial',28))
show_hint.pack(pady=10)

textentry= Entry(window, width=5, borderwidth=1, font=('Arial',50),justify='center')
textentry.pack()

def update_clue(guess, secret_word, clue):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i]= guess
    clue_str.set(' | '.join(clue))        
    win = ''.join(clue) == secret_word
    return win

#update screen
def update_screen():
    global game_finished,score, lives, secret_word, clue, hint
    guess= textentry.get().strip()
    guess= guess.lower()
    if guess in secret_word:
        win=update_clue(guess, secret_word, clue)
        if win:
            print('ถูกต้องแล้วมันคือ: '+ secret_word)
            score= score+1
            print('คะแนนตอนนี้:' + str(score))
            clue_str.set("You're right! It's a: " + secret_word)
            window.update()
            time.sleep(2)# sน้าจอรันค้างไว้ 2 วินาที

            if len(word) < 1:
                game_finished = True
                clue_str.set('Congrat!')
            else:
                secret_word, clue = get_new_secret_word()
                category_str.set(word_dict[secret_word]['category'])
                clue_str.set(' | '.join(clue))
                hint = word_dict[secret_word]['hint']
                hint_str.set('\n'.join(hint))
    
    else:
        print('ผิดนนะครับ โปรดตั้งสติแล้วทายใหม่')
        lives= lives- 1
        if lives < 1:
            clue_str.set('Game Over!')
            game_finished=True
    status_str.set('คะแนนตอนนี้คือ: '+ str(score)+'|'+'❤️'*lives)
    textentry.delete(0,'end')

submit_btn=Button(window, text='Submit', command=update_screen)
submit_btn.pack()

#โปรแกรมที่check ว่าเกมจบหรือยัง
def main():
    if not game_finished:
        window.after(1000, main)
    else:
        submit_btn['state']= 'disable'
        print('Quitting...')
        window.quit()  

window.after(1000, main)
window.mainloop()
