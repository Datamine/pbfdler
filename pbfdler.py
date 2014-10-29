# John Loeber | www.johnloeber.com | Dec 25, 2013
# instructions: run this script in the directory where you want the comics to be.

import urllib
from time import time
from sys import argv

# to give the user updates on the status of downloads
def timer(start,n,i):
    elapsed = int(round(time() - start))    
    # assuming downloads are sufficiently low-freq. for int-cast to be reasonable.
    # (if the user's internet speed is very fast, then this becomes useless.)
    timeleft = (elapsed/i) * (n-i)
    # minutes elapsed, seconds elapsed, minutes left, seconds left
    t = map(str, [elapsed/60,elapsed%60, timeleft/60, timeleft%60])
    for i in range(0,len(t)):
        if len(t[i])==1:
            t[i]= "0"+t[i]
    return t

def main():
    #set n to the number of comics published so far
    loc = argv[1]
    n = 261
    start = time()
    for i in range(1,n+1):
        x = (float(i)*100)/n
        url = "http://pbfcomics.com/"+str(i)
        inf = urllib.urlopen(url)
        html1 = inf.readlines() 
        #to prevent cases in which pbfcomics/n is just a blank page
        if html1==[]:
            t = timer(start,n,i)
            print("Completion: %.3f%%. Time Elapsed: %s:%s. ETA: %s:%s."
                  " Comic %d skipped (nonexistant)."%(x,t[0],t[1],t[2],t[3],i))
            continue
        html = html1[44]
        imgurlstart = html.index("src=")
        imgurlend = html.index("\" border")
        imgurl = html[imgurlstart+5:imgurlend]
        filename=loc+imgurl[14:]
        urllib.urlretrieve("http://pbfcomics.com" + imgurl, filename)
        t = timer(start,n,i)
        print("Completion: %.3f%%. Time Elapsed: %s:%s. ETA: %s:%s."
              " Comic %d downloaded."%(x,t[0],t[1],t[2],t[3],i))

if __name__=='__main__':
    main()
