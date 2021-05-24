from datetime import datetime
from playsound import  playsound
n=input("time HH:MM:SS")
hour=n[0:2]
min=n[3:5]
sec=n[6:8]
period=n[8:10].upper()
while True:
      now=datetime.now()
      hour_now=now.strftime("%H")
      min_now=now.strftime("%M")
      sec_now=now.strftime("%S")
      period_now=now.strftime("%p")
      if hour_now==hour:
          if min_now==min:
              if sec_now==sec:
                  if period_now==period:
                       print("wake up")
                       playsound()
                       break
