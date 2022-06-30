#|/////////////////////////! The Libraries !\\\\\\\\\\\\\\\\\\\\\\\\\|#
try:
    from PyQt5.QtGui       import *
    from PyQt5.QtWidgets   import *
    from PyQt5.QtCore      import *
    import speech_recognition as sr
    from datetime import datetime
    from threading import Thread
    from tkinter import ttk
    import subprocess as sp
    from tkinter import *
    from PIL import Image
    import tkinter as tk
    import webbrowser
    from time import sleep
    from random import choice ,randint
    from wmi import WMI
    from Ui_Act import Ui_MainWindow
    from Developer_Ui import Ui_MainWindow as Developer_Ui
    from ui_splash_screen import Ui_SplashScreen
    from Developer_Ui import Class_Method
    from PIL import Image
    import pyttsx3
    import pyautogui
    import pywhatkit
    import wikipedia
    import requests
    import getpass
    import platform
    import socket
    import psutil
    import uuid
    import sys
    import os
except:
    None



USERNAME = ('Youssef')
BOTNAME = ('Lazeez')

#|/////////////////////////! Graphical User Interface !\\\\\\\\\\\\\\\\\\\\\\\\\|#

class Graphical_User_Interface(tk.Tk):
    """
        Class UI: | Here is The User Interface
    """
    def __init__(self):
        self.T1=Thread(target=self.Start).start()
    def Start(self):
        super().__init__()
        global label
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        app_width= 250
        app_height= 55
        screen_width= self.winfo_screenwidth()
        screen_height= self.winfo_screenheight()
        X = (screen_width ) - (app_width)
        Y = (screen_height ) - (app_height)-40
        self.geometry(f'{app_width}x{app_height}+{int(X)}+{int(Y)}')
        self.attributes('-alpha', 0.8)
        self.configure(bg='black')
        label = ttk.Label(self,background= 'black' ,foreground='White',text=f'Hello,I\'m  !',font = "Verdana 10 bold" )
        label.place(x=125, y=28, anchor="center")
        self.mainloop()

#|/////////////////////////! GREET USER !\\\\\\\\\\\\\\\\\\\\\\\\\|#

counter = 0
jumper = 0
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.progressBarValue(0)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)
        self.show()
    
    def progress (self):
        global counter
        global jumper
        value = counter

        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
 
            self.ui.labelPercentage.setText(newHtml)
            jumper += 3

        if value >= 100: value = 1.000
        self.progressBarValue(value)

        if counter > 100:

            self.timer.stop()
            self.main = UI_ACT()
            self.main.show()

            self.close()
        counter += 0.1

    def progressBarValue(self, value):

        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgress.setStyleSheet(newStylesheet)
    


#|///////////////////////! Ui_Activation !\\\\\\\\\\\\\\\\\\\\\\\|#

