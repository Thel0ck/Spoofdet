from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import filedialog
import customtkinter
import files as files
import pandas as pd
from openpyxl.formula import tokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import re

######################          Starting Window         #######################

w = Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate', )


def mail_a():

    def clear_frame():
        for widgets in output_frame3.winfo_children():
            widgets.destroy()

        for widgets in output_frame4.winfo_children():
            widgets.destroy()
    clear_frame()

    c = '#2d2340'
    filename = filedialog.askopenfilename(title='Select a text file',
                                            filetypes=[("Text files", '*.txt')])
    fo = open(filename, "r")  # fo=filehandle
    data = fo.read()

#####################            DKIM check              ########################

    d = re.search("DKIM=" + '.*', data, re.M | re.I).group(0)
    if d:
        string = d
        pattern = ("dkim=")
        d1 = re.split(pattern, string)
        d2 = (d1[1])

        def text12():
            lb4 = Label(output_frame3, text='Initializing Process ...', font=('Calibri (Body)', 9, 'bold'),
                        bg=c,
                        fg='white', justify='center')
            lb4.place(x=10, y=10, anchor="w")

        output_frame3.after(200, text12)

        def text12():
            lb4 = Label(output_frame3, text='Collecting Email information ...', font=('Calibri (Body)', 9, 'bold'),
                        bg=c,
                        fg='white', justify='center')
            lb4.place(x=10, y=30, anchor="w")

        output_frame3.after(2000, text12)

        def text12():
            lb4 = Label(output_frame3, text='Initializing DKIM authenticatin check ...',
                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                        fg='white', justify='center')
            lb4.place(x=10, y=50, anchor="w")

        output_frame3.after(4000, text12)

        if 'pass' in d2:

            def text12():
                lb4 = Label(output_frame3, text='The email passes DKIM authentication', font=('Calibri (Body)', 9, 'bold'), bg=c,
                            fg='white', justify='center')
                lb4.place(x=10, y=70, anchor="w")

            output_frame3.after(6000, text12)
            def text12():
                lb4 = Label(output_frame3, text='Initializing SPF authenticatin check ...', font=('Calibri (Body)', 9, 'bold'), bg=c,
                            fg='white', justify='center')
                lb4.place(x=10, y=90, anchor="w")

            output_frame3.after(8000, text12)

##############################            SPF check              ########################

            d = re.search("SPF=" + '.*', data, re.M | re.I).group(0)
            if d:
                string = d
                pattern = ("spf=")
                d1 = re.split(pattern, string)
                d2 = (d1[1])
                if 'pass' in d2:
                    def text12():
                        lb4 = Label(output_frame3, text='The email passes SPF authentication',
                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                    fg='white', justify='center')
                        lb4.place(x=10, y=110, anchor="w")

                    output_frame3.after(10000, text12)

                    if 'pass' in d2:
                        def text12():
                            lb4 = Label(output_frame3, text='Initializing DMARC authentication check ...',
                                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                                        fg='white', justify='center')
                            lb4.place(x=10, y=130, anchor="w")

                        output_frame3.after(12000, text12)

