def returnSec(h,m,s):
    return int(h)*3600+int(m)*60+int(s)
def makeoutput(sec):
    h = sec//3600
    sec = sec-h*3600
    m = sec//60
    sec = sec-m*60
    s = sec
    return h,m,s
def matchruleoutput(ans):
    return ans[0] if ans[0] >=10 else '0'+str(ans[0]), ans[1] if ans[1] >= 10 else '0'+str(ans[1]),ans[2] if ans[2] >= 10 else '0'+str(ans[2]),


c_h,c_m,c_s = input().split(':') #str
h,m,s = input().split(':') #start
alltime = returnSec('24','00','00')
rtol,ltor = alltime-abs(returnSec(c_h,c_m,c_s)-returnSec(h,m,s)),abs(returnSec(c_h,c_m,c_s)-returnSec(h,m,s))
ans = makeoutput(ltor) if returnSec(c_h,c_m,c_s) <= returnSec(h,m,s) else makeoutput(rtol)
ans = matchruleoutput(ans)
print(f"{ans[0]}:{ans[1]}:{ans[2]}")
