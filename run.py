import requests,json,os,sys,random,time,re,calendar
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

from rich import pretty
from rich.panel import Panel
from rich import print as print
from rich.console import Console
from rich.console import Console as sol


console = Console()
tokenku=[]
sys.stdout.write('\x1b]2; Dump ID Facebook\x07')

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
        banner()
        Console().print(Panel("""[bold white]Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account """,width=80,style=f"{color_panel}", title="SARAN"))
        your_cookies = console.input(f" {H2}• {P2}Masukan Cookie : ")
        with requests.Session() as r:
            try:
                r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
                data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop('content-type')
                r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print(" [+] Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
                    r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop('content-type');r.headers.pop('origin')
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
                        data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop('content-type');r.headers.pop('origin')
                        r.headers.update({'referer': 'https://m.facebook.com/',})
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            Console().print(Panel(f"""[bold cyan][+] Token : [bold green]{access_token}""",width=80, style=f"{color_panel}", title="[bold green]>[hot_pink2] (PILIHAN) [bold green]<"))
                            tokenew = open(".token.txt","w").write(access_token)
                            cook= open(".cok.txt","w").write(your_cookies)
                            
                            Console().print("[bold cyan]  ─> [bold green]Login Berhasil, jalankan Ulang File[bold white]")
                           

            except Exception as e:
                Console().print(f"[bold cyan]   ╰─>[bold red] Cookies Mokad Bang")
                os.system('rm -rf .token.txt && rm -rf .cok.txt')
                print(e)
                time.sleep(3)
                exit()
    except:pass

def publikv2():
    with requests.Session() as ses:
        banner()
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        a = console.input(f" {H2}• {P2}Masukan Id Target : ")
        filetex = console.input(f" {H2}• {P2}Nama File Dump  : ")
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
                print('\r  Mengumpulkan %s Id'%(len(id)),end='')
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
