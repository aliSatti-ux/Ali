import os
import sys
sys.stdout.write('\x1b]2;😘TERMUX GAME🔰\x07')
logo2 = ("""

 ████╗   ███╗    ███████╗
████╗ ████║    ██╔════╝
██╔████╔██║    ███████╗
██║╚██╔╝██║    ╚════██║
██║ ╚═╝ ██║    ███████║
╚═╝     ╚═╝    ╚══════╝ """)

logo3 = ("""
\033[36m
_________          _______  _        _                   _______          
\__   __/|\     /|(  ___  )( (    /|| \    /\  |\     /|(  ___  )|\     /|
   ) (   | )   ( || (   ) ||  \  ( ||  \  / /  ( \   / )| (   ) || )   ( |
   | |   | (___) || (___) ||   \ | ||  (_/ /    \ (_) / | |   | || |   | |
   | |   |  ___  ||  ___  || (\ \) ||   _ (      \   /  | |   | || |   | |
   | |   | (   ) || (   ) || | \   ||  ( \ \      ) (   | |   | || |   | |
   | |   | )   ( || )   ( || )  \  ||  /  \ \     | |   | (___) || (___) |
   )_(   |/     \||/     \||/    )_)|_/    \/     \_/   (_______)(_______)
                                                                          
                                                                          """)


logo4 = ("""\033[35m


██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
 \033[39m                                                     
                                                 

""")



                                                           
logo = ("""       


                         ██████╗  █████╗ ███╗   ███╗███████╗███████╗
                        ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
                        ██║  ███╗███████║██╔████╔██║█████╗  ███████╗
                        ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
                        ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
                         ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
                                                                    

                                                

\033[1;31m┏━━┓━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━┏━━┓
\033[1;31m┃🎭┃   💛\033[46m TERMUX GAME SCRIPT MADE BY MASOOM \033[40m 💛   \033[40m\033[00m\x1b[1;91m┃🎭┃
\033[1;31m┗━━┛━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━┗━━┛
\033[38;5;46m═════════\033[33;1m════════════\x1b[38;5;196m══════════\033[34;1m═════════
\033[34;1m✮⃝ 𝐗𝐘𝐋𝐎𝐍𝄟⃝\x1b[38;5;196m {🤍}\033[38;5;46m\x1b[38;5;196m╔══➻〱𝐍𝐀𝐌𝐄\033[33;1m➽   \033[38;5;46mUsᴇʀ Nᴏᴛ Fᴏᴜɴᴅ
\033[34;1m✮⃝ 𝐗𝐘𝐋𝐎𝐍𝄟⃝\x1b[38;5;196m {🤍}\033[38;5;46m\x1b[38;5;196m╚══➻〱𝐌𝐎𝐁𝐈𝐋𝐄\033[33;1m➽ \x1b[38;5;196m 𝟬𝟭𝟵63\033[31m°\033[32m°\033[33m°\033[34m°\033[36m°\x1b[38;5;196m𝟬
\033[34;1m✮⃝ 𝐗𝐘𝐋𝐎𝐍𝄟⃝\x1b[38;5;196m {🤍}\033[38;5;46m\033[38;5;46m╔══➻〱𝐒𝐓𝐀𝐓𝐔𝐒\033[33;1m➽ \033[34;1m𝐅𝐫𝐞𝐞
\033[34;1m✮⃝ 𝐗𝐘𝐋𝐎𝐍𝄟⃝\x1b[38;5;196m {🤍}\033[38;5;46m\033[38;5;46m╚══➻〱𝐕𝐄𝐑𝐒𝐎𝐍\033[33;1m➽ \033[33;1m𝐯𝟰.𝟱
\033[34;1m✮⃝ 𝐗𝐘𝐋𝐎𝐍𝄟⃝\x1b[38;5;196m {🤍}\033[38;5;46m\033[33;1m╔══➻〱𝐓𝐎𝐎𝐋\033[33;1m➽  \033[33;1m𝐓𝐄𝐑𝐌𝐔𝐗 𝐆𝐀𝐌𝐄
\033[34;1m✮⃝ 𝐗𝐘𝐋𝐎𝐍𝄟⃝\x1b[38;5;196m {🤍}\033[38;5;46m\033[33;1m╚══➻〱𝐅𝐑𝐎𝐌\033[33;1m➽  \x1b[38;5;196mRAWALPINDI
\033[38;5;46m═════════\033[33;1m════════════\x1b[38;5;196m══════════\033[34;1m═════════
""") 
def linex():
	print(f'')
