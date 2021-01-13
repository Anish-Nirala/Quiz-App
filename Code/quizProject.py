import tkinter
from tkinter import *
from questionModule import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

win = tkinter.Tk()
win.title("QuizBrain")
windowWidth = 500
windowHeight = 550
win.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(int((win.winfo_screenwidth() - windowWidth)/2))+"+"+str(int((win.winfo_screenheight() - windowHeight)/2)))
win.resizable(0, 0)
win.configure(background="#375362")
userCount = 1

def HomeInterface():
    global win, labelImg, labeltext, btnStart, userCountLabel, userCount

    img1 = ImageTk.PhotoImage(Image.open("E:\VScode\Python\Tkinter\myquiz.png").resize((100, 100), Image.ANTIALIAS))
    labelImg = Label(
        win,
        image = img1,
    )
    labelImg.pack(pady=(50, 70))

    labeltext = Label(
        win,
        text = "QuizBrain",
        font = ("Consolas", 24, "bold"),
        background = "#375362",
        foreground = "#ffffff"
    )
    labeltext.pack(pady = (0, 70))

    img2_pic = Image.open("E:\VScode\Python\Tkinter\quizstart.png")
    img2_resized = img2_pic.resize((100, 50), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2_resized)

    btnStart = Button(
        win,
        image = img2,
        border = 0,
        background = "#375362",
        relief = FLAT,
        command = QuizInterface,
    )
    btnStart.pack(pady = (0, 70))
    userCountLabel = Label(
        win,
        text = "Live User Count: "+str(userCount),
        anchor = SE,
        background = "#375362",
        foreground = "#ffffff",
        font = ("Consolas", 10, "italic")
    )
    userCountLabel.pack(pady=(0, 70))

    win.mainloop()

