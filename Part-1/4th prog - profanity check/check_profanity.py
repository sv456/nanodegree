import urllib
def read_text():
    quotes=open(r"C:\Users\I326017\Desktop\udacity_full_stack\Part-1\4th prog - profanity check\movie_quotes.txt")
    content=quotes.read()
    #print content
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    con=urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text_to_check)
    output=con.read()
    #print output
    con.close()

    if "true" in output:
        print "has curse words"

    elif "false" in output:
        print "no curse words,safe to send"

    else:
        print "not sure what's wrong"
    
read_text()