def main():
    os.system('clear');print(logo)
    print(f'\033[32m➽  [𝟭] \x1b[38;5;196m\033[38;5;46m\x1b[38;5;196m╔══➻〱𝐁𝐀𝐒𝐓𝐄𝐑 𝐆𝐀𝐌𝐄              \033[32m[𝟳] \033[35m╔══➻〱𝐂𝐁𝐎𝐀𝐑𝐃 𝐆𝐀𝐌𝐄')
    print(f'\033[32m➽  [𝟮] \033[38;5;46m\x1b[38;5;196m╚══➻〱𝐍𝐄𝐓𝐇𝐀𝐂𝐊 𝐆𝐀𝐌𝐄            \033[32m [𝟴] \033[35m╚══➻〱𝐌𝐎𝐎𝐍-𝐁𝐔𝐆𝐆𝐘 𝐆𝐀𝐌𝐄')
    print(f'\033[32m➽  [𝟯] \033[36m╔══➻〱𝐏𝐀𝐂𝐌𝐀𝐍 𝐆𝐀𝐌𝐄          \033[32m    [𝟵] \033[32m╔══➻〱𝐓𝐓𝐘 𝐆𝐀𝐌𝐄')
    print(f'\033[32m➽  [𝟰] \033[36m╚══➻〱𝐆𝐍𝐀𝐒𝐊𝐈 𝐆𝐀𝐌𝐄         \033[32m    [𝟭𝟬] \033[32m╚══➻〱𝐌𝐘𝐌𝐀𝐍 𝐆𝐀𝐌𝐄')
    print(f'\033[32m➽  [𝟱] \033[33m╔══➻〱𝐙 𝐆𝐀𝐌𝐄')
    print(f'\033[32m➽  [𝟲] \033[33m╚══➻〱𝐒𝐍𝐀𝐊𝐄 𝐆𝐀𝐌𝐄')
    print("\033[36m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱")
    print('')
    print(f'\033[32m➽  [𝐀] \033[34m╔══➻〱𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍')
    print(f'\033[32m➽  [𝐗] \033[34m╚══➻〱𝐄𝐗𝐈𝐓');linex()
    print("\033[36m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱")
    
    t=input('\033[32m[➽] \033[31m𝐒\033[32m𝐄\033[33m𝐋\033[34m𝐄\033[35m𝐂\033[36m𝐓\033[37m 𝐎\033[33m𝐏\033[34m𝐓\033[35m𝐈\033[36m𝐎\033[37m𝐍  \033[32m➽ ')
    if t in ["1","01"]:
        bhoot()    
    if t in ["2","02"]:
        ax()
    if t in ["3","03"]:
        b()    
    if t in ["4","04"]:
        nn()    
    if t in ["5","05"]:
        sb()  
    if t in ["6","06"]:
        pp()   
    if t in ["7","07"]:
        tt() 
    if t in ["8","08"]:
        oo()
    if t in ["9","09"]:
        ll() 
    if t in ["10","10"]:
        gg()                             
    if t in ["x","X"]:
        x()
    if t in ["a","A"]:
        an()    
        
def bhoot():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "bastet game Install please wait."')
    os.system('pkg install bastet')
    os.system('apt install bastet')
    os.system('bastet')
    
    
def ax():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "nethack game Install please wait."')
    os.system('pkg install nethack')
    os.system('apt install nethack')
    os.system('nethack')  

def b():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "greed game Install please wait."')
    os.system('pkg install greed')
    os.system('apt install greed')
    os.system('greed')  

    
def sb():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "z game Install please wait."')
    os.system('pkg install frotz -y')
    os.system('apt install frotz -y')
    os.system('zgames')      
    
def nn():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "gnuski game Install please wait."')
    os.system('pkg install gnuski')
    os.system('apt install gnuski')
    os.system('gnuski')      

def pp():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "snake game Install please wait."')
    os.system('pkg install snake')
    os.system('apt install snake')
    os.system('clear')
    os.system('snake')     

def tt():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "cboard game Install please wait."')
    os.system('pkg install cboard')
    os.system('apt install cboard')
    os.system('cboard')     

def oo():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "moon-buggy game Install please wait."')
    os.system('pkg install moon-buggy')
    os.system('apt install moon-buggy')
    os.system('moon-buggy')     

def ll():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "tty-solitaire game Install please wait."')
    os.system(' pkg install tty-solitaire')
    os.system('apt install tty-solitaire')
    os.system('ttysolitaire')     

def gg():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "myman game Install please wait."')
    os.system('pkg install myman')
    os.system('apt install myman')
    os.system('myman')    

            
def x():
    os.system('clear')
    print(logo3)
    print('Thank For My Tool')
    os.system('exit')


def an():
    os.system('clear');print(logo2)
    os.system('espeak -a 300 "animation tool"')
    print(f'\033[32m➽  [𝟭] \033[32m╔══➻〱𝐓𝐑𝐀𝐈𝐍')
    print(f'\033[32m➽  [𝟮] \033[32m╚══➻〱𝐂𝐌𝐀𝐓𝐑𝐈𝐗')
    print(f'\033[32m➽  [𝟯] \033[33m╔══➻〱𝐅𝐈𝐑𝐄')
    print(f'\033[32m➽  [𝟰] \033[33m╚══➻〱𝐈𝐍𝐅𝐎')    
    print(f'\033[32m➽  [X] EXIT TOOLS ');linex()
    t=input('\033[32m[➽] \033[31m𝐒\033[32m𝐄\033[33m𝐋\033[34m𝐄\033[35m𝐂\033[36m𝐓\033[37m 𝐎\033[33m𝐏\033[34m𝐓\033[35m𝐈\033[36m𝐎\033[37m𝐍  \033[32m➽ ')  
    if t in ["1","01"]:
        am()        
    if t in ["2","02"]:
        ad()   
    if t in ["3","03"]:
        AK()         
    if t in ["4","04"]:
        un()        
    if t in ["x","X"]:
        v()        
def am():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "train animation Install please wait."')
    os.system('apt install sl')
    os.system('sl')
    os.system('python games.py') 
    
          
def ad():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "cmatrix animation Install please wait."')
    os.system('apt install cmatrix')
    os.system('cmatrix')    
    
    
def AK():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "fire animation Install please wait."')
    os.system('pkg install libcaca')
    os.system('pkg install cacafire')
    os.system('cacafire')    
    
    
def un():
    os.system('clear')
    print(logo4)
    os.system('espeak -a 300 "screenfetch animation Install please wait."')
    os.system('pkg install screenfetch')
    os.system('screenfetch')
    print('python games.py')     
  
def v():
    os.system('clear')
    print(logo3)
    print('Thank For My Tool')
    os.system('exit')    
    
    
    
    
    
    
    
    
    
main()