from tkinter import *
# 현호
# 기본 프레임
root = Tk()
root.title ("Salary_Calculator")
root.geometry("640x600+300+100")
root.resizable(False, False)
# 설정
setting_frame = LabelFrame(root, text="설정",padx=5, pady=5)
setting_frame.pack(fill="x", ipady=5)

# 시급
label_money = Label(setting_frame, text="시급 :",width=7)
label_money.pack(side="left")

money = Entry(setting_frame, width=10,justify="right",fg ='black',bg='#fff',bd=1)
money.pack(side="left")


# 메인 화면
main_frame = LabelFrame(root, text="메인",padx=5, pady=5)
main_frame.pack(fill="x", ipady=5,side="top")

# 요일 프레임
day_frame = Frame(main_frame)
day_frame.pack(padx=5, pady=10,side="top")

# 리셋 버튼
def reset():
    for i in range(1,36):
        eval(f"label_time{i}.delete(0,END)")
        eval(f"label_time{i}.configure(fg ='black',bg='#fff',bd=1)")
    money.delete(0,END)
    money.configure(fg ='black',bg='#fff',bd=1)
    result.config(text="0")

# 요일
btn_reset = Button(day_frame, text="초기화",width=9,command=reset)
btn_reset.pack(side="left")
day_list = ["월요일","화요일","수요일","목요일","금요일"]

for i in day_list:
    label1 = Label(day_frame, text=f"{i}",width=10)
    label1.pack(side="left")

label1 = Label(day_frame, text="토요일",width=10,fg='blue')
label1.pack(side="left")
label1 = Label(day_frame, text="일요일",width=10,fg='red')
label1.pack(side="left")

total_time = 0
# 모든 프레임
# 1주차
week1_frame = Frame(main_frame)
week1_frame.pack(padx=5,pady=5,side="top")
time_frame = Frame(main_frame)
time_frame.pack(side="top")
# 2주차
week2_frame = Frame(main_frame)
week2_frame.pack(padx=5,pady=5,side="top")
time_frame2 = Frame(main_frame)
time_frame2.pack(padx=5,side="top")
# 3주차
week3_frame = Frame(main_frame)
week3_frame.pack(padx=5,pady=5,side="top")
time_frame3 = Frame(main_frame)
time_frame3.pack(padx=5,side="top")
# 4주차
week4_frame = Frame(main_frame)
week4_frame.pack(padx=5,pady=5,side="top")
time_frame4 = Frame(main_frame)
time_frame4.pack(padx=5,side="top")
# 5주차
week5_frame = Frame(main_frame)
week5_frame.pack(padx=5,pady=5,side="top")
time_frame5 = Frame(main_frame)
time_frame5.pack(padx=5,side="top")

# 1주차
label_time = Label(week1_frame, text="1주차",width=10)
label_time.pack(side="left")
label_time = Label(time_frame, text="",width=10)
label_time.pack(side="left")

# 1주차 평일
for i in range(1,6):
    label_time = Label(week1_frame, text="일한 시간",width=10)
    label_time.pack(side="left")
    globals()[f"label_time{i}"] = Entry(time_frame, width=3,justify="center",fg ='black',bg='#fff',bd=1)
    globals()[f"label_time{i}"].pack(side='left',padx=25)

# 1주차 토요일
label_time = Label(week1_frame, text="일한 시간",width=10,fg='blue')
label_time.pack(side="left")
label_time6 = Entry(time_frame, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time6.pack(side='left',padx=25)

# 1주차 일요일
label_time = Label(week1_frame, text="일한 시간",width=10,fg='red')
label_time.pack(side="left")
label_time7 = Entry(time_frame, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time7.pack(side='left',padx=25)


# 2주차
label_time = Label(week2_frame, text="2주차",width=10)
label_time.pack(side="left")
label_time = Label(time_frame2, text="",width=10)
label_time.pack(side="left")

# 2주차 평일
for i in range(8,13):
    label_time = Label(week2_frame, text="일한 시간",width=10)
    label_time.pack(side="left")
    globals()[f"label_time{i}"] = Entry(time_frame2, width=3,justify="center",fg ='black',bg='#fff',bd=1)
    globals()[f"label_time{i}"].pack(side='left',padx=25)
# 2주차 토요일
label_time = Label(week2_frame, text="일한 시간",width=10,fg='blue')
label_time.pack(side="left")
label_time13 = Entry(time_frame2, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time13.pack(side='left',padx=25)
# 2주차 일요일
label_time = Label(week2_frame, text="일한 시간",width=10,fg='red')
label_time.pack(side="left")
label_time14 = Entry(time_frame2, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time14.pack(side='left',padx=25)

# 3주차
label_time = Label(week3_frame, text="3주차",width=10)
label_time.pack(side="left")
label_time = Label(time_frame3, text="",width=10)
label_time.pack(side="left")

# 3주차 평일
for i in range(15,20):
    label_time = Label(week3_frame, text="일한 시간",width=10)
    label_time.pack(side="left")
    globals()[f"label_time{i}"] = Entry(time_frame3, width=3,justify="center",fg ='black',bg='#fff',bd=1)
    globals()[f"label_time{i}"].pack(side='left',padx=25)

# 3주차 토요일
label_time = Label(week3_frame, text="일한 시간",width=10,fg='blue')
label_time.pack(side="left")
label_time20 = Entry(time_frame3, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time20.pack(side='left',padx=25)

# 3주차 일요일
label_time = Label(week3_frame, text="일한 시간",width=10,fg='red')
label_time.pack(side="left")
label_time21 = Entry(time_frame3, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time21.pack(side='left',padx=25)

# 4주차
label_time = Label(week4_frame, text="4주차",width=10)
label_time.pack(side="left")
label_time = Label(time_frame4, text="",width=10)
label_time.pack(side="left")

# 4주차 평일
for i in range(22,27):
    label_time = Label(week4_frame, text="일한 시간",width=10)
    label_time.pack(side="left")
    globals()[f"label_time{i}"] = Entry(time_frame4, width=3,justify="center",fg ='black',bg='#fff',bd=1)
    globals()[f"label_time{i}"].pack(side='left',padx=25)

# 4주차 토요일
label_time = Label(week4_frame, text="일한 시간",width=10,fg='blue')
label_time.pack(side="left")
label_time27 = Entry(time_frame4, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time27.pack(side='left',padx=25)

# 4주차 일요일
label_time = Label(week4_frame, text="일한 시간",width=10,fg='red')
label_time.pack(side="left")
label_time28 = Entry(time_frame4, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time28.pack(side='left',padx=25)

# 5주차
label_time = Label(week5_frame, text="5주차",width=10)
label_time.pack(side="left")
label_time = Label(time_frame5, text="",width=10)
label_time.pack(side="left")

# 5주차 평일
for i in range(29,34):
    label_time = Label(week5_frame, text="일한 시간",width=10)
    label_time.pack(side="left")
    globals()[f"label_time{i}"] = Entry(time_frame5, width=3,justify="center",fg ='black',bg='#fff',bd=1)
    globals()[f"label_time{i}"].pack(side='left',padx=25)

# 5주차 토요일
label_time = Label(week5_frame, text="일한 시간",width=10,fg='blue')
label_time.pack(side="left")
label_time34 = Entry(time_frame5, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time34.pack(side='left',padx=25)

# 5주차 일요일
label_time = Label(week5_frame, text="일한 시간",width=10,fg='red')
label_time.pack(side="left")
label_time35 = Entry(time_frame5, width=3,justify="center",fg ='black',bg='#fff',bd=1)
label_time35.pack(side='left',padx=25)

# 결과
result_frame = LabelFrame(root, text="결과 값 보기", padx=5, pady=50)
result_frame.pack(fill="x", ipady=5, side="top")

# 세금 비율
label_tax_rate = Label(result_frame, text="세금 비율(%):", width=15, anchor='w')
label_tax_rate.pack(side="top", fill="x")
tax_rate = Entry(result_frame)
tax_rate.pack(side="top", fill="x")

# 세후 월급
label_after_tax = Label(result_frame, text="세후 월급 :", width=15, anchor='w')
label_after_tax.pack(side="top", fill="x")
after_tax = Label(result_frame, text="0", width=60)
after_tax.pack(side="top", fill="y")

def start():
    total_time = []
    if money.get() == "":
        money.insert(0,0)
    money.configure(fg ='black',bg='#F0F0F0',bd=0)
    for i in range(1,36):
        if eval(f"len(label_time{i}.get())") <= 0:
            eval(f"label_time{i}.insert(0,0)")
            eval(f"label_time{i}.configure(bg='#F0F0F0',bd=0)")
        if eval(f"int(label_time{i}.get())") > 0:
            eval(f"label_time{i}.configure(fg ='red',bg='#F0F0F0',bd=0)")
        total_time.append(eval(f"int(label_time{i}.get())"))
    total_money = sum(total_time) * int(money.get())
    tax_ratio = int(tax_rate.get() or 0)
    after_tax_money = total_money * (1 - tax_ratio/100)
    after_tax.config(text = after_tax_money)

    result.config(text = total_money )

result = Label(result_frame, text="0",width=60)
result.pack(side="top",fill="y")

#시작 버튼
btn_start = Button(result_frame, text="결과 보기", command=start,pady=300)
btn_start.pack(side="right", before=after_tax)


root.mainloop()
