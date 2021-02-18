#الحقوق :
import time as mm 
import sys as n 
from colorama import Fore,Style
def slow(M):
     for c in M + '\n':
         n.stdout.write(c)
         n.stdout.flush()
         mm.sleep(1. / 100)
slow(Fore.BLUE+'''

##      ## ######## ########          ########  ########           ######   ######     ###    ##    ## 
##  ##  ## ##       ##     ##         ##     ## ##     ##         ##    ## ##    ##   ## ##   ###   ## 
##  ##  ## ##       ##     ##         ##     ## ##     ##         ##       ##        ##   ##  ####  ## 
##  ##  ## ######   ########  ####### ##     ## ########  #######  ######  ##       ##     ## ## ## ## 
##  ##  ## ##       ##     ##         ##     ## ##                      ## ##       ######### ##  #### 
##  ##  ## ##       ##     ##         ##     ## ##                ##    ## ##    ## ##     ## ##   ### 
 ###  ###  ######## ########          ########  ##                 ######   ######  ##     ## ##    ##   


make by --> d5tr & popeye <--
insta = d_5tr
insta = popeye01010

'''+Fore.RED+Style.BRIGHT)
#------------------------------------------------------------#
#المكتبات :
import socket 
import sys
from geoip import geolite2
import os
import requests 


#------------------------------------------------------------#
# you went is ? :
print('''
[1] information gathering
[2] xss reflected
[3] domin scan 
[4] Guess the tracks

''')
you_went = int(input('enter number ! :'))
#------------------------------------------------------------#
# http or https
print('''
[1] web >> http !
[2] web >> https !
''')

num = int(input('enter number :'))
#------------------------------------------------------------#
#تحميل المكتبات 
os.system('clear')
os.system('pip install geoip')
os.system('pip install colorama')


#------------------------------------------------------------#
#url_website
if you_went == 1:
    # http or https
    print('''
    [1] web >> http !
    [2] web >> https !
    ''')

    num = int(input('enter number :'))
    url_web = input ('enter url website >>>')
    #------------------------------------------------------------#
    # get ip :
    ip = socket.gethostbyname(url_web)

    print(Fore.GREEN+'IP >>>'+' '+ip)
    print(Fore.BLUE+'URL >>>'+' '+url_web)
    print('==========================================')
    #-----------------------------------------------------------#
    #ip_info
    local = geolite2.lookup(ip)
    print(local)
    print('==========================================')
    #-----------------------------------------------------------#

    #port scan :


    def scanner(ip,port):
        try:
            serv = socket.getservbyport(port)
            s = socket.socket()
            s.settimeout(0.3)
            s.connect((ip, port))
            print(Fore.YELLOW+f'[+] port{ port } is open---->'+serv)
        except:
            pass
    for port in range(1,65535):
        scanner(ip,port)

    #--------------------------------------------------------------#
    print('==========================================')
    # robots.txt :

    if num == 1:
        url_for_txt = 'http://'+url_web+'/robots.txt'

        url_robots = requests.get(url_for_txt).status_code

        if url_robots == 200 :
            print('[+] Fond robots.txt ! '+ ' : '+url_for_txt)


        else :
            print('not fond robots.txt !!')

    elif num == 2:
        url_for_txt = 'https://'+url_web+'/robots.txt'

        url_robots = requests.get(url_for_txt).status_code

        if url_robots == 200 :
            print('[+] Fond robots.txt !'+' '+ url_for_txt)


        else :
            print('not fond robots.txt !!')

    #--------------------------------------------------------------#
    print('==========================================')
    #--------------------------------------------------------------#
    #get headers for any website :
    if num == 1:
        http1 = 'http://'+url_web
        print ('headers :')
        response = requests.get(http1)

        headers = response.headers

        html = response.text

        print(html)
    elif num == 2:
        https1 = 'https://'+url_web
        print('headers :')
        r1 = requests.get(https1)
        had = r1.headers
        html2 = r1.text
        print(html2)
    print('==========================================')
    #--------------------------------------------------------------#
    #get cookies :
    if num == 1:
        http2 = 'http://'+url_web
        print('cookies:')
        responsee = requests.get(http2)

        htmll = responsee.cookies

        print(htmll)
    elif num == 2:
        https2 = 'https://'+url_web
        print('cookies :')
        re2 = requests.get(https2)
        html3 = re2.cookies
        print(html3)

    print('==========================================')
    #--------------------------------------------------------------#
elif you_went == 2 :
    # XSS Reflected :

    target = input('enter url+get_name : ')



    payload = str(open(input('enter name file :'), "r"))

    for x in payload:

                                  # شكوك !!!
        req = requests.get(target + x,"html.parser").text

        if payload in req :
            print("[Found XSS ! ]"+req)
        

        else :
            print("[Don't Found XSS !!]")



    #--------------------------------------------------------------#
    # domin scan :
elif you_went == 3:
    hosts = str (input('enter domin , url :'))

    filee = open(input('enter name file :'))
    re = filee.read()
    subdomin = re.splitlines()

    for sub in subdomin():
        domin = 'http://'+sub+'.'+hosts 
        print(domin)
        try:
            requ = requests.get(domin, 'html parser')
            if requ.status_code == 200 :
                print('[+] Found ! ' +domin)

        except requests.ConnectionError:
            pass 

        except KeyboardInterrupt:
            print('exit...')
            sys.exit()

    #--------------------------------------------------------------#
    # تخمين مسارات       
elif you_went == 4:            
    hostt = str(input('enter url website >> '))

    wordlist = open(input('enter name file :'),'r')

    r = wordlist.read()

    words = r.splitlines()
                                    #بحث عن لسته حقت url
    try :
        for word in words:
            urll = hostt+"/"+word

            reqq = requests.get(urll,"html.parser")

            if reqq.status_code == 200 :
                print("[+] Fond : "+ urll)

    except:
        print("ERROR ...")
        sys.exit()

    #--------------------------------------------------------------#