HDD_Serial_Number = WMI().Win32_PhysicalMedia()[0].wmi_property('SerialNumber').value.strip()
current_machine_id = sp.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
__ACT__ID__ = (hex(uuid.getnode()) + HDD_Serial_Number + current_machine_id)
codeA =int(randint(1000000,9999999))
codeB =int(randint(1000000,9999999))
KEY__ = 2*codeA + 30 +3* codeA + 50+ 6*codeA +30
print(KEY__)
class UI_ACT(QMainWindow, Ui_MainWindow):
    def __init__(self):
        try:
            Pss  = open(r'C:/windows/System32/config/Act.txt').read()
            if __ACT__ID__ == Pss:
                self.Greet_user()
                
            else:
                self.Ui_Act__()
                
        except Exception as er:
            print(er)
            self.Ui_Act__()
            

            
    def Ui_Act__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        Class_Method.Speak("Please contact the developer to get the activation code")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.movie = QMovie(":/image/IMGE/GIF____LZ.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.pushButton.setShortcut('Return')
        self.pushButton_2.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(lambda: self.Submit())
        self.pushButton_3.clicked.connect(lambda: self.open_dv())
        self.label_3.setText('Code A: ' + str(codeA))
        self.label_4.setText('Code B: ' + str(codeB))



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Enter:
            self.Submit()
        elif event.key() == Qt.Key_Backspace:
            self.open_dv()
    def open_dv(self):
        self.win = QMainWindow()
        self.ui = Developer_Ui()
        self.ui.setupUi(self.win)
        self.win.show()
    def Submit(self):
        pw = self.lineEdit.text()
        if pw == str(KEY__):
            self.f= open(r"C:/windows/System32/config/Act.txt","w+")
            self.f.write(__ACT__ID__)
            self.f.close()
            self.close()
            Say(f"you access SIR")
            self.Greet_user()

        elif len(pw) == 0:
            Class_Method.Speak("Please Entry Code Activation")
            self.label_5.setText("Please Entry Code Activation")

        else:
            Class_Method.Speak("Code Activation Error")
            self.label_5.setText("       Code Activation Error")
        self.lineEdit.setText("")

    def Greet_user(self):
        #super().__init__()
        QMainWindow.__init__(self)
        Thread(target=self.Greet).start()
        self.setObjectName("MainWindow")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet("background-color: rgb(5,1,23,255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.setCentralWidget(self.centralwidget)
        self.movie = QMovie(":/image/IMGE/end.gif")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMovie(self.movie)
        self.movie.start()
        self.showFullScreen()


    def Greet(self):
        hour = (datetime.now().hour)
        if (hour >= 0) and (hour < 12):
           Say(f"Good Morning {USERNAME}")
        elif (hour >= 12) and (hour < 18):
                Say(f"Good afternoon {USERNAME}")
        elif (hour >= 18) and (hour < 24):
            Say(f"Good Evening {USERNAME}")
        Say(f"I am {BOTNAME}. How may I assist you?")
        self.close()
        Main_Start()

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    
#|/////////////////////////!   Listening   &   Say    !\\\\\\\\\\\\\\\\\\\\\\\\\|#

class Listening():
    """
        Class Listening: | Here There is The Task of Listening To Speech
    """
    def __str__(self) -> str:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                label.configure(text="Listening...")
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source , phrase_time_limit=5)
                
                print("Recognizing..")
                label.configure(text="Recognizing..")
                self.query = r.recognize_google(audio,language="en-US")
                self.query = str(self.query)
                self.query = self.query.lower()
                print(f"You Said :{self.query}")
        except:
            return Listening().__str__()

        return self.query


class Say():
    """
        Class Say: | Here is The Task of Speaking
    """
    def __init__(self,audio):
        super().__init__()
        self.Definition()
        try:label.configure(text=audio)
        except:None
        print(audio)
        self.engine.say(audio)
        self.engine.runAndWait()
    def Definition(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        self.engine.setProperty('rate',170)

#|/////////////////////////!!!      Functions      !!!\\\\\\\\\\\\\\\\\\\\\\\\\|#
Name_Pc = getpass.getuser()
Paths = {
    'notepad' :"C:\\Program Files\\Notepad++\\notepad++.exe",
    'run_dir' : f"C:\\Users\\"+Name_Pc+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run",
    'my_computer_dir' :f"C:\\Users\\"+Name_Pc+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer",
    'Visual Studio Code' :f"C:\\Users\\"+Name_Pc+"\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'Telegram_dir' :f"C:\\Users\\"+Name_Pc+"\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    'discord' :f"C:\\Users\\"+Name_Pc+"\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe",
    'opera_dir' :f"C:\\Users\\"+Name_Pc+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Opera Browser",
    'League of Legends' :"D:\\Riot Games\\Riot Client\\RiotClientServices.exe",
    'google_chrome' :"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'Team_Viewer' :"D:\\Telegram Desktop\\Telegram.exe",
    'my_computer_dir_D' :"D:",
}
Key_words = [
    "how are you sir",
    "I'm fine, and you, sir",
    "I'm at my best",
    "I'm fine, how are you?",
    "I'm good sir and you?",
]
GREETINGS = [f"hello {BOTNAME}", f"{BOTNAME}", f"wake up {BOTNAME}", f"you there {BOTNAME}", f"time to work {BOTNAME}", f"hey {BOTNAME}",f"are you there {BOTNAME}"]
GREETINGS_RES = ["always there for you sir", "i am ready sir","your wish my command", "how can i help you sir?", "i am online and ready sir"]

class Functions:
    """
        Class Functions: | Here There Are All The Tasks
    """


#|/////!!!  help  !!!\\\\\|#
    def i_help():
        text_help = open(r'C:\Users\Youssef\Desktop>', "w+")
        text_help.write("""what is your name هيقلك اسمو\n
                            i want to change your name لو عايز تغير اسمو\n
                            what the time هيقلك الساعه بي الثانيه""")
        text_help.close()
        pass

#|/////!!!  Open_App & Open_URL & Close_App  !!!\\\\\|#
    
    def Open_App(Name_path):
        try:
            os.startfile(Paths[Name_path])
        except:
            Say("The path Error")
    
    def Open_URL(URL):
        webbrowser.open_new(URL)

    def Close_App(Name_App):
        os.system(f"TASKKILL /F /IM {Name_App}")


#|/////!!!  Time & Date & Year & Month & Day  !!!\\\\\|#
    
    def time():
        Time = datetime.now().strftime("%I:%M:%S")
        Say(f"sir , the time is {Time}")

    def date():
        year = int(datetime.now().year)
        month = int(datetime.now().month)
        day = int(datetime.now().day)
        Say(f"sir the date is. {day} {month} {year} ")

    def year():
        year = int(datetime.now().year)
        Say(f"sir the year is {year}")

    def month():
        month = int(datetime.now().month)
        Say(f"sir the month is {month}")

    def day():
        day = datetime.now().strftime("%A")
        Say(f"sir the day is {day}")


#|! Ip & Send_Whatsapp & get_Weather & get_News & get_Joke & Nasa_News & Search_in_Windows !|#
    
    def find_my_ip():
        ip_address = requests.get('https://api64.ipify.org?format=json').json()
        return ip_address["ip"]

    def send_whatsapp_message(number, message):
        pywhatkit.sendwhatmsg_instantly(f"+20{number}", message)

    def get_weather_report(city):
        OPENWEATHER_APP_ID = ("18c11d697932b3daa3363bfaa0e4bc9b")
        res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
        weather = res["weather"][0]["main"]
        temperature = res["main"]["temp"]
        feels_like = res["main"]["feels_like"]
        return weather, f"{temperature}℃", f"{feels_like}℃"

    def get_latest_news():
        NEWS_API_KEY = ("35a434db479844ecbb20a76d7a100222")
        news_headlines = []
        res = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
        articles = res["articles"]
        for article in articles:
            news_headlines.append(article["title"])
        return news_headlines[:5]

    def get_random_joke():
        headers = {
            'Accept': 'application/json'
            }
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        return res["joke"]

    def Nasa_News():
        try:
            Say("Extracting Data from Nasa .")
            API_KAY = ('h7RViL5uB6xX9Ugm0DC6e1ZfCO51vBQ2VBVGZRBV')
            Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(API_KAY)
            Params = {'date':str()}
            r = requests.get(Url,params= Params)
            Data = r.json()
            Info = Data['explanation']
            Title = Data['title']
            Image_Url = Data['url']
            Image_r = requests.get(Image_Url)
            FileName = str() + 'C:\\Nasa.jpg'
            with open (FileName,'wb') as f:
                f.write(Image_r.content)
            Path = (FileName)
            img =Image.open(Path)
            img.show()
            Say(f"Title: {Title}")
            Say(f"According To Nasa: {Info}")
            os.remove(Path)
        except:
            Say("Error: in nasa news Sir")
    
    def search_in_windows(name_file):
        sp.Popen(f'explorer /root,"search-ms:query={name_file}&crumb=location:"&"')


#|/////!$ Information: | System & CPU & Memory & Hard_Disk & Network  !!!\\\\\|#
    
    def System_information():
        print("="*40, "System Information", "="*40)
        Say("i show you System Information  sir ..")
        uname = platform.uname()
        Say(f"System: {uname.system}")
        Say(f"Node Name: {uname.node}")
        Say(f"Release: {uname.release}")
        Say(f"Version: {uname.version}")
        Say(f"Machine: {uname.machine}")
        Say(f"Processor: {uname.processor}")
        Say(f"Ip-Address: {socket.gethostbyname(socket.gethostname())}")
        
    def Boot_Time():  
        print("="*40, "Boot Time", "="*40)
        Say("i will show Information about  Boot Time sir ")
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        Say(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        
    def CPU_information():
        print("="*40, "CPU Info", "="*40)
        Say("CPU Info Physical cores ")
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        cpufreq = psutil.cpu_freq()
        Say(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        Say(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        Say(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        Say("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            Say(f"Core {i}: {percentage}%")
        Say(f"Total CPU Usage: {psutil.cpu_percent()}%")
        
    def CPU_frequencies():
            cpufreq = psutil.cpu_freq()
            Say(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            Say(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            Say(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        
    def CPU_usage():
            Say("CPU Usage Per Core:")
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                Say(f"Core {i}: {percentage}%")
            Say(f"Total CPU Usage: {psutil.cpu_percent()}%")
    
    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
    
    def Memory_information():
            print("="*40, "Memory Information", "="*40)
            Say("Memory Information")
            svmem = psutil.virtual_memory()
            Say(f"Total: {Functions.get_size(svmem.total)}")
            Say(f"Available: {Functions.get_size(svmem.available)}")
            Say(f"Used: {Functions.get_size(svmem.used)}")
            Say(f"Percentage: {svmem.percent}%")
        
    def Disk_Information():
        print("="*40, "Disk Information", "="*40)
        Say("Disk Information")
        Say("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            Say(f"Device: {partition.device}")
            Say(f"Mountpoint: {partition.mountpoint}")
            Say(f"File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            Say(f"Total Size: {Functions.get_size(partition_usage.total)}")
            Say(f"Used: {Functions.get_size(partition_usage.used)}")
            Say(f"Free: {Functions.get_size(partition_usage.free)}")
            Say(f"Percentage: {partition_usage.percent}%")
        disk_io = psutil.disk_io_counters()
        Say(f"Total read: {Functions.get_size(disk_io.read_bytes)}")
        Say(f"Total write: {Functions.get_size(disk_io.write_bytes)}")
        
    def Network_information():
        print("="*40, "Network Information", "="*40)
        Say("Network Information")
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                Say(f"Interface: {interface_name}")
                if str(address.family) == 'AddressFamily.AF_INET':
                    Say(f"IP Address: {address.address}")
                    Say(f"Netmask: {address.netmask}")
                    Say(f"Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    Say(f"MAC Address: {address.address}")
                    Say(f"Netmask: {address.netmask}")
                    Say(f"Broadcast MAC: {address.broadcast}")
        
    def Internet_usage():
        net_io = psutil.net_io_counters()
        Say(f"Total Bytes Sent: {Functions.get_size(net_io.bytes_sent)}")
        Say(f"Total Bytes Received: {Functions.get_size(net_io.bytes_recv)}")


#|/////////////////////////!!!      Main Start      !!!\\\\\\\\\\\\\\\\\\\\\\\\\|#

class Main_Start():
    def __init__(self):
        super().__init__()
    
######################################################################################################################################
        Graphical_User_Interface()
        while True:
                query = Listening().__str__()

                if 'how are you' in query or 'how are you today' in query:
                    Say(choice(Key_words))

                elif 'i help' in query or 'help' in query:
                    Functions.i_help()
                    Say('done sir')

                elif query in GREETINGS:
                        Say(choice(GREETINGS_RES))

                elif 'what is your name' in query or "what's your name" in query:
                    try:
                        Say(f"I am {BOTNAME}")
                    except:
                        Say("Please put a name for me")

                    query = Listening().__str__()
                    if 'put the name' in query or 'put the name is' in query or 'make the name' in query:
                        query = query.replace("put the name", "")
                        query = query.replace("put the name is", "")
                        query = query.replace("make the name", "")
                        BOTNAME = query.upper()
                        Say(f"My new name is {BOTNAME}")
                
                elif 'i want to change your name' in query or 'change your name' in query:
                    Say("What is the new name sir?")
                    query = Listening().__str__().upper()
                    BOTNAME = query
                    Say(f"My new name is {BOTNAME}")


#|//////////!!!      TIME      !!!\\\\\\\\\\|#

                elif 'the time' in query:
                        Functions.time()
                    
                elif 'the day' in query:
                        Functions.day()
                    
                elif 'the month' in query:
                        Functions.month()
                    
                elif 'the year' in query:
                        Functions.year()
                    
                elif 'the date' in query:
                        Functions.date()


#|//////////!!!     OPEN App    !!!\\\\\\\\\\|#

                elif 'open calculator' in query:                            
                                        os.system('calc.exe')
                                        Say("calculator is open sir ..")
                    
                elif 'open notepad' in query:
                                        Functions.Open_App("notepad")
                                        Say(" Notepad++ open .... sir .., ...what do you want me to do ")
                    
                elif 'open cmd' in query or 'cmd open' in query or 'open command prompt' in query:
                                        os.system('start cmd')
                                        Say(" cmd open .... sir .., ...what do you want me to do ")
                    
                elif 'open run' in query:
                                        Functions.Open_App("run_dir")
                                        Say(" Run open .... sir .., ...what do you want me to do ")
                    
                elif 'open my computer' in query:
                                        Functions.Open_App("my_computer_dir")
                                        Say("your computer open .... sir ..")
                    
                elif 'open d' in query:
                                        Functions.Open_App("my_computer_dir_D")
                                        Say("your D open .... sir ..")
                    
                elif 'open control panel' in query:
                                        os.system('start Control Panel')
                                        Say(" Control Panel open .... sir .., ...what do you want me to do ")

                elif 'open google chrome' in query:
                                        Functions.Open_App("google_chrome")
                                        Say("open google chrome..sir..what do you want me to do ")

                elif 'open visual studio' in query or 'open code' in query:
                                        Functions.Open_App("Visual Studio Code")
                                        Say("Visual Studio Code open .... sir .., ...what do you want me to do ")

                elif 'open telegram' in query:
                                        Functions.Open_App("Telegram_dir")
                                        Say(" Telegram open .... sir .., ...what do you want me to do")

                elif 'open opera' in query:
                                        Functions.Open_App("opera_dir")
                                        Say(f"okay professor {USERNAME}")

                elif 'open team viewer' in query or 'open teamviewer' in query:
                                        Functions.Open_App("Team_Viewer")
                                        Say(f"okay professor {USERNAME}")

                elif 'open league of legends' in query:
                                        Functions.Open_App("League of Legends")
                                        Say(f"okay professor {USERNAME}") 

                elif 'open youtube' in query:
                                        Functions.Open_URL("https://www.youtube.com/")
                                        Say(f"okay professor {USERNAME}")

                elif 'open facebook' in query:
                                        Functions.Open_URL("https://www.facebook.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open instagram' in query:
                                        Functions.Open_URL("https://www.instagram.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open twitter' in query:
                                        Functions.Open_URL("https://www.twitter.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open github' in query:
                                        Functions.Open_URL("https://www.github.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open stack overflow' in query or 'open steak overflow' in query:
                                        Functions.Open_URL("https://stackoverflow.com")
                                        Say(f"okay professor {USERNAME}")
                
                elif 'open yahoo' in query:
                                        Functions.Open_URL("https://www.yahoo.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open gmail' in query:
                                        Functions.Open_URL("https://mail.google.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open amazon' in query:
                                        Functions.Open_URL("https://www.amazon.com")
                                        Say(f"okay professor {USERNAME}")

                elif 'open camera' in query:
                                        sp.run('start microsoft.windows.camera:', shell=True)
                                        Say("camera open... sir")

                elif 'open paint' in query:
                                        os.system("mspaint.exe")
                                        Say(f"okay professor {USERNAME}")


#|//////////!!!      CLOSE      !!!\\\\\\\\\\|#

                elif 'close the app' in query:
                                pyautogui.hotkey('alt','f4')
                                Say("done... sir..")

                elif 'close league of legends' in query or 'exit league of legend' in query:
                                Functions.Close_App("RiotClientServices.exe")
                                Functions.Close_App("LeagueClient.exe")
                                Say("done... sir..")

                elif 'close visual studio' in query or 'close code' in query or 'exit visual studio' in query:
                                Functions.Close_App("code.exe")
                                Say("done... sir..")

                elif 'close team viewer' in query or 'close teamviewer' in query or 'exit teamviewer' in query:
                                Functions.Close_App("TeamViewer.exe")
                                Say("done... sir..")

                elif 'close google chrome' in query or 'close chrome' in query or 'exit google' in query:
                                Functions.Close_App("chrome.exe")
                                Say("done... sir..")

                elif 'close calculator' in query or 'exit calculator' in query:
                                Functions.Close_App("Calculator.exe")
                                Say("done... sir..")

                elif 'close notepad' in query or 'exit notepad' in query:
                                Functions.Close_App("notepad++.exe")
                                Say("done... sir..")

                elif 'close paint' in query or 'exit paint' in query:
                                Functions.Close_App("mspaint.exe")
                                Say("done... sir..")

                elif 'close cmd' in query or 'close command prompt' in query or 'exit cmd' in query:
                                Functions.Close_App("cmd.exe")
                                Say("done... sir..")


#|//////////!!!      Tasks      !!!\\\\\\\\\\|#

                elif 'what is ip address' in query:
                    Say(f"okay professor {USERNAME}")
                    ip_address = Functions.find_my_ip()
                    Say(f'Your IP Address is {ip_address}')

                elif 'get news' in query or 'get me news' in query:
                    Say(f"okay professor {USERNAME}")
                    Say(f"I'm reading out the latest news headlines, sir")
                    Say(Functions.get_latest_news())
                    Functions.get_latest_news()

                elif 'space news' in query or 'nasa news' in query:
                    Say(f"okay professor {USERNAME}")
                    Functions.Nasa_News()

                elif 'the weather' in query:
                    Say(f"okay professor {USERNAME}")
                    ip_address = Functions.find_my_ip()
                    city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                    Say(f"Getting weather \n report for your city \n {city}")
                    weather, temperature, feels_like = Functions.get_weather_report(city)
                    Say(f"The current \n temperature is {temperature}, but it feels like {feels_like}")
                    Say(f"Also, the weather report talks about {weather}")
                    Say("For your convenience,\n I am printing it on the screen sir.")
                    Say(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

                elif 'send whatsapp message' in query: # عاوز ابحث بالاسم  i need search to name
                    Say("Speak the number: ")
                    query_number =  Listening().__str__()
                    Say("What is the message sir?")
                    query_message =  Listening().__str__()
                    Functions.send_whatsapp_message(query_number, query_message)
                    Say("I've sent the message sir.")

                elif 'get a joke' in query or 'get me joke' in query:
                    Say(f"okay professor {USERNAME}")
                    Say(f"Hope you like this one sir")
                    joke = Functions.get_random_joke()
                    Say(joke)
                    Say("hahah......hahaha")

                elif "wikipedia" in query:
                    name = str(query).replace("wikipedia","")
                    result = wikipedia.summary(name,sentences=1)
                    Say(result)

                elif "google search" in query:
                    query = str(query).replace("google search","")
                    pywhatkit.search(query)
                    Say(f"searching for: {query} sir..")



#|//////////!!!      SYSTEM CONTROL      !!!\\\\\\\\\\|#
                
                elif 'take a screenshot' in query or 'screenshot' in query:
                                pyautogui.hotkey('winleft', 'prtscr')
                                Say("done sir")
                
                elif 'task manager' in query:
                                pyautogui.hotkey('ctrl','shift','esc')
                                Say(f"okay professor {USERNAME}")
                
                elif 'shut down system' in query or 'shut down the system' in query:
                                Say("are you sure...{USERNAME}")
                                query = Listening().__str__()
                                if 'yes' in query:
                                    Say(f"Goodbye {USERNAME}..")
                                    os.system("shutdown /s /t 5")
                                
                                elif 'no' in query:
                                    Say(f"okay {USERNAME}")

                                else:
                                    print("error")

                elif 'restart system' in query:
                                Say("are you sure...{USERNAME}")
                                query = Listening().__str__()
                                if 'yes' in query:
                                    Say(f"okay {USERNAME}... the computer is restarting now ..")
                                    os.system("shutdown /r /t 5")
                                
                                elif 'no' in query:
                                    Say(f"okay {USERNAME}")

                                else:
                                    print("error")
                                
                elif 'sleep system' in query:
                                Say("are you sure...{USERNAME}")
                                query = Listening().__str__()
                                if 'yes' in query:
                                    Say(f"okay {USERNAME}... the computer is sleeping now ..")
                                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                                
                                elif 'no' in query:
                                    Say(f"okay {USERNAME}")

                                else:
                                    print("error")
                
                elif 'settings windows' in query:
                                pyautogui.hotkey('winleft', 'i')
                                Say(f"okay professor {USERNAME}")

                elif 'close tab' in query:
                                pyautogui.hotkey('ctrl', 'w')
                                Say("done sir")
                
                elif 'open new tab' in query:
                                pyautogui.hotkey('ctrl','t')
                                Say("done sir")
                
                elif 'switch the window' in query:
                                pyautogui.keyDown("alt")
                                pyautogui.press("tab")
                                sleep(1)
                                pyautogui.keyUp("alt")
                                Say('okay sir')

                elif 'switch the tab' in query:
                                pyautogui.keyDown('ctrl')
                                pyautogui.press("tab")
                                Say("done sir")

                elif 'search in windows' in query:
                                Say("What do you want to search for? Sir")
                                query =  Listening().__str__()
                                Functions.search_in_windows(query)
                                Say(f"Searching in Windows at! {query}")
                                Say(f"working on it.. {USERNAME}")

                elif 'volume up' in query:
                                pyautogui.press("volumeup")
                                Say("done sir")
                
                elif 'volume down' in query:
                                pyautogui.press("volumedown")
                                Say("done sir")

                elif 'volume mute' in query:
                                Say("done sir")
                                pyautogui.press("volumemute")

                elif 'up' in query:
                                x = 1
                                while x <= 27:
                                    pyautogui.keyDown('up')
                                    x +=1
                                Say("done sir")
                
                elif 'down' in query:
                                x = 1
                                while x <= 27:
                                    pyautogui.keyDown('down')
                                    x +=1
                                Say("done sir")

                elif 'boot time' in query:
                                Functions.Boot_Time()

                elif 'system information' in query:
                                Functions.System_information()

                elif 'cpu information' in query:
                                Functions.CPU_information()

                elif 'cpu frequencies' in query:
                                Functions.CPU_frequencies()

                elif 'cpu usage' in query:
                                Functions.CPU_usage()

                elif 'memory information' in query:
                                Functions.Memory_information()

                elif 'hard disk information' in query:
                                Functions.Disk_Information()

                elif 'network information' in query:
                                Functions.Network_information()

                elif 'internet usage information' in query:
                                Functions.Internet_usage()

                elif "go to sleep" in query:
                    Say("i go sleep sir .. ")
            
            
                else:
                    label.configure(text=f"I did not understand: {query}")
                    sleep(1.0)



#|//////////!!!      Run      !!!\\\\\\\\\\|#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
