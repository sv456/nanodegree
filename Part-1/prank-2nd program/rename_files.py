import os

def rename_f():
    files=os.listdir(r"C:\Users\I326017\Desktop\udacity_full_stack\Part-1\prank-2nd program\prank\prank")
    cur_path=os.getcwd()
    print "pointing to "+cur_path
    os.chdir(r"C:\Users\I326017\Desktop\udacity_full_stack\Part-1\prank-2nd program\prank\prank")
    for i in files:
        print "old name:"+i
        print "newname:"+i.translate(None,"0123456789")
        os.rename(i,i.translate(None,"0123456789"))
        print "\n"
    os.chdir(cur_path)
    

rename_f()
