import time
import webbrowser

total_breaks = 3
break_count = 0

print('This program started on ' + time.ctime())

while break_count < total_breaks:
    time.sleep(15)
    webbrowser.open('https//youtube.com/watch?v=z1b2m_MgahE&t=24s')
    break_count += 1
