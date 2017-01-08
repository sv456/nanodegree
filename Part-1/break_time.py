import webbrowser
import time
break_total=3
break_count=0
while(break_count<break_total):
    print "this program started on:"+time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=0zGcUoRlhmw")
    time.sleep(10)
    break_count+=1