def QuizInterface():

    global win, labelImg, labeltext, btnStart, userCountLabel, userCount, questionList, answerChoice, correctAnswer, labelQuestion, r1, r2, r3, r4, submitBtn, nextBtn, flag, score, questionIndex, labelScore, homeBtn

    radioVar = IntVar()
    radioVar.set(-1)

    flag, score = 0,0
    questionIndex = []

    def generateQuestion():
        global questionIndex
        while(len(questionIndex)<10):
            idx = random.randint(0, 19)
            if idx not in questionIndex:
                questionIndex.append(idx)

    def nextBtnSelected():
        global labelQuestion, r1, r2, r3, r4, flag, nextBtn, submitBtn, score, labelNumber
        x = radioVar.get()
        radioVar.set(-1)
        if(x==-1):
            messagebox.showerror("Error", "Please choose an option")
        else:
            if(answerChoice[questionIndex[flag]][x]==correctAnswer[questionIndex[flag]]):
                score+=1
            flag+=1
            if(flag<9):
                labelNumber['text'] = f"Question: {flag+1}/10"
                labelQuestion['text'] = questionList[questionIndex[flag]]
                r1['text'] = answerChoice[questionIndex[flag]][0]
                r2['text'] = answerChoice[questionIndex[flag]][1]
                r3['text'] = answerChoice[questionIndex[flag]][2]
                r4['text'] = answerChoice[questionIndex[flag]][3]
            elif(flag==9):
                labelNumber['text'] = f"Question: {flag+1}/10"
                nextBtn.destroy()
                submitBtn = Button(
                    win,
                    text = "SUBMIT",
                    font = ("Arial", 15),
                    command = submitBtnSelected,
                    background = "#375362",
                    foreground = "#ffffff",
                )
                submitBtn.pack(pady = (25, 0))
                labelQuestion['text'] = questionList[questionIndex[flag]]
                r1['text'] = answerChoice[questionIndex[flag]][0]
                r2['text'] = answerChoice[questionIndex[flag]][1]
                r3['text'] = answerChoice[questionIndex[flag]][2]
                r4['text'] = answerChoice[questionIndex[flag]][3]
                if(radioVar.get()==correctAnswer[questionIndex[flag]]):
                    score+=1

    def comeToHomeInterface():
        global labelScore, homeBtn, labelResultImage, labelResultText
        labelResultImage.destroy()
        labelResultText.destroy()
        labelScore.destroy()
        homeBtn.destroy()
        HomeInterface()

    def submitBtnSelected():
        global labelQuestion, r1, r2, r3, r4, submitBtn, labelScore, homeBtn, score, labelResultImage, labelResultText, labelNumber
        x = radioVar.get()
        radioVar.set(-1)
        if(x==-1):
            messagebox.showerror("Error", "Please choose an option")
        else:
            if(answerChoice[questionIndex[flag]][x]==correctAnswer[questionIndex[flag]]):
                score+=1
            labelNumber.destroy()
            labelQuestion.destroy()
            r1.destroy()
            r2.destroy()
            r3.destroy()
            r4.destroy()
            submitBtn.destroy()
            labelScore = Label(
                win,
                text = "Result: " +str(score*10),
                font = ("Arial", 20, "italic"),
                justify = "center",
                background = "#375362",
                foreground = "#ffffff",
            )
            labelScore.pack(pady=50)
            labelResultImage = Label(
                win,
                background = "#ffffff",
                foreground = "#ffffff",
            )
            labelResultImage.pack(fill="both")
            labelResultText = Label(
                win,
                background = "#375362",
                foreground = "#ffffff",
                font = ("Arial", 20, "italic"),
            )
            labelResultText.pack(pady=(20, 0))
            if(score>=9):
                imgExcellent = ImageTk.PhotoImage(Image.open("E:\VScode\Python\Tkinter\Excellent.png").resize((100, 100), Image.ANTIALIAS))
                labelResultImage['image'] = imgExcellent
                labelResultImage.image = imgExcellent
                labelResultText['text'] = "You are Superb !!!"
            elif(score>=3 and score<9):
                imgOk = ImageTk.PhotoImage(Image.open("E:\VScode\Python\Tkinter\Ok.png").resize((100, 100), Image.ANTIALIAS))
                labelResultImage['image'] = imgOk
                labelResultImage.image = imgOk
                labelResultText['text'] = "Can be Better."
            else:
                imgFail = ImageTk.PhotoImage(Image.open("E:\VScode\Python\Tkinter\Fail.png").resize((100, 100), Image.ANTIALIAS))
                labelResultImage['image'] = imgFail
                labelResultImage.image = imgFail
                labelResultText['text'] = "Need to Improve."

            homeBtn = Button(
                win,
                text = "HOME",
                font = ("Arial", 15),
                background = "#375362",
                foreground = "#ffffff",
                command = comeToHomeInterface
            )
            homeBtn.pack(pady=(70, 0))

    def startQuiz():
        global labelQuestion, r1, r2, r3, r4, nextBtn, labelNumber
        labelNumber = Label(
            win,
            text = "Question: 1/10",
            font = ("Arial", 20, "italic"),
            background = "#375362",
            foreground = "#ffffff",
        )
        labelNumber.pack(pady=(10, 0))
        labelQuestion = Label(
            win,
            text = questionList[questionIndex[flag]],
            font = ("Arial", 20, "italic"),
            width = 500,
            background = "#375362",
            foreground = "#ffffff",
            justify = "center",
            wraplength = 400
        )
        labelQuestion.pack(pady=(50,50))

        r1 = Radiobutton(
            win,
            text = answerChoice[questionIndex[flag]][0],
            font = ("Arial", 12, "italic"),
            value = 0,
            background = "#375362",
            foreground = "#000000",
            variable = radioVar,
        )
        r1.pack(pady=5)
        r2 = Radiobutton(
            win,
            text = answerChoice[questionIndex[flag]][1],
            font = ("Arial", 12, "italic"),
            value = 1,
            background = "#375362",
            foreground = "#000000",
            variable = radioVar
        )
        r2.pack(pady=5)
        r3 = Radiobutton(
            win,
            text = answerChoice[questionIndex[flag]][2],
            font = ("Arial", 12, "italic"),
            value = 2,
            background = "#375362",
            foreground = "#000000",
            variable = radioVar
        )
        r3.pack(pady=5)
        r4 = Radiobutton(
            win,
            text = answerChoice[questionIndex[flag]][3],
            font = ("Arial", 12, "italic"),
            value = 3,
            background = "#375362",
            foreground = "#000000",
            variable = radioVar
        )
        r4.pack(pady=5)
        nextBtn = Button(
            win,
            text = "NEXT",
            font = ("Arial", 15),
            command = nextBtnSelected,
            relief=GROOVE,
            background = "#375362",
            foreground = "#ffffff",
        )
        nextBtn.pack(pady = (25, 0))
    userCount+=1
    userCountLabel['text'] = "Live User Count: " + str(userCount)
    labelImg.destroy()
    labeltext.destroy()
    userCountLabel.destroy()
    btnStart.destroy()
    generateQuestion()
    startQuiz()

HomeInterface()




