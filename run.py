import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid,calendar
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        print('• Sedang Menginstall Modul Rich •')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('• Sedang Menginstall Modul stdiomask •')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('• Sedang Menginstall Modul requests •')
	os.system('pip install requests && pip install mechanize ')
#------------------[ IMPORT MODULE ]-------------------#
from time import sleep
from datetime import date,datetime
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as print
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from licensing.models import *
from licensing.methods import Key, Helpers

sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
free=[]
liu=[]
ugent = []
licenseKey=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | Multi Brute Facebook\x07')

#------------[ INDICATION ]---------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
def banner():
    Console().print(Panel("""
      [bold green]Fanky[bold white]
[bold red]███████████████████████             
[bold red]███████████████████████          [bold yellow]Github    : [bold green]https://github.com/Rudal-XD
[bold red]███████████████████████          [bold yellow]Wa        : [bold green]+62895386194***
[bold white]███████████████████████          
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",width=80,style=f"{color_panel}"))
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            publikv2()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print("[bold cyan]   ╰─>[bold red] Problem Internet Connection, Check And Try Again")
            exit()
    except IOError:
        login123()
        
        
def login123():
    try:
        os.system('clear')
        banner() 
        asu = random.choice([m,k,h,b,u])
        cookie=console.input(f' {H2}• {P2}\nMasukkan Cookies :{asu} ')
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        ken = open(".token.txt", "w").write(tok)
        cok = open(".cok.txt", "w").write(cookie)
        console.print(f' {H2}• {P2}LOGIN BERHASIL KONTOL..Jalankan Lagi Perintahnya!!!!');time.sleep(1)
        exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        console.print(f' {H2}• {P2}LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!')


def publikv2():
    with requests.Session() as ses:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        a = console.input(f" {H2}• {P2}Masukan Id Target : ")
        filetex = console.input(f" {H2}• {P2} Nama File Dump  : ")
        rspd  = ('/sdcard/RUDAL-DUMP/' + filetex + '.txt').replace(' ', '_')
        koli = open(rspd, 'w')
        try:
            params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
            b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
            for c in b["friends"]["data"]:
                id.append(c["id"]+"|"+c["name"])
                koli.write(c['id']+'|'+c['name']+ '\n')
                console.print('\r {H2}• {P2}Mengumpulkan %s Id '%(len(id)),end='')
                time.sleep(0.0050)
            console.print(' {H2}• {P2}Total Id Dump : {}'.format(len(id)))
            console.print(' {H2}• {P2}File Disimpan Di %s'%(rspd))
            exit()
        except Exception as e:
            print(e)
            
            
            
            
            
            
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('/sdcard/RUDAL-DUMP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('clear')
	except:pass
	login()
