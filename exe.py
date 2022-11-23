
# import calendar # 달력
from tkinter import * # GUI 만들기
# import tkinter
# from PIL import Image #이미지 사이즈 변경

# 이미지 사이즈 변경

# img = Image.open('month.png')

# img_resize_lanczos = img.resize((540, 700), Image.LANCZOS)
# img_resize_lanczos.save('month_resize.png')

# # calender 
# def month_calender(year, month):
#     {calendar.month(year, month)}

# print(month_calender(2022, 11))

# print(cal)
schedule = Tk()
schedule.title("calender")
schedule.geometry("540x700")


# schedule.im
image=PhotoImage(file="month.png")
label=Label(schedule, image=image)
label.pack()

schedule.mainloop()