########################################            DMARC check              ########################

                        d = re.search("DMARC=" + '.*', data, re.M | re.I).group(0)
                        if d:
                            string = d
                            pattern = ("dmarc=")
                            d1 = re.split(pattern, string)
                            d2 = (d1[1])
                            if 'pass' in d2:
                                def text12():

                                    lb4 = Label(output_frame4, text='The email passes DKIM, SPF and DMARC\nauthentication',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='left')
                                    lb4.place(x=10, y=20, anchor="w")

                                output_frame4.after(14000, text12)

                                def text12():
                                    lb4 = Label(output_frame4, text='The email is safe',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='center')
                                    lb4.place(x=10, y=50, anchor="w")

                                output_frame4.after(16000, text12)

                            else:

                                def text12():
                                    lb4 = Label(output_frame3, text='The email passes DKIM authentication',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='center')
                                    lb4.place(x=10, y=70, anchor="w")

                                output_frame3.after(6000, text12)

                                def text12():
                                    lb4 = Label(output_frame3, text='Initializing SPF authenticatin check ...',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='center')
                                    lb4.place(x=10, y=90, anchor="w")

                                output_frame3.after(8000, text12)

                                def text12():
                                    lb4 = Label(output_frame3, text='The email passes SPF authentication',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='center')
                                    lb4.place(x=10, y=110, anchor="w")

                                output_frame3.after(10000, text12)

                                if 'pass' in d2:
                                    def text12():
                                        lb4 = Label(output_frame3, text='Initializing DMARC authentication check ...',
                                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                    fg='white', justify='center')
                                        lb4.place(x=10, y=130, anchor="w")

                                    output_frame3.after(12000, text12)

                                def text12():
                                    lb4 = Label(output_frame4, text='The email passes DKIM and SPF authentication'
                                                                    '\nbut the email does not pass DMARC\nauthentication',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='left')
                                    lb4.place(x=10, y=30, anchor="w")

                                output_frame4.after(14000, text12)


                                def text12():
                                    lb4 = Label(output_frame4, text='The email is fake',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='center')
                                    lb4.place(x=10, y=60, anchor="w")

                                output_frame4.after(16000, text12)

                        else:

                            def text12():
                                lb4 = Label(output_frame3, text='The email passes DKIM authentication',
                                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                                            fg='white', justify='center')
                                lb4.place(x=10, y=70, anchor="w")

                            output_frame3.after(6000, text12)

                            def text12():
                                lb4 = Label(output_frame3, text='Initializing SPF authenticatin check ...',
                                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                                            fg='white', justify='center')
                                lb4.place(x=10, y=90, anchor="w")

                            output_frame3.after(8000, text12)

                            def text12():
                                lb4 = Label(output_frame3, text='The email passes SPF authentication',
                                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                                            fg='white', justify='center')
                                lb4.place(x=10, y=110, anchor="w")

                            output_frame3.after(10000, text12)

                            if 'pass' in d2:
                                def text12():
                                    lb4 = Label(output_frame3, text='Initializing DMARC authentication ...',
                                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                                fg='white', justify='center')
                                    lb4.place(x=10, y=130, anchor="w")

                                output_frame3.after(12000, text12)

                            def text12():
                                lb4 = Label(output_frame4, text='The email passes DKIM and SPF authentication\nbutThe '
                                                                'email does not pass DMARC\nauthentication',
                                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                                            fg='white', justify='left')
                                lb4.place(x=10, y=30, anchor="w")

                            output_frame4.after(14000, text12)

                            def text12():
                                lb4 = Label(output_frame4, text='The email is fake',
                                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                                            fg='white', justify='center')
                                lb4.place(x=10, y=60, anchor="w")

                            output_frame4.after(16000, text12)

                    else:
                        def text12():
                            lb4 = Label(output_frame3, text='The email passes DKIM authentication',
                                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                                        fg='white', justify='center')
                            lb4.place(x=10, y=70, anchor="w")

                        output_frame3.after(6000, text12)

                        def text12():
                            lb4 = Label(output_frame3, text='Initializing SPF authenticatin check ...',
                                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                                        fg='white', justify='center')
                            lb4.place(x=10, y=90, anchor="w")

                        output_frame3.after(8000, text12)


                        def text12():
                            lb4 = Label(output_frame4, text='The email passes DKIM authentication\nbut does not pass '
                                                            'SPF authentication',
                                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                                        fg='white', justify='left')
                            lb4.place(x=10, y=20, anchor="w")

                        output_frame4.after(10000, text12)

                        def text12():
                            lb4 = Label(output_frame4, text='No further analysis is done',
                                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                                        fg='white', justify='center')
                            lb4.place(x=10, y=50, anchor="w")

                        output_frame4.after(12000, text12)

                        def text12():
                            lb4 = Label(output_frame4, text='The email is fake',
                                        font=('Calibri (Body)', 9, 'bold'), bg=c,
                                        fg='white', justify='center')
                            lb4.place(x=10, y=70, anchor="w")

                        output_frame4.after(14000, text12)

                else:

                    def text12():
                        lb4 = Label(output_frame3, text='The email passes DKIM authentication',
                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                    fg='white', justify='center')
                        lb4.place(x=10, y=70, anchor="w")

                    output_frame3.after(6000, text12)

                    def text12():
                        lb4 = Label(output_frame3, text='Initializing SPF authenticatin check ...',
                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                    fg='white', justify='center')
                        lb4.place(x=10, y=90, anchor="w")

                    output_frame3.after(8000, text12)

                    def text12():
                        lb4 = Label(output_frame4, text='The email passes DKIM authentication but\ndoes not pass SPF '
                                                        'authentication',
                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                    fg='white', justify='left')
                        lb4.place(x=10, y=20, anchor="w")

                    output_frame4.after(10000, text12)

                    def text12():
                        lb4 = Label(output_frame4, text='No further analysis is done',
                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                    fg='white', justify='center')
                        lb4.place(x=10, y=50, anchor="w")

                    output_frame4.after(12000, text12)

                    def text12():
                        lb4 = Label(output_frame4, text='The email is fake',
                                    font=('Calibri (Body)', 9, 'bold'), bg=c,
                                    fg='white', justify='center')
                        lb4.place(x=10, y=70, anchor="w")

                    output_frame4.after(14000, text12)

            else:
                def text12():
                    lb4 = Label(output_frame4, text='The email does not pass DKIM authentication',
                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white', justify='center')
                    lb4.place(x=10, y=10, anchor="w")

                output_frame4.after(6000, text12)

                def text12():
                    lb4 = Label(output_frame4, text='No further analysis is done',
                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white', justify='center')
                    lb4.place(x=10, y=30, anchor="w")

                output_frame4.after(8000, text12)

                def text12():
                    lb4 = Label(output_frame4, text='The email is fake',
                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white', justify='center')
                    lb4.place(x=10, y=50, anchor="w")

                output_frame4.after(10000, text12)

        else:
            def text12():
                lb4 = Label(output_frame3, text='The email does not pass DKIM authentication',
                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                            fg='white', justify='center')
                lb4.place(x=10, y=10, anchor="w")

            output_frame3.after(6000, text12)

            def text12():
                lb4 = Label(output_frame4, text='No further analysis is done',
                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                            fg='white', justify='center')
                lb4.place(x=10, y=30, anchor="w")

            output_frame3.after(8000, text12)

            def text12():
                lb4 = Label(output_frame4, text='The email is fake',
                            font=('Calibri (Body)', 9, 'bold'), bg=c,
                            fg='white', justify='center')
                lb4.place(x=10, y=50, anchor="w")

            output_frame3.after(10000, text12)

def start_win():
    global outer_frame2
    global output_frame4
    global output_frame3

    k = Tk()
    k.state('zoomed')
    k.title('UrlDet')
    k.configure(background='#50223c')
    c = '#2d2340'
    lb2 = Label(k, text='Choose the text file with Email header address', fg='white', bg='#50223c', font=
    ('Calibri (Body)', 15, 'bold'))
    lb2.pack(padx=15, pady=30)


    b3 = customtkinter.CTkButton(k, text='Open', fg_color='white', bg_color=c, command=mail_a)
    b3.pack(padx=15, pady=25)

    outer_frame2 = LabelFrame(k, height=440, width=340, bg='#f0dac5')
    outer_frame2.pack(padx=20, pady=20)

    lbl2 = Label(outer_frame2, padx=5, pady=5, text="Email analysis progression", width=24, fg='white', bg=c,
                font=('Calibri (Body)', 14, 'bold'))
    lbl2.pack(padx=20, pady=10)

    output_frame3 = LabelFrame(outer_frame2, height=300, width=302, padx=5,
                              pady=5, bg=c, font=('Calibri (Body)', 11, 'bold'))
    output_frame3.pack(padx=20, pady=5)

    lbl2 = Label(outer_frame2, padx=5, pady=5, text="Final Results", bg=c, fg='white', width=24,
                 font=('Calibri (Body)', 14, 'bold'))
    lbl2.pack(padx=20, pady=20)

    output_frame4 = LabelFrame(outer_frame2, height=90, width=302, padx=5,
                               pady=5, bg=c, font=('Calibri (Body)', 11, 'bold'))
    output_frame4.pack(padx=20, pady=10)

    k.mainloop()


def clear_frame():
   for widgets in output_frame.winfo_children():
      widgets.destroy()

def getting():
    def clear_frame():
        for widgets in output_frame.winfo_children():
            widgets.destroy()

        for widgets in output_frame1.winfo_children():
            widgets.destroy()
    clear_frame()


    e=input_frame.get()



    if len(e)==0:
        def text9():
            lb3 = Label(output_frame, text='The Entry cannot be Empty', font=('Calibri (Body)', 9, 'bold'), bg=c,
                        fg='white', justify='center')
            lb3.place(x=10, y=10, anchor="w")

        output_frame.after(500, text9)
    else:
        urls_data = pd.read_excel("C:/Users/acer/Desktop/urls.xlsx")

        urls_data.drop_duplicates(inplace=True)

        if len(e) >= 4:

            if '.' in e:
                def text():
                    lb3 = Label(output_frame, text='Initializing Process ...', font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white', justify='center')
                    lb3.place(x=10, y=10, anchor="w")

                output_frame.after(2000, text)

                def text1():
                    lb3 = Label(output_frame, text='Getting words tokenized ...', font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white', justify='center')
                    lb3.place(x=10, y=30, anchor="w")

                output_frame.after(4000, text1)

                def makeTokens(f):
                    tkns_BySlash = str(f.encode('utf-8')).split('/')
                    total_tokens = []

                    for i in tkns_BySlash:
                        tokens = str(i).split('-')  # make tokens after splitting by dash
                        tkns_ByDot = []

                    for j in range(0, len(tokens)):
                        temp_Tokens = str(tokens[j]).split('.')  # make tokens after splitting by dot
                        tkns_ByDot = tkns_ByDot + temp_Tokens
                    total_tokens = total_tokens + tokens + tkns_ByDot
                    total_tokens = list(set(total_tokens))
                    # removing .com since it occurs a lot of times and it should not be included in our features
                    if 'com' in total_tokens:
                        total_tokens.remove(
                            'com')

                    return total_tokens

                def text2():
                    lb3 = Label(output_frame, text='Words have been tokenized', font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white')
                    lb3.place(x=10, y=50, anchor="w")

                output_frame.after(6000, text2)

                def text3():
                    lb3 = Label(output_frame, text='Implementing Logistic Regression ...',
                                font=('Calibri (Body)', 9, 'bold'), bg=c, fg='white')
                    lb3.place(x=10, y=70, anchor="w")

                output_frame.after(8000, text3)

                url_list = urls_data["url"]
                y = urls_data["label"]

                vectorizer = TfidfVectorizer(tokenizer=makeTokens)

                X = vectorizer.fit_transform(url_list)

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=110)

                logit = LogisticRegression(max_iter=1000, dual=False)
                logit.fit(X_train, y_train)

                def text4():
                    lb3 = Label(output_frame, text='Accuracy has been calculated', font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white')
                    lb3.place(x=10, y=90, anchor="w")

                output_frame.after(10000, text4)

                def text5():
                    lb3 = Label(output_frame, text='Testing Accuracy: ' + str(logit.score(X_test, y_test) * 100),
                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white')
                    lb3.place(x=10, y=110, anchor="w")

                output_frame.after(12000, text5)

                def text6():
                    lb3 = Label(output_frame, text='Training Accuracy: ' + str(logit.score(X_test, y_test) * 100),
                                font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white')
                    lb3.place(x=10, y=130, anchor="w")

                output_frame.after(14000, text6)

                in1 = input_frame.get()
                print(in1)

                X_predict = [in1]

                X_predict = vectorizer.transform(X_predict)
                New_predict = logit.predict(X_predict)

                def text7():
                    lb3 = Label(output_frame, text='Analysing Website ...', font=('Calibri (Body)', 9, 'bold'), bg=c,
                                fg='white')
                    lb3.place(x=10, y=150, anchor="w")

                output_frame.after(15000, text7)

                if New_predict == "bad":
                    def text8():
                        lb3 = Label(output_frame1, text='The website is malicious', font=('Calibri (Body)', 10, 'bold'),
                                    bg=c,
                                    fg='white')
                        lb3.place(x=10, y=10, anchor="w")

                        lb3 = Label(output_frame1, text='Please visit with caution',
                                    font=('Calibri (Body)', 10, 'bold'), bg=c,
                                    fg='white')
                        lb3.place(x=10, y=30, anchor="w")

                    output_frame1.after(17000, text8)
                    print('bad')
                else:
                    def text9():
                        lb3 = Label(output_frame1, text='The website is not malicious', font=('Calibri (Body)', 10, 'bold'),
                                    bg=c,
                                    fg='white')
                        lb3.place(x=10, y=10, anchor="w")
                        lb3 = Label(output_frame1, text='It is safe to Visit',
                                    font=('Calibri (Body)', 10, 'bold'), bg=c,
                                    fg='white')
                        lb3.place(x=10, y=30, anchor="w")

                    output_frame1.after(17000, text9)
                    print('good')



        else:
            def text():
                lb3 = Label(output_frame, text='Please Enter a valid URL', font=('Calibri (Body)', 9, 'bold'), bg=c,
                            fg='white', justify='center')
                lb3.place(x=10, y=10, anchor="w")

            output_frame.after(500, text)

            #else:

#############            Main window         ######################################
def new_win():
    global c
    global output_frame1
    global output_frame
    global input_frame
    q = Tk()
    q.state('zoomed')
    q.title('UrlDet')
    q.configure(background= '#50223c')
    c=   '#1c2340'
    lb2 = Label(q, text='Enter the URL to Check Below',fg='white',bg='#50223c',font=('Calibri (Body)', 15, 'bold'))
    lb2.pack(padx=15, pady=30)

    input_frame = Entry(q, width=40)
    input_frame.pack(padx=15, pady=1)

    b3= customtkinter.CTkButton(q,text='Submit', fg_color='white' ,bg_color=c, command=getting)
    b3.pack(padx=15, pady=25)



    outer_frame = LabelFrame(q,height=440, width=340,bg='#f0dac5')
    outer_frame.pack(padx=20, pady=20)

    lbl=Label(outer_frame,padx=5, pady=5, text= "Website analysis progression",width=24,fg='white',bg=c,font=
    ('Calibri (Body)', 14, 'bold'))
    lbl.pack(padx=20,pady=10)

    output_frame = LabelFrame(outer_frame, height=300,width=302, padx=5,
                              pady=5,bg=c,font=('Calibri (Body)', 11, 'bold'))
    output_frame.pack(padx=20,pady=5)

    lbl1 = Label(outer_frame, padx=5, pady=5, text="Final Results", bg=c,fg='white',width=24, font=('Calibri (Body)', 14, 'bold'))
    lbl1.pack(padx=20, pady=20)

    output_frame1 = LabelFrame(outer_frame, height=70,width=302, padx=5,
                              pady=5, bg=c, font=('Calibri (Body)', 11, 'bold'))
    output_frame1.pack(padx=20,pady=10)


    q.mainloop()

####################             Loading bar            ####################################

def bar():
    l4 = Label(w, text='Loading...', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=210)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r = r + 1

    w.destroy()
    new_win()

progress.place(x=-10, y=235)


def bar1():
    l4 = Label(w, text='Loading...', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=210)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r = r + 1

    w.destroy()
    start_win()

progress.place(x=-10, y=235)

##############              frame for loading screen            ############

'''
def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''

a = '#50223c'
Frame(w, width=427, height=241, bg=a).place(x=0, y=0)  # 249794

b2= customtkinter.CTkButton(w,text='Analyse URL', command=bar, fg_color='white' ,bg_color=a).place(x=140, y=205)

b3= customtkinter.CTkButton(w,text='Analyse Email', command=bar1, fg_color='white' ,bg_color=a).place(x=140, y=170)

l1 = Label(w, text='SPOOF', fg='white', bg=a)
lst1 = ('Calibri (Body)', 18, 'bold')
l1.config(font=lst1)
l1.place(x=50, y=80)

l2 = Label(w, text='DET', fg='white', bg=a)
lst2 = ('Calibri (Body)', 18)
l2.config(font=lst2)
l2.place(x=135, y=82)

l3 = Label(w, text='Detect Malicious Urls and Emails', fg='white', bg=a)
lst3 = ('Calibri (Body)', 9)
l3.config(font=lst3)
l3.place(x=50, y=110)

w.mainloop()

