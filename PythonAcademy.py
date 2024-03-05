# https://www.w3resource.com/python-exercises/
# https://www.flynerd.pl/2018/06/500-zadan-w-pythonie-i-kazdym-innym-jezyku.html


from calendar import c
from formatter import AS_IS
import inspect
from msilib.schema import Class
from pickletools import read_uint8
from smtplib import SMTP_SSL, _Reply
from tkinter import Y
from turtle import width

server = SMTP_SSL('smtp.gmail.com',465)
server.ehlo()

server.login('myname@gmail.com','password')
server.sendmail('myname@gmail.com','somebody@gmail.com','Hello there!')

smtp.quit()

#Dla podlaczenia do serwera wykorzystylamy klas SMTP_SSL .W jego argumentach podajemy adres port serwera
#Autoryzacja odbywa sie za pomoca metody logowania do ktorej przekzujemy odpowiednio nazwe uzytkownika i haslo 
#Mozesz wyslac listy za pomoca metody sendmail o tej samej nazwie ktora akcepcuje adres nadawcy i jest odbierana
# a takze sam tekst .Zamknac polaczenie za pomoca metody quit()

import psutil
psutil.cpu_count()
psutil.cpu_percent(percpu=True)
[4,3,4,0,2.9,2.2,0.1,0.0,0.0,0.0]
psutil.virtual_memory()
...
psutil.disk_usage('/')
...
psutil.sensors_battery()
...
#Uzyskiwanie informacji o systemie
#Wieloplatformowa biblioteka psutil pozwala uzyskać informacje o procesorze, pamięci, dysku, sieci, czujnikach 
#i uruchomionych procesach w systemie.  Podstawowe przykłady użycia pokazane są na rysunku.
#W praktyce psutil jest przydatny głównie do monitorowania systemu, ograniczania zasobów procesów i zarządzania 
# uruchomionymi procesami.
#Oprócz znanych systemów Windows, MacOS i Linux, biblioteka obsługuje również systemy FreeBSD, OpenBSD, 
# NetBSD, Sun Solaris i AIX.

from pywebcopy import save_website
save_webpage(
    url='http://example-site.com/',
    project_foder='single-page/',
)

save_website(
    url='https://example.com/',
    project_folder='full-website/'
)
#Pobieranie całych stron internetowych
#Najprostszy, ale potężny pakiet pywebcopy pomoże ci sklonować pojedyncze strony internetowe, a nawet całe witryny.
#Funkcja save_webpage pobiera stronę z podanego linku, możesz również podać w argumentach ścieżkę, gdzie zapisać 
# wynik.
#Ale save_website umożliwia rekurencyjne pobieranie całej witryny.  Na przykład, jeśli witryna jest blogiem, skrypt pobiera wszystkie artykuły 
# znajdujące się w witrynie.
#Ale tutaj musisz być ostrożny, takie rekurencyjne pobieranie wyśle ​​​​dużo żądań do serwera i może go mocno załadować, jeśli w witrynie jest 
# dużo stron.
#pywebcopy

import pyqiwi
wallet = pyqiwi.Wallet(token='our_token',number='7921***')
#dostajemy ile jest na koncie
wallet.balance()
#Wysylamy kase komus
payment=wallet.send(pid=99,recipient='7900***',amount=100,
comment='Czesc!')
payment.fields['account'] # wysylamy
payment.sum # suma wyslanej kasy
payment.transaction['state']['code'] # statud oplaty

#Praca z portfelem QIWI
#QIWI ma otwarty interfejs API, który umożliwia wykonywanie wszelkiego rodzaju operacji za pomocą portfela.  Ale pierwszym krokiem jest 
# uzyskanie tokena w celu korzystania z tego interfejsu API.
#Do pracy z QIWI dostępny jest wygodny pakiet pyqiwi.  Klasa Wallet implementuje reprezentację portfela, do argumentów konstruktora 
# przekazujemy otrzymany wcześniej token i nasz numer telefonu.  Saldo można sprawdzić za pomocą metody balance().
#Pieniądze do innego portfela możesz przesłać metodą send(), w której przekazujemy identyfikator dostawcy, numer telefonu odbiorcy, kwotę
#płatności oraz komentarz.
#pyqiwi

statements = [True,True,False]
if any(statements):
    print('Jak minimum jeden argument')
if all(statements):
    print('wszystkie wyrazy do jednego ')
if any(statements) and not all(statements):
    print('feafafj')

#Boolean wszystko i wszystko
#Jednym z wielu powodów, dla których Python jest tak popularnym językiem, jest jego czytelność i ekspresja.  Proponuję rzucić 
# okiem na załączony kod.
#Funkcja any zwraca True, jeśli przynajmniej jedna z przekazanych instrukcji jest prawdziwa, jeśli wszystkie są prawdziwe.
#Moim zdaniem te dwie cechy zasługują na szczególną uwagę właśnie ze względu na łatwość obsługi.
#wszystkie #dowolne

from faker import Faker
faker = Faker('ru_Ru')
faker.name() # imie nazwisko 
faker.addres() # ulica miasto dom
faker.email() # fsfpofa@gmail.com
faker.job() # Organizator czegos tam
print.faker.text() # pencja przeszla miasto 

#Generujemy fałszywe dane
#Faker to lekki pakiet, który umożliwia tworzenie fałszywych danych, które mogą być przydatne jako skróty.
#Na przykład imię i nazwisko, adres, e-mail i metody pracy wygenerują dla Ciebie losowe nazwiska, adresy, e-maile i stanowiska.
#Istnieje również metoda text(), która generuje losowy tekst, ale jak widać w przykładzie, wynik jest bez znaczenia.
#Generalnie w pakiecie jest wiele metod, nierealne jest zademonstrowanie wszystkiego w jednym poście, więc możesz przeczytać więcej w
#  dokumentacji.
#Zaletą jest to, że dane można zlokalizować zgodnie z Twoim językiem.  Na przykład stawiamy rosyjski.
#fałsz

from moviepy.editor import *
#instalujemy wideo 
clip_1=VideoFileClip('video_1.mp4')
clip_2=VideoFileClip('video_2.mp4')
#Laczymy w jednego
final_clip= concatenate_video_clips([clip_1,clip_2])
#przecinamy wideo 
final_clip=final_clip.subclip(30,35)
#zmniejszamy glosnoc wideo
final_clip=final_clip.volumex(0.5)
#pobieramy rezultat
final_clip.write_videofile('output.mp4')

#Edytowanie wideo
#Pakiet moviepy umożliwia wycinanie i wklejanie filmów, dodawanie efektów wideo i edycję dźwięku.
#Ogólnie opakowanie nie jest trudne do zrozumienia, podstawowe zastosowanie pokazano na zdjęciu.  
# W przykładzie otwieramy dwa filmy, łączymy je w jeden, przycinamy powstały klip, zmniejszamy głośność dźwięku i na koniec zapisujemy wynik.
#Należy również zauważyć, że uruchomienie i wykonanie skryptów przetwarzania wideo może zająć stosunkowo dużo czasu.
#Taki pakiet przydaje się w przypadkach, gdy trzeba przetworzyć wiele filmów według tej samej zasady.
#film

print('{0!r:20}'.format('Hello'))
#napisalo 'Hello'
print('{0!s:20}'.format('Hello'))
#napisalo bardziej jasno Hello

#Jawne flagi konwersji
#Flaga jawnej konwersji służy do konwersji wartości pola formatu przed jego bezpośrednim formatowaniem.
#To pole może służyć do zastąpienia zachowania formatu dla określonego typu i sformatowania wartości.  Obecnie powszechne są dwie flagi 
# jawnej konwersji:

# !r — konwertuje wartość na ciąg znaków za pomocą funkcji repr().
# !s — konwertuje wartość na ciąg znaków za pomocą funkcji str().

# W Pythonie najpopularniejszymi metodami formatowania napisów są:
# %-formatting (printf-style String Formatting, stary styl),
# str. format() (nowy styl),
# f-strings (formatted strings, od Pythona 3.6).

# https://chyla.org/artykuly/python/python-tutorial/formatowanie-napisow.html

#W przykładzie, w przypadku flagi !r, w polu o szerokości co najmniej 20 znaków zostanie wydrukowany napis 'Hello', a w przypadku flagi !s 
# zostanie on wydrukowany bez cudzysłowów (w bardziej czytelny formularz).
#linie

from boltons import strutils
strutils.split_punct_ws("Hello,world! Its Python Academy ")
#['Hello','world','It','s','Python','Academy']
strutils.slugify("Hello,world! Its Python Academy")
#'hello_world_it_s_python_academy'
strutils.html2text('<div><a href="#">Hello, <b>world</b>!</href></div>')
#'Hello , world!'
strutils.find_hashtags('Some text #python #strings')
#['python','strings']

# strutils.split_punct_ws
# strutils.html2text
# strutils.find_hashtags


#Niezbędna biblioteka dla każdego projektu

#Jak się okazało, nie wszyscy jeszcze znają topową bibliotekę boltons, która doskonale uzupełnia standardową bibliotekę.  
# Sam regularnie korzystałem z narzędzi stamtąd w ostatnim miesiącu i teraz nie rozumiem, jak wcześniej żyłem bez tego pakietu.
#Nazwa boltons pochodzi od słowa builtins i jest to nazwa wbudowanej już funkcjonalności.  Oznacza to, że programiści bezpośrednio sugerują, 
# e ich biblioteka powinna być domyślną w Pythonie.
#Wewnątrz znajduje się ponad 250 potężnych narzędzi, w tym buforowanie, 2 rodzaje kolejek priorytetowych, zaawansowane narzędzia 
# itertools, struktury danych 2d, wrappery gniazd i wiele innych.
#Jako przykład podam użyteczność strutils.  Pozwala na wykonywanie wszelkiego rodzaju operacji na ciągach i oszczędza czas pisania o kulach.
#Powyższy obrazek pokazuje, jak łatwo podzielić ciąg znaków za pomocą znaków interpunkcyjnych, zrobić ślimak, wyciągnąć tekst z HTML i 
# znaleźć hashtagi w ciągu.
#boltony #struny

import jmespath
jmespath.search('foo.bar',{'foo': {'bar':'baz'}})
#'baz'
jmespath.search('foo.*.name',{'foo':{'bar': {'name': 'one'},'baz':
{'name':'two'}}})
#['one','two']

#Uproszczona praca z JSON
#Wydawałoby się to znacznie prostsze, ale jest jeden interesujący pakiet JMESpath, który pozwala deklaratywnie określić, 
# jak wyodrębnić elementy z dokumentu JSON.
#Główne przypadki użycia są pokazane na obrazku, nie ma tam nic skomplikowanego.  Metoda wyszukiwania akceptuje wzorzec, z którego pobierane
#  są dane, a także słownik (który jest ogólnie podobny do JSON).
#Ogólnie pakiet ma wystarczająco dużo funkcji, więc jest wart przestudiowania i zastosowania w projektach.  Radzę przeczytać więcej w 
# dokumentacji.
#json #jmespath

class Something:
    def set_value(self,value):
        self.value=value
#tworzymy egzemplarz
obj = Something()
#wzywamy metody w objekcie
obj.set_value('one')
#wzywamu metody w klasie
Something.set_value(obj,'two')

#Co oznacza „self” w metodach?

#Podczas wywoływania metod na obiektach sam obiekt jest przekazywany jako pierwszy argument, chyba że jest to metoda statyczna.  I taki argument
#  jest zwykle nazywany self, który początkujący przepisują na zajęciach, nawet nie zastanawiając się nad jego znaczeniem.
#I na szczęście wszystko to dzieje się automatycznie - nie trzeba ręcznie przenosić obiektu.  Aby jednak lepiej zrozumieć ten punkt, możesz 
# wywołać metodę bezpośrednio na klasie i jawnie przekazać obiekt (przykład na obrazku).
#Co więcej, już wewnątrz metody możesz uzyskać dostęp do atrybutów i innych metod obiektu.  Dlatego jest przekazywany dalej.
#       Mówiąc prościej, jeśli odrzucimy wszystkie szczegóły techniczne, możemy powiedzieć, co następuje: self wskazuje, że niejako stosujemy metodę
#  do samego obiektu.
#klas 

from notifiers import get_notifier
#wiadomosc na poczte 
email = get_notifier('email')
email.notify(username='first@example.com',password='qwerty',
to='second@example.com',message='Hey!')

#wiadomosc przez telegram bot 
# https://core.telegram.org/bots/api
# chat_id ----->  https://core.telegram.org/bots/api#getchat
telegram = get_notifier('telegram')
telegram.notify(token='token',chat_id=123456,message='Hello!')

#patrzymy na obowiazkowe argumenty
email.required # {'reqired':['message','to','username','password']}
telegram.required # {'required' : ['message','chat_id','token']}

#Wysyłanie powiadomień uniwersalnych
#Natknąłem się na ciekawy pakiet powiadomień, który umożliwia wysyłanie powiadomień na pocztę, przez bota Telegram, do Slacka i wiele więcej. 
#  Dostępnych jest łącznie 16 dostawców, więcej o nich w dokumentacji.
#Przekazujemy nazwę dostawcy jako ciąg do funkcji get_notifier i otrzymujemy obiekt, z którym możemy pracować.  Powiadomienie można wysłać za 
# pomocą ogólnej metody powiadamiania.
#Jeśli nie jesteś pewien, jakie argumenty musisz przekazać, aby wysłać powiadomienie, możesz je zobaczyć poprzez wymagany atrybut utworzonego 
# obiektu.
#Na przykład w przypadku Telegrama musisz przekazać token bota, identyfikator czatu i samą wiadomość.  W przypadku poczty musisz podać nazwę 
# użytkownika, hasło, adresata, a także wiadomość.
#powiadomienia #powiadomienia

type(...) #<class 'ellipsis'
bool(...) #true
x=[]
x.append(x)
print(x) #[[...]]
def function():
    ...

#Obiekt wielokropka
#W Pythonie istnieje niezwykle interesujący obiekt, który jest oznaczony jako ..., czyli wielokropek.  Ten obiekt nazywa się Ellipsis i jest 
# używany głównie jako skrót dla czegoś, co jeszcze nie zostało zaimplementowane.
#Jest często używany podczas pracy z plasterkami w Numpy, ale można go również znaleźć w zwykłym kodzie.  Na przykład ... występuje okresowo 
# w treści funkcji jako skrót.
#Jeśli rzucimy go na typ danych binarnych, zobaczymy True - to ważny punkt, ponieważ None, który jest w istocie podobny, generuje False.
#elipsa

def foo():
    if not hasattr(foo,'ncalls'):
        foo.ncals=0
    foo.ncals +=1
    print(f'ile razy wylawana funkcja : {foo.ncalls}.')
foo()
#ile razy wylawna funkcja: 1
foo()
#ile razy wylawna funkcja: 2
foo()
#ile razy wylawna funkcja: 3

print(dir(foo))
# [__annotations__ , __call__ , _class__ , __closure__ , __code__ , __code__ , __defaults__ , __delattr__ , __dict__ , __dir__ , __doc__
# , __eq__ , __format__ , __ge__ , __get__ , __getattribute__ , globals__ , __gt__ , __hash__ , __init__ , __init_subclass__ , __kwdefaults__
# , __le__ , __lt__ , __module__ , __name__ , __ne__ , __new__ , __qualname__ , __reduce__ , __reduce_ex__ , __repr__ , __setattr__ , __sizeof__ , 
# '__str__' , '__subclasshook__' , 'ncalls'

#Atrybuty funkcji
#Teraz będzie to szok dla początkujących, ale funkcje to zwykłe obiekty, które po prostu mają zaimplementowaną metodę _call_.  To on pozwala wykonać składnię z wywołaniem przez nawiasy.
#W związku z tym funkcje, podobnie jak inne obiekty, mogą mieć przypisane atrybuty, a nawet inne metody.  Ale teraz dotkniemy tylko atrybutów.
#Alternatywnie w tym przykładzie zaimplementowałem licznik wywołań funkcji, ale bez użycia zmiennych globalnych - wszystko za pomocą atrybutu w obiekcie funkcji.
#Generalnie nie pamiętam żadnego praktycznego zastosowania w produkcji, ale znajomość tego faktu przydaje się do ogólnego zrozumienia budowy języka i struktury obiektów.
#funkcje #obiekty

import tempfile
temp = tempfile.TemporaryFile()
try:
    temp.write(b'Hello !')
    temp.seek(0)
    print(temp.read())
finally:
    temp.close()
#Output: b'Hello !'

#https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile

# Unlike TemporaryFile(), the user of mkstemp() is responsible for deleting the temporary file when done with it.

#Pliki tymczasowe
#Standardowa biblioteka Pythona posiada moduł tempfile, który zawiera klasy i metody do poprawnej pracy z plikami i katalogami tymczasowymi.
#Funkcja TemporaryFile tworzy plik tymczasowy w katalogu systemowym i zwraca obiekt plikopodobny.
#Utworzony plik tymczasowy zostanie automatycznie usunięty po zamknięciu pliku lub przy wyjściu z menedżera kontekstu.
# #Ponadto inne procesy i aplikacje nie będą mogły uzyskać dostępu do tego pliku tymczasowego.
#plik temp

import pytube
import subprocess

#tworzymy objekt YouTube
youtube = pytube.YouTube('https://yotu.be/dQw4w9WgXcQ')

#wybiermay potok dla ladowania nagrania 
video = youtube.streams.filter(res='1080').first()
audio = youtube.streams.filter(only_audio=True).first()

#tworzymy proces ffmeg dla zaladowania  i laczenia potokuw
process_call_str = f'ffmpeg -i "{video.url}" -i "{audio.url}" -c:v copy -c:a aac "{video.title}".mp4'
subprocess.check_call(process_call_str,shell=True)

# https://www.obliczeniowo.com.pl/973

#Łączenie strumieni wideo i audio
#A więc dodatek do poprzedniego posta.
#Ze względu na technologię przesyłania strumieniowego DASH (Dynamic Adaptive Streaming over HTTP) używaną
#  przez YouTube, nie możemy od razu uzyskać wideo w pożądanej jakości ze ścieżką audio ze względu na jej brak w strumieniu.
#Jako rozwiązanie możemy osobno wziąć audio i wideo i połączyć je za pomocą narzędzia ffmpeg.  Aby to zrobić, wybierz żądane strumienie wideo i 
# audio, po czym przekazujemy adresy URL do polecenia, aby zainicjować tworzenie procesu pobierania i łączenia strumieni za pomocą ffmpeg.
#youtube

import textwrap
text = 'The textwrap module can be used to format text for output in situations where pretty-printing is desired.'
textwrap.fill(text,width=20)
#The textwrap module
#can be used to
#format text for 
#output in situations
#where pretty-
#printing is desired 


# Wydaje się, że użyłeś funkcji textwrap.fill() w poprawny sposób. Jednak, w wyniku nie zobaczysz wynikowego tekstu podzielonego na linie o szerokości 7 znaków z powodu braku przypisania rezultatu tej operacji do zmiennej lub braku wyświetlenia go za pomocą funkcji print().
# Spróbuj użyć funkcji print() w celu wyświetlenia rezultatu, a także przypisz wynik operacji textwrap.fill() do zmiennej, aby móc później z niej korzystać, jeśli to konieczne. Oto przykład:
import textwrap

text = 'dfsdfkmsdflsmflksmflsmfslmfslkfmslfm'
wrapped_text = textwrap.fill(text, width=7)
print(wrapped_text)


#https://docs.python.org/3/library/textwrap.html

#Wcześniej pojawił się już post o wbudowanym module textwrap - tam mówiliśmy o tym, jak skrócić tekst do określonej liczby znaków bez łamania w 
# środku wyrazu.
#Ale zaawansowane funkcje pięknego formatowania tekstu nie kończą się na tym.  Moduł posiada również wypełnienie, które pozwala ustawić 
# szerokość tekstu w znakach.
#Jak widać na przykładzie na obrazku, słowa są zawijane do nowych wierszy i nic nie łamie się w środku słowa.
#zawijanie tekstu

hash(42)
#42
hash('hello')
# -4537375484935939
hash((1,2,3))
# 824928473248327
hash(-1) == hash(-2)
#True
hash(float('inf'))
# 314159
hash(float('nan'))
# 0 
hash({})

hashed_value = hash(42)
print("Hash wartości liczbowej:", hashed_value)

hashed_string = hash("Hello, World!")
print("Hash łańcucha znaków:", hashed_string)

import hashlib # modul hash lib

# Przykład haszowania tekstu za pomocą różnych funkcji skrótu z modułu hashlib
text = "Hello, World!"

# SHA-256
hashed_sha256 = hashlib.sha256(text.encode()).hexdigest()
print("SHA-256:", hashed_sha256)

# MD5
hashed_md5 = hashlib.md5(text.encode()).hexdigest()
print("MD5:", hashed_md5)


# https://www.fxmag.pl/artykul/co-to-jest-hashowanie-jak-dziala-algorytm-haszujacy-czy-to-w-ogole-jest-potrzebne-zlamanie-kryptograficznej-funkcji-skrotu-to-mozliwe

#haszowanie
#Hash to liczba całkowita o stałym rozmiarze, która identyfikuje konkretną wartość.  Każda unikalna wartość musi mieć swój własny skrót.
#Istnieje wbudowana funkcja hash() dla wartości haszujących.  Służy głównie do porównywania wartości różnych obiektów – porównywanie hashów 
# jest łatwiejsze i bardziej opłacalne.
#Ale obiekty mutowalne, takie jak listy i słowniki, nie mogą być haszowane - interpreter wyrzuci odpowiedni błąd.
#Nawiasem mówiąc, są tu dwa pisanki.  Hash nieskończoności jest równy pierwszym cyfrom liczby Pi, a skrót funkcji Not a Number wynosi zero.
#Zdarzają się również kolizje: na przykład skróty liczb -1 i -2 są takie same.
#haszysz

raw_text = 'This\nstring\ has\tsome whitespaces\r\n'
character_map = {
    ord('\n'): ' ',
    ord('\t'): ' ',
    ord('\r'): None
}
text = raw_text.translate(character_map)
# ' This string has some whitespaces '

#Sprzątanie linii
#Najczęściej przetwarzanie danych wejściowych ogranicza się do zamiany znaków na duże lub małe litery.  Czasami dane można wyczyścić za pomocą
#  wyrażenia regularnego.
#Ale w przypadkach, gdy zadanie staje się bardziej skomplikowane, możesz zastosować skuteczniejszy sposób jego rozwiązania.  Dzięki słownikowi 
# wartości zastępczych znaków i metodzie tłumaczenia otrzymujesz niezwykle zwięzły kod.
#W tym przykładzie widzimy, jak znaki końca wiersza „\n” i tabulacja „\t” są zastępowane zwykłymi spacjami, a znak „\r” jest całkowicie usuwany
#  z ciągu.
#linie

import httpx
r = httpx.get('https://www.example.org/')
r
#<Response [200 OK]>
r.status_code
#200
r.headers['content-type']
'text/html; charset=UTF-8'
r.text 
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'

#Wysyłanie żądań przez HTTPX

# https://www.youtube.com/watch?v=qAh5dDODJ5k

#Ciekawy pakiet do pracy z żądaniami sieciowymi.  Jak mówią sami programiści, jest to klient HTTP nowej generacji.

#W porównaniu ze zwykłymi żądaniami, httpx ma następujące zalety:
#- Standardowy interfejs synchroniczny, ale jest też obsługa asynchronii
# - Wsparcie dla HTTP/1.1 i HTTP/2
# - Możliwość wysyłania żądań bezpośrednio do aplikacji WSGI i ASGI
# - Pełne wsparcie dla adnotacji typu
# — 100% pokrycia testowego

#Ogólnie bardzo fajna alternatywa dla większości popularnych pakietów, radzę zajrzeć do ich doków.  Mają też samouczek do zaawansowanego użycia.
#httpx

#pip3 install speedtest-cli
import speedtest
st = speedtest.Speedtest()
download_speed=st.download()
print(download_speed / (2**20))
#85.1632678362873
upload_speed = st.upload()
print(upload_speed / (2 ** 20))
#20.93454954395430

#Sprawdzanie szybkości internetu
#Każdy przynajmniej raz sprawdził prędkość swojego Internetu na Speedtest.  I okazuje się, że mają nie tylko stronę internetową i aplikacje, ale także pakiet Pythona dla tego biznesu.
#W przypadku obiektu klasy Speedtest metody download() i upload() podają odpowiednio szybkość pobierania i przesyłania danych.
#Metody podają wynik w bajtach, więc dla jasności przykładu przetłumaczyłem wszystkie dane na megabajty podczas wyprowadzania.
#test prędkośc

#glowna funkcja
def main():
    print('Hello world!')
#wejscie
if __name__ == '__main__':
    main()

#  Jest to użyteczne, gdy chcesz zdefiniować funkcje, które będą dostępne do użycia, ale nie będą automatycznie uruchamiane, gdy moduł jest importowany do innego pliku.

#Punkt wejścia

#Niektóre języki programowania mają funkcje main(), które uruchamiają wykonywanie programu.  Ale w Pythonie cały kod jest wykonywany linia po 
# linii.
#Alternatywnie, wiele osób pisze główną logikę programu w zwykłej funkcji main() i wywołuje ją tylko w warunku if _name_ == '_main_'.  Tutaj 
# warto osobno wyjaśnić, czym jest _name_.
#Zmienna _name_ jest specjalną zmienną, która będzie równa '_main_' tylko wtedy, gdy plik jest uruchamiany jako program główny.  A 
#  importowania jako moduł jest on ustawiony na taką samą nazwę modułu.
#Dzięki temu program będzie działał poprawnie tylko wtedy, gdy uruchomisz go bezpośrednio.  Jeśli zaimportujesz go jako moduł w innym skrypcie,
#  warunek nie zadziała.
#(main)

#pip install qrcode[pil]
import qrcode
image = qrcode.make('https://example.com')
image.save('qr.png')

#Generjemy QRcode
#Prosty, ale wygodny i użyteczny pakiet do tworzenia kodów QR.  Poduszka służy do renderowania obrazów, więc upewnij się, że masz ją 
# zainstalowaną.
#Aby utworzyć obiekt obrazu z kodem QR, musisz wywołać metodę make() i przekazać dane jako argument.  Aby zapisać, musisz zastosować metodę
#  save() do wynikowego obiektu.
#Kolejny pakiet pozwala na tworzenie kodów QR na podstawie zdjęć i w 6 różnych stylach.  Ale o tym wszystkim, a także o zaawansowanych 
# przypadkach użycia, przeczytałeś już w ich dokumentacji.
# #Kod QR

number =20 
number.__add__(5) # 20 + 5 = 25
number.__sub__(15) # 20 - 15 = 5
number.__mul__(3) # 20 * 3 = 60
number.__floordiv__(2) # 20 / 2 = 10

#Warto również zauważyć, że float obsługuje dzielenie z resztą, czyli metodę _div_.  A int ma tylko podział z zaokrągleniem, 
# zaimplementowany w metodzie _floordiv_.
#magia

from contextlib import redirect_stdout
file = open('out.txt','w')
with redirect_stdout(file):
    print('Hey there!')
file.close()
file = open ('out.txt','r')
content = file.read()
file.close()
print(f'File: {content}')
#Output: 
#File: Hey there!

#Przekierowanie wyjścia programu
#Contextlib ma innego fajnego menedżera kontekstu, redirect_stdout, który pozwala przekierować standardowe wyjście programu.
#Menedżer kontekstu przyjmuje argument, w którym możemy określić, gdzie należy przekierować wszystkie dane wyjściowe w kolejnym bloku.
#W ten sposób dane z print() w menedżerze kontekstu zostaną przekierowane do poprzednio otwartego pliku, ponieważ przekazaliśmy go do argumentu redirect_stdout.
#Możemy to zweryfikować, otwierając plik ponownie i odczytując stamtąd dane.
#contextlib

class Salary:
    def __init__(self,pay):
        self.pay = pay
    def get_total(self):
        return self.pay * 12
class Employee:

    def __init__ (self,pay,bonus):
        self.salary = Salary(pay)
        self.bonus = bonus

    def get_salary(self):
        return self.salary.get_total() + self.bonus 

employee = Employee(5000,1000)
print(employee.get_salary()) #70000

#OOP: kompozycja
#Kompozycja to relacja, w której obiekty jednej klasy są powiązane z obiektami innej.  Ten sposób organizowania interakcji między klasami
#  nazywany jest również stowarzyszeniem.
#Z reguły w tym przypadku przedmiotem jednej z klas (w powyższym przykładzie jest to Wynagrodzenie) jest polem innej (Pracownik).  Jak widać, 
# nie ma tu nic skomplikowanego.
#Skojarzone obiekty często mogą się cyklicznie odnosić do siebie, co łamie standardowy mechanizm garbage collection.
#W takim przypadku musisz użyć słabych referencji z modułu słaberef, o czym porozmawiamy później.
#zajęcia #oop

complex(1,3) #(1+3j)
complex(1, 3).real # 1.0
complex(1,3).imag #3.0
abs(complex(3, 4)) #5.0
str(complex(1, 3)) # '(1+3j)'
(3 + 2j) - (2 - 5j) # (1 + 7j)

# https://www.kodolamacz.pl/blog/wyzwanie-python-2-podstawowe-instrukcje/

# Liczba zespolona to j 

#Używanie liczb zespolonych w Pythonie
#Nikogo tutaj nie dziwią takie wbudowane typy, jak int, float i tym podobne.  Ale oprócz nich w Pythonie jest jeszcze jeden dość interesujący 
# typ, a mianowicie złożony.
#W Pythonie liczby zespolone są reprezentowane jako x + iy.  Dokładniej, litera j jest tutaj użyta zamiast litery i, aby uniknąć pomyłki, 
# ponieważ i jest najczęściej zajęte przez pętle.  Python konwertuje liczby rzeczywiste x i y (niezależnie od tego, czy są int, czy float) na 
# liczbę zespoloną za pomocą funkcji complex(x,y).
#Liczbę zespoloną można łatwo przekonwertować na łańcuch za pomocą funkcji str lub jej moduł można obliczyć za pomocą funkcji abs, a metody 
# real i imag można również wykorzystać do uzyskania dostępu do jej części rzeczywistych lub urojonych.
# #Chociaż complex jest typem wbudowanym, zaleca się zaimportowanie modułu cmath, aby ułatwić pracę ze złożonymi operacjami.

 #złożony


import sys 
sys.getsizeof(5) #25
sys.getsizeof(range(0, 10000)) #48
sys.getsizeof([1,2,'c']) #88

# https://www.programiz.com/python-programming/methods/built-in/range -----> range 

#Obliczanie wielkości obiektów

#Aby obliczyć rozmiar obiektu, możemy użyć funkcji getsizeof(object[, default]) z modułu sys.  Ponieważ w Pythonie wszystko jest zasadniczo 
# obiektem, możemy obliczyć rozmiar każdego takiego obiektu w pamięci.
#Chociaż wszystkie obiekty wbudowane zwrócą właściwy rozmiar, generalnie nie powinno to dotyczyć żadnych obiektów niestandardowych.
#Argument domyślny umożliwia określenie wartości, która zostanie zwrócona, jeśli typ obiektu nie zapewnia środków do wyodrębnienia rozmiaru i 
# zgłasza TypeError .
#Funkcja getsizeof wywołuje metodę _sizeof_ obiektu i dodaje dodatkowy narzut odśmiecania pamięci.
#getsizeof


def function (*, a, b ):
    pass
function ('value  for a', 'value for b')
# TypeError: function() takes 0 positional arguments...
function(a='value', b='value 2') # A tak wszystko pracuje 

#Działa tylko z nazwanymi argumentem
#Aby zapewnić, że funkcja może komunikować tylko nazwane argumenty, można użyć argumentu * przed listą nazwanych argumentów.
#Tak więc, jeśli po prostu przetransferujesz dwa argumenty do funkcji, otrzymasz wyjątek TypeErr. Ale jeśli przekaże je jako nazwane argumenty, wszystko będzie działać dobrze.
#Ta technika może być przydatna w celu poprawy zrozumiałości kodu. Tutaj jest całkiem oczywiste, można użyć argumentów pozycji - jeśli je umieścić do *.


import glob 
glob.glob('*.txt')
['first.txt', 'second.txt']
glob.glob('test[0-9].py')
['test1.py', 'test2.py']
glob.glob('selenium/**/', recursive = True)
['selenium/', 'selenium/webdriver/', 'selenium/webdriver/firefox', 'selenium/webedriver/firefox/amd64', 'selenium/webdriver/firefox/x86/']

# Znajdź pliki według szablonu
# Główną cechą modułu glob jest wygodna i zwięzła praca z wyszukiwaniem plików według wzorów. Co więcej, można nawet przechodzić przez książki adresowe rekursywie.
# W tej samej metodzie globu jest podawany szablon do wyszukiwania plików i zwracana jest lista wyników. Wszystkie metody są zgodne z mechanizmem i regułami dopasowania wzorca Unix.
# Ogólnie moduł jest wbudowany, ale w niektórych sytuacjach import może wydać wyjątek. W takim przypadku wystarczy zainstalować go ponownie za pomocą menedżera pakietów pip.


a = [i for i in range(5)]
x = (i for i in range(5))
a # [0, 1, 2, 3, 4]
x # <generator object <genexpr> at 0x100abed60>
for i in x:
    print(i, end=' ') # 0 1 2 3 4 

#Różnica między wyrażeniami generatora a generatorami zbiorów
#Wpisy w pierwszej i drugiej linii powyższego kodu są bardzo podobne, ale różnią się typami nawiasów. W generatorach list są kwadratowe, a w wyrażeniu generatora są okrągłe.
#Wpisując zmienne, można zobaczyć, że wartość zmiennej A jest listą, a zmienna x przechowuje obiekt generatora. I tutaj pojawia się pytanie, co należy wykorzystać.
#Jeśli potrzebujesz wyników, takich jak lista, aby kontynuować uruchamianie programu, użyj generatory kolekcji.
#A jeśli wartości nie muszą być szybko lub wcale nie wiedzą, czy są potrzebne, zaleca się stosowanie generatory, aby nie zajmować zbyt dużej ilości pamięci i nie ładować systemu.


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '({0}, {1})'.format (self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point (x, y)
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)

#Przeciążenie operatora
#Po pierwsze, należy przypomnieć, że metody, które rozpoczynają się i kończą się podwójnym podkreślaniem, nazywane są magią.
#Na przykład, wyższa w klasie punktowej zdefiniowaliśmy __str_, która odpowiada za sposób wyświetlania obiektów klas na ekranie.
#Aby przeciążyć operatora „+”, należy zdefiniować metodę __ADD__. It przyjmuje dwa argumenty, które są dodatkowo odpowiednio roaskami.
#Tak więc, gdy programista zapisuje rekord p1 + p2, interpreter postrzega go jako punkt. __add__(p1, p2). Dla wszystkich operatorów w języku, w tym logicznym, istnieją magiczne metody.


def bubble_sort(array):
    for i in range (len(array), 0, -1):
        for j in range(1, i):
            if array[j - 1] > array[j]:
                tmp = array[j-1]
                array[j-1] = array[j]
                array[j] = tmp 
    return array 
numbers = [4, 2, 1, 3]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

#Bubblesort
#Python ma już wbudowaną funkcję sortowaną () i metodę . sortowaną() do sortowania list, ale bardzo ważne jest, aby wiedzieć co najmniej kilka implementacji.
#Istotą algorytmu jest to, że kilka przejść są wykonywane na tablicy. W przebiegu, pary elementów w tablicy są porównywane w kolejności, a w przypadku niezgodności z wybranym porządkiem, pary są zamieniane. Jeśli pary elementów są we właściwej kolejności, nic się nie dzieje.
#W wyniku pierwszego przejścia, maksymalny element będzie na końcu, czyli pojawi się jak fiolka. Jest to następnie powtarzać aż do momentu posortowania całej tablicy. Ostatni przejazd będzie sortowaną tablicą.


from abc import ABCMetal, abstractmethod
class AbstractClass(metaclass=ABCMetal):
    @abstractmethod
    def method(self):
        pass
class BadExample(AbstractClass):
    pass
child = BadExample()
# TypeError: cant instantiate abstract class
# BadExample with abstract methods method
class GoodExample(AbstractClass):
    def function(self):
        print('Everything is ok')
anotherchild = GoodExample()
# Works well 

#Klasy i metody abstrakcyjne
#W klasie abstrakcyjnej, wspólna część kilku podmiotów jest zwykle realizowana, czyli innymi słowy, jednostka abstrakcyjna.
#Metoda abstrakcyjna jest metodą, która nie ma implementacji w klasie bazowej i musi być wdrożona w klasie następcy.
#Aby stworzyć klasę abstrakcyjną z metodami abstrakcyjnymi, konieczne jest zaimportowanie pomocniczej metaklicy ABCMeta i dekoratora metody abstrakcyjnej z modułu abc.
#Jeśli usuniemy nową klasę z klasy abstrakcyjnej bez zastępowania metod abstrakcyjnych, w tym przypadku i spróbujemy utworzyć instancję, dostajemy wyjątek TypeErr.
#Aby kod działał prawidłowo, musimy ponownie zdefiniować wszystkie abstrakcyjne metody. To znaczy, w rzeczywistości po raz kolejny po prostu napisać metodę, ale już w nowej klasie.
#UPD. W kodzie literowym, w klasie GoodExample metoda powinna być nazywana metodą, a nie funkcją.




from functools import total_ordering
class Number:
    def __init__(self,value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value 
print(Number(20) > Number(3))
print(Number(1) < Number(5))
print(Number(15) >= Number(15))
print(Number(10) <= Number(2))

#Uproszczenie tworzenia operatorów porównania
#Aby tworzyć obiekty z obsługą instrukcji porównań, w klasie zazwyczaj wymagana jest duża liczba metod magii, a mianowicie - ___lt___le__, ____eq__, ______ ne_____ gt_, ______ ge_.
#O tym, co sprawia, że każdy z nich mówi osobny post, ale teraz pokazujemy, jak można znacznie uprościć implementacji tej klasy. Można użyć dekoratora TOTAL_ORDER z pakietu narzędzi funkcyjnych.
#W takim przypadku wystarczy wprowadzić tylko __lt_ i __eq__. Te dwie metody są minimum, że dekorator musi zaprojektować inne metody.


class Number:
    def __init__(self, value):
        self.value = value 
    def __lt__(self, other): # x < y
        return self.value < other.value
    def __le__(self, other): # x <= y
        return self.value <= other.value 
    def __eq__(self, other): # x == y
        return self.value == other.value
    def __ne__(self, other): # x > y
        return self.value != other.value 
    def __gt__(self, other): # x > y 
        return self.value > other.value
    def __ge__(self, other): # x <= y
        return self.value <= other.value 
        
#Porównanie przeciążeń operatora
#W przypadku, gdy trzeba porównać obiekty dowolnej klasy w kodzie, trzeba wdrożyć magiczne metody, które są wywoływane podczas porównywania.
#Na przykład pod maską symbolu < b, nazywa się a.__lt__(b). Każdy operator porównania ma własną magiczną metodę. Więcej informacji na temat metody, za którą odpowiada operator, znajduje się w powyższym kodzie.
#Pisanie wszystkich sześciu metod jest trochę uciążliwe, więc często używać decorator TOTAL_ordering z funcuts. Ostatnio przebywał w poście.

from functools import total_ordering


@total_ordering
class Students:
	def __init__(self, cgpa):
		self.cgpa = cgpa

	def __lt__(self, other):
		return self.cgpa<other.cgpa

	def __eq__(self, other):
		return self.cgpa == other.cgpa

	def __le__(self, other):
		return self.cgpa<= other.cgpa
	
	def __ge__(self, other):
		return self.cgpa>= other.cgpa
		
	def __ne__(self, other):
		return self.cgpa != other.cgpa

Arjun = Students(8.6)

Ram = Students(7.5)

print(Arjun.__lt__(Ram))
print(Arjun.__le__(Ram))
print(Arjun.__gt__(Ram))
print(Arjun.__ge__(Ram))
print(Arjun.__eq__(Ram))
print(Arjun.__ne__(Ram))

# Total_ordering False
# False
# True
# True
# False
# True 

# Moduł Functools w Python pomaga w realizacji funkcji wyższego rzędu. Funkcje wyższego rzędu są zależne od funkcji,
#  które wywołują inne funkcje. TOTAL_ORDER dostarcza bogatych metod porównywania klas, które pomagają porównywać klasy 
#  bez wyraźnego definiowania funkcji dla nich. Tak więc, It pomaga w nadmiarowości kodu.

import shelve
#Zapisane dane 
with shelve.open('data') as shelf:
    shelf['key'] = {'int': 7, 'float': 12.5, 'string': 'something'}
#Czytanie dane 
with shelve.open('data') as shelf:
    print(shelf['key'])

#Minimalna baza danych
#Wbudowany moduł regału umożliwia zapisywanie i odczytywanie dowolnych danych. W ten sposób można zapisać dowolne obiekty Pythona do dalszego użytku.
#Dostęp do danych można uzyskać za pomocą kluczy, jak w przypadku słowników. A metoda shelve.open obsługuje kontekstowy protokół menedżera, czyli nie można wywołać blisko.
#W dokumentacji stwierdza się, że taka baza danych jest „niezawodna”. Jednak ze względu na to, że schroniska są pisane w pikle, powinny być używane tylko w bardzo małych projektach.


import pickle
greetings = {'russian': 'prywit', 'english': 'hello'}
with open ('data.p','wb') as file:
    pickle.dump('greetings' ,file)
with open('data.p','rb') as file:
    data = pickle.load(file)
print(data)

#Zapisz dane binarne
#Moduł PICKLE, o którym wspominaliśmy w poprzednim poście, wdraża protokoły binarne do serializacji i deserializacji obiektów. Możesz zapisać dowolny obiekt, jeśli jest możliwe przekształcenie każdego atrybutu na binarny.
#Ale klasy, funkcje i metody nie zostaną zachowane. Ważne jest również, aby zrozumieć, że podczas zapisywania obiektu zapisywany jest ciąg znaków określający klasę, do której należy obiekt.
#Uważaj jednak, aby pickle nie były chronione przed błędnymi lub złośliwymi danymi. Nigdy nie pobieraj danych z niewiarygodnych lub niezzweryfikować źródeł.


string = 'Hello world!'
string.replace('Hello', 'Goodbye')
# Goodbye, world 
another_string = 'Run Run Run!'
another_string.replace('Run','Stop', 2)
# 'Stop Stop Run!

#Zastąp część tekstową
#It jest bardzo wygodny w pracy z ciągnami Pythona, ponieważ istnieje wiele wbudowanych metod dla nich. Jedną z metod jest str.replace(), który pozwala na wymianę części łańcucha.
#Pierwszy argument przechodzi przez podciąg, który zostanie zmieniony w oryginalnym ciągu. Drugim argumentem jest to, co zostanie zastąpione.
#Istnieje również trzeci, opcjonalny argument, który jest odpowiedzialny za ile razy chcesz zastąpić stary podciąg nowym. Domyślnie wszystkie wpisy są zastępowane.


exit
# Use exit() or Ctrl-D(i.e.EOF) to exit
exit()
#albo 
#import sys 
#try:
    #code 
#except:
#   sys.exit('Error ocurred')

#Zakończenie programu
#Funkcja wyjścia jest przeznaczona do interakcji, ale nie zaleca się jej używania w skryptach.
#W rzeczywistości funkcja podnosi po prostu wyjątek systemExit. Podczas próby wywołania bez nawiasów wypisze wskazówkę na temat właściwego wyjścia z tłumacza.
#It jest warty korzystania sys.exit() ponieważ metoda ta jest w standardowym module i jest zawsze dostępna tam. Jest to również dość oczywisty sposób na zakończenie programu.
1

class Calculator :
    def add(x, y):
        return x + Y
    def substruct(x, y):
        return x - y 
Calculator.add = staticmethod(Calculator.add)
Calculator.add(10, 15)
# 25
Calculator.substruct(30, 20)
# 10

#Metody statyczne
#Metody statyczne różnią się od metod konwencjonalnych, ponieważ są powiązane z klasą, a nie obiektem. Oznacza to, że można je nazwać bezpośrednio w klasie.
#Metoda statyczna nie akceptuje ani obiektu (własnego), ani klasy (cls) w argumentach. Oznacza to, że takie metody nie mogą modyfikować obiektu ani klasy.
#Istnieją dwa sposoby implementacji metody statycznej. Jedną z nich jest przypisanie nowej metody do klasy poprzez bezpośrednie przeniesienie oryginalnej metody do funkcji metody statyczne.
#Ale to nie jest akceptowane, więc najczęściej metoda statyczna jest stosowana jako dekorator przy pisaniu metod bezpośrednio w klasie.


import random 
import heapq 
x = [random.randint(0, 100) for _ in range(100)]
heapq.nsmallest(5, x) # [0, 1, 3, 5, 5]
heapq.nlargest(5, x) # [199, 99, 96, 92]

#Znajdź najmniejszy i największy
#W standardowej bibliotece znajduje się moduł heapq, który, jak sama nazwa wskazuje, wdraża strukturę stosu danych.
#Cechy i korzyści tej struktury danych nie zostaną jeszcze przeanalizowane, ale przyjrzyjmy się dwóm ciekawym metodom w tym module.
#Dzięki najmniejszym i największym, możesz uzyskać najmniejsze i największe elementy na liście.
#Pierwsze argumenty są przekazywane, ile elementów do podjęcia, drugie - lista.


import time 
start_time = time.time()
# Some code ... ( jakis kod )
end_time = time.time()
print('Czas programy : %.2f sekund' %(end_time - start_time))

#Czas wykonania programu
#Często konieczne jest zmierzenie czasu wykonania kodu, aby zrozumieć, w jaki sposób wybrano optymalne rozwiązanie.
#Można również użyć funkcji czasu z modułu czasu, który zwraca bieżący czas w formacie Unix.
#Przed wykonaniem naszego kodu, zapisujemy początkowy czas, a po - ostateczny czas. Poprzez odjęcie pierwszego od drugiego i uzyskanie czasu realizacji programu.
#Użycie Time.Time() nie jest najdokładniejszą i najlepszą opcją, ale na przykład szybkie porównanie dwóch różnych części kodu jest dobre.


from itertools import compress 
letters = ['A', 'B', 'C', 'B', 'D']
mask = [1, 0, 1, 0, 0]
result = compress(letters, mask)
list(result) #['A','C']

#Czyszczenie sekwencji
#Wbudowany moduł iteracji został zaprojektowany do obsługi bardziej złożonych iteratorów. Zaletą modułu jest jego szybkie działanie i optymalizacja pod względem pamięci.
#Czasami konieczne jest usunięcie zbędnych obiektów sekwencji. Z tego powodu używane są iteracje, a mianowicie metoda kompresji.
#Pierwszy argument przechodzi przez kontener, taki jak lista. Drugim argumentem są wartości logiczne odpowiadające danym elementem w sekwencji.
#Jeśli wartość logiczna to True (Prawda) lub 1, element jest zapisywany w sekwencji, w przeciwnym razie zostanie z niego usunięty.


from gtts import gTTS
text = 'Czesc swiat !'   #Tekst
obj = gTTS(text, lang = 'pl') #rezultat
obj.save('hw.mp3')  #Zapisanie plika

#Przekształć tekst w przemówienie
#Python ma świetną bibliotekę gTTS (Google Text-to-Speech), która współpracuje z interfejsem API TEXT-to-Speech w usłudze Google Translate i umożliwia tworzenie plików dźwiękowych z tekstu. Pakiet jest zawsze instalowany w programie pip.
#Tworząc instancję gTTS, przekażemy kod źródłowy z pierwszym argumentem. Można również podać opcjonalny argument dla języka domyślnie angielskiego.
#Wynik można zapisać przy użyciu metody zapisu, do której należy przekazać nazwę pliku.


nums = [2, 3, 1, 5, 6, 4, 0]
print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums) # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())   # None
print(nums)  # [0, 1, 2, 3, 4, 5, 6]

#Sortowanie listy
#Python ma dwa wbudowane sposoby sortowania list - sortowane() i list.sort(). Wyniki w obu przypadkach są takie same, ale nadal istnieją niuanse.
#Funkcja Sort() akceptuje argument wejściowy jako listę i zwraca nową posortowaną listę. Lista źródłowa nie została zmieniona.
#Metoda sortowania z kolei ma zastosowanie do listy, zmienia ją bezpośrednio i nic nie zwraca.


str1 = 'Hello'
str2 = 'Hello'
str1 = str2 #True
str1 is str2 #True poniewaz Hello to krotkie wyrazenie 

str1 = 'Hello, my crazy world!'
str2 = 'Hello, my crazy world!'
str1 == str2 #True
str1 is str2 #False poniewz to dlugie wyrazenie 

#Różnica między == a wynosi
#Wielu programistów nie rozumie różnicy między dwoma operatorami. Z powodu nieprawidłowego użycia == i IS w aplikacjach mogą wystąpić dziwne błędy.
#Operator == sprawdza równność wartości obu obiektów. Operator sprawdza tożsamość samych obiektów. It służy do sprawdzenia, czy zmienne wskazują na ten sam obiekt w pamięci.
#Ale Python buforuje małe liczby i krótkie struny do wykonania, więc niektóre przypadki są możliwe, jak w przykładzie powyżej.


import re 
def slugify(s):
    s = s.lowe().strip()
    s = re.sub(r'[^\w\s-','', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s
print(slugify('Hello, World!')) # Output: hello-world

#Formatuj ciąg dla adresu URL
#Na początek warto pamiętać, że ślimak (slug) jest unikatowym identyfikatorem linii, zrozumiałym dla osoby i zawierającym tylko „bezpieczne” znaki: Małe litery alfabetu łacińskiego, cyfry i łącznik.
#Jest to najczęściej widoczne w kontekście adresów URL. Na przykład można utworzyć występ z tytułu artykułu i wstawić go do łącza, aby ludzie mogli zrozumieć, gdzie się znajdują.
#Powyżej w kodzie napisaliśmy prostą funkcję, w której użyliśmy metod LEW() Lotdove() i Strip() do usuwania spacji po lewej i prawej stronie.
#Wyrażenia regularne i wbudowany pakiet RE również zostały użyte do usunięcia niektórych znaków i zastąpienia ich hyphens.


from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, world!'
if __name__ == '__main__':
    app.run()

#Prosta, ale potężna struktura sieci Web
#Najbardziej popularną ramką dla rozwoju części serwera na Python jest kolba. Nawiasem mówiąc, pokonuje nawet Django przez gwiazdy na Gitkoncentrator.
#Kolba jest przeznaczona do szybkiego i łatwego rozruchu z możliwością skalowania do skomplikowanych zastosowań. A społeczność zapewnia wiele rozszerzeń ram.
#Powyższy kod jest wystarczający do utworzenia minimalnej aplikacji roboczej. Po uruchomieniu takiego skryptu można przejść do http://localhost:5000/ i zobaczyć wynik.


#Spis cyfer 
numbers = [1, 2, 3, 4, 5]

#Przez cykl for
squares = []
for num in numbers:
    squares.append(num * num)

#Przez generator listy
squares = [num * num for num in numbers]

#Przez funkcje map
squares = map(lambda x: x * x, numbers)

#Unikaj cykli ze zbiorami
#Rozważ problem: Chcesz utworzyć nową listę, której elementami będą kwadraty liczb z innej listy. Większość natychmiast zapisze pętlę dla.
#Ale to podejście będzie przyjmować co najmniej trzy linie: Deklarowanie nowej zmiennej, tworzenie pętli i kodu wewnątrz niej. Ponadto szybkość skryptu jest również zmniejszona.
#W powyższym kodzie podano dwie dobre alternatywy - generator listy i funkcję mapy. W obu wariantach kod staje się nie tylko bardziej zwięzły, ale także zauważalnie poprawiony.


import pdftotext
with open('lorem_ispum.pdf','rb') as file:
    pdf = pdftotext.PDF(file)  #Instalujemy PDF-dokument 
print(len(pdf))  #Ile stron zawiera 
for page in pdf:
    print(page)  #Czytanie  stron
print(pdf[0])  #Dostajemy oddzielne strony
print(pdf[1])
print('\n\n' .join(pdf)) #Wyprowadzamy caly tekst jako wyglad jednej strony

#Przekształć plik PDF w tekst
#Myślę, że wszystkie okresowe prace z dokumentami PDF. I często jest to praca ręczna i nudna. Ale Python może zautomatyzować nawet takie rutynowe zadanie.
#Moduł pdftotext jest przeznaczony do pracy z dokumentami PDF. System It jest instalowany za pośrednictwem menedżera pakietów pip i jest łatwy w użyciu. Wszystkie podstawowe czynności przedstawiono na powyższym rysunku.
#Nawiasem mówiąc, interesujące jest również to, że kod źródłowy modułu jest zapisany w C++. Jest więc mała szansa, że będziesz musiał walczyć z zależnościami.


from string import Template
#notification = Template('Hey, $name! You have $number notification.' )
message = notification.substitute(name='Adrian',number=3)
notification = Template('Hey, $name! You have $number notification.' )
print(message)
# Hey, Adrian! You have 3 notifications.

#Formatowane szablony ciągów
#Moduł tekstowy ze standardowej biblioteki zawiera interesującą klasę szablonu, która umożliwia łatwe tworzenie szablonów ciągów w celu dalszego formatowania.
#Ta metoda została wprowadzona w Python 2.4 jako zamiennik %formatowania (PEP 292), ale nigdy nie stała się popularna. Obsługuje wysyłanie wartości według nazwy i używa składni $PHP.
#Nowe projekty oczywiście używają większości ciągów f, a czasem metody formatowania, ale nadal warto wiedzieć o Template w przypadku, gdy trzeba pracować z starszym kodem.


from zipfile import ZipFile
file_name = 'archive.zip' #Ukazujemy nazwe archiwa
with ZipFile(fie_name, 'r') as zip: #Otwieramy fajl w reszym czytania
    zip.printdir() #Patzymy to co mamy
    zip.extractall() # Pokacujemy fajly

#Praca z archiwami zip
#Aby uprościć pracę z plikami zip, można użyć wbudowanego modułu zip. Jeśli ktoś nie pamita, plik zip to archiwum zawierające skompresowane pliki.
#Zawartość archiwum można przeglądać za pomocą prindir, a wszystkie pliki można wyodrębnić, wywołując plik extractfile.
#Moduł ten umożliwia również tworzenie własnych archiwów zip, ale postanowiliśmy nie skomplikować przykładu, więc wystarczy dołączyć link do dokumentacji.


import paramiko 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    '10.255.254.235',
    port=22,
    username='root',
    password='qwerty',
)
stdin, stdout, stderr = ssh.exec_cammand('uptime -p')
result = stdout.read().splitlines()
print(result)  # [b'up 2 days, 2 hours, 7 minutes']

#Połącz się z serwerem za pomocą ssh
#Pakiet paramiko pozwala na łączenie się ze zdalnym komputerami przy użyciu protokołu SSH2 i wykonywanie wszystkich tych samych operacji tam, jeśli łączysz się za pośrednictwem, na przykład, narzędzia ssh na Linuksie.
#Korzystanie z modułu jest bardzo proste, przykład głównych metod na powyższym rysunku. Nawiasem mówiąc, ciekawym faktem, Paramiko jest połączeniem słów "paranoid" i "przyjaciel" w Esperanto.
#Pakiet należy zainstalować w zwykły sposób za pośrednictwem menedżera pakietów pip. Dokumentacja jest dostępna tutaj.


import humanize
import datetime as dt
humanize.fractional(0.3) # '3/10'
humanize.scientific(500) # '5.00 x 10 (**2)'
humanize.intword(123455913) # '123.5 million'
delta = dt.timedelta(seconds=3633,days=2,microseconds=123000)
humanize.precisedelta(delta) # '2 days, 1 hour and 33.12 seconds'
humanize.naturaltime(dt.datetime.now() - dt.timedelta(seconds=3600)) # 'an hour ago'

# https://pypi.org/project/humanize/

#Włącz Python w człowieka
#Znaleziono niesamowite Humanize pakiet, który może przetłumaczyć numery i daty na tekst czytelne dla człowieka. Oznacza to, że wszystkie kule do takich zadań są natychmiast zastępowane dosłownie jedną linią.
#Na przykład ze złożonego obiektu timedelta można uzyskać „2 dni, 1 godzinę i 33.12 sekund” lub „5.00 x 10²” z 500. Więcej przykładów można zobaczyć na zdjęciu załączonym do postu.
#Ale nawet chłodniejsze niż angielski, pakiet obsługuje wiele innych języków, w tym rosyjski. I ogólnie, polecam przeczytać ich dokumentację, istnieje wiele ciekawych funkcji.


from spellchecker import SpellChacker
spell = SpellChecker()
misspelled = spell.unknown(['something','is','hapenning','here']) # Szukamy slow ktore sa napisane nie poprawnie
for word in misspelled: # Szukamy slow ktore maja blad
    print(spell.correction(word)) # Nie poprawnie napisane slowa : 'happenning'
    print(spell.candidates(word)) # Korekta na poprawne slowo : {'happenning', 'hapening'}

#W tekście znajdziemy literówki
#Przydatny pakiet Spellcheker pozwala znaleźć literówki w tekście, a nawet daje możliwe poprawki.
#Pod maską moduł wykorzystuje algorytm odległości Levenstein. A sam kod opiera się na artykule napisanym na Blog Petera Norviga. Krótko mówiąc, wdrożenie jest interesujące, radzę, aby zbadać.
#Ale nawet jeśli nie pójdziesz w szczegóły, pakiet jest niezwykle łatwy w użyciu. Przykłady użycia klasy Spellchekera oraz metod jego korekcji i kandydata przedstawiono na ilustracji.
#Pakiet obsługuje 6 języków, w tym rosyjski. Ale po szczegóły wysyłam cię do przeczytania dokumentacji.


import schedule 
def job():
    print("I'm working...")
schedule.every(1).seconds.do(job) #Kazda sekunde 
schedule.every().hour.do(job) #Kazda godzine 
schedule.every().day.at("10:30").do(job) #Codziennie o godzinie 10:30
schedule.every().manday.do(job) #Co poniedzialek 
schedule.every().wednesday.at("13:15").do(job) #Kazda sekunde o 13:15

while True:
    schedule.run_pending()

#Harmonogram zadań
#Ku mojemu zaskoczeniu, nie każdy wie o pakiecie harmonogramu, który pozwala zaplanować zadania i powtórzyć je w czasie.
#Jego główną zaletą jest to, że jest maksymalnie intuicyjny i ma elastyczną funkcjonalność. A harmonogram nie wymaga zewnętrznych zależności i jest ogólnie odciążony.
#Nie ma tu zbyt wiele do wyjaśnienia, logika metod zawartych w tym pakiecie jest jasna na przykładach.


from PIL import Image 
import pytesseract 
# Konwertacja obrazka na tekst i pokazujemy wynnik 
print(pytesseract.image_to_string(Image.open('test.png')))
#Ukazujemy rosyjski jezyk w argumenty 
print(pytesseract.image_to_string('test-russian.jpg',lang='rus'))
try:
    # Ukazujemy max czas ocekiwania 
    print(pytesseract.image_to_string('test.jpg',timeuot=2))
except RuntimeError as timeout_error:
    pass 

#Pobierz tekst ze zdjęcia
#Google posiada system Tesetact, który pozwala analizować tekst ze zdjęć z optycznym rozpoznawaniem znaków.
#A jako owijarka, pakiet Pytessert został stworzony przez ich system, który jest najwygodniejszym i najwygodniejszym w użyciu pakietem.
#Aby pobrać tekst ze zdjęcia, należy zadzwonić pod numer Image_to_string. Jeśli interesuje Cię tekst w języku rosyjskim, określ język rozszerzenia jako „ru”.
#Ważne jest również, aby użyć panelu otwierania zdjęć, choć można po prostu określić ścieżkę pliku jako ciąg.


from smtlib import SMTP_SSL
server = SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login('myname@gmail.com','password')
server.sendmail('myname@gmail.com','somebody@gmail.com','Hello there!')
smtp.quit()

#E-mail wysylamy mejla
#SMTP (Simple mail Transfer Protocol) to protokół umożliwiający wysyłanie wiadomości e-mail. Standardowa biblioteka posiada pakiet smtplib, który wdraża jego zachowanie.
#Aby połączyć się z serwerem, użyjemy klasy SMTP_SSL, która obejmuje szyfrowanie. W swoich argumentach przekażemy adres serwera i port. Uwierzytelnianie odbywa się przy użyciu metody logowania, do której wysyłamy odpowiednio login i hasło.
#Można wysyłać wiadomości e-mail przy użyciu metody Sendmail o tej samej nazwie, która akceptuje adresy i adresy nadawcy, a także sam tekst. Po zakończeniu programu zamknij połączenie za pomocą metody quit().
#Ale tutaj należy również zwrócić uwagę na fakt, że niektóre usługi pocztowe mogą nie pozwolić tak natychmiast połączyć się z ich serwerami i wykonać operacje. W naszym przypadku mieliśmy trochę walki z Gmailem.


import psutil
psutil.cpu_count() # 8
psutil.cpu_percent(percpu=True)
# [4.3 , 4.0 , 2.9 , 2.2 , 0.1 , 0.0 , 0.0 ]
psutil.virtual_memory()
psutil.disk_usage('/')
psutil.sensors_battery()

#Pobieranie danych systemowych
#Biblioteka psutil cross-platform dostarcza informacji o procesorach, pamięci, dyskach, sieci, sensorach i uruchomionych procesach w systemie. Przykłady podstawowych zastosowań przedstawiono na ilustracji.
#W przypadku zastosowań praktycznych, psutil jest przydatny głównie do monitorowania systemu, ograniczeń zasobów procesowych i zarządzania procesami.
#Oprócz systemów Windows, MacOS i Linux biblioteka obsługuje również programy FreeBSD, OpenBSD, NetBSD, Sun Solaris i AIX.


from pywebcopy import save_website
save_webpage (
    url='http://example-site.co,',
    project_folder='singe-page/',
)
save_website(
    url='http://example.co3/',
    project_folder='full-website/',
)

#Pobierz całą stronę internetową
#Tak proste, jak to możliwe, ale potężny pakiet pywebcopy pomoże klonować poszczególne strony internetowe, a nawet całe strony.
#Funkcja Save_Webpage pobiera stronę z określonym łączem, można również przekazać ścieżkę do argumentów, gdzie zapisać wynik.
#Ale Save_website pozwala na cykliczne pobieranie całej witryny. Na przykład, jeśli witryna jest blogi, skrypt pobiera wszystkie artykuły znajdujące się na stronie.
#Ale tutaj jest to konieczne, aby być bardziej ostrożnym, takie cykliczne ładowanie będzie wysyłać wiele żądań do serwera i może załadować go znacznie, jeśli strona ma wiele stron.


class Something:
    def set_value(self, value):
        self.value = value 
#Trorzymy egzemplarz 
obj = Something()
obj.set_value('one')
Something.set_value(obj,'two')

#Oznacza self  w metodach
#Podczas wywoływania metod na obiektach, sam obiekt jest przekazywany przez pierwszy argument, chyba że jest to metoda statyczna. I ten argument nazywa się jaźnią, którą początkujący przepisują w klasach, nawet nie biorąc pod uwagę jego znaczenia.
#I na szczęście wszystko dzieje się automatycznie - nie musisz ręcznie przenosić obiektu. Aby jednak lepiej zrozumieć ten moment, można wywołać metodę bezpośrednio z klasy i wyraźnie przenieść obiekt (przykład na zdjęciu).
#Następnie można odwołać się do atrybutów i innych metod na obiekcie już wewnątrz metody. To jest to, co jest przekazywane.
#Mówiąc proś, jeśli wyrzucisz wszystkie szczegóły techniczne, możesz powiedzieć: Jaźń wskazuje, że zastosujemy metodę do samego obiektu.


import urllib.request
import chardet
data = urllib.request.urlopen('http://yahoo.co,/')
chardet.detect(rawdata.read())
{encoding: utf-8, 'confidience': 0.99, 'language': ''}

#Dowiedz się, jak zakodować tekst
#Myślę, że każdy miał sytuacje, w których otworzyłeś plik lub dostałeś odpowiedź z serwera, a wewnątrz był zestaw dziwnych znaków w nieprzejrzystego kodowania.
#Pakiet chardet został właśnie stworzony do pracy z kodowaniem. Jego metoda wykrywania pozwala na uzyskanie założonego kodowania z dokładnością od 0 do 1.
#W przykładzie na obrazku otrzymaliśmy odpowiedź na żądanie serwera, wzięliśmy jego zawartość i sprawdzono sposób kodowania przy użyciu tej metody.


def get_user_by_id(user_id):
    assert type(user_id) is int, 'user_id must be integer'
    print('Searching...')
get_user_by_id(4253)
#Seaching...
get_user_by_id('foo')
#AssertionError: user_id must be integer

#Złap błędy z asert
#Wyrażenie Assert akceptuje wyrażenie logiczne i opcjonalny komunikat. It służy do sprawdzania typów, wartości argumentu i wyników funkcji, a także do debugowania, ponieważ zatrzymuje program w przypadku błędu.
#Jeśli wyegzekwujesz stwierdzenie Assert z prawdziwym wynikiem, nic się nie stanie. Ale w przypadku Fałsz, zostanie utworzony wyjątek AsertionErm.
#Nie ma jednak potrzeby podejmowania prób z wyjątkiem wyjątku Błąd przypisania. W tym przypadku twierdzić traci swoje znaczenie.
#W przykładzie sprawdzono, czy dany argument był typem danych liczbowych. Jeśli tak nie jest, zostanie wywołany wyjątek i wyświetlony zostanie określony komunikat.


from newspaper import Article 
url = 'https://teletype.on/@python_academy/first-steps'
article = Article(url)
article.download()
article.parse()
article.authors # ['Python Academy']
article.title # 'Pierwsze kroki w Python'
article.text # '...'
article.publish_date # datetime.datetime(2021, 2, 23, 3, 26, 3)

#Artykuły parsera uniwersalnego
#Pakiet gazetowy 3k umożliwia analizowanie artykułów i wyodrębnianie tytułów, tekstu, daty publikacji, nazwisk autorów i wiele innych.
#Zaletą pakietu jest to, że cały proces analizy składni jest zautomatyzowany i nie trzeba ręcznie wyszukiwać właściwych znaczników i pobierać z nich danych.
#Ale dokładność parsera zależy głównie od tego, jak dobrze ukończył żądaną stronę. W związku z tym w niektórych przypadkach wynik może różnić się od oczekiwań.


import tempfile 
temp = tempfile.TemporaryFile()
try:
    temp.write(b'Hello world!')
    temp.seek(0)
    print(temp.read())
finally:
    temp.close()
# Output: b'Hello world!

#Pliki tymczasowe
#Standardowa biblioteka Python posiada moduł tempfile, który zawiera klasy i metody prawidłowej pracy z plikami tymczasowymi i katalogów.
#Funkcja TemporaryFile tworzy plik tymczasowy w katalogu systemowym i zwraca obiekt podobny do pliku.
#Utworzony plik tymczasowy zostanie automatycznie usunięty po zamknięciu pliku lub po zamknięciu menedżera kontekstu.
#Inne procesy i aplikacje nie mogą również uzyskać dostępu do tego pliku tymczasowego.


import pytube 
import subprocess 
# Tworzymy obiekt YouTube 
youtube = pytube.YouTube('htttps://youtu.be/dQw4w9WgXcQwfgd')
#Wybieramy potoki dla zaintalowania 
video = youtube.streams.filter(res='1080').first()
audio = youtube.streams.filter(only_audio=True).first()
#Tworzymy proces ffmpeg dla zainstalowania i laczenia potoka 
process_call_str = f'ffmpeg -i "{video.url}" -i "{audio.url}" -c:v copy -c:a aac "{video.title}".mp4'
subprocess.check_call(process_call_str, shell=True)

#Łączenie strumieni wideo i audio
#Tak więc, dodatek do poprzedniego postu.
#Ze względu na technologię strumieniowej transmisji DASH (Dynamic Adaptive Stream over HTTP) używaną przez youtube nie możemy natychmiast uzyskać obrazu w odpowiedniej jakości ze ścieżką dźwiękową ze względu na jej brak w strumieniu.
#Jako rozwiązanie możemy indywidualnie odebrać dźwięk i obraz i połączyć go z ffmpeg. W tym celu należy wybrać odpowiednie strumienie wideo i audio, a następnie przesłać adresy url do polecenia, aby zainicjować proces pobierania i łączenia strumieni przy użyciu polecenia ffmpeg.


import textwrap 
text = 'The textwrap module can be used to format text for output in situations where pretty-printing is desired.'
textwrap.fill(text, widtch=20)
#The textwrap module 
#can be used to 
#format text for 
#output in situations 
#where pretty- 
#printing is desired 

#Określ szerokość tekstu
#Wcześniej był post o wbudowanym module SMS-Twrap - mówiliśmy o tym, jak zmniejszyć tekst do pewnej liczby znaków bez przerwy w środku słowa.
#Ale zaawansowane funkcje do pięknego formatowania tekstu nie kończą się tam. W module nadal znajduje się pole, które umożliwia określenie szerokości tekstu w postaci znaków.
# #Jak widać na przykładzie na rysunku, słowa są przenoszone do nowych linii i nic nie jest odcinane na pół słowa.

#Wyrażenia lambda sa to jednolinijkowe anonimowe funkcje , bez nazwy Tworzesą za pomocą słówa kluczowego
# lambda po którym nastepuje lista parametrów .Po dwokropku znajuje się właściwy kod funkcji .Funkcję 
#lambda mozna tez przypisac do zmiennej i wywołać jak zwykłą funkcję.

# Ponizsza funkcja lambda przyjmuje dwa argumenty a oraz b i zwrac ich sumę , return nie jest potrzebne ,
#wynik wyrazenia jest automatycznie zwracany z lambda.

sum = lambda a,b:a+b
print( sum(10,5) ) #15
print( sum(4,3) ) #7



#Wyrazenie lambda moze byc równiez zwrocone przez zwykłą funkcję , dzięki czemu mozna ją wywołać w razie 
# potrzeb

#zwróona jest funkcja lambda która zapamięta wartość n
def genFunc(n):
    return lambda a: a * n

doubler = genFunc(2)  #w doubler jest lambda z n o wartosci 2

print(doubler(5) ) #10
print(doubler(7) ) #14

tripler = genFunc(3)   
print( tripler(2) )    #6
print(tripler(3) )     #9

#Wyrażenie lamda z map()
#Wyrażenie lambda przydają się najbardziej w funkcjach wyższego rzędu czyli takich , które jako argument
#przyjmują inne funkcje lub zwracają funkcję 
# Przykładem jest funkcja r = map(func,seq) przyjmuje funkcję którą wywoła na wszystkich elementach seq,
#po czym zwróci sekwencję zmodyfikowanych przez func elementów w postaci literatora więc można skonwerować 
# wynik na listę poprzez list()
listData = [1,2,3,4,5]
result = map (lambda x:x*2,listData)
print(list(result) )    # [2,4,8,10]

print(list(map(lambda x : x * 3,[1,2,3,4])))    #[3,6,9,12]


#Wyrazenie lambda przydają się najbardziej w funkcjach wyższego rzędu czyli takich,które jako argument
# przyjmują inne funkcje lub zwracają funkcje.

#Funkcja reduce redukuje sekwencję do pojedynczej wartości 

from functools import reduce  #import funkcja reduce
numSum = reduce((lambda x, y:x+y),[1,2,3,4,5])
print("Suma liczb :",numSum)  

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    @staticmethod
    def is_adult(age):
        return age >= 18
mark = Person('Mark',25)
#Wyzywamy metody u egzemplarza
mark.is_adult(32)
#Wyzywamy metody w klasie 
Person.is_adult(16)

#Jak działają metody statyczne
#Metody statyczne są tworzone w klasie przy użyciu metody@STaticmethod. Metody te są powiązane z klasą, a nie obiektem - jest to główna różnica.
#Ten typ metody nie może modyfikować obiektu ani samej klasy, czyli nie trzeba przekazywać obiektu ani klasy i zapisywać własnych lub cls w argumentach.
#Normalna funkcja powinna być wprowadzona do klasy jako metoda statyczna, gdy ta funkcja logicznie należy do klasy i ma sens być tam.

#Organiczenia sposobu przekazywania danych do fukcji - programista za pomocą / oraz *
# może okrelic dopuszczalne sposoby przekazywania argumentów do funkcji.

#Slash oznacza parametry tylko pozycyjne , ważna jest koejność tych parametrów i nie mogą być przekazywane
# jako argumenty nazwane.Uwaga parametry tylko pozycyjne umieszczane są przed / dzięki temu rozdziela para
# metry tylko pozycyjne od reszty parametrów.

def printData(string,number = 10 , /):
    print(string,number);
printData("Test",5) #działa prawidłowo,argumenty pozycyjne : Test 5

printData(string = "Test",number = 11) #bład nie mozna uzywac argumentów nazwanych'
####################################################################################################

#Gwiazdka oznacza argumenty nazwane ,musi byc umieszczona przed pierwszym parametrem ktory ma byc tak 
#przekazany

def printData(*,string,number = 10):
    print(string,number);
printData(string = "Test",number = 11) #działą prawidłowo : Test 11
printData("Test",5) #bład oa mają być przekaane jako nazwane


#parametry po gwiazdce muszą być przekazane jako argumenty nazwane
#parametry przed gwiazdką mogą być przekazane jako nazwane albo pozycyjne
def printData(float,bool,*,string,number = 10):
    print(float,bool,string,number);
printData(12.5,bool = True , string = "Test" , number = 11)      #12.5 True Test 11
printData(float = 12.5,bool=False,number = 11,string = "Test")   #12.5 False Test 11
printData(20.3,False,number=11,string = "Test")  #20.3 False Test 11
####################################################################################################

def printCar(brand, / ,name = "concept", * ,year = 1960 ,color="black"):
    print(brand,name,year,color)
#printCar(brand = "Ford","Mustang",color = "blue",year = 1974) -blad
printCar("Ford","Mustang",year = 1974,color = "blue")
#printCar("Ford",name="Mustang","blue",year = 1974) -blad

import random 
mylist = ["apple","banana","cherry","strawberry","orange"]
print(random.sample(my.list,k=2))
# ['apple','strawberry']
# losowo.próbka

#Metoda sample() zwraca listę elementów o określonej długości wybranych z sekwencji. Sekwencja może być listą, root, ciągiem lub zestawem. Parametr k jest rozmiarem zwracanej listy.


class Data:
    def __bool__(self):
        return True
x = Data()
res = bool(x)
print(res) #True 
# bool () realzuje wbudowane funkcje 
#Metoda bool() wdraża wbudowaną funkcję bool(). Podczas połączenia z booklem(x) Python próbuje wywołać x.bool(). Jeśli zwrócona wartość nie jest logiczna, Python wydaje błąd typu.

############################################################################## #####
Check if list conlains integer x
#Sprawdź, czy lista zawiera liczbę całkowitą x
l=[3,3,4,5,2,111,5]
print(111 in 1) #True

#########################################################

#Find duplicate number in integer list
#Znajdź zduplikowany numer na liście liczb całkowitych
def find_duplicates(elements):
    duplicates,seen = set(),set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
        return list(duplicates)

#########################################################

#Check if lwo strings are anagrams 
#Sprawdź, czy dwa ciągi znaków są anagramami
def is_anagram(s1,s2):
    return set(s1) == set(s2)
print(is_anagram("elvls","lives")) #True

#########################################################

#Remove all duplicates from list
#Usuń wszystkie duplikaty z listy
lst=list(range(10)) + list(range(10))
lst = list(set(lst))
print(lst)  # [0,1,2,3,4,5,6,7,8,9]

#########################################################

#Find pairs of integers in list so that their sum is equal to integer x
#Znajdź pary liczb całkowitych na liście, tak aby ich suma była równa liczbie całkowitej x
def find_pairs(l,x):
    pairs = []
    for (i,el_1) in enumerate(l):
        for(j,el_2) in enumerate(l[i+1]):
            if el_1 + el_2 == x:
                pairs.append((el_1,el_2))
    return pairs

#########################################################

#Check if a string is a palindrome 
#Sprawdź, czy ciąg jest palindromem
def is_paindrome(phrase):
    return phrase == phrase[ ::-1 ]
print(is_paindrome("anna"))  #True

#########################################################

#Use list as stack array and queue
#Użyj listy jako tablicy stosu i kolejki
#as a listVB  
l=[3,4]
l += [5,6] #l = [3,4,5,6]

# ... as a stack ... 
l.append(10) # l = [4,5,0,10]
l.pop() #l = [4,5,6]

# ...and as a queue
l.insert(0,5) #l=[5,4,5,6]
l.pop() #l = [5,4,5]

#########################################################

#Get mssing number in[1...100]
#Pobierz numer wiadomości w[1...100]
def get_missing_number(lst):
    return set(range(lst[len(lst) -1 ])[1:]) - set(1)
l = list(range(1,100))
l.remove(50)
print(get_missing_number(1)) #50

#########################################################

#Compute the interseclion of two lists 
#Oblicz przecięcie dwóch list
def intersect(lst1,lst2):
    res,lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res

#########################################################

#Find max and min in unsorled list
#Znajdź max i min na niesortowanej liście
l = [4,3,6,3,4,888,1,-11,22,3]
print(max(l)) #888
print(min(l)) #-11

#########################################################

#Reverse string using recursion 
#Odwróć ciąg znaków za pomocą rekurencji
def reverse(string):
    if len(string)<=1: return string
    return reverse(string[1:]+string[0])
    print(reverse("hello")) #ollek

#########################################################

#Compule the first n Fibonacci numbers
#Oblicz pierwsze n liczby Fibonacciego
a,b =0,1
n=10
for i in range(n):
    print(b)
    a,b = b,a+b # 1,1,2,3,5,8

#########################################################

#Sort list with Quicksort algorithm
#Sortuj listę z algorytmem Quicksort
def qsort(L):
    if L ==[]:return[]
    return qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
lst = [44,33,22,5,77,55,999]
print(qsort(lst))  #[5,22,33,44,55,77,999]

#########################################################

#Find all permutations of string
#Znajdź wszystkie permutacje ciągu
def get_permutations(w):
    if len(w)<=1: 
        return set(w)
    smaller = get_permutations(w[1:])
    perms = set()
    for x in smaller:
        for pos in range(0,len(x)+1):
            perm = x[:pos]+ w[0] + x[pos:]
            perms.add(perm)
    return perms
print(get_permutations("nan"))  # ('nna','ann','nan')
    
############################################################################## ####

import numpy as np 
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
points = np.array([
    [2, 4]
    [3, 4]
    [3, 0]
    [2, 2]
    [4, 1]
    [1, 2]
    [5, 0]
    [3, 1]
    [1, 2]
    [0, 2]
])
hull=ConvexHull(points)
hul_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()

#SciPy: Gleboka powłoka
#Pusta skorupa zawiera zestaw punktów i działa jako granica klastra, która pomaga zidentyfikować wszystkie punkty w klastrze. Używając metody ConvexHull(), można utworzyć pustą skorupę.



import math 
math.pi
math.sqrt(85) # 0.70820484894

S='Mielonka'
len(S) #8
S[0] # 'M'
S[1] # 'i'
S[-1] # perwszy element do konca zmiennej S 'a'
S[-2] # drugi element od konca zmennej S 'k'
S[-1] # ostatni element w zmiennej zmienne S 'a'
S[len(S)-1] # 'a' lub zapisac w taki spsob
S[1:3] # 'ie'
S[1:] # 'ielonka'
S[0:7] #'Mielonk'
S[:7] #To samo co S[0:7]
S[:] # 'Mielonka'
S + 'xyz' #Mielonkaxyz
S * 8 #Mielonka 8 razy
S= 'z' + S[1:] # 'zielonka'

S1='taczka'
L = list(S)
L #['t' 'a' 'c' 'z' 'k' 'a' ]
L[1]='p' 
''.join(L) # 'paczka'

B = bytearray(b'mini') # Hybryda zbioru bajtow i listy 
B.extend(b'maraton') #'b' jest potrzebne w wersji 3x ale w 2x juz nie
B # bytearray(b'minimaraton')  #B[i] = ord(x) tez tutaj bedzie dzialac
B.decode() # 'minimaraton'

S = 'Mielonka'
S.find('ie') # odnalezienie przesuniecia podlancucha w S  1
S.replace('ie', 'XYZ') # MXYZlonka

line = 'aaa,bbb,ccccc,dd' #podzial na podciagi wedlug znakow separatora
line.split(' , ')  # ['aaa' , 'bbb', 'ccccc', 'dd']

S='mielonka'
S.upper() #'MIELONKA'    Konwersja na wielkie litery
S.isalpha() # sprawdzanie zawartosci  isalpha,isdigit itd. True
line= 'aaa,bbb,ccccc,dd\n' 
line=line.rsstrip() # Usuniecie bialych znakow po prawej stronie 'aaa,bbb,ccccc,dd'
line.rstrip().split(' , ') # Polaczenie dwoch operacji ['aaa' , 'bbb' , 'ccccc', 'dd']

'%s, jajka i %s' % ('mielonka', 'MIELONKA!') #Wyrazenie formatujace (wszystkie wersje)
# 'mielonka,jajka i MIELONKA!'

'{0}, jajka i {1}'.format('mielonka','MIELONKA!') #metoda formatujace wersje 2.6+ i 3.0
# 'mielonka,jajka i MIELONKA!'

'{},jajka i {}'.format('mielonka','MIELONKA!') #Wartosci liczbowe sa opcjonalne 
# 'mielonka,jajka i MIELONKA! '

'{:,.2f}'.format(296999.2567) #separatory, mejsca po przecinku 
# '296,999.26

'%.2f | %+0.5' % (3.14159, 42) # Cyfry dopelnienie znaki 
# '3.14 | 0042'

dir(S)

S + 'NI'

S.__add__('NI!') #'spamNI!

S = 'A\nB\tC' #\n oznacza znak konca wiersza, a\t to tabulatora
len(S) #5 #Każdy z elementów składowych S to jeden znak
ord('\n') # \n to jeden znak zakodowany jako wartosc dziesiętna 10
S='A\OB\OC' # \0 binarny bajt zerowy nie konczy lancucha znakow
len(S) #5
S  # 'A\xOOB\xOOC' #Znaki niedrukowalne wyswietlane są jako sekwenje szestnackowe \xNN

msg="""aaaaaaaaaaa 
bbb '''bbbbbbbbbb""bbbbbbbbb'bbbbbcccccccccc
"""
'sp\xc4m' #'spAm'  # 3x normalny ciag str to tekst Unicode 
'a\x01c' #b'a\x01c # Normalnie ciągi str mogą zawierać tekst i dane bajtowe
b'a\x01c' # literały Unicode z wersji 3.x działają w wersji 2.6 traktowane jak str

'spam' #spam 
'spam'.encode('utf8')  #b'spam' #ciąg znaków zakodowany w formacie UTF-8 zajmuje 4 bajty
'spam'.encode('utf16') #b'\xff\xfes\xOOp\xOOa\xOOm\xOO' #W standardzie UTF-16 zajmuje juz 10 bajtow

'sp\xc4\uOOc4\UOOOOOOc4m' #'spAAAm'

import re 
match = re.match('Witaj,[\t]*(.*)Robinie','Witaj , sir Robinie')
match.group(1) #'sir'

match = re.match('[/:](.*)[/:](.*)[/:](.*)','/usr/home:lumberjack')
match.groups()  #('usr','home','lumberjack')
re.split('[/:]','/usr/home/lumberjack')  # [' ' , 'usr','home','lumberjack']

L=[123,'mielonka',1.23]
len(L) # 3

L[0] #123
L[:-1] # [123,'mielonka']
L + [4,5,6] # [123,'mielonka',1.23,4,5,6]
L*2 # [123,'spam',1.23,123,'spam',1.23]
L #[123,'mielonka',1.23]

L.append('NI')
L #[123,'mielonka',1.23,'NI']
L.pop(2) #1.23
L # [123,'mielonka','NI']

M=['bb','aa','cc']
M.sort()
M #['aa','bb','cc']
M.reverse()
M # ['cc','bb','aa']

M = [[1,2,3],
[4,5,6],
[7,8,9]]
M #[[1,2,3],[4,5,6],[7,8,9]]
M[1] #[4,5,6]
M[1][2] #Pobranie drugiego wiersza a z niego trzeciego elemntu czyli 6

col2=[row[1] for row in M] # Zebranie elementów z drugiej kolumny
col2 #[2,5,8]
M # wszystko bez zmian

[row[1] +1 for row in M] #Dodanie 1 do kazdego elemntu w drugiej kolumnie [3,6,9]
[row[1]for row in M if row[1] % 2==0] #Odfiltrowanie elementów nieparzystych [2,8]

diag=[M[i][i] for i in [0,1,2]]     #Pobranie przekatnej z macierzy 
diag #[1,5,9]

doubles = [c*2 for c in 'mielonka'] #Powtorzenie znakow w lancuchu 
doubles # ['mm' 'ii' 'ee' .....]

list(range(4)) #[0,1,2,3]
list(range(6,7,2) ) #[6,4,2,0,2,4,6]

G = (sum(row) for row in M ) #Utworzenie generatora sum wierszy
next(G) #uzycie funkcji iter(G) niej est tu wymagane # [6]
next(G) # Obliczenie kolejnej sumy # [15]
next(G) # 24

list(map(sum,M)) #[6,15,24] #wykonanie funkcji sum da elementow macierzy M [6,15,24]  
                                
#                                    167 stron

{sum(row) for row in M} # {24,6,15} Utworzenie zbioru sum wierszy
{i:sum(M[i])for i in range(3)} #Utworzenie tabeli klucz-wartosc sum wierszy
#{0:6,1:15,2:24}

[ord(x)for x in 'mielonka'] #Lista numerów porządkowych znaków
# [109,105,101,108,111,111,110,107,97]
{ord(x) for x in 'mielonka'} # Zbiory pozwalają na usunięcie duplikatów
# {97,101,105,107,108,109,110,111}
{x:ord(x)for x in 'mielonka'} #Klucze słownika są unikalne
# {'a':97,'e':101,'i':105,'k':107,'m':109,'l':108,'o':111,'n':110}
(ord(x)for x in 'spaam') #Generator wartości

D = {'jedzenie':'Mielonka','ilość':4,'kolor':'różowy'}
D['jedzenie'] #Pobranie wartosci klucza jedzenie czyli 'Mielonka'
D['ilość'] +=1  #Dodanie 1 do wartości kucza "ilosc" to bedzie 5

D= {}
D['imię'] = 'Robert' #Tworzenie kluczy przez przypisanie
D['zawód'] = 'programista'
D['wiek'] = 40
D 
# {'wiek':40,'zawód': 'programista','imię':'Robert'}
print(D['imię']) # Robert

bob1 = dict(imię='Robert',zawód='programista',wiek=40)
# {wiek:40,imię:Robert,zawod:programista}
bob2 = dict(zip(['imię','zawód','wiek'],['Robert','programista',40])) #Łącznie
# { 'zawod':'programista','imie':'Robert,'wiek':40}

rec = {'dane osobowe':{'imię':'Robert','nazwisko':'Zielony'},
'zawód': ['programista','inżynier'] , 
'wiek': 40.5}
rec['dane osobowe'] # to zagnieżdrzony słownik
# {'nazwisko':'Zielony','imię':'Robert'}
rec['dane osobowe']['nazwisko']
# 'Zielony'
rec['zawód']
rec['zawód'][-1] #indeksowanie zagnieżdrzonej listy 
# 'inżynier
rec['zawód'].append('leśniczy') #Rozszerzenie listy zawodów Roberta

D = {'a':1,'b':2,'c':3}  # Przypisanie nowego klucza rozszerza słownik
D['e'] = 99      

value = D.get('x',0)
value # 0
value = D['x'] if 'x' in D else 0
# 0

D = {'a':1,'b':2,'c':3}
D

Ks=list(D.keys())
# ['a','c','b']
Ks.sort()
Ks
# ['a','b','c']
for key in Ks:              #Iteracja przez posortowane klucze
    print(key, '=>',D[key]) # <==Tutaj należy dwukrotnie nacisnąć Enter
# a => 1
# b => 2
# c => 3

for key in sorted(D):
    print(key, '=>',D[key])
# a => 1
# b => 2
# c => 3

for c in 'mielonka':
    print(c.upper())
# M
# I
# E
# L
# O 
# N
# K
# A

x=4
while x>0:
    print('mielonka!'* x)
    x -= 1
# mielonka mielonka mielonka mielonka 
# mielonka mielonka mielonka
# mielonka mielonka
# mielonka

squares = [x ** 2 for x in [1,2,3,4,5]]
squares
# [1,4,9,16,25]

T = (1,2,3,4)
len(T)
T + (5,6)
T[0] #1

T.index(4) #3
T.count(4) #1

T = (2,)+T[1:] #Utwórz nową krotkę dla nowej wartosci 
T 
# (2,2,3,4)

T='mielonka', 3.0 , [11,22,33]
T[1]
# 3.0
T[2][1]
# 22
T.append(4) # ==> Error

#Wbudowane funkcje matematyczne 
pow, abs, round, int, hex, bin 
#Moduly narzedziowe 
random , math 

#Liczby zmiennoprzecinkowe  maja na przyklad 
metode = "as_integer_ratio"  #przydajaca sie dla typu liczby ulamkowej 

#Czy liczba jest calkowita uzywamy 
metode = " is_integer "

# Podaje liczbe bitow  niezbedna do odwierciedlenia wartosci obiektu uzywamy 
metode = " bit_length "
###

# yield x = Protokol send funkcji generatora 
# lambda argumenty: wyrazenie = Generowanie funkcji anonimowej 
# x if y else z = Trojargumentowe wyrazenie wyboru (x jest obliczane jedynie wtedy gdy y jest prawdzile ) 
# x or y  = Logiczne OR (y jest obliczne tylko wtedy gdy x jest falszywe )
# x and y = logiczne AND (y jest obliczane tylko wtedy gdy x jest prawdziwe)
# not x = Logiczna negacja 
# x in y , x not in y = Przynaleznosc (obiekty po ktorych mozna interowac  zbiory)
# x is y, x is not y = Testy identycznosci obiektow 
# x < y, x <= y, x > y , x >= y = Operatory porownania , podzbiory i nadzbiory zbiorow 
# x == y, x!= y  = Operatory rownosci wartosci 
# x | y = Bitowe OR suma zbiorow 
# x ^ y = Bitowe XOR symetryczna roznica zbiorow 
# x & y = Bitowe AND  czesc wspolna zbiorow 
# x << y , x >> y = Przesuniecie  x w lewo lub prawo o y bitow 
# x + y = Dodawanie i kontanecja 
# x - y = Odejmowanie  roznica zbiorow 
# x * y 
# x % y 
# x / y, x // y = Dzielenie  prawdziwe i bez reszty 
# -x, +x = Negacja identycznosc 
# -x  = Bitowe NOT
# x ** y 
# x[i] = Indeksowanie (sekwencje odwzorowanie inne)
# x[i:j:k] = Wycinki 
# x(...) = Wylowanie (funkcji, metod, klasy , innych obiektow ktore mozna wywolywac )
# x.atrybut = Odwolanie  do atrybutu 
# (...) = Krotka wyrazenie , wyrazenie generatora 
# [...] = Lista lista skladana 
# {...}  = Slownik zbior a takze zbior i slownik skladany 
 
###
str , repr # dla liczb 

[...] # literal listy albo wyrazenie list skladanych 

(...) # skladnia jest wykorzystana  do grupowanie wyrazen wyrazeniach generatorow 
# list skladanych 

{...} # wykorzystywana jest w literalach slownikow 

yield , if/else # pierwsze z nich zwraca argumenty send(...) 
# a drugie jest  skrutem dla dla wielowierszowej instrukcji  if 
# wyrazewnie yield wymaga nawiasy 

# Operatory porownania mozna ze soba laczyc kod 
X < Y < Z # zwraca ten sam wynik co 
x < Y and Y < Z  # Porownanie zwykle i laczone 

# Wycinek X[I :J : K ] jest rownowazne z indeksowaniem z obiektem wycinka X[slice(I, J, k)]

# Testy rownosci  (porownanie wilkosci slownikow )
sorted(dict.items())

# POLACZENIE OPERATORY STODUJA SIE DO PRIORYTETOW  
AUC = 0
CRC = 1
AUC * B + CRC * D

# PODLYRAZENIE GRUPOWANE SA W NAWIASACH 

int(3.1415) # 3
float(3) # 3.0

# Zmienne  i podstawowe wyrazenia 
#### Zmienne tworzone sa  kiedy pierwszy raz przypisze sie do wartosc 
#### Zmienne zastepowane sa wartosciami kiedy wykorzystywane sa w wyrazeniach 
#### Zmienne musza byc przypisane przed uzyciem w wyrazeniach 
#### Zmienne odnosza sie do obiektow i nigdy nie sa wczesniej deklarowane 

# Formaty wyswietlenia funkcje repr i str 
repr('spam') # " 'spam' " # Wyswieltenie w postaci jak w kodzie (sesja interaktywna)
str('spam') # 'spam'  # Wyswietlenie w formie przyjaznejj dla uzytkownika (odpowiednik print)
# Funkcja repr zwraca wyniki wygladajace tak jakby byly one kodem 
# Funkcja str  (i operacja print) wykonuje dla formy bardziej dla uzytkownika jezeli on jest 
# str do uzytku ogolnego i repr z dodatkowymi szczegolami 
# str moze byc takze nazwa 


import math 
5/2 # Zachowanie reszty 2.5
math.trunc(5/2) #Odciecie reszty zamiast zaokraglenia w dol tak samo jak w przypadki (int) 2
5//2 # Zaokraglenie wynniku w dol  -3

# Operacje na poziomie bitow 
x = 1 # Liczba 1 dzisietne to 0001 w zapisie bitowym 
x << 2 # Przesuniecie o 2 bity w lewo : 0100  ( 4 )
x | 2 # Bitowe OR (dowolny z bitow = 1): 0011 ( 3 )
x & 1 # Bitowe AND (oba bity = 1 ): 0011 ( 1 )

# W pierwszym wyrazeniu binarne 1 (w systemie  dwojkowym - 0001) przesuwane jest w lewo o dwa miejsca
#tworzac binarne 4 (0100) Ostatnie dwie operacje wykonuja binarne  OR w celu polaczenia bitow (0001 | 0010 = 0011) oraz
#binarne AND w celu wybrania wspolnych bitow (0001 & 0001 = 0001) Takie operacje na maskach bitowych pozwalaja na zakodowanie
#(lub wyodrenienie wielu flag i innych wartosci w jednej liczbie calkowitej )


#OBSLUGA LICZB DWOJKOWYCH I SAZESTNASTKOWYCH 
X = 0B0001 #lITERALY DWOJKOWE 
X << 2 #Przesuniecie w lewo  ( 4 )
bin(X << 2) # Lancuch cyfr dwojkowych  '0b100'
bin(X | 0b010) #Bitowe OR '0b11'
bin(X & 0b1) #Bitowe AND '0b1'

# Inne wbudowane narzedzia numeryczne 
import math 
math.pi, math.e     #Czesto uzywane stale 
# (3.142352344 , 2.7124124312)
math.sin(2 * math.pi / 180) #Sinus, tanges , cosinus 
math.sqrt(144), math.sqrt(2) #Pierwiastek kwadratowy (12 , 1.1231231)
pow(2, 4), 2 ** 4, 2.0 ** 4.0 # Potegowanie (16, 16, 16.0)
abs(-42.0), sum((1, 2, 3, 4)) # Wartosc bezwgledna suma
min(3, 1, 2, 4), max(3, 1, 2, 4) # Minimum i maksimum (1, 4)

math.floor(2.567), math.floor(-2.567) # Zaokraglenie do najblizszej liczby calkowitej (2, 3)
math.trunc(2.567), math.trunc(2.567) # Odciecie (pominiecie czesci ulamkowej) (2, 2)
int(2.567), int( 2.567) #Odciecie (konwersja na liczbe calkowita ) (2, 2)
round(2.567), round(2.467), round(2.567, 2) #Zaokraglenie (Python 3x) (3, 2, 2.57)

import math 
math.sqrt(144)   # Modul (12.0)
144 ** .5     # Wyrazenie  12.0
pow(144, .5) # Funkcja wbudowana (12.0)

# Takie jak math trzeba importowac jednak funkcje wbudowane takie jak abs czy round dostepne sa zawsze 
#bez importowania .Innymi slowy moduly to komponenty zewnetrzne natomiast funkcje wbudowane  znajduja sie 
#w domyslnej przestszeni nazw  ktora python przeszukuje domyslnie w celu odnalezienia nazw uzytych  w programie
# Modul to importowanie 

import random 
random.random() # 0.53454353354
random.random() # 0.525234523234   Losowe liczby zmiennoprzcinkowe calkowite wybieranie i tasowanie elementow 
random.randint(1, 10) # 5
random.randint(1, 10) # 9 

random.choice(['Zywot Briana', 'Swiety Graal', 'Sens zycia ']) # 'Swiet graal'
random.choice(['Zywot Briana', 'Swiety Graal','Sens zycia']) # 'Zywot Briana'
suits = ['kier','karo','trefl','pik']
random.shuffle(suits)
suits # ['trefl' 'karo' 'kier' 'pik']

# TYP DECIMAL 
from decimal import Decimal 
Decimal ('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # Decimal('0.0')

# GLOBALNE USTAWIENIE PRECYZJI LICZB DZIESIETNYCH 
# Pozwala na przyklad na okreslenie precyzji (liczby miejsc dziesietnych) i trybu zaokraglenie (w dol , w gore)
# Ustawienie precyzji stosowanego jest globalne dla wszystkich liczb dzisietnych utworzonych w watku wywolujacym
import decimal 
decimal.Decimal(1) / decimal.Decimal(7)  # Domyslnie 28 cyfr
# Decimal ('0.14282412412412412425')

decimal.getcontext().prec = 4
decimal.Decimal(1) / decimal.Decimal(7) # Stala precyzja 
#Decimal('0.1429')

1999 + 1.33 # Wynik w pamieci ma wieksz liczbe miejsc dziesietnych niz jest wyswietlane w wersji 3.3
decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
pay # Decimal ('2000.33')

# MENEDZER KONTEKSTU DZIESIETNEGO 
import decimal 
decimal.Decimal('1.00') / decimal.Decimal('3.00')
#Decimal ('0.33333333333333333333333333)
with decimal.localcontext() as ctx:
    ... ctx.prec = 2 
    ... decimal.Decimal('1.00') / decimal.Decimal('3.00')
    #Decimal ('0.33')
decimal.Decimal('1.00') / decimal.Decimal('3.00')
# Decimal ('0.3333333333333333333333')


# TYP FRACTION - zagadnienia podstawowe 
from fraction import Fraction 
x = Fractrion(1, 3) #Licznik mianownik 
y = Fraction(4, 6) # Uproszczony do 2, 3 przez gcd 

x  # Fraction (1, 3) 
y # Fraction (2, 3)
print(y) #2/3

x + y # Fraction(1, 1) 
x - y # Fraction (-1, 3)
x * y # Fraction (2, 9)

# Obiekty Fractrion moga rowniez byc tworzone z ciagow znakow reprezentujacych liczby zmiennoprzecinkowe 
# podobnie jak liczby dzisitne 
Fraction('.25') # Fraction (1.4)
Fraction('1.25') # Fraction (5, 4)


# DOKLADNOSC NUMERYCZNE ULAMKOW ZWYKLYCH I DZISIETNYCH 
a = 1 / 3.0  # Dokladnosc taka, jak procesora do obliczen zmiennoprzecinkowych 
b = 4 / 6.0  # Moze tracic precyzje w miare wykonywanie kolejnych obliczen 
a # 0.3333333333333
b # 0.6666666666666
a + b # 1.0
a-b # -0.333333333
a*b # 0.222222222

from fraction import Fraction 
Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
# Fraction (0, 1)

from decimal import Decimal 
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal ('0.0')

Fraction(1, 3) # Fraction(1, 3) Dokladnosc liczb dwa sposoby 

import decimal 
decimal.getcontext().prec = 2
Decimal(1) / Decimal(3)
# Decimal('0.33')


# Tak naprawde liczby ulamkowe zachowuja dokladnosc jak i automatycznie upraszczaja wyniki
# kontynujac poprzednia sesje interaktywna 

Fraction(6, 12) # Automatyczne skrocenie ulamka 
# Fraction (1, 2)

Fraction(1, 3) + Fraction(6, 12)
# Fraction (5, 6)

decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
# Decimal ('0.83')

1000.0 / 1234567890
# 8.10000000000242e-07
Fraction(1000, 1234567890) #Znacznie prosztrze !
Fraction(100, 123456789)


# KONWERSJE ULAMKOL I TYPY MIESZANE 

(2.5).as_integer_ratio # Metoda obiektu liczby zmiennoprzecinkowej 
# (5, 2)

f = 2.5 
z = Fraction(*f.as_integer_ratio()) # Konwersacja z liczby zmiennoprzecinkowej na ulamek 2 argumenty 
z # To samo co Fraction(5,2)  # Fraction (5, 2)

x # Fraction(1, 3)  x z poprzedniej interakcji
x + z # Fraction(17, 6)   # 5/2 + 1/3 = 15/6 + 2/6
float(x) # Konwersjacja z ulamku na liczbe zmiennoprzecinkowa  0.33333333333
float(z) # 2.5
float(x + z) # 2.8333333333
17/6 # 2.83333333333

Fraction.from_float(1.75) # Konwersacja z liczby zmiennoprzecinkowej na ulamek inny sposob
# Fraction (7, 4)

Fraction(*(1.75).as_integer_ratio()) # Fraction (7, 4)

# Mieszanie typow w wyrazeniach ale czasami trzeba recznie rozszerzyc typ Fraction w celu
# zachowania dokladnosci by przekonac sie jak to dziala 
x # Fraction (1, 3)
x + 2 # Fraction (7, 3)  = Ulamek + liczba calkowita  -> ulamek 
x + 2.0 # 2.333333335  = Ulamek + liczba zmiennoprzecinkowa  -> liczba zmiennoprzecinkowa 
x + (1./3) # 0.666666666 = Ulamek + liczba zmiennoprzecinkowa -> liczba zmiennoprzecinkowa 
x + Fraction(4, 3) # Fraction (5, 3) = Ulamek + ulamek -> ulamek 

# Mozna dokonac konwersji z liczby zmiennoprzecinkowej na ulamek 
4.0 / 3 # 1.333333333
(4.0 / 3).as_integer_ratio() #Utrata precyzji z liczb zmienoprzecinkowej (to jest zle )
# (600930943908423098, 92048124821241)
a.limit_denominator(10) # Uproszczenie do najblizszego ulamku  
# Fraction(5, 3)
 
# Podstawy zbiorow w Pythonie 2.6 i wrsjach wczejscniejszych 
z = x.intersection(y) #To samo co x y 
z # set(['b', 'd'])
z.add('MIELONKA')
z  #set (['b', 'd', 'MIELONKA'])
z.update(set(['X', 'Y'])) # Polaczenie suma w miejscu 
 
# Metoda add wstawia jeden elemnt  update to suma zbiorow w miejscu a remove usuwa element 
# update to suma zbiorow w miejscu a remove usuwa element  o podanej wartosci aby zobaczyc wszystkie dostepne metody
# trzeba wykonac polecenie dir na dowolnej instancji zbioru lub nazwie typu zbioru 
z = x.intersection(y)
z # set(['b','d'])
z.add('MIELONKA')  # Wstawienie jednego elementu 
z # set(['b','d','MIELONKA'])
z.update(set(['X','Y'])) # Polaczenie suma w miejscu 
z # set(['Y','X','b','d','MIELONKA'])
z.remove('b')  # Usuniecie jednego elementu 
z # set(['Y','X','d','MIELONKA'])

# Zbiory w operacjach takich jak len petle for czy listy skladane 
for item in set('abc'): print(item * 3)
# aaa
# ccc
# bbb

# Wyrazenie zbiorow wymagaja podania dwoch zbiorow 
S = set([1, 2, 3])
S | set([3, 4])    # Wyrazenie wymaga by oba operandy byly zbiorow  # set([1, 2, 3, 4])
S | [3, 4]

S.union([3, 4])    # Metody zbiorow akceptuja dowolne typy iterowalne  # set([1, 2, 3, 4])
S.intersection((1, 3, 5))  # set([1, 3])
S.issubset(range(-5, 5))  # True

# Literaly zbiorow 3.x i 2.7
set([1, 2, 3, 4])  # {1, 2, 3, 4}  
set([1, 2, 3, 4])
set('mielonka') # Dodawanie wszystkich elementow obiektu iterowalnego 
# {'a', 'e', 'i', 'k', 'm', 'l', 'o', 'n'}
S.add('konserwowa') # Metoda add dziala jak poprzednio 
# {' ' ,  ...  , 'koserwowa' , 'e'}
S1 = {1, 2, 3, 4}
S1 & {1, 3}   # Czesc wspolna  # {1, 3}
{1, 5, 3, 6} | S1  # Suma  # {1, 2, 3, 4, 5, 6}
S1 - {1, 3, 4} # Roznica (2)
S1 > {1, 3} # Nadzbior  # True 
S1 - {1, 2, 3, 4} # Puste zbiory wyswietlane sa inaczej # set()
S = set()  # Inicjacja pustego zbiory 
S.add(1.23)
S # {1.23}
{1, 2, 3} | {3, 4} # {1, 2, 3, 4}
{1, 2, 3}.union([3, 4])   # {1, 2, 3, 4}
{1, 2, 3}.intersection((1, 3, 5))  # {1, 3}
{1, 2, 3}.issubset(range(-5, 5)) # True 

# Zbiory skladane w Pythonie 3.x
{x for x in 'mielonka'}  # To samo co : set('mielonka') # {'a', 'e' ,'i','k','m','l',o','n''}
{c*4 for c in 'mielonka'} # Zbior zebranmnych wynikow wyrazenie {'iiii','eeee','oooo','nnnn','mmmm','aaaa','llll','kkkk'}
{c * 4 for c in 'szynkajajka'} # {'yyyy','jjjj','nnnn','zzzz','ssss','aaaa','kkkk'}
S = {c*4 for c in 'mielonka'}
S | {'mmmm','xxxx'} # {'mmmm' 'eeee' 'xxxx' 'oooo' 'nnnn' 'iiii' 'aaaa' 'llll' 'kkkk'}
S & {'mmmm', 'xxxx'} # {'mmmm'}

L = [1, 2, 1, 3, 2, 4, 5]
set(L) #{1, 2, 3, 4, 5}
L = list(set(L)) # Usuwamy duplikaty 
L # [1, 2, 3, 4 , 5] 
set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]) # Wyszukawanie roznic w listach {3, 7}
set('abcdefg') - set('abdghij') # Wyszukiwanie roznic w ciagach znakow # {'c' 'e' 'f'}
set('spam') - set(['h','a','m']) # Wyszukiwanie roznic tryb mieszany {'p','s'} 
set(dir(bytes)) - set(dir(bytearray)) # Rozniva atrybutow miedzy typem bytes a bytearray ('__getnewargs__')
set(dir(bytearray)) - set(dir(bytes)) # {'append' , 'copy' , '__alloc__' , '__imul__' , 'remove' , 'pop' , 'insert' , ...i tak dalej ...}

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
L1 = L2  # Kolejnosc elementow w sekwencjach ma znaczenie  # False
set(L1) == set(L2) # Testowanie rownosci niezalezne od kolejnosci elementow 
sorted(L1) == sorted(L2) # Podobne dzialanie ale wyniki sa posortowane  # True
'spam' == 'asmp' , set('spam') == set('asmp') , sorted('spam') == sorted('asmp') # (False, True, True)

engineers = {'robert' ,'amedeusz' , 'anna' , 'aleksander'}
managers = {'edward' , 'amadeusz'} 
robert in engineers # True
enginners & managers  # Kto jest inzynierem i menedzerom?
enginners | managers  # Wszystkie osoby z dowolnej kategorii 
engineers - managers  # Inzynierowie ktorzy nie sa menedzerami  {'robert' , 'aleksander' , 'anna'}
managers - engineers  # Menedzerowie ktorzy nie sa inzynierami {'edward'}
engineers > managers  # Czy wszysscy menedzerowie sa inzynierami? (nadzbior) # False
{'robert','amadeusz'} < engineers # Czy obaj sa inzynierami ? (podzbior) # True 
(managers | engineers) > managers # Nadzbiorem menedzerow sa wszyscy pracownicy # True 
managers ^ engineers # Kto jest w jednym zbiorze ale nie obu? {'robert', 'edward', 'aleksander', 'anna'}
(managers | engineers) - (managers ^ engineers) # Czesc wspolna ! {'amadeusz'}

import sys 
sys.getrefcount(1) # 647 wskaznikow do tego miejsca w pamieci ( 647 )

S = ' ' # Pusty lancuch znakow 
S = "mielonka o nazwie 'Mielonksa' " # Cudzyslowy
S = 'm\ni\te\x00lonka' # Sekwencje znakow specjalnych 
S = """ ...wiele wierszy...""" # Blok w potrojnych cudzyslowach 
S = r'\temp\mielonka' # sUROWY LANCUCH ZNAKOW (BEZ znakow uczieczki)
S[i] # Indeeksowanie wycinek dlugosc 
S[i:j]
len(S)
"mala %s papuga" % kind # Wyrazenie formatujace lancuch znakow 
S.find('ie') # Wywolania metod lancuchow znakow (wszystkie 43 metody znajdziesz w dalszej czesci rozdzialu ): wyszukiwanie 
S.rstrip() # Usuwanie bialych znakow 
S.replace('ie','xx') # Zastepowanie 
S.split(',') # Dzielenie w miejscu wystapienia separatora 
S.isdigit() # Sprawdzania zawartosci 
S.lower() # Konwersja wielkosci liter 
S.endswith('mielonka') # Sprawzdanie koncowki lancucha znakow 
'mielonka'.join(strlist) # Zlaczenie z uzyciem separatora 
S.encode('latin-1') # Kodowanie Unicode 
for x in S: print(x) # Iteracja przynaleznosc 
'mielonka' in S 
[c * 2 for c in S] 
map(ord, S)
re.math('mi(.*)nka',line) # Dopasowywanie wzorca modul biblioteki 

# Lancuchy znakow w apostrofach i cudzyslowach sa tym samym 
'ryce"rz' , "ryce'rz" # ( 'ryce"rz' , "ryce'rz" )
'ryce\'rz' , "ryce\"rz" # ( "ryce'rz" , 'ryce"rz' )

# Sekwencje ucieczki reprezentuja znaki specjalne 
\<klawisz 
Enter>     # Znak kontynuacji wiersza 
\\  # Ukosnik lewy(zachowuje jeden znak \)
\a  # Sygnal dzwiekowy 
\b  # Znak cofania 
\f  # Wysuniecie strony (ang.form feed)
\n  # Powrot karetki 
\t  # Tabulator poziomy 
\v  # Tabulator pionowy 
\xhh  # Znak w zapisie szestnastkowym hh (dokladnie dwie cyfry)
\ooo  # Znak w zapisie osemkowym ooo (najwyzej trzy cyfry)
\O  # Null - binarny zapis znaku o kodzie 0 (nie sygnalizuje konca lancucha znakow)
\N{id}  # id to nazwa znaku w bazie Unicode 
\uhhh  # Szesnastobitowy kod znaku Unicode (zapisany w postaci dwoch liczb hex)
\hhhhhhhh  # Trzydziestobitowy kod znaku Unicode (zapisany w postaci czterech liczb hex)
\inny  # Nie jest sekwencja ucieczki (zachowuje znak \ oraz znak nastepujacy po nim)


mantra = """Zawsze patrz 
    na jasna
strone zycia """ 
mantra # 'Zawsze patrz\n na jasna\nstrone zycia.'
print(mantra) 
# Zawsze patrz 
#   na jasna 
# Strone zycia .

menu = """ szynka #komentarz umieszczony tutaj zostana dodane do tekstu!
       # o tym mowimy
       """
menu # 'szynka # komentarz umieszcziny tutaj zostana dodane do tekstu!\njajka # o tym mowimy \n'
menu = ( 
    ... "szynka\n" #tutaj komentarze sa ignorowane 
    ... "jajka\n" # ale nowe wiersze nie sa tworzone automatycznie 
)
menu # 'szynka\njajka\n'

len ('abc') # Dlugosc (len), czyli liczba znakow # ( 3 )
'abc' + 'def' # Konkatenacja - nowy lancuch znakow # 'abcdef'
'Ni' * 4
print('-' * 80) # 80 myslinow 

S = 'mielonka'
S[0], S[-2]   # Indeksowanie od poczatku lub od konca # ('m','k')
S[1:3], S[1:], S[:-1] #Wycinek - ekstrakcja czesci lancucha 

S = 'abcdefgijklmnop'
S[1:10:2]  # Pomijanie co drugagie elementu # 'bdfhj'
S[::2] 

S = 'halo'
S[::-1] # 'olah' # Odwracanie kolejnosci elementow

S = 'abcedfg'
S[5:1:-1] # Zmiana znaczenie granic # 'fdec'

'mielonka'[1:3]  # 'ie'  # Skladnia wycinania 
'mielonka'[slice(1, 3)] # Obiekty wycinkow 
'mielonka'[::-1] # 'aknoleim'
'mielonka'[slice(None, None, -1)] # 'aknoleim'

"42" + 1 # Type Error
"42" + 1 # TypeError
int("42"), str(42) # Komwersja z lancucha i na lancuch  # ( 42 , '42' ) 
repr(42) # Konwersja na lancuch w postaci kodu  # ( '42' )

S = "42"
I = 1
S + I # TypeError
int(S) + I # 43 # Wymuszenie dodawania
S + str(I) # '421' # Wymuszenie konkatenacji
str(3.1415), float("1.5") # ( '3.14.15' , '1.5' )
text = "1.234E-10"
float(text) 

#KONWERSJE KODU ZNAKOW 
ord('s') # 115
chr(115) # 's'
S = '5'
S = chr(ord(S) + 1) 
S = chr(ord(S) + 1)
S # '7'
int('5') # 5
ord('5') - ord('O') # 5
B = '1101' # Przeksztalcenie lancucha znakow w notacji dwojkowej na liczbe calkowita z uzyciem fukcji ord()
I = 0
while B: != '':
I = I * 2 + (ord(B[0]) - ord('0'))
B = b[1:]
I 
int('1101', 2) # 13 # Przeksztalcenie liczby binarnej na lczbe calkowita fukncja wbudowana

# MODYFIKOWANIE LANCUCHOW ZNAKOW 
S = S + 'MIELONKA!' # Aby zmienic lancuch nalezy utworzyc nowy 
S # 'mielonkaMIELONKA!'
S = S[:8] + 'Jajka' + S[-1]
S # 'mielonkaJajka!'

S = 'mielonka'
S = S.replace('lon', 'lonecz')
S # 'mieloneczka'

# SLADNIA WYWOLYWANIA METOD 
# Pobieranie atrybutu - Wyrazenie w  postaci obiekt.atrybut oznacza: "pobierz wartosc artybutu z obiektu"

# Wywolanie - Wyrazenie w postaci funkcja(argumenty) oznacza : "wywolaj kod funkcji , przekazujac jej zero lub wieksza liczba
# rozdzielonych przecinkami obiektow argumentow i zwroc wyniki dzialania funkcji"

# Polaczenie ze soba tych dwoch elementow pozwala na wywolanie metody obiektu .Metody sa wywplywamiem za pomoca nastepujacego wyrazenia
# obiekt.metoda(argumenty)

# Przetwarzane od lewej strony do prawej.Oznacza to ze Python najpierw pobiera metode obiektu a nastepnie wywoluje  ja przekazujac do niej 
# zarowno sam obiekt jak i argumenty Wyrazenie wywolujace 
# Wywolaj metode ktora bedzie przetwarzala obiekt razem z argumentami.

S = 'spam'
result = S.find('pa') # Wywolanie metody find w celu wyszukania ciagu znakow 'pa' w lancuchu znakow 


# METODY 
S.capitalize()
S.casefold()
S.center(width[ fill])
S.count(sub [, start [,end]])
Sencode([encoding [ , errors]])
S.endswith(suffix [ , start [ ,end]])
S.expandtabs([tabsize])
S.find(sub [, start [, end]])
S.format(fmtstr , *args, **kwargs)
S.index(sub[.start[, end]])
S.isalnum()
S.isalpha()
S.isdecimal()
S.isdigit()
S.isidentifier()
S.islower()
S.isnumeric()
S.isprintable()
S.isspace()
S.istitle()
S.isupper()
S.join(iterable)
S.ljust(width[, fill])
S.lower()
S.lstrip([chars])
S.maketrans(x[ , y[ , z]])
S.partition(sep)
S.replace(old, new[, count])
S.rfind(sub [ , start[ , end]])
S.rindex(sub [ , sub[, start [,end]]])
S.rjust(width [, full])
S.rpartition(sep)
S.rsplit([chars])
S.split([sep [ , maxsplit ]])
S.splitlines([keepends])
S.startswith(prefix [ , start [ , end]])
S.strip([chars])
S.swapcase()
S.title()
S.traslate(map)
S.upper()
S.zfill(width)

S = 'jajka'
S = S.replace('jk','blka') # Zamieniamy wszystkie wystapienia 'jk' na 'blk' w ciagu S
S # 'jablka'

S = 'xxxxJAJKAxxxxJAJKAxxxx'
where = S.find('JAJKA')      # Odszukanie pozycji 
where  # Wystepuje z przesunieciem  # 4
S = S[:where] + 'MIELONKA' + S[(where+4):]
S # 'xxxxMIELONKAxxxxJAJKAxxxx'

S = 'brama'
L = list(S)
L # ['b', 'r', 'a', 'm', 'a']
L[2] = 'e'
L[3] = 'j'
L # ['b' 'r' 'e' 'j' 'a']
S = ''.join(L)
S # 'breja'

'JAJKA'.join(['mielonka','ser','szynka','tost']) 
# 'mielonkaJAJKAserJAJKAszynkaJAJKAtost'

###########

# Metoda Wielka () konwertuje pierwszy znak ciągu na wielką literę, a wszystkie pozostałe litery na małe.
sentence = "python is AWesome"
#capitalize the first character
capitalized_string = sentence.capitalize()
print(capitalized_string)
# Python is awesome 

############

# Metoda składania () konwertuje wszystkie znaki ciągu na małe litery i zwraca nowy ciąg
text = "pYtHon"
# convert all characters to lowercase
lowercased_string = text.casefold()
print(lowercased_string)
# Output: python

#############

# Metoda Center() wycentruje łańcuch, używając określonego znaku (domyślnie spacja) jako znaku wypełnienia.
# LENGTH Wymagana długość. Długość zwróconego ciągu
# CHARACTER Znak opcjonalny. Znak, który wypełnia brakujące miejsce po obu stronach. Domyślnie jest to „ ” (spacja)
txt = "banana"
x = txt.center(20. "0") # 10 AAbnanaAA
print(x)
# OOOOOOObananaOOOOOOO

##############

# S.count = Metoda count() zwraca liczbę wystąpień podciągu w danym ciągu.
message = 'python is popular programming language'
# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p'))
# Output: Number of occurrence of p: 4

# Skladnia 
# Parametry COUNT()

# metoda count() wymaga tylko jednego parametru do wykonania. Posiada on jednak również dwa parametry opcjonalne:
string.count(substring, start = ... , end = ... )
#SUBSTRING  - PODciąg, którego liczba ma zostać znaleziona.
#Start (optional) - początkowy indeks w ciągu, w którym rozpoczyna się wyszukiwanie.
#End (optional) (opcjonalnie) - końcowy indeks w ciągu, w którym kończy się wyszukiwanie.
# Uwaga: Indeks w Python rozpoczyna się od 0, a nie 1.

# Liczba wystąpień danego podciągu
# define string
string = "Python is awesome , isn't it?"
substring = "is"
count = string.count(substring)
# print count
print("The count is:", count)
# The count is 2

# Policz liczbę wystąpień danego podciągu przy użyciu początku i końca
# define string
string = "Python is awesome , isnt it?"
substring = "i"
# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)
# print count
print("The count is:", count)
# Output The count is: 1

# Tutaj liczenie rozpoczyna się po pierwszym wystąpieniu, tj. 7. Pozycji indeksowej.
#I kończy się przed ostatnim i, tj. 25. Pozycją indeksu.
##################

# Sposób pyton endswith () stosuje się w celu określenia, czy dany łańcuch kończy sufiksów jeśli końcowy o określonej sufiksu powraca prawda inaczej False. Opcjonalne parametry "start" i "end" dla położenia początku i na końcu łańcucha wyszukiwania.
endswith () #Składnia metody:

str.endswith(suffix[, start[, end]])
# parametry
# sufiks - Parametr może być ciągiem lub element.
# start - położenie początku łańcucha.
# końcowy - pozycja końca bohaterów.
# Jeśli ciąg zawiera określony sufiks zwraca True, w przeciwnym wypadku False.
# Poniższy przykład ilustruje sposób endswith () instancji:

#!/usr/bin/python

str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);
#Przykłady powyższych wyników wyjściowych, są następujące:
True
True
True
False

#####################

# Metoda expandtabs() zwraca kopię ciągu ze wszystkimi znakami tabulatora „ ” zastąpionymi znakami whitespace do następnego parametru rozmiaru tabulatora.
# Składnia metody expandtabs() jest następująca:
string.expandtabs(tabsize)
#  Parametry rozszerzeń
# Expnaptabs() przyjmuje argument o rozmiarze tabeli liczby całkowitej. Domyślny rozmiar tabeli to 8.
# Exptables() zwraca ciąg znaków, w którym wszystkie znaki '' są zastępowane znakami whitespace do następnego parametru rozmiaru tabeli.

str = 'xyz\t12345\tabc'
# no argument is passed
# default tabsize is 8
result = str.expandtabs()
print(reslut)
# xyz 12345 abc

str = "xyz\t12345\tabc"
print('Original String:' str)
#ntabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))
print('Tabsize 3:', str.expandtabs(3))
print('Tabsize 4:',str.expandtabs(4))
print('Tabsize 4:',str.expandtabs(5))
print('Tabsize 4:',str.expandtabs(6))

# Tabsize 2: xyz 12345 abc
# Tabsize 3: xyz    12345 abc
# Tabsize 4: xyz 12345   abc
# Tabsize 5: xyz  12345     abc
# Tabsize 6: xyz   12345 abc

#Wyjaśnienie
#Domyślny rozmiar tabeli to 8. Ograniczniki uchwytów to 8, 16 itd. Dlatego też po wyrażeniu „xyz” i 3 po „12345” po wydruku oryginalnego ciągu znajduje się 5 spacji.
#Po ustawieniu rozmiaru tabeli na 2. Ograniczniki tabulacji to 2, 4, 6, 8 itd. W przypadku wartości „xyz” ogranicznik zakładki wynosi 4, a w przypadku wartości „12345” ogranicznik zakładki wynosi 10. Stąd jest 1 miejsca po 'xyz' i 1 miejsca po '12345'.
#Po ustawieniu rozmiaru tabeli na 3. Ograniczniki tabulacji to 3, 6, 9 itd. W przypadku wartości „xyz” ogranicznik zakładki wynosi 6, a w przypadku wartości „12345” ogranicznik zakładki wynosi 12. Stąd, po 'xyz' i 1 spacji po '12345', jest 3 spacji.
#Po ustawieniu rozmiaru tabeli na 4. Ograniczniki tabulacji to 4, 8, 12 itd. W przypadku wartości „xyz” ogranicznik zakładki wynosi 4, a w przypadku wartości „12345” ogranicznik zakładki wynosi 12. Stąd jest 1 miejsca po 'xyz' i 3 spacji po '12345'.
#Po ustawieniu rozmiaru tabeli na 5. Ograniczniki tabulacji to 5, 10, 15 itd. W przypadku wartości „xyz” ogranicznik zakładki wynosi 5, a w przypadku wartości „12345” ogranicznik zakładki wynosi ...

##################

# Metoda find() zwraca indeks pierwszego wystąpienia podciągu (jeśli został znaleziony). Jeśli nie zostanie znaleziony, zwraca -1.
message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))

# Output: 12

str.find(sub[,start[,end]])
# Metoda find() wymaga maksymalnie trzech parametrów:
# SUB - It to podciąg, który ma być wyszukiwany w ciągu str.
# start and end (optional) - zakres str[start:end], w którym wyszukiwany jest podciąg.

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

#Substring 'let it': 11
#Substring 'small ': -1
#Contains substring 'be,'



quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

# -1
# 3
# -1
# 9

################
# Przyklad 1
S.format(fmtstr , *args, **kwargs)
def funk(a,b,c):
    pass
#Z czasem, pojawia się konieczność, przygotowania naszej funkcji na przyjęcie zmiennej liczby parametrów. Tutaj, z pomocą przychodzi nam pojedyncza * i podwójna **.

def funk(*args):
    print(args)
        
funk(1,2,3)
funk(1,2,3,4)
# A w rezultacie otrzymamy:
def funk(*args):
    print(args)
funk(1 , 2 , 3)
funk(1, 2, 3, 4)

# Definicja naszej funkcji, zawiera zmienną, której nazwa rozpoczyna się od *
# Jest to informacja, że parametry przekazane do funkcji, należy 'spakować’, do zmiennej typu krotka. Czyli forma podobna do listy, lecz niemodyfikowalna.
# Tym samym, niezależnie, z jaką ilością parametrów, wywołamy funkcję, czy 0 czy 100, wszystkie zostaną umieszczone w krotce. W tym przypadku, jest to nazwa args
# Nazwa args, jest standardową nazwą w tym przypadku, jednak, może to być dowolna, inna nazwa zmiennej, jak np. *a.

# Przykład 2 – *args:
def funk(*args):
    print("Liczba przekazanych parametrów:",len(args))
    for arg in args:
        print ("Wartość:",arg)
    
lista = [1,3,5,6]
    
funk(1,lista,2,'xyz',3)
# Co w rezultacie, da nam:

# Liczba przekazanych paranetrow : 5
# Wartosc : 1
# Wartosc : [1, 3, 5, 6]
# Wartosc : 2
# Wartosc : xyz
# Wartosc : 

# Przykład 3 – **kwargs:
def funk(**kwargs):
    print("Liczba przekazanych parametrów:",len(kwargs))
    
    for key, item in kwargs.items():
        print ("Klucz:", key, "Wartość:", item)

funk(a=1,b=2,c=3)
# Liczba przekazanych parametrow : 3
# Klucz c Wartosc : 3
# Klucz b Wartosc : 2
# Klucz a Wartosc : 1

# Przykład 4 – *args oraz **kwargs:
def funk(*args, **kwargs):
    
    print("Liczba przekazanych parametrów *args:",len(args))
    for arg in args:
        print ("Args - Wartość:", arg)
    
    print("Liczba przekazanych parametrów **kwargs:",len(kwargs))
    for key, item in kwargs.items():
        print ("Kwargs - ", "Klucz:", key, "Wartość:", item)

funk(11,22,['x','y','z'],a=1,b=2,c=3)

# liczba przekazanych parametrow *args : 3
# Args - Wartosc : 11
# Args - Wartosc : 22
# Args - Wartosc: ['x', 'y' , 'z']
# Liczba przekazanych parametrow **kwargs : 3
# Kwargs - Klucz : c Wartosc : 3
# Kwargs - Klucz : b Wartosc : 2
# Kwargs - Klucz : a Wartosc : 1

#Ćwiczenie 1: Należy, przygotować funkcję, sumującą, wszystkie zmienne, podane jako parametry funkcji. Przykładowo:
#funk(1,2,3,4), zwróci, wartość 10

#Ćwiczenie 2: Należy, przygotować funkcję, która zawsze przyjmuje co najmniej jeden parametr – nazwisko, natomiast jako parametr, imię oraz wiek, znanych osób z rodziny. Np
#funk(’Kowalscy’,Ewa=33, Michał=44)

def funk(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

print ( funk(1,2,3,4)  )

def funk(nazwisko, **kwargs):
    print("Nazwisko:", nazwisko)
    for key, item in kwargs.items():
        print("Imię:",key,"Wiek:", item)
        
funk ("Kowalscy",Ewa=33, Michał=44)

#############################

S.index(sub[.start[, end]])
#Metoda index() zwraca indeks podciągu w ciągu (jeśli został znaleziony). Jeśli podciąg nie zostanie odnaleziony, pojawia się wyjątek.

#Przykład
text = 'Python is fun'


# find the index of is
result = text.index('is')
print(result)

# Output: 7
#Parametry Index()

#Metoda index() przyjmuje trzy parametry:

# sub - podciąg, który ma być wyszukiwany w stru str.
# początek i koniec (opcjonalnie) - wyszukiwany jest podciąg w str[start:end]

# Index() wartość zwrotna

# Jeśli w ciągu istnieje ciąg podrzędny, zwraca on najniższy indeks w ciągu, w którym znajduje się ciąg podrzędny.
# Jeśli w ciągu nie ma podciągu, pojawia się wyjątek ValueErm.
# Metoda index() jest podobna do metody find() dla ciągów znaków.

# Jedyna różnica polega na tym, że metoda find() zwraca -1 jeśli podciąg nie zostanie znaleziony, podczas gdy index() rzuca wyjątek.
sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)
#Substring 'is fun': 19

#Traceback (most recent call last):
#  File "<string>", line 6, in 
#    result = sentence.index('Java')
# ValueError: substring not found

# Example 2: index() With start and end Arguments
sentence = 'Python programming is fun.'

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))

# 15
# 17

######################

S.isalnum()

#Metoda Isalnum() zwraca wartość True, jeśli wszystkie znaki w ciągu są alfanumeryczne (alfabetami lub cyframi). Jeśli nie, zwraca Fałsz.
#Przykład
# string contains either alphabet or number 
name1 = "Python3"

print(name1.isalnum()) #True

# string contains whitespace
name2 = "Python 3"

print(name2.isalnum()) #False

# isalnum() Syntax
# The syntax of the isalnum() method is:
# W tym miejscu metoda Isalnum() sprawdza, czy wszystkie znaki ciągu są alfanumeryczne czy nie.

S.isalnum()
# Metoda Isalnum() zwraca:

# True - jeśli wszystkie znaki w ciągu są alfanumeryczne
# Fałsz - jeśli co najmniej jeden znak nie jest alfanumeryczny

# contains either numeric or alphabet
string1 = "M234onica"

print(string1.isalnum()) # True 

# contains whitespace
string2 = "M3onica Gell22er"

print(string2.isalnum()) # False

# contains non-alphanumeric character 
string3 = "@Monica!"

print(string3.isalnum()) # False 

True
False
False
# W powyższym przykładzie użyliśmy metody Isalnum() z różnymi ciągnami, aby sprawdzić, czy każdy znak w ciągu jest alfanumeryczny.

# W tym miejscu, string1 zawiera albo litery, albo wartości numeryczne, więc metoda zwraca True.

# Metoda zwraca wartość Fałsz dla string2 i string3, ponieważ zawierają znaki niealfanumeryczne, tj. białe, @, !.

text = "Python#Programming123"

# checks if all the characters are alphanumeric 
if text.isalnum() == True:
   print("All characters of string are alphanumeric.")
else:
    print("All characters are not alphanumeric.")

# All characters are not alphanumeric.
# Tutaj użyliśmy instrukcji IF..else, aby sprawdzić, czy wszystkie znaki w tekście są alfanumeryczne czy nie.

# Ponieważ "Python#Programming123" zawiera #, który nie jest ani alfabetem, ani cyfrą, tekst.isalnum() zawiera False.

# Tak więc program wykonuje wyrażenie ELSE.

###################

S.isalpha()
# Metoda isalpha() zwraca wartość True, jeśli wszystkie znaki w ciągu są alfabetami. Jeśli nie, zwraca Fałsz.

# Składnia isalpha() jest:
string.isalpha()
# Isalpha() zwraca:

# Prawda, jeśli wszystkie znaki w ciągu są alfabetami (może to być zarówno małe, jak i wielkie litery).
# Fałsz, jeśli co najmniej jeden znak nie jest alfabetem.

name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())
True 
False
False


name = "MonicaGeller"

if name.isalpha() == True:
   print("All characters are alphabets")
else:
   print("All characters are not alphabets.")

# All characters are alphabets

########################

S.isidentifier()

# Metoda z izjfifą zwraca wartość True, jeśli ciąg jest prawidłowym identyfikatorem w Python. Jeśli nie, zwraca Fałsz.
string.isidentifier()
# Metoda z zastosowaniem operatora() zwraca:

# Prawda, jeśli ciąg jest prawidłowym identyfikatorem
# Fałsz, jeśli ciąg nie jest nieprawidłowym identyfikatorem
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())

True
False
False
False
# Example 2: More Example of isidentifier()

str = 'root33'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
  
str = '33root'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')
  
str = 'root 33'
if str.isidentifier() == True:
  print(str, 'is a valid identifier.')
else:
  print(str, 'is not a valid identifier.')

# root33 is a valid identifier.
# 33root is not a valid identifier.
# root 33 is not a valid identifier.

########################

S.islower()
string.islower()
# Metoda isniżej() nie bierze żadnych parametrów.
# Metoda isniżej() zwraca:

# Prawda, jeśli wszystkie alfabety istniejące w ciągu są alfabetami małymi literami.
# Fałsz, jeśli ciąg zawiera co najmniej jedną wielką literę alfabetu.
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

# True
# True
# False

s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
  
s = 'this is Good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')

# Does not contain uppercase letter.
# Contains uppercase letter.

#####################
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
col1 # 'aaa'
col3 # 'ccc'

line = 'aaa bbb ccc'
cols = line.split( )
cols ['aaa','bbb','ccc']

line = 'amadeusz,haker,40'
line.split(',')
# ['amadeusz','haker','40']

line = "jestemMIELONKAdrwalemMIELONKAiMIELONKAjestemMIELONKAOK"
line.split("MIELONKA")
# ['jestem','drwalem','i','jestem','Ok']

line = "Rycerz, ktorzy mowia Ni!\n"
line.rstrip() # "Rycerz, ktorzy mowia Ni!"
line.upper() # "Rycerz, ktorzy mowia Ni!\n"
line.isalpha( ) # False
line.endswith('Ni!\n') # True
line.startswith('Rycerze') # True

S = 'a+b+c'
x = S.replace('+','jajka')
x # ' ajajkabjajkacjajka '

import string 
y = string.replace(S, '+' , 'jajka')
y  # ' ajajkabjajkacjajka ' 

' Ten %d %s jest martwy!' % (1 , 'ptak')   # Wyrazenie formatujace   # Ten 1 ptak jest martwy! 

exclamation = "Ni"
"Rycerze, ktorzy mowia %s!" % exclamation # Podstawianie lancucha znakow  # ' Rycerze ktorzy mowia Ni! '
"%d %s %d you " % (1,'spam', 4) # Podstawienie zalezne od typu  # ' 1 spam 4 you '
"%s -- %s -- %s" % (42, 3.14159, [1, 2, 3])  # Wszystkie typy pasuja do znacznika %s   # " 42 -- 3.14159 -- [1, 2, 3]"

 
# 1.  s ------> Lancuch znakow (lub dowolny obiekt str( X ))
# 2.  r ------> To samo co s z tym ze wykorzystuje funkcje repr, anie str
# 3.  c ------> Znak (int lub str)
# 4.  d ------> Liczba dziesietnych 
# 5.  i ------> Liczba calkowita 
# 6.  u ------> To samo co d (przestrzale dawniej wymuszalo liczbe calkowita bez znaku)
# 7.  o ------> Liczba osemkowa (podstawa 8)
# 8.  x ------> Liczba szestnastkowa (podstawa 16)
# 9.  X ------> To samo co x, jednak wyswietlane wielkimi literami 
# 10. e ------> Liczba zmiennoprzecinkowa w formacie wykladniczym mala litera 
# 11. E ------> To samo co e , wyswietlane wielka litera 
# 12. f ------> Liczba zmiennoprecinkowa w zapisie dziesietnym(wielkie litery)
# 13. F ------> Liczba zmiennoprzecinkowa w zapisie dziesietnym( wielkie litery )
# 14. g ------> Zmienoprzecinkowe e lub f 
# 15. G ------> Zmiennoprzecinkowe E llub F 
# 16. % ------> Literal (zapisywany jako %%)
  
x = 1234
res = "integers: ...%d...%-6d...%06d" % (x, x, x)
res # 'integers: ...1234....1234....001234'

x = 1.23456789
x # 1.123456789

'%e | %f | %g % (x, x, x)'
# '1.23468e+000 | 1.234568 | 1.23457'

'%E' % x  # '1.234568e+00'

import pyjokes 
pyjokes.get_joe()
# What does 'Emacs' stand for ? Exclusively used by middle aged comp[uter scientists
pyjokes.get_joke(category='neutral')
# A programmer had a problem He thought to himself , 'I know I'll solveit with theads! has Now problems two he 
pyjokes.get_joke(category='chuck')
# There is no Esc key no Chuck Norris ' keyboARD, because no one escapes Chuck Norris"
pyjikes.get_joke(category='chuck')
# Chuck Norris can write infinitely recursive  functions and have them return 
pyjokes.get_joke(category='chuck')
# Chuck Norris programs never exit , they are terminated 
# Wygeneruj anegdoty
# Nie najbardziej użyteczny, ale bardzo ciekawa paczka pyjokes daje różne dowcipy i anegdoty w 6 językach. Ale rosyjski, niestety, nie jest uwzględniony w tym numerze.
# Metoda Get_joke zwraca ciąg zawierający losowy żart. Można określić język w argumencie, domyślnie jest to język angielski.
# Można również określić kategorię w argumentach - szczególnie fajne, aby przejść do rzeczy o Chuck Norris oznaczone 'Chuck'.



class A :
    pass 
class B :
    value = 1
class C :
    value = 3
class D(A,B,C):
    def __str__(self):
        return str(self.value)
print(D())
#Output: 1
print(D.__mro__)
# Procedura rozwiązywania metod
# W języku Python istnieje tzw. metoda Resolion Order (MRO) lub klasa rozdzielczości. Wszystko, co musisz wiedzieć, to kolejność, w jakiej Python szuka odpowiedniego atrybutu lub metody.
# To zamówienie można uzyskać przez __mro__. Mówi on, że jeśli w powyższym przykładzie spróbujemy odnieść się do atrybutu wartości, Python najpierw wyszuka w klasie A, a następnie w B, Potem w C i na samym końcu w obiekcie.
# Z tego wynika jasno, że artykuł zostanie znaleziony jako pierwszy w klasie B i będzie miał wartość 1.


# pip install qrcode[pil]
import qrcode 
image = qrcode.make('https://example.com')
image.save('qr.png')

#Wygeneruj kod QR
#Prosty, ale wygodny i przydatny pakiet do tworzenia kodów QR. Do rysowania zdjęć jest używana poduszka, więc upewnij się, że jest zainstalowana.
#Aby utworzyć obiekt obrazu z kodem QR, należy wywołać make() i przekazać dane jako argument. Aby zapisać, należy zastosować metodę Save() do uzyskanego obiektu.
#Inny pakiet pozwala na tworzenie kodów QR na podstawie zdjęć i w 6 różnych stylach. Ale o tym wszystkim, a także o zaawansowanych przykładach użycia przeczytasz w ich dokumentacji.

txt = "Thank you for the music\n"
"Welcome to the jungle"
x = txt.splitlines()
print(x)
# ['Thank you for the music ',
# 'Welcome to the jungle ']

#przewody rozdzielające splitlines()
#Metoda splitlines() powoduje podział wiersza na listę. Podział jest wykonywany na liniach podziałowych. Opcjonalnie określ, czy mają być uwzględnione odstępy między wierszami (Prawda) czy nie (Fałsz). Wartością domyślną jest Fałsz.

import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) # (array([3, 5, 6]))

#NumPy: Wyszukuje w masywy
#Możesz wyszukać konkretną wartość w tablicy i zwrócić indeks, który chcesz dopasować. Użyj metody where(), aby wyszukać w tablicy. W tym przykładzie wyszukuje się współczynniki, dla których wartość wynosi 4.

nums = [2, 3 , 1, 5, 6, 4, 8]
print(sorted(nums))  # [0, 1, 2, 3, 4, 5, 6]
print(nums)  # [2, 3, 1, 5, 6, 4, 0]
print(nums.sort())  # None 
print(nums)  # [0, 1, 2, 3, 4, 5, 6]

# Sortowanie list
#Python ma dwie wbudowane metody sortowania list: Funkcję sortowane() i metodę list.sort(). Wynik jest taki sam w obu przypadkach, ale nadal istnieją niuanse.
#Funkcja Sort() akceptuje argument w postaci listy i zwraca już nową, posortowaną listę. W tym momencie lista źródeł nie zmienia się.
#Metoda sort() jest z kolei stosowana do listy, bezpośrednio ją zmienia i nie zwraca niczego.


try:
    print(1/0)
except Exception as exc:
    print(exc)
"""Division by zero"""

try:
    import asdsad
except ImportError as exc:
    print(exc)
"""No module named asdasd"""

#Przetwarzanie wyjątków
#Wyjątki to rodzaj danych, które należy nam przekazać w przypadku błędów.
#Istnieje podstawowy wyjątek BaseException, z którego dziedziczone są wszystkie inne wyjątki.
#W bloku Try (Spróbuj) stosujemy się do instrukcji, która może spowodować wyjątek, a w polu poza blokiem wychwytujemy błędy i wykonujemy nasze operacje.
#Warto wziąć pod uwagę, że możemy zrobić wiele zainwestowanych bloków.
#Jest to dobry sposób na łapanie tylko tych wyjątków, których oczekujemy.


complex(1,3)
# (1+3j)
complex(1, 3).real 
# 1.0
complex(1, 3).imag 
# 3.0
abs(complex(3, 4))
# 5.0
str(complex(1, 3))
# '(1+3j)'
(3+2j) - (2-5)
# (1+7j)



#Korzystanie ze złożonych liczb w Python
#Nikt nie może zaskoczyć takich wbudowanych typów jak int, float i podobne. Ale oprócz nich, Python ma inny dość interesujący typ, mianowicie złożony.
#W Python Complex liczby są reprezentowane w postaci x + yy. A dokładniej, zamiast liter i tutaj litera j służy uniknięciu jakiegoś pomylenia, jak często zajmowałem się cyklami. Python przekształca rzeczywiste liczby x i y (int lub float) w złożone liczby za pomocą funkcji Complex(x,y).
#Złożony numer można łatwo przekształcić w ciąg za pomocą str lub jego moduł może być rozważany przez funkcję abs, a także rzeczywiste lub wyimaginowane części można uzyskać za pomocą metod rzeczywistych i imag.
#Mimo że kompleks jest wbudowany, zaleca się importowanie modułu cmath w celu wygodniejszej obsługi skomplikowanych operacji.

class Foo(object):__slots__=('foo')
class Bar(object): pass 
def get_set_delete(obj):
    obj.foo = 'foo'
    obj.foo
    del obj.foo
def test_foo():
    get_set_delete(Foo())
def test_bar():
    get_set_delete(Bar())

#Zbiór szkiełek ( slots )
#Python używa dict do przechowywania atrybutów specyficznych dla obiektu. Jest to przydatne w przypadku dowolnej liczby atrybutów. W małych klasach jest to problem – dict spędza dużo pamięci RAM. Python nie może po prostu przypisać statycznej ilości pamięci do przechowywania wszystkich atrybutów. Aby to zrobić, musisz użyć gniazd. Natychmiast wskaż wszystkie oczekiwane atrybuty. W ten sposób można zmniejszyć zużycie pamięci RAM o prawie 40-50 procent.
#Film pomoże Ci zrozumieć gniazda.

import sys 
sys.getsizeof(5)
# 28
sys.getsizeof(range(0, 10000))
# 48
sys.getsizeof([ 1, 2, 'c'])
# 88 
#Obliczanie rozmiaru obiektów
#Aby obliczyć rozmiar obiektu, możemy użyć funkcji gessizeof(Object[, default]) z modułu sys. Ponieważ Python wszystkie w rzeczywistości są obiektami, następnie obliczyć rozmiar pamięci możemy na każdym obiekcie.
#I chociaż wszystkie wbudowane (wbudowane) obiekty i obracają się w odpowiednim rozmiarze, ogólnie rzecz biorąc, nie powinny być poprawne dla żadnych obiektów użytkownika.
#Domyślny argument pozwala określić wartość, która zostanie zwrócona, jeśli typ obiektu nie zapewni środków do usunięcia rozmiaru i wyświetli TypeErr.
#Funkcja getsizeof wywołuje metodę obiektu __sizeof__ i dodaje dodatkowe dane biurowe do kolekcji śmieci.


##############

#Wyrażenia lambda sa to jednolinijkowe anonimowe funkcje , bez nazwy Tworzesą za pomocą słówa kluczowego
# lambda po którym nastepuje lista parametrów .Po dwokropku znajuje się właściwy kod funkcji .Funkcję 
#lambda mozna tez przypisac do zmiennej i wywołać jak zwykłą funkcję.

# Ponizsza funkcja lambda przyjmuje dwa argumenty a oraz b i zwrac ich sumę , return nie jest potrzebne ,
#wynik wyrazenia jest automatycznie zwracany z lambda.

sum = lambda a,b:a+b
print( sum(10,5) ) #15
print( sum(4,3) ) #7



#Wyrazenie lambda moze byc równiez zwrocone przez zwykłą funkcję , dzięki czemu mozna ją wywołać w razie 
# potrzeb

#zwróona jest funkcja lambda która zapamięta wartość n
def genFunc(n):
    return lambda a: a * n

doubler = genFunc(2)  #w doubler jest lambda z n o wartosci 2

print(doubler(5) ) #10
print(doubler(7) ) #14

tripler = genFunc(3)   
print( tripler(2) )    #6
print(tripler(3) )     #9

#Wyrażenie lamda z map()
#Wyrażenie lambda przydają się najbardziej w funkcjach wyższego rzędu czyli takich , które jako argument
#przyjmują inne funkcje lub zwracają funkcję 
# Przykładem jest funkcja r = map(func,seq) przyjmuje funkcję którą wywoła na wszystkich elementach seq,
#po czym zwróci sekwencję zmodyfikowanych przez func elementów w postaci literatora więc można skonwerować 
# wynik na listę poprzez list()
listData = [1,2,3,4,5]
result = map (lambda x:x*2,listData)
print(list(result) )    # [2,4,8,10]

print(list(map(lambda x : x * 3,[1,2,3,4])))    #[3,6,9,12]


#Wyrazenie lambda przydają się najbardziej w funkcjach wyższego rzędu czyli takich,które jako argument
# przyjmują inne funkcje lub zwracają funkcje.

#Funkcja reduce redukuje sekwencję do pojedynczej wartości 

from functools import reduce  #import funkcja reduce
numSum = reduce((lambda x, y:x+y),[1,2,3,4,5])
print("Suma liczb :",numSum)  

######################

complex (1, 3) # (1+3j)
complex(1, 3).real # 1.0
complex(1, 3).imag #  3.0
abs(complex(3, 4)) # 5.0
str(complex(1, 3)) # '(1+3j)' 
(3 + 2j) - (2 - 5j) # (1 + 7j)
# Korzystanie ze złożonych liczb w Python
# Nikt nie może zaskoczyć takich wbudowanych typów jak int, float i podobne. Ale oprócz nich, Python ma inny dość interesujący typ, mianowicie złożony.
# W Python Complex liczby są reprezentowane w postaci x + yy. A dokładniej, zamiast liter i tutaj litera j służy uniknięciu jakiegoś pomylenia, jak często zajmowałem się cyklami. Python przekształca rzeczywiste liczby x i y (int lub float) w złożone liczby za pomocą funkcji Complex(x,y).
# Złożony numer można łatwo przekształcić w ciąg za pomocą str lub jego moduł może być rozważany przez funkcję abs, a także rzeczywiste lub wyimaginowane części można uzyskać za pomocą metod rzeczywistych i imag.
# Mimo że kompleks jest wbudowany, zaleca się importowanie modułu cmath w celu wygodniejszej obsługi skomplikowanych operacji.

######################

class Foo(object): __slots__ = ('foo',)
class Bar(object): pass 

def get_set_delete(obj):
    obj.foo = 'foo'
    obj.foo
    del obj.foo
def test_foo():
    get_set_delete(Foo())
def test_bar():
    get_set_delete(Bar())
#Zbiór szkiełek

#Python używa dict do przechowywania atrybutów specyficznych dla obiektu. Jest to przydatne w przypadku dowolnej liczby atrybutów. W małych klasach jest to problem – dict spędza dużo pamięci RAM. Python nie może po prostu przypisać statycznej ilości pamięci do przechowywania wszystkich atrybutów. Aby to zrobić, musisz użyć gniazd. Natychmiast wskaż wszystkie oczekiwane atrybuty. W ten sposób można zmniejszyć zużycie pamięci RAM o prawie 40-50 procent.

######################

format(0.1,'.17f')
# '0.1000000000000000001'
from decimal import Decimal 
Decimal(1) / Decimal(3)
#Decimal('0.33333333333333333333333')
(Decimal(1) / Decimal(3)) * Decimal(3) == Decimal(1)
# False

from fractions import Fraction 
(Fraction(1) / Fraction(3)) + Fraction(3) == Fraction(1)
# True 

# Decimal i fraction

#Ponieważ liczby ułamkowe z punktem pływającym są przechowywane w podwójnej formie, zazwyczaj pracujemy z przyblionymi wartościami, tak jak w pierwszym wariancie na ekranie.
#Aby uzyskać dokładniejsze wyniki, można użyć klasy Decimal, ale w niektórych przypadkach może to nie wystarczyć.
#W tym przypadku lepiej jest użyć frakcji klasowej(Fraction) do idealnych obliczeń, ponieważ działa z licznikiem w postaci frakcji rozumowych.

######################

import pymongo 
myclient = pymongo.Mongo.MongoClient("mongodb://localhost://localhost:4234234/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)
    MongoDB: Sortuj

#Użyj metody sort(), aby posortować wynik w kolejności wzrostu lub spadku. metoda sort() akceptuje jeden parametr dla nazwy pola i jeden parametr dla kierunku (domyślny kierunek wzrostu). Jeśli chcesz posortować w kolejności redukcji, użyj -1 jako drugiego parametru.

#####################

import sys
sys.getsizeof(5) # 28
sys.getsizeof(range(0, 1000)) # 48
sys.getsizeof([1, 2, 'c']) # 88

#Obliczanie rozmiaru obiektów
#Aby obliczyć rozmiar obiektu, możemy użyć funkcji gessizeof(Object[, default]) z modułu sys. Ponieważ Python wszystkie w rzeczywistości są obiektami, następnie obliczyć rozmiar pamięci możemy na każdym obiekcie.
#I chociaż wszystkie wbudowane (wbudowane) obiekty i obracają się w odpowiednim rozmiarze, ogólnie rzecz biorąc, nie powinny być poprawne dla żadnych obiektów użytkownika.
#Domyślny argument pozwala określić wartość, która zostanie zwrócona, jeśli typ obiektu nie zapewni środków do usunięcia rozmiaru i wyświetli TypeErr.
#Funkcja getsizeof wywołuje metodę obiektu __sizeof__ i dodaje dodatkowe dane biurowe do kolekcji śmieci.

######################

import math 
print(math.ceil(1.4)) # 2
print(math.ceil(5.3)) # 6
print(math.ceil(-5.3)) # -5
print(math.ceil(22.6)) # 23
print(math.ceil(10.0)) # 10

#math.ceil
#math.ceil() zaokrągla liczbę do najbliższej liczby całkowitej do większej strony, jeśli to konieczne i zwraca wynik. Aby zaokrąglić liczbę w dół do najbliższej całości, użyj metody matematyka.floor().

######################

def function(value, *args, **kwargs):
    print(value)
    print(keys)
    print(kwargs)
function(42,'text',12345,[1, 2, 3], pi = 3.14, name='Adrian')

#42
# {'text' 12345, [1, 2, 3]}
# {'pi': 3.14, 'name': Adrian}

#Parametry * Args i **krakergs
#Przynajmniej raz zobaczyliśmy taki zapis, a teraz dowiemy się, co to jest dla symboli. Powiem od razu, że argi i kawargi są powszechnie akceptowanymi nazwami zmiennych, a my posortujemy gwiazdy przed nimi.
#W tym przykładzie funkcja akceptuje argument wartości obowiązkowej i inne argumenty, których nie oczekuje. W tym przypadku *args pakowaÄ wszystkie nienazwane argumenty w oblężeniu, i **kawargi – wszystkie nazwane w słowniku.
#Budowa *args, ** kawargi jest bardzo przydatna, jeśli nie wiemy, kto i w jakich celach będzie korzystać z naszej funkcji. Oznacza to, że możemy prosi o argumenty prawie wszystko.

######################

import difflib 
m_list = ['ape','apple','peach','puppy']
difflib.get_close_matches('appel', m_list, n=2)
# ['apple', 'ape']

#Znajdziemy podobne linie
#Domyślna biblioteka Python ma moduł dyfklib, który posiada metodę Get_Close_matches.
#Ta metoda wyszukuje „najlepsze” możliwe mecze. Pierwszy argument określa ciąg, drugi argument określa listę, na której przeprowadzane jest wyszukiwanie.
#Można również przekazać opcjonalny argument n do metody, która ustawia maksymalną liczbę dopasowań zwrotu.

######################

from itertools import cycle, islice
colors = cycle(['red', 'white', 'blue'])
for item in colors:
    print(item, end= ' ')
for color in islice(colors, 3,5):
    print(color, end=' ')
#Output: red white
#Utwórz beztwarzy iteratora
#Funkcja cycle() from itertools akceptuje obiekt, który jest czyszczony i tworzy niekończący się iterator, który cyklicznie cofa elementy obiektu.
#Chip polega na tym, że po zakończeniu elementów sekwencji iteracja rozpoczyna się ponownie od pierwszego elementu.
#Ale jeśli przejdziesz przez cykl na takim instrumentrze, ważne jest, aby przewidzieć wyjście z cyklu, w przeciwnym razie będzie ono nieograniczone (jak mamy w pierwszym przypadku na zdjęciu).
#Możemy również użyć islice(), który zwróci Iterator na podzbiór przesłanych obiektów.

######################

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) # #hELLO mY nAME iS peter

#swapcase
#Metoda swapCase() konwertuje wszystkie wielkie litery na małe i wszystkie małe litery na wielkie.
#Jeśli chcesz skonwertować ciąg znaków tylko do małych liter, użyj funkcji Dolna(). Podobnie, jeśli chcesz przekonwertować ciąg tylko na wielkie litery, użyj Upper()

######################

import pprint
data = [
    {'Name': 'Allice XXX', 'Age': 40, 'Points': [80, 20]},
    {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]}
]
pprint.pprint(data, depth=2)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [...]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [...]}]
pprint.pprint(data, width=41)
# [{'Age': 40,
#   'Name': Alice XXX',
#   'Points': [80, 20]},
#  {'Age': 20,
#   'Name': 'Bob YYY',
#   'Points': [90, 10]}]
text = pprint.pformat(data) 

#Wytworzymy wstawione słowniki i listy
#Kiedy wyjmujesz wstawione słowniki i listy za pomocą zwykłej Print(), otrzymujemy wszystko w jednej linii i w niewybiórczej formie.
#Ale standardowa biblioteka ma moduł druku, który pomoże przynieść taki przypadek w dobrym formacie – wystarczy zastąpić Print() w kodzie pprint.pprint().
#Ciekawymi argumentacją jest głębokość, która odpowiada za głębokość wyjścia, a szerokość, czyli szerokość wyjścia w konsoli.

#####################

from captcha.image import ImageCaptcha
pattern = "1234ABCD"
#Robimy obiekt zdjecia pod captcha
captcha = ImageCaptcha(width=300, height=200)
# Generujemy i zapisujemy captcha do pliku 
captcha.write(pattern,"captcha.png")

#Generowanie captcha
#Dziś pokażemy stworzenie najprostszej captcha. Aby to zrobić, potrzebujemy captcha i poduszki do tworzenia obrazów w captcha.
#Wszystko jest tak proste, jak to możliwe, w rzeczywistości wszystko odbywa się w kodzie modułu. Utwórz obiekt programu Image Captcha, na którym chcesz drukować. Następnie należy wywołać metodę zapisu z podanym tekstem i nazwą pliku, do którego zostanie zarejestrowany obraz.

######################

set1 = {2, 4, 5, 6}
set2 = {7, 8, 9, 10}
set3 = {1, 2}
print("set1 and set2 are disjoint?",
set1.isdisjoint(set2)) # True 
print("set1 and set3 are disjoint",
set1.isdisjoint(set3)) #False

#isdisjoint
#Metoda isdispjoint() zwraca wartość True, jeśli żaden z elementów nie jest obecny w obu zbiorach. W przeciwnym razie wraca fałsz. Można użyć listy, rekordu, słownika lub ciągu. W tym przypadku, isdispjoint() najpierw konwertuje iterację na zestaw, a następnie sprawdza, czy nie jest ona przekreślona.

######################

import inspect 
def function(a, b):
    # product of two numbers
    return a * b
print(inspect.getsource(function))
# def function(a, b):
#   # product of two numbers
#   return a * b

#Pobierz kod źródłowy obiektu
#Wbudowany moduł inspect pomaga programistów w badaniu już napisanych programów.
#W przypadku gdy mówimy tylko o getisource(), który zwraca cały kod wyjściowy funkcji, klasy lub modułu w postaci ciągu.
#To wystarczy, aby przekazać niezbędny obiekt do argumentów. Należy jednak pamiętać, że wbudowane funkcje nie będą mogły być skontrolowane.

######################

value = 42 
f'value={value}' # 3.6 + # 'value=42'
f'{value=}' # 3.8 + # 'value=42'

#Sztuczka F-strings
#Myślę o f-strings jako metoda formatowania już każdy wie. Pojawiły się one w Python 3.6.
#W aktualizacji 3.8 dodały one kolejną cyfrę klasy — można wyświetlić nazwę zmiennej i jej wartość w tym samym czasie, dodając symbol, jak pokazano na rysunku.

######################

import emoji 
print("\U0001F604") # To smiejaca buzka 
print("\N{flushed face}") # To zdziwiona buzka 
print(emoji.emojize(":partying_face:")) # Buzka z urodzin

#Emoji
#Do wydania emoji w Python istnieje kilka metod.
#1. Ponieważ wszystkie emotikony są zasadniczo znakami Unicode, możemy używać kodów znaków ze stołu Unicode, zastępując je 000 przed wyjściem.
#2. Wszystkie emoji mają krótkie nazwy CLDR, które możemy również wykorzystać do wyjścia.
#3. Można również użyć modułu emoji. Funkcja emojize podaje nazwę CLDR, spacje, w których są zastępowane przez niższe podkreślniki i dodaje dwa punkty na końcach.

######################

txt = "Company12"
x = txt.isalnum()
print(x) # True

txt1 = "Company 12"
x1 = txt1.isalnum()
print(x1) # False 

#Kod wykonujemy zgodnie z harmonogramem
#Często programista powinien napisać kod, który powinien być wykonywany w określonym czasie lub według harmonogramu. Istnieje wiele rozwiązań tego problemu, ale jednym z nich jest biblioteka aiocron.
#It pozwala po prostu opisać konfigurację harmonogramu w dekoderze, zgodnie z którą metoda zostanie uruchomiona. W powyższym przykładzie funkcja attime będzie wykonywana codziennie rano od 6 do 10 wieczorem w dni robocze tygodnia. Aby uzyskać więcej informacji na temat pisania harmonogramów, kliknij tutaj.

######################



######################

def function (value *args, **kwargs):
    print(value)
    print(args)
    print(kwargs)
function( 42 , 'text' , 12345 , [1, 2, 3], pi=3.14, name='Adrian')

# 42
# ('text', 12345 , [1, 2, 3])
# {'pi' : 3.14 , name : 'Adrian'}

# Parametry * Args i **krakergs
#Przynajmniej raz zobaczyliśmy taki zapis, a teraz dowiemy się, co to jest dla symboli. Powiem od razu, że argi i kawargi są powszechnie akceptowanymi nazwami zmiennych, a my posortujemy gwiazdy przed nimi.
#W tym przykładzie funkcja akceptuje argument wartości obowiązkowej i inne argumenty, których nie oczekuje. W tym przypadku *args pakowaÄ wszystkie nienazwane argumenty w oblężeniu, i **kawargi – wszystkie nazwane w słowniku.
#Budowa *args, ** kawargi jest bardzo przydatna, jeśli nie wiemy, kto i w jakich celach będzie korzystać z naszej funkcji. Oznacza to, że możemy prosi o argumenty prawie wszystko.

int ("42") , str(42)  # Konwersja z lancucha i na lancuch 
# (42 , '42')
repr(42)      # Konwersja na lancuch w powstaci kodu 
# '42'

# funkcja int przksztalca lancuch znakow na liczbe natomiast funkcja str liczbe na 
# znakow (czyli jak wyglada po wyswietleniu ) . Funkcja repr dokonuje konwersji liczby 
# na jej reprezentacje lancuchowa jednak zwraca obiekt w postaci lancucha kodu ktory mozna ponownie wykonac
# w celu odtworzenia obiektu Wynik wyswietlamy za pomoca print jest ujety w apostrofy np --->

print(str('mielonka'), repr ('mielonka')) 
# mielonka 'mielonka' 
str('mielonka'), repr('mielonka') # Bezposrednie wyswietlanie wyniku
# ('mielonka', " ' mielonka ' ")  # Bezposrednie wysietlanie wyniku 

str (3.1415) , float("1.5") # Podobnie funkcje wbudowane obsluguja konwersje liczb zmiennoprzecinkowych na lancuchy 
# znakow i odwrotnie 
# ('3.1415' , 1.5)  
text = "1.234E-10"
float(text) # 1.234e-10

ord('s') # 115
chr(115) # 's'
# ord zwraca ona wartosc kodu liczbowego odpowiadajacego danemu znakowi w pamieci .Funkcja 
# chr wykonuje operacje odwrotna przyjmujac kod liczbowy i przeksztalcajac go na odpowiadajacy 

S = '5'
S = chr(ord(S) + 1)
S # '6'
S = chr(ord(S) + 1)
S # '7'

int('5')   # Taka konwersje mozna wykorzystac w polaczeniu z petlami 
ord('5') - ord('O')

#B = '1101' # Przeksztalcenie lancucha znakow w notacji dwojkowej na liczbe calkowita z uzyciem funkcji ord()
#I = 0
#while B: != '':
#    I = I * 2 + (ord(B[0] - ord('0')))
#    B = B[1:]
#I

int('1101', 2) # 13 Przeksztalcenie liczby binarnej na liczbe calkowita funkcja wbudowana
bin(13) # '0b1101  # Przeksztalcenie liczby calkowitej na liczbe binarna : funkcja wbudowana

s = 'mielonka'
S[0] = 'x' # Zglasza blad 
S = S + 'MIELONKA' #Aby zmienic lancuch nalezy utworzyc nowy
S  # 'mielonkaMIELONKA'
S = S[:8] + 'Jajka' + S[-1]
S # 'mielonkaJajka'

S = 'mielonka'
S = S.replace('lon' , 'loczka')
S # 'mieloczkaka'

'Ten %d %s jest martwy !' % (1, 'ptak')
# 'Ten 1 ptak jest martwy ! '  # Wyrazenie formatujace : wszystkie wersje Pythona
' Ten {0} {1} jest martwy ! ' .format(1, 'ptak') 
# 'Ten 1 ptak jest martwy ! '

S = 'jajka'
S = S.replace('jk', 'blk') # Zamieniamy wszystkie wystapienia 'jk' na 'blk' w ciagu S
S # 'jablka'

# Metoda replace jest bardziej ogolna niz na to wskazuje powyzszy przyklad. Jako argumenty 
# przyjmuje poszukiwany podciag znakow (dowolnej dlugosci) oraz ciag docelowy (rowniez dowolnej dlugosci) ktorym 
# zostanie on zastapiony  a nastepnie wykonuje globalne wyszukiwanie i zastepowanie ciagow znakow 
'aa$bb$cc$dd'.replace('$', 'JAJKA')
# ' aaJAJKAbbJAJKAccJAJKAdd '

S = 'xxxxJAJKAxxxxJAJKAxxxx'
where = S.find('JAJKA') # Odzukanie pozycji
where # 4  # Wystepuje z przesunieciem 4 
S = S[:where] + 'MIELONKA' + S[(where + 4) : ]
S # 'xxxxMIELONKAxxxxJAJKAxxxx'
S = 'xxxxMIELONKAxxxxJAJKAxxxx'
S.replace('JAJKA' , 'MIELONKA') # Nastepuje wszystkie wystapienia 
# 'xxxxMIELONKAxxxxMIELONKAxxxx'
S.replace('JAJKA', 'MIELONKA ' , 1) # Zastepuje jedno wystapienie
# 'xxxxMIELONKAxxxxJAJKAxxxx'   

S = 'brama'
L = list(S)
L # ['b', 'r' , 'a' , 'm' , 'a' ]
L[2] = 'e'
L[3] = 'j'    # Dziala dla list ale nie dla lacuchow znakow
L # ['b' , 'r' , 'e' , 'j' , 'a']
S = ' '.join(L)
S # 'breja'

'JAJKA'.join(['mielonka', 'ser', 'szynka', 'tost'])
# 'mielonkaJAJKAserJAJKAszynkaJAJKAtost'

line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
col1 # 'aaa'
col3 # 'ccc'

line = 'aaa bbb ccc'
cols = line.split()
cols  # ['aaa' , 'bbb' , 'ccc']

# Metoda lancuchow znakow split dzieli lancuch na liste  podlancuchow wedlug separatora 
line = 'amadeusz,haker,40'
line.split(',') # [ ' amadeusz' , 'haker' , '40']

line = "jestemKURWAdrwalemMIELONKAiZAJKAjestemMIELONKAOK"
line.split("MIELONKA","KURWA","ZAJKA")
# [ 'jestem' , 'drwalem' , 'i', 'jestem' , 'OK']

line = "Rycerze ktorzy mowia Ni!\n"
line.rstrip()
# ' Rycerze ktorzy mowia Ni! '
line.upper()
# ' RYCERZE , KTORZY MOWIA NI !\n '
line.isalpha() 
# False
line.endswith('NI\n')
# True
line.startswith('Rycerze')
# True 

# Polaczenie operacji obliczania dlugosci i sporzadzanie wycinkow moze natomiast zastapic metode endswith

line 
# ' Rycerze , ktorzy mowia Ni!\n '
line.find('Ni') != -1 # Szukanie za pomoca wywolania lub wyrazenia 
# True 
'Ni' in line 
# True

sub = 'Ni!\n' 
line.endswith(sub)  # Sprawdzanie konca lancucha za pomoca wywolania metody lub wycinka
# True
line[-len(sub):] == sub 
# True 

S = 'a+b+c+'
x = S.replace('+','jajka')
x
# ' ajajkabjajkacjajka '

import string 
y = string.replace(S , '+' , 'jajka')
y 
# # ' ajajkabjajkacjajka '

# %
# s ------> Lancuch znakow(lub dowolny obiekt str(X)) 
# r ------> To samo co s , z tym ze wykorzystuje funkcje repr a nie str
# c ------> Znak (int lub str)
# d ------> Liczba dziesietna 
# i ------> Liczba calkowita 
# u ------> To samo co d (przestarzale, dawniej wymuszalo liczbe calkowita bez znaku)
# o ------> Liczba osemkowa (podstawa 8)
# x ------> Liczba szestnastkowa (podstawa 16)
# X ------> To samo co x , jednak wyswietlane wielkimi literami 
# e ------> Liczba zmiennoprzecinkowa w formacie wykladniczym mala litera 
# E ------> To samo co e , wyswietlane wielka litera 
# f ------> Liczba zmiennoprzecinkowa w zapisie dziesietnym 
# F ------> Liczba zmiennoprzecinkowa w zapisie dziesietnym (wielkie litery)
# g ------> Zmiennoprzecinkowe e lub f
# G ------> Zmiennoprzecinkowe E lub F 
# % ------> Literal %(zapisywany jako %%)

'Ten %d %s jest martwy!' %(1 , 'ptak') # Wyrazenie formatujace 
# Ten 1 ptak jest martwy!

exclamation = "Ni"
"Rycerze , ktorzy mowia %s!" % exclamation # Podstawienia lancucha znakow
# 'Rycerze ktorzy mowia Ni!'
" %d %s %d you " %(1, 'spam', 4) # Podstawienia zalezne od typu 
# '1 spam 4 you '
"%s -- %s -- %s" %(42 , 3.14159 , [1, 2, 3]) # Wszystkie typy pasuja do znacznika %s
# ' 42 -- 3.14159 --[1, 2, 3] ' 

x = 1234
res = "integers: ...%d...%-6d...%06d" %(x, x, x)
res # 'inegers: ...1234...1234...001234'

'%-6.2f | %05.2f | %+06.1f' %(x, x, x)
# '1.23 | 01.23 | +001.2'
'%s' %x, str(x)
('1.23456789', '1.23456789')

'%f, %.2f, %.*f' %(1/3.0 , 1/3.0, 4, 1/3.0)
# '0.333333 , 0.33 , 0.3333 '

"%(ilosc)d  %(towar)s" % {"ilosc":1, "towar": "mielonka"}
# '1 mielonka'

reply = """              # Szablon ze znacznikami podstawiania 
Witamy ...
Witaj %(name)s!
Twoj wiek to %(age)s lat
"""

values = {'name':'Amadeusz', 'age': 40} # Slownik wartosci do podstawienia 
print reply % value    # Operacja podstawienia 


# Witamy ...
# Witaj Amadeusz! 
# Twoj wiek to 40 lat

# Ta sama sztuczka jest rowniez wykorzystywana w polaczeniu z wbudowana funkcja vars ktora zwraca slownik zawierajacy wszystkie zmienne
# isniejace w miejscu jej wywolania 
food = 'mielonka'
qty = 10 
vars ()
# {'food' : 'mielonka', 'qty' : 10 , ...plus wbudowane nazwy Pythona...}

"%(qty)d razy %(food)s" % vars( ) # Nazwy zmiennych sa kluczami w slowniku vars( )
# ' 10 razy mielonka '

template = '{0}, {1} i {2}'                     # Podstawianie pozycyjne
template.format('Tytus', 'Romek' , 'Atomek')
# 'Tytus , Romek i Atomek '

template = '{pieczywo}, {wedlina} i {nabial}'    # Podstawianie po slowie kluczowym
template.format(pieczywo = 'chleb' , wedlina = 'szynka' , nabial = 'jajka')
# 'chleb , szynka i jajka'

template = '{pieczywo}, {0} i {nabial}'       # Obydwie techniki
template.format('szynka', pieczywo='chleb' , nabial='jajka')
# 'chleb , szynka i jajka'


template = '{} , {} i {}'        # Podstawienie przez pozycje wzgledna 
template.format ('chleb ' , 'szynka', 'jajka')


template = '%s , %s i %s'     # To samo z wykorzystaniem wyrazenia formatujacego
template %('chleb ' , 'szynka', 'jajka')
# 'chleb ' , 'szynka', 'jajka'

template = '%(pieczywo)s , %(wedlina)s i %(nabial)s'
template % dict(pieczywo = 'chleb' , wedlina = 'szynka' , nabial = 'jajka')
# 'chleb ' , 'szynka', 'jajka'


'{pieczywo}, {0} i {nabial}'.format(42, pieczywo = 3.14 , nabial=[1, 2])
# '3.14, 42 i [1, 2]'

X = '{pieczywo}, {0} i {nabial}'.format(42, piczywo=3.14, nabial=[1, 2])
X 
# '3.13, 42, ,[1, 2] '
X.split('i')
# '3.13, 42, , '[1, 2]' '
Y = X.replace('i', 'ale pod zadnym pozorem nie')
# ' 3.14 , 42 ale pod zadnym pozorem nie [1, 2] '

'Moj {1[spam]} ma zainstalowany system {O.platform}'.format(sys, {'spam': 'laptop'})
# 'Moj laptop ma zainstalowany system win32'
'Moj {map[spam]} ma zainstalowany system {sys.platform}'.format(sys=sys,
map={'spam': 'laptop'})
# 'Moj laptop ma zainstalowany system win32'

# Parts ktore sluzy do rozpakowania elementow krotki do indywidualnych argumentow funkcji
somelist = list('JAJKO')
somelist 
# ['J' , 'A' , 'J' , 'K' , 'O']
'pierwszy = {0[0]} , trzeci={0[2]}'.format(somelist)
# 'pierwszy = J , trzeci = J'
'pierwszy = {0[0]} , ostatni={1}'.format(somelist[O], somelist[-1])  # [-1] w szablonie
#'Pierwszy = J, ostatni = O'  # foramtujacym nie dziala
parts = somelist[O] , somelist[-1] , somelist[1:3]      # [1:3] w szablonie nie dziala
'pierwszy={0}, ostatni={1}, srodkowy={2}'.format(*parts) # Lub '{}' w wersjach 2.7/3.1
# "Pierwszy=J , ostatni=0, srodkowy=['A', 'j']"

# Zaawansowana skladnia wywolan metody format 
# {nazwa_pola komponenty !znacznik_przeksztalcenia :specyfikacji_formatu} 
# [[wypelnienie]wyrownanie][znak][#][0][serokosc][,][.precyzja][kod_typu]

'{:10} = {:10}'.format('jajo', 123.4567)
# 'jajo = 123.4567'
'{:>10} = {:<10}'.format('jajo', 123.4567)
# 'jajo = 123.4567'
'{.platform:>10} = {[kind]:<10'.format(sys, dict(kind='laptop')) 

'{0:.2f}'.format(1 / 3.0)   # Parametry zakodowane w szablonie
# '0.33'
'%.2f'% (1 / 3.0) # To samo dotyczy wyrazenia 
# '0.33'
'{0:.{1}f'.format(1 / 3.0, 4) # To samo odczytywana z argumentow 
# '0.3333'
'%.*f' % (4, 1 / 3.0)  # Podobnie w przypadku wyrazenia 
# '0.3333'

'{0:.2f}'.format(1.2345) # Metoda lancucha znakow
# '1.23'
format(1.2345, '.2f') # Funkcja wbudowana
# '1.23'
'%.2f' % 1.2345    # Wyrazenie
# '1.23'

# Porownanie metody format z wyrazeniami formatujacymi 

print('%s=%s' % ('spam' , 42))  # Wyrazenie formatujace wszystkie indeksy 2.x/3/x+
print('{0}={1}'.format('spam', 42)) # Metoda format wersje 3.0 i 2.6 
print('{}={}'.format('spam' , 42)) # Z automatycznym numerowaniem wersje 3.1+ i 2.7

'%s, %s and %s' % (3.14, 42, [1, 2]) # Dowolne typy
# '3.14, 42 and [1, 2]'
'Moj %(kind)s ma zainstalowany system %(platform)s' %{'kind': 'laptop', 'platform': sys.platform}
# 'Moj laptop ma zainstalowany win32 '
'Moj %(kind)s ma zainstalowany system %(platform)s' % dict(kind = 'laptop', platform = sys.platform)
# 'Moj laptop ma zainstalowany win32 '

somelist = list('JAJKA')
parts = somelist[0], somelist[-1], somelist[1:3]
'first=%s, last=%s, middle=%s' %parts 
# "pierwsza = J, ostatnia=0, srodkowe['A', 'J']"
###########################################################
command= ""
while command != "quit":
    command == input("> ").lower()
    if command == "start":
        print("car ready to go")
    elif command == "stop":
        print("car stoped")
    elif command == "help":
        print("""
                 strt- cart to start for ride
                 stop- cart stoped 
                 quit- out of the game
              """)
    elif command == "quit":
        break
    else:
        print("sorry i don't understand ")
# Używam pętli z wartościami z tablicy. Jeśli istnieje wyjątek podczas analizowania kodu z tą wartością. Chcę uruchomić kolejne wystąpienie pętli o tej samej wartości, co po wyjątku użyta zostanie następna wartość tablicy, której nie chcę.
##############################################################
# Python 3: List comprehensions
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
['BANANA', 'APPLE', 'LIME']

# List and the enumerate function
list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]

# For loop on a list
numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
    product = product * number
print('The product is:', product)
#The product is: 384
#################################################################

# Zastosowanie specyficznego formatowania 
'%-10s = %10s' % ('jajo', 123.4567)
# 'jajo = 123.4567'
'%10s = %-10s' % ('jajo', 123.4567)
# 'jajo = 123.4567'

# Budowanie danych i dynamiczne formatowanie 
data = dict(platform=sys.platform, kind='laptop')
'Moj {kind:<8} ma zainstalowany system {platform:>8}'.format(**data)
# 'Moj laptop ma zainstalowany win32 '
'Moj %(kind)-8s ma zainstalowany system %(platform)8s' % data
# 'Moj laptop ma zainstalowany win32 '

# Argument **data w wylowaniu metody jest przykladem specjalnej skladni ktora rozpakowuje slownik kluczy i wartosci na poszczegolne argumenty w 
# postaci par slow kluczowych ,, nazwa = wartosc '' dzieki czemu mozna sie do nuich odlowywac wedlug nazwy w wyrazeniu formatujacym 

'{name} {job} {name}'.format(name='Adam', job='dev') 
# Adam dev Adam 
'%(name)s %(job)s %(name)s' % dict(name= 'Adam', job = 'dev')
# Adam dev Adam

##### ##### ##### ##### ##### ##### 

D = dict(name='Adam', job='dev') 
'{0[name]} {0[job]} {0[name]}'.format(D) # Metoda format odwolania do kluczy slownika
# 'Adam dev Adam' 
'{name} {job} {name}'.format(**D) # Metoda format odwolania do slownika 
# 'Adam dev Adam '
'%(name)s %(job)s %(name)s' %D # Wyrazenie , odwolania do kluczy 
# 'Adam dev Adam '

'Zawsze {0} na {1} z {2}'.format('patrz', 'zycie', 'humorem')  # Python 3x, 2.6+
# 'Zawsze patrz na zycie z humorem'
'Zawsze {} na {} z {}'.format('patrz', 'zycie', 'humorem')  # Python 3.1+, 2.7+
# 'Zawsze patrz na zycie z humorem'
'Zawsze %s na %s z %s' %('patz', 'zycie', 'humorem') # Wszystkie wersje Pythona
# 'Zawsze patrz na zycie z humorem'

'%.2f' % 1.2345  # Pojedyncza wartosc
# '1.23'
'%.2f %s' %(1.2345, 99) # Krotka z wieloma wartosciami 
# '1.23 99'

'%s' %1.23  # Pojedyncza wartosc zapisana wprost
# '1.23'
'%s' % (1.23,) # Pojedyncza wartosc zapisana w krotce 
# '1.23'
'%s' % ((1.23,),) # Pojedyncza wartoswc bedaca krotka i zapisana w krotce 
# '(1.23,)'

def myformat(fmt, args): return fmt % args   # str 288
myforamt('%s %s', (88, 99)) # Wywolanie wlasnej funkcji 
str.format('{} {}', 99, 99)  # Wywolanie funkcji wbudowanej 
otherfunction(myformat) # Twoja funkcja rowniez jest obiektem 

'%(num)i = %(title)s' %dict(num=7, title='Strings')
# '7 = Strings'
'{num:d} = {title:s}'.format(num=7,title='Strings')
# '7 = Strings'
'{num} = {title}'.format(**dict(num=7, title='String'))
# '7 = String'

import string 
t = string.Template('$num = $title')
t.substitute({'num':7,'title': 'Strings'}) 
# '7 = Strings'
t.subtitute(num=7,title='String')
# '7 = Strings'
t.subtitute(dict(num=7,title='Strings'))
# '7 = Strings'

#################################################################

class Salary:
    def __init__(self,pay):
        self.pay = pay 
    def get_total(self):
        return self.pay == 12
class Employee:
    def __init__(self, pay, bonus):
        self.salary = Salary(pay)
        self.bonus = bonus 
    def get_salary(self):
        return self.salaraty.get_total() + self.bonus
employee = Employee(5000, 10000)
employee.get_salary() # 70000

# PLO: Skład
#Kompozycja jest relacją, w której obiekty jednej klasy są związane z obiektami innej klasy. Taki sposób organizowania interakcji między klasami jest również nazywany stowarzyszeniem.
#Z reguły w tym przypadku przedmiotem jednej z klas (w przykładzie powyżej tego wynagrodzenia) jest pole innej kategorii (pracownik). Nie ma tu nic skomplikowanego, jak widać.
#Powiązane obiekty mogą być często odniesione cyklicznie, łamiąc standardowy mechanizm zbierania śmieci.
#W tym przypadku należy użyć słabych linków z modułu słabnref, który zostanie omówiony później.

#################################################################

L = [] # Pusta lista
L = [123, 'abc', 1.23, {}] # Cztery elementy indeksy od 0 do 3
L = ['Adam', 40.0, ['dev', 'mgr']] # Zagniezdzone podlisty
L = list('mielonka') # Lista elementow obiektu iterowanego 
L = list(range(-4, 4)) # Lista kolejnych liczb calkowitych 
L [i] # Indeks, indeks indeksu, wycinek , dlugosc 
L [i][j]
L[i:j]
len(L)
L1 + L2 # Konkatenacja, powtorzenie
L * 3 
for x in L:print(x) # Iteracja, przynaleznosc 
3 in L 
L.append(4) # Metody dodawania elementow 
L.extend([5, 6, 7])
Linsert(i, X)
L.index(x) # Metody przeszukiwanie 
L.count(X)
L.sort(X) # Metody sortowanie, odwracanie , kopowianie , czyszczenia 
L.reverse()
L.copy()
L.clear()
L.pop(i) # Metody , wyrazenia zmniejszenie listy 
L.remowe(x) 
del L[i]
del L[i:j]
L[i:j] = []
L[i] = 3     # PRZYPISANIE DO INDEKSU PRZYPISANIE DO WYCINKU
L[i:J] = '[4, 5 , 6]'
L = [x**2 for x in range(5)] # Listy skladane i odwzorowanie(rozdzialy 4, 14 oraz 20)

len([1, 2, 3]) # Dlugosc 
[1, 2, 3] + [4, 5, 6] # Konkatenacja 
# [1, 2, 3, 4, 5, 6]
['Ni'] * 4  # Powtorzenie 
# ['Ni' , 'Ni' , 'Ni' , 'Ni']

str([1, 2]) + "34" # To samo co "[1, 2]" + "34"
# '[1, 2]34'
[1, 2] + list("34") # To samo co [1, 2] + ["3", "4"]
# [ 1, 2, 3, 4 ]

3 in [1, 2, 3] # Przynaleznosc True 
for x in [1, 2, 3]:
    print(x, end='') # Iteracja (w wersji 2.x uzywamy print x)

res = [c*4 for c in 'JAJKO'] # Lista skladana
res 
# ['JJJJ' , 'AAAA' , 'JJJJ' , 'KKKK' , 'OOOO']

res = []
for c in 'JAJKO':
    res.append(c*4) # Odpowiednik listy skladanej 
res 
# ['JJJJ' , 'AAAA' , 'JJJJ' , 'KKKK' , 'OOOO']

list(map(abs, [ 1, 2, 0, 1, 2])) # Wywolanie funkcji map na sekwencji
# [1, 2, 0, 1, 2]

# Indeksowanie, wycinki i macierze 
L = ['mielonka', 'Mielonka', 'MIELONKA!']
L [2]   # Wartosc przesuniecia rozpoczynaja sie od 0  # 'MIELONKA!'
L[-2]   # Wartosc ujemna obliczamy od konca  # 'Mielonka'
L[1:]   # Wycinki pobiera czesci listy  # ['Mielonka' , 'MIELONKA']

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1]
# [4, 5, 6]
matrix[1][1]
# 5
matrix[2][0]
# 7
matrix = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
matrix[1][1]
# 5

L = ['mielonka' , 'Mielonka' , 'MIELONKA!']
L[1] = 'jajka'   # Przypisanie do indeksu 
L 
# ['mielonka' , 'Mielonka' , 'MIELONKA!']
L[0:2] = ['najsmaczniejsza' , 'jest'] # Przypisanie do wycinku usuniecie i wstawienie 
L # Zastapienie elementow 0 i 1
#  ['najsmaczniejsza' , 'jest' , 'MIELONKA!']

L = [1, 2, 3]
L[1:2] = [4, 5] # Zamiana / ustawiania 
L 
# [1, 4, 5, 3]
L[1:1] = [6, 7]  # Wstawianie (nic nie zmieniamy) 
L 
# [1 , 6, 7, 4, 5, 3]
L[1:2] = []  # Usuwanie (nic nie wstawiamy)
L 
# [1, 7, 4, 5, 3] 

L = [1]
L[:0] = [2, 3, 4] # Wstaw wszystko na pozycji :0, pusty wycinek na poczatku
L 
# [2, 3, 4, 1]
L[len(L):] = [5, 6, 7] # Wstaw wszystko na pozycji len(L) pusty wycinek na koncu 
L 
# [2, 3, 4, 1, 5, 6, 7] 
L.extend([8, 9, 10])  # Wstaw wszystko na koncu uzywamy metody extend 
L 
# [2, 3, 4, 1, 5, 6, 7, 8, 9, 10] 

L = ['najsmaczniejsza' , 'jest' , 'mielonka'] 
L.append('puszkowana') 
L.sort() # Sortowanie listy ('M'<'j')

L = ['abc', 'ABD', 'aBe']
L.sort()  # Sortowanie bez uzwglednienia wielkosci liter 
# ['ABD' , 'aBe' , 'abc']
L = ['abc' , 'ABD' , 'aBe']
L.sort(key=str.lower)  # Normalizacja do malych liter 
L 
# ['abc' , 'ABD' , 'aBe']
L = ['abc' , 'ABD' , 'aBe']
L.sort(key=str.lower, reverse=True) # Zmiana kolejnosci sortowania 
L 
['aBe' , 'ABD' , 'abc']
################################################################################################################################
D = {} # Pusty slownik                                                                                                         #
D = {'name': 'Adam' , 'age': 40} # Slownik dwuelementowy                                                                       #
E = {'cto': {'name': 'Adam' , 'age' : 40}} # Zagniezdzanie                                                                     #
D = dict(name = 'Adam', age=40) # Alternatywne techniki tworzenia                                                              #
D = dict([('name', 'Adam') , ('age' , 40)]) # Slowa kluczowe pary klucz-wartosc , piete pary klucz-wartosc, listy kluczy       #
D = dict(zip(keylist, valueslist))                                                                                             #
D = dict.fromkeys(['name' , 'age'])                                                                                            #
D['name']  # Indeksowanie po kluczu                                                                                            #
D['cto']['age']                                                                                                                #
'age' in D  # Metody sprawdzanie przynaleznosci klucza                                                                         #                                                                                                                             
D.keys() # Metody wszystkie klucze                                                                                             #     
D.values() # Metody wszystkie wartosci                                                                                         #                                                                                                                #
D.items() # Wszystkie krotki klucz+wartosc                                                                                     #
D.copy() # Kopiowanie                                                                                                          #
D.clear() # Czyszczenie (usuwa wszystkie elementy )                                                                            #
D.update(D2) # Laczenie wedlug kluczy                                                                                          #
D.get(key, default) # Pobieranie wedlug klucza wartosci domyslne (lub None) gdy brak klucza                                    #
D.pop(key, default) # Usuwanie wedlug klucza wartosci domyslne (lub blad) gdy brak klucza                                      #
D.setdefault(key, default) #  # Pobieranie wedlug klucza wartosci domyslne (lub None) gdy brak klucza                          #
D.popitem() # usuwanie lub zwracanie pary(klucz, wartosci) itp.                                                                #
len(D) # Dlugosc (liczba przechowywanych wpisow)                                                                               #
D[key] = 42 # Dodawanie lub modyfikacja kluczy                                                                                 #
del D[key] # Usuwanie elementu wedlug klucza                                                                                   #
list(D.keys()) # Widoki slownikow                                                                                              #
D1.keys() & D2.keys()                                                                                                          #
D.viewkeys(), D.viewvalues() # Widoki slownikow (Python 2.7)                                                                   #
D = {x: x*2 for x in range(10)} # Slowniki skladane (Python 3.x, 2.7)                                                          #
################################################################################################################################

D = {'mielonka': 2, 'szynka' : 1, 'jajka': 3} # Utworzenie slownika 
D['mielonka']  # Pobranie wartosci po kluczu
D # Kolejnosc zostaje pomieszna {'jajka': 3, 'mielonka': 2, 'szynka': 1} 

len(D) # Liczba wpisow w slowniku 
# 3
'szynka' in D # Alternatywne sprawdzanie isnienia klucza # True 
list(D.keys()) # Utworzenie nowej listy kluczy slownika D
# ['jajka', 'mielonka', 'szynka']

D # {'jajka': 3, 'mielonka': 2, 'szynka': 1}
D['szynka'] = ['grillowanie', 'pieczenie','smazenie'] # Zmiana wpisu (wartosc = lista)
D # {'jajka': 3, 'mielonka': 2, 'szynka': ['grillowanie','pieczenie','smazenie']}
del D['jajka'] # Usuniecie wpisu 
D['lunch'] = 'Bekon' # Dodanie nowego wpisu 

D = {'mielonka': 2, 'szynka': 1, 'jajka': 3}
lisr(D.values()) # [3, 2, 1]
list(D.items())
# [('jajka', 3), ('mielonka', 2), ('szynka', 1)]

D.get('mielonka') # Klucz isnieje # 2
print(D.get('tost')) # Nieistniejacy klucz
D.get('tost', 88) # 88

D 
# {'jajka': 3, 'mielonka': 2, 'szynka': 1}
D = {'tost': 4 , 'ciastko': 5} 
D.update(D2)
D 
# {'jajka': 3, 'ciastko' : 5, 'tost' : 4 ,'mielonka': 2, 'szynka': 1}
D.pop('ciastko') # 5 # Usuniecie i zwrocenie wartosci klucza
D.pop('tost') # 4 
D # {'jajka': 3, 'mielonka': 2, 'szynka': 1}

# Przyklad baza danych o filmach 
table = {'1975' : 'Monty Python i Swiety Graal',   # Kluczowartosc 
         '1979': 'Zywot Briana',
         '1983': 'Sens zycia wedlug Monty Pythona'}
year = '1983'
movie = table[year] # Slownik[klucz] --> wartosc
movie # 'Sens zycia wedlug Monty Pythona'
for year in table:
    print(year + '\t' + table[year]) # To samo co: for year in table.keys()
# 1979 Zywot Briana 
# 1975 Monty Python i Swiety Graal 
# 1983 Sens zycia wedlug Monty Pythona

# Przyklad - mapowanie wartosci na klucze 
table = {'Monty Python i Swiety Graal' :'1975' ,   # klucz ---> wartosc(tytul --> data premiery)

         'Zywot Briana' : '1979',
         'Sens zycia wedlug Monty Pythona' : '1983'}
table['Monty Python i Swiety Graal'] # '1975'
list(table.items())  # wartosc --> klucz (data premiery --. tytul)
# [('Sens zycia wedlug Monty Pythona' : '1983'), ('Monty Python i Swiety Graal' :'1975') , ('Monty Python i Swiety Graal' :'1975')]
[title for (title, year) in table.items() if year == '1975']
# ['Monty Python i Swiety Graal ']

K = 'Monty Python i Swiety Graal' # klucz ---> wartosc(normalny sposob uzycia)
table[K] # '1975'
V = '1975' 
[key for (key, value) in table.items() if value == V] # Wartosc ----> klucz
# ['Holly Grail']
[key for key in table.keys() if table[key] == V] # jw
# ['Holly Grail']

D = {}
D[99] = 'mielonka'
D[99] # 'mielonka'
D # {99: 'mielonka'}

table = {1975: 'Monty Python i Swiety Graal',
         1979: 'Zywot Briana', # Klucze sa liczbami calkowitymi , anie ciagami znakow 
         1983: 'Sens zycia wedlug Monty Pythona '}
table[1975] # 'Holy Grail'
list(table.items()) 

#Matrix = {}
#Matrix[(2, 3, 4) = 88]
#Matrix[(7, 8, 9) = 99]
#X = 2; Y = 3; Z = 4  # Srednik rozdziela poszczegolne polecenia zobacz rozdzial 10
#Matrix([X, Y, Z]) # 88
#Matrix {(2, 3, 4): 88, (7, 8, 9): 99} 

# Unikanie bledow z brakujacymi kluczami 

if (2,3,6) in Matrix : # Sprawdzanie indeksowania 
    print(Matrix[(2,3,6)]) 
else: 
    print (0)

try:
    print(Matric[(2,3,6)]) # Proba indeksowania 
except KeyError: # Przecwycenie i obsluga bledu
    print(O) 
Matrix.get((2,3,4), O) # Istnieje --pobieramy i zwracamy  wartosc # 88
Matrix.get((2,3,6), O) # Nie istnieje -- uzywamy wartosci domyslnej 

# Zagniezdzanie slownikow 
##########################################################################################################################################################################################
print (DUZA SCIAGA Z PYTHON 

Główne typy danych Pythona
Każda wartość w Python nazywa się „obiektem”. Każdy obiekt ma określony typ danych. Trzy najczęściej używane typy danych to:
Liczby całkowite (int) — liczba całkowita reprezentująca obiekt, taki jak „liczba 3”.
Liczby zmiennoprzecinkowe (zmiennoprzecinkowe) — używane do przedstawiania liczb zmiennoprzecinkowych.
Strings — kodyfikacja ciągu znaków za pomocą ciągu. Na przykład słowo „hello”. W Python 3 struny są niezmienne. Jeśli już go zdefiniowano, nie można go później zmienić.
Chociaż można zmodyfikować ciąg za pomocą takich poleceń, jak replace() lub join(), to jednak utworzą on kopię ciągu i zastosują do niego modyfikacje, a nie przepisać oryginalny ciąg.
Dodatkowo warto wspomnieć o trzech kolejnych typach: Listach, słownikach i fałdowaniu. Wszystkie z nich są omówione w następnych sekcjach.
Na razie skupiajmy się na sznurkach.

Jak utworzyć ciąg w Python
Ciąg znaków można utworzyć na trzy sposoby, korzystając z pojedynczych, podwójnych lub potrójnych wycen. Oto przykład każdej opcji:
Podstawowy ciąg Pythona
my_string = „Learns Python!”
another_string = „może się wydawać trudny pierwszy, ale ty
może to zrobić!”
a_long_string = "Tak, można nawet opanować wiele linii

strings  
    obejmuje to więcej niż jedną linię
    z niektórymi praktykami"

IMP! Niezależnie od wybranej opcji, należy trzymać się jej i używać jej konsekwentnie w ramach programu.
W następnym kroku możesz użyć funkcji Print(), aby wyprowadzić ciąg tekstowy w oknie konsoli. Pozwala to sprawdzić kod i upewnić się, że wszystkie funkcje są prawidłowe.
Oto fragment dla tego:

Print („Wydrukujmy ciąg!”)

Łączenie ciągów
Kolejną rzeczą, którą można opanować, jest połączenie — sposób na dodanie dwóch ciągów razem za pomocą operatora „+”. Oto jak to zrobić:

string_one = “Im reading “
string_two = “a new great book!”
string_three = string_one + string_two

Uwaga: Nie można zastosować operatora + do dwóch różnych typów danych, np. string + liczba całkowita. Jeśli to zrobisz, otrzymasz następujący błąd Pythona:
TypeErr: Nie można przekonwertować obiektu „int” na str pośrednio

TypeError: Cant convert 'int' object to str implicitly

Replikacja ciągu
Jak sama nazwa wskazuje, polecenie to pozwala powtórzyć ten sam ciąg kilka razy. W tym celu należy użyć operatora *. Należy pamiętać, że operator ten działa jako replikatory tylko z typami danych ciągów. W odniesieniu do liczb działa on jako mnożnik.
Przykład replikacji ciągu:
„Alice” * 5 „AliceAliceAliceAlice” 
I z nadrukiem ()
Print (“Alice” * 5)
A Twoje wyniki będą pisane pięć razy z rzędu przez Alice.

Jak przechowywać struny w zmiennych
Zmienne w Python 3 są specjalnymi symbolami, które przypisują konkretną lokalizację do przypisanej do niej wartości. W istocie zmienne są jak specjalne etykiety, które można umieścić na jakiejś wartości, aby wiedzieć, gdzie jest przechowywany.
Łańcuchy zawierają dane. Więc można “spakować” je wewnątrz zmiennej. Ułatwia to pracę ze złożonymi programami Pythona.
Oto jak można przechowywać ciąg wewnątrz zmiennej.
my_str = „Witaj świecie”

Popsujmy to nieco dalej:
• my_str jest nazwą zmiennej.
• = jest operatorem przypisania.
• „Tylko losowy ciąg” to wartość, którą przywiązasz do nazwy zmiennej.

Teraz, gdy wydrukujesz ten tekst, otrzymasz jego wynik.
print(my_str)
= Witaj świecie
Zobacz? Używając zmiennych, można zaoszczędzić mnóstwo wysiłku, ponieważ nie trzeba ponownie wpisać cały ciąg za każdym razem, gdy chcesz go używać.

Wbudowane funkcje w Python
Znasz już najpopularniejszą funkcję w Python — Print(). Przyjrzyjmy się teraz równie popularnym kuzyniom, które są wbudowane w platformę.
Funkcja Input()
funkcja input() jest prostym sposobem na monitowanie użytkownika o wprowadzenie niektórych danych (np. podanie nazwy). Wszystkie dane wprowadzone przez użytkownika są przechowywane jako ciąg.
Oto krótki fragment, który ilustruje to:

name = input(“Hi! Whats your name? “)
print(“Nice to meet you “ + name + “!”)
age = input(“How old are you “)
print(“So, you are already “ + str(age) + “ years old, “
+ name + “!”)

Po uruchomieniu tego krótkiego programu wyniki będą wyglądać następująco:

Hi! Whats your name “Jim”
Nice to meet you, Jim!
How old are you 25
So, you are already 25 years old, Jim!



len() Function
len() function helps you find the length of any string, list, tuple, dictionary, or another data type. It’s a handy command to determine excessive values and trim them to optimize the performance of your program.
Heres an input function example for a string:

# testing len()
str1 = “Hope you are enjoying our tutorial!”
print(“The length of the string is :”, len(str1))

Output:
The length of the string is: 35



filtr()
Użyj funkcji Filter(), aby wykluczyć elementy z iteracyjnego obiektu (listy, pule, słowniki itp.)
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)


Jak przekazać argumenty słowa kluczowego do funkcji
Funkcja może również akceptować argumenty słów kluczowych. W takim przypadku można użyć parametrów w kolejności losowej, ponieważ interpreter Pythona użyje podanych słów kluczowych do dopasowania wartości do parametrów.
Oto prosty przykład, jak przekazać argument słowa kluczowego do funkcji.

# Define function with parameters
def product_info(product name, price):
print(“productname: “ + product name) print(”Product Name: “ + product_name)
print(“Price “ + str(dollars)) print(”Price: “ + str(price))
# Call function with parameters assigned as above product_info(“”White T-sShirt”:,“1,51d5o)llars)
# Call function with keyword arguments
# Call function with keyword arguments
product_info(productname=”jJeans”“, price=45)

Output:
ProductnaNmaem:eW: hWihteitTe-shTi-rtShirt 
Priiccee: 1:515 
ProductnaNmaem:eJ:eaJnesans
Priiccee: 4:545


Listy
Listy są kolejnym typem danych o zasadniczym charakterze w Python używanym do określenia kolejności elementów. Krótko mówiąc, pomagają one zachować powiązane dane razem i wykonywać te same operacje na kilku wartościach naraz. W przeciwieństwie do ciągów, listy mogą być zmienne (=zmienne).
Każda wartość na liście jest nazywana pozycją i są one umieszczane pomiędzy nawiasami kwadratowymi.
Listy przykładów
my_list = [1, 2, 3]
my_list2 = [“a”, “b”, “c”]
my_list3 = [“4”, d, “book”, 5]

Można również użyć funkcji list(), aby wykonać te same czynności:

alpha_list = list((“1”, “2”, “3”))
print(alpha_list)


Dodawanie elementów do listy
Istnieją dwa sposoby dodawania nowych elementów do istniejących list. Pierwsza z nich korzysta z funkcji append():
beta_list = [“apple”, “banana”, “orange”]
beta_list.append(“grape”)
print(beta_list)

Druga opcja to wstawianie() funkcji dodawania elementu w określonym indeksie:
beta_list = [“apple”, “banana”, “orange”] 
beta_list.insert(“22,“grape”) 
print(beta_list)

Jak usunąć element z listy
Ponownie, masz kilka sposobów, aby to zrobić. Najpierw można użyć funkcji Remove():
beta_list = [“apple”, “banana”, “orange”]
beta_list.remove(“apple”)
print(beta_list)

Po drugie, można użyć funkcji pop(). Jeśli nie określono indeksu, usunie on ostatni element.
beta_list = [“apple”, “banana”, “orange”]
beta_list.pop()
print(beta_list)

Ostatnią opcją jest użycie słowa kluczowego del w celu usunięcia określonego elementu:
beta_list = [“apple”, “banana”, “orange”]
del beta_list [1]
print(beta_list)

Łączenie dwóch list
Aby zmialić dwie listy, użyj operatora +.
my_list = [1, 2, 3]
my_list2 = [“a”, “b”, “c”]
combo_list = my_list + my_list2
combo_list
[1, 2, 3, 'a', 'b', 'c']

Utwórz listę zagnieżdżoną
Możesz także utworzyć listę list, jeśli masz ich mnóstwo :)
my_nested_list = [my_list, my_list2]
my_nested_list
[[1, 2, 3], ['a', 'b', 'c']]

Sortowanie listy
Użyj funkcji Sort(), aby uporządkować wszystkie elementy na liście.
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
alpha_list
[2, 23, 34, 67, 88, 100]

Lista warstw A
Teraz, jeśli chcesz wywołać tylko kilka elementów z listy (np. pierwsze 4 elementów), musisz określić zakres numerów indeksowych oddzielonych dwukropkiem [x:y]. Oto przykład:
alpha_list[0:4]
[2, 23, 34, 67]

Zmień wartość elementu na liście
Można łatwo zastąpić wartość jednego elementu listy:
beta_list = [“apple”, “banana”, “orange”]
beta_list[1] = “pear”
print(beta_list)

Output:
['apple', 'pear', 'cherry']

Przeglądanie listy
Użycie dla pętli pozwala na zwiększenie wykorzystania określonych elementów, podobnie jak w przypadku operatora *. Oto przykład:
for x in range(1,4): beta_list += ['fruit'] print(beta_list)

Kopiowanie listy
Użyj wbudowanej funkcji Copy(), aby zreplikować dane:
beta_list = [“apple”, “banana”, “orange”]
beta_list = beta_list.copy()
print(beta_list)

Można również skopiować listę przy użyciu metody list():
beta_list = [“apple”, “banana”, “orange”]
beta_list = list (beta_list)
print(beta_list)

Lista obaw
Zrozumienie listy jest przydatną opcją tworzenia list na podstawie istniejących list. Podczas korzystania z nich można budować za pomocą ciągów i kęs, jak również.
Wymienić przykłady zrozumienia
list_variable = [x for x in iterable]

Oto bardziej złożony przykład, który zawiera operatory matematyczne, integratory i
funkcja range():
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

Rury
Kroje są podobne do list — umożliwiają wyświetlenie uporządowanej sekwencji elementów. Są one jednak niezmienne i nie można zmieniać wartości przechowywanych w pęczku.
Zaletą używania podwielokrotności nad listami jest to, że te pierwsze są nieco szybsze. Jest to więc dobry sposób na optymalizację kodu.
How to Create a Tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0:3]
(1, 2, 3)

Sposób przesuwania pęczku
Proces ten jest podobny do krojenia list.
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(numbers[1:11:2])

Output:
(1,3,5,7,9)

Konwertuj pęcznienie na listę
Ponieważ sieci Tufles są niezmienne, nie można ich zmienić. Można to zrobić, ale jest przekształcenie kęs na listę, dokonać edycji, a następnie przekształcić go z powrotem do kęs.
Oto jak to osiągnąć:
x = (“apple”, “orange”, “pear”)
y = list(x)
y[1] = “grape”
x = tuple(y)
print(x)

Słowniki
Słownik zawiera indeki z kluczami, które są mapowane do określonych wartości. Te pary o kluczowym stosunku wartości do ceny oferują świetny sposób na porządkowanie i przechowywanie danych w Python. Są one zmienne, co oznacza, że można zmienić przechowywane informacje.
Wartość klucza może być ciągiem, logicznym lub liczbą całkowitą. Oto przykładowy słownik ilustrujący to:
Customer 1= {‘username’: ‘john-sea’, ‘online’: false, ‘friends’:100}

Jak utworzyć słownik Pythona
Oto krótki przykład pokazujący, jak zrobić pusty słownik. 
Opcja 1: new_dict = {}
Opcja 2: other_dict= dict()
Można również użyć tych samych dwóch metod, aby dodać wartości do słownika:

new_dict = { “brand”: “Honda”, “model”: “Civic”, “year”: 1995
}
print(new_dict)

Jak uzyskać dostęp do wartości w słowniku
Dostęp do dowolnej wartości w słowniku można uzyskać w następujący sposób:
x = new_dict[“brand”]
Można również użyć następujących metod, aby wykonać to samo.
• dict.keys() izoluje klucze
• dict.values() izoluje wartości
• dict.items() zwraca elementy w formacie listy (klucz, wartość) par

Zmień wartość elementu
Aby zmienić jeden z elementów, należy odwołać się do niego za pomocą jego nazwy klucza:
#Change the “year” to 2020:
new_dict= { “brand”: “Honda”, “model”: “Civic”, “year”: 1995
}
new_dict[“year”] = 2020

Przeglądanie słownika
Aby ponownie wdrożyć pętlę, należy użyć polecenia pętli.
#print all key names in the dictionary
for x in new_dict:
  print(x)
#print all values in the dictionary
for x in new_dict:
  print(new_dict[x])
#loop through both keys and values
for x, y in my_dict.items():
  print(x, y)

If Statements (Conditional Statements) in Python
Just like other programming languages, Python supports the basic logical conditions from math:
• Equals: a == b
• Not Equals: a != b
• Less than: a < b
• Less than or equal to a <= b
• Greater than: a > b
• Greater than or equal to: a >= b
You can leverage these conditions in various ways. But most likely, you’ll use them in “if statements” and loops.

Jeśli przykład wyciągu
Celem oświadczenia warunkowego jest sprawdzenie, czy jest to prawda czy fałsz.
if 5 > 1:
        print(“That’s True!”)
Output:
Thats True!

Zagnieżdżenie instrukcji IF
W przypadku bardziej złożonych operacji można utworzyć zagnieżdżenia instrukcji IF. Oto jak to wygląda:
x = 35
if x > 20:
  print(“Above twenty,”)
  if x > 30:
    print(“and also above 30!”)

Oświadczenia Elif
słowo kluczowe elif monituje program, aby spróbował innego warunku, jeśli poprzednie nie były prawdziwe. Oto przykład:
a = 45
b = 45
if b > a:
  print(“b is greater than a”)
elif a == b:
  print(“a and b are equal”)

Jeśli inne stwierdzenia If Else Statements 
inne słowo kluczowe pomaga dodać dodatkowe filtry do klauzuli warunków. Oto jak wygląda kombi IF-elif-else:
if age < 4: ticket_price = 0
elif age < 18: ticket_price = 10
else: ticket_price = 15

Jeśli-nie-stwierdzeń If-Not-Statements
Nie słowa kluczowego sprawdźmy, czy wartość nie jest wartością True:
new_list = [1, 2, 3, 4]
x = 10
if x not in new_list:
    print(“’x’ isn’t on the list, so this is True!”)

Zdania zaliczenia Pass Statements
Jeśli stwierdzenia nie mogą być puste. Ale jeśli tak jest, dodaj zdanie, aby uniknąć błędu:
a = 33 b = 200
if b > a: pass

Jako Pętla For Loop 
Jak już pokazano w innych sekcjach tej listy kontrolnej Pythona, pętla jest przydatnym sposobem na iterację nad sekwencją, taką jak lista, pętelka, słownik, ciąg itp.
Oto przykład pokazujący, jak wykonać pętlę przez ciąg:
 for x in “apple”:
  print(x)

Podczas operacji pętli 
While Loops
Pętla pozwala na wykonanie zestawu rozpoznań, o ile warunek dla nich jest spełniony.
#print as long as x is less than 8
i =1 while i< 8:
  print(x)
  i += 1

How to Break a Loop
You can also stop the loop from running even if the condition is met. For that, use the break statement both in while and for loops:
Jak przełamanie pętli
Pętlę można również zatrzymać, nawet jeśli warunek jest spełniony. W tym celu należy użyć instrukcji break zarówno w przypadku pętli, jak i w przypadku pętli:
i =1
while i < 8:
  print(i)
  if i == 4:
break
i += 1

Klasa Class
Ponieważ Python jest obiektowym językiem programowania, niemal każdy jego element jest obiektem – jego metodami i właściwościami.
Klasa działa jak plan tworzenia różnych obiektów. Obiekty są instancją klasy, gdzie klasa przejawia się w pewnym programie.

Jak utworzyć klasę
Zał ówmy klasę o nazwie TestClass, z jedną właściwością o nazwie z:
Class TestClass: 
    z =5

Jak utworzyć obiekt
Następnym krokiem jest utworzenie obiektu przy użyciu klasy. Oto jak to zrobić:
p1 = TestClass()
print(p1.x)

Ponadto można przypisać do obiektu różne atrybuty i metody. Przykład znajduje się poniżej:
class car(object):
    “””docstring”””
    def __init__(self, color, doors, tires):
        “””Constructor”””
        self.color = color
        self.doors = doors
        self.tires = tires
    def brake(self):
        “””
        Stop the car
        “””
        return “Braking”
    def drive(self):
        “””
        Drive the car
        “””
        return “Im driving!”
    
Jak utworzyć podklasę
Każdy obiekt może być dalej podklasyfikowane. Oto przykład
class Car(Vehicle):
    “””
    The Car class
    “””
    def brake(self):
        “””
        Override brake method
        “””
        return “The car class is breaking slowly!”
if __name__ == “__main__”:
    car = Car(“yellow”, 2, 4, “car”)
    car.brake()
    ‘The car class is breaking slowly!’
    car.drive()
    “I’m driving a yellow car!”

Postępowanie z wyjątkami Pythona (błędy)
Python ma listę wbudowanych wyjątków (błędów), które będą wyświetlane za każdym razem, gdy popełnisz błąd w kodzie. Jako początkujący dobrze jest wiedzieć, jak je naprawić.
Najczęstsze wyjątki Pythona
• AttributeError — pojawia się, gdy odniesienie atrybutu lub przypisanie nie powiedzie się.
• IOError— pojawia się, gdy niektóre operacje we/wy (np. funkcja Open()) nie powiedzie się
Z powodu i/o, np. „nie znaleziono pliku” lub „dysk pełny”.
• ImportError — pojawia się, gdy wyrażenie import nie może zlokalizować definicji modułu. Ponadto, gdy import z... Nie może znaleźć nazwy, która musi być importowana.
• IndexError Błąd indeksowania — pojawia się, gdy sekwencja subscript jest poza zakresem.
• KeyError — pojawia się, gdy klucz słownika nie znajduje się w zestawie istniejących kluczy.
• KeyboardInterrupt (przerwanie klawiatury) — zapala się, gdy użytkownik dotknie klawisza przerwania (np. Control-C lub Delete).
• NameError Błąd nazwy — pojawia się, gdy lokalny lub globalny...
• OSError (Błąd systemu) — wskazuje na błąd związany z systemem.
• SyntaxError — pojawia się, gdy parser napotyka błąd składni.
• TypeError — pojawia się, gdy operacja lub funkcja zostanie zastosowana do obiektu o niewłaściwym typie.
• ValueError Błąd wartości — pojawia się, gdy wbudowana operacja/funkcja otrzymuje argument, który ma właściwy typ, ale nie odpowiednią wartość, a sytuacja nie jest opisana przez dokładniejszy wyjątek, taki jak IndexErErErErErd.
• ZeroDivisionError — pojawia się, gdy drugi argument operacji podziału lub modułu wynosi zero.

Jak rozwiązać problemy związane z błędem  How to Troubleshoot the Errors
Python ma przydatne oświadczenie, projekt tylko w celu obsługi wyjątków – Try/except. Oto fragment kodu pokazujący, jak można złapać KeyErrors w słowniku za pomocą tego oświadczenia:
my_dict = {“a”:1, “b”:2, “c”:3}
try:
        value = my_dict[“d”]
    except KeyError:
        print(“That key does not exist!”)
    
Można również wykryć kilka wyjątków jednocześnie za pomocą jednego oświadczenia. Oto przykład na to:
my_dict = {“a”:1, “b”:2, “c”:3}
try:
    value = my_dict[“d”]
except IndexError:
    print(“This index does not exist!”)
except KeyError:
    print(“This key is not in the dictionary!”)
except:
    print(“Some other problem happened!”)

wypróbuj/z wyjątkiem klauzuli else   try/except with else clause
Dodanie klauzuli ELSE pomoże Ci potwierdzić, że nie ma błędów
znaleziono:
 my_dict = {“a”:1, “b”:2, “c”:3}
try:
    value = my_dict[“a”]
except KeyError:
    print(“A KeyError occurred!”)
else:
    print(“No error occurred!”)
##########################################################################################################################################################################################################################################
db = []
db.append(rec) 
db.append(other)  # Baza danych w postaci listy 
db[0]['jobs']

db = {}
db['adam'] = rec 
db['kasia'] = other # Baza danych w postaci slownika  
db['adam']['jobs']

dict(zip(keyslist, valueslist)) # polaczone krotki zawierajace klucz/wartosc
dict.fromkeys(['a','b'], 0) # {'a' : 0, 'b' : 0}

L = ['Adam', 40.5,['dev', 'mgr']] # rekord oparty naliscie 
L[0] # 'Adam' 
L[1] # 40.5 # Pozycje/numery pol 
L[2][1]  # 'mgr'

D = {'name': 'Adam', 'age': 40.5,'jobs': ['dev', 'mgr']}
D['name'] # 'Adam' 
D['age'] # 40.5 # Rekord oparty na slowniku
D['jobs'][1] # 'mgr' # Nazwy znacza wiecej niz liczby

D = dict(name='Adam', age=40.5,jobs=['dev', 'mgr'])
D['name'] # 'Adam'
D['jobs'].remove('mgr')
D  # ['jobs':['dev'],'age':40.5,'name':'Adam']

D = {}
D['state1'] = True # Slownik odzwiedzonych stanow
# 'state' in D 
# True

S = set()
S.add('state1') # To samo ale za pomoca zbioru 
'state1' in S 
# True 

# Metody D.keys, D.values i D.items zamiast liczby zwracaja widoki podobne do zbiorow bedace obiektami iterowalnymi 
# Metody D.viewkeys, D.viewvalues,D.viewitems iterowalne widoki podobne do zbiorow a pozostale metody zwracaja listy jak poprzednio

# Jest polaczenie jego kluczy i wartosci za pomoca funckji zip i przekazanie wynniku tej operacji do wywolania konstruktora dict
list(zip(['a','b','c'], [1, 2, 3])) # Polaczenie kluczy i wartosci # [('a',1), ('b',2), ('c', 3)]       

D = dict(zip(['a','b','c'], [1, 2, 3])) # Utworzenie slownika z wyniku funkcji zip
D  # {'b':2,'c':3,'a':1}

D = {k: v for (k, v) in zip (['a','b','c'], [1, 2, 3])}
D # {'b': 2, 'c': 3, ' a': 1}

D = {x: x** 2 for x in [1, 2, 3, 4]} # Lub:range(1, 5)
D # [1: 1, 2: 4, 3: 9, 4: 16]

D = {c: c * 4 for c in 'JAJKO'} # Iteracja po dowolnym iteratorze 
D # {'A': 'AAAA', 'K': 'KKKK', 'J': 'JJJJ', 'O': 'OOOO'} 

D = {c.lower(): c + '!' for c in ['Mielonka', 'Jajka','SZYNKA']}
D # {'szynka': 'SZYNKA!', 'jajka':'JAJKA!', 'mielonka':'MIELONKA!'}

# Slowniki skladane sa rowniez przydatne do inicjalizacji slownikow za pomoca list kluczy podobnie jak robi to metoda fromkeys, ktora spotkalismy w poprzednim podrozdziale:
D = dict.fromkeys(['a','b','c'], 0) # Inicjalizacja slownika za pomoca listy kluczy
D  # {'b': 0, 'c': 0, ' a': 0}

D = {k:0 for k in ['a', 'b', 'c']} # To samo ale z uzyciem slownika skladanego
D # # {'b': 0, 'c': 0, ' a': 0}

D = dict.fromkesys('spam') # Inne iteratory uzycie wartosci domyslnej
D # {'s': None, 'p': None, 'a': None, 'm': None } 

D = dict(a=1, b=2, c=3) 
D {'b': 2,'c': 3, 'a':1}

K = D.keys()  # W 3.x tworzy obiekt widoku a nie liste 
K # dict_keys(['b','c','a'])
list(K)  # W razie potrzeby w 3.x mozemy wynusic liste  
# ['b','c','a'] 

V = D.values() # To samo w przypadku metod values i items 
V # dict_values([2, 3, 1]) 
list(v)
# [2, 3, 1]

D.items()
# dict_items([('b', 2), ('c', 3), ('a', 1) ])
list(D.items())
# [('b', 2), ('c', 3), ('a', 1)]

K[0] # Operacje list nie dzialaja dopoki widoki nie zostana przeksztalcone
list(K)[0]
# 'b'

for k in D.keys(): print(k) # Iteratory sa automatycznie uzywanie w petlach 
...
b
c
a

for key in D: print(key) # Nie ma potrzeby wywolywania metody keys() do iteracji 
... 
b
c
a

D = {'a':1, 'b':2, 'c':3}
D # {'b':2, 'c':3,'a':1}

K = D.keys()
V = D.values() 
list(K)  # Widok zachowuje te sama kolejnosc elementow co slownik zrodlowy 
list(K) # ['b','c','a']
list(V) # [2, 3, 1]
del D['b'] # Modyfikacja slownijka w miejscu 
D # {'c':3, 'a':1}
list(K) # Zmiana jest odzwierciedlenia w biezacym obiekcie widoku  # ['c','a']
list(V) # W 2.x tak sie nie dzieje -- lista nie jest powiazana ze slownikiem [3, 1]

K,V 
# (dict_keys(['c','a']), dict_values([3, 1]))
K | {'x': 4} # Wyniki dzialania metody keys (i czasami items)zachowuja sie jak zbiory 
# {'c','x','a'}
V & {'x': 4} # TypeError
V & {'x': 4}.values() #TypeError

D = {'a':1,'b':2,'c':3} 
D.keys() & D.keys() # Iloczyn widokow keys {'b','c','a'}
D.keys() & {'b'} # Iloczyn widoku keys i zbioru {'b'}
D.keys() & {'b': 1} # Iloczyn widoki keys i slownika {'b'}
D.keys() | {'b', 'c', 'd'} # Unia widoku keys i zbioru  {'b','c','a','d'}

# Widok items jest rowniez obiektem zbiorowym pod warunkiem ze zawiera wylacznie elementy niemutowalne 
D = {'a': 1}
list(D.items()) # Widok items zachowuje sie jak zbior jezeli jest haszowalny # [('a', 1)]
D.items() | D.keys() # Unia widoku items i keys  # {('a',1), 'a'}
D.items() | D # Slownik jest traktowany jak jego widok keys  # {('a',1), 'a'}

D.items() | {('c', 3), ('d', 4)} # Zbior par klucz/wartosc  # {('d', 4), ('a', 1), ('c', 3)}
dict(D.items() | {('c', 3), ('d', 4)})  # Funkcja dict akceptuje rowniez zbiory iterowalne  # {'c': 3, 'a': 1, 'd': 4}

D = {'a':1, 'b':2, 'c':3}
D # {'a':1, 'b':2, 'c':3}

Ks = D.keys() # Sortowanie obiektu widoku nie dziala 
K.sort()

Ks = list(Ks) # Przeksztalcenie na liste i posortowanie wyniku
Ks.sort() 
for k in Ks: print(k, D[k])
...
a 1
b 2
c 3

Ks = D.keys()                         # Mozna tez uzyc  funkcji sorted() na kluczach 
for k in sorted(Ks): print(k, D[k])   # Funkcja sorted() akceptuje dowolny obiekt iterowany
for k in sorted(Ks): print(k, D[k])   # sorted() zwraca liste 

...
a 1
b 2
c 3


sorted(D1.items()) < sorted(D2.items())  # Odpowiednik D1 < D2 w 2.x

import dbm                      # W pythonie 2.x modul ten nosi nazwe anybdm
file = dbm.open("nazwa_pliku")  # Lacze do pliku
file['key'] = 'data'            # Zapisanie  danych wedlug klucza 
data = file['key']              # Pobranie danych wedlug klucza 

import cgi 
form = cgi.FieldStorage()  # Analiza danych z formularza 
if form.has_key('name'):
    showReply('Witaj,  ' + form['name'].value) 

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
L # [21, 22, 23, 24, 25]

T = (1, 2, 3, 2, 4, 2)  # Metody krotek w Pythonie 2.6 oraz 3.0 i nowszych wersjach 
T.index(2) # Offset pierwszego wystapienia  elementu o wartosci 2 # 1
T.index(2, 2) # Offset wystapienia elementu o wartosci 2 po przesunieciu o 2 pozycje # 3
T.count(2) # Ile jest elementow o wartosci 2 (3)

T = (1, [2, 3], 4) 
T[1] = 'mielonka' # Nie dziala nie da sie zmienic krotki # TypeError

T[1][0] = 'mielonka' # Dziala -- mozna modywikowac mutowalne elementy krotki 
T  # (1, [2, 3], 4)

adam = dict(name='Adam', 40.5, ['mgr'])  # Rekord w postaci krotki 
adam #('Adam' , 40.5, ['dev', 'mgr'])

adam[0], adam[2]    # Dostep do pol wedlug pozycji w krotce 
# ('Adam', ['dev', 'mgr'])   

adam = dict(name='Adam', age=40.5, jobs=['dev', 'mgr']) 
adam
# {'jobs':['dev','mgr'], 'name': 'Adam', 'age': 40.5}

adam['name'], adam['jobs'] # Dostep wedlug kluczy 
# ('Adam', ['dev', 'mgr'])

tuple(adam.values())  # Zmiana wartosci na krotke 
# (['dev','mgr'], 'Adam', 40.5)

from collections import namedtuple    # Import typu rozszerzonego
Rec = nametuple('Rec', ['name', 'age', 'jobs'])  # Utworzenie instancji klasy
adam = Rec('Adam', age=40.5, jobs=['dev', 'mgr']) # Rekord w postaci nazwanej krotki 
adam
# Rec(name='Adam', age=40.5, jobs=['dev', 'mgr'])

adam[0], adam[2]   # Dostep wedlug pozycji elementow 
# ('Adam', ['dev', 'mgr'])
adam.name, adam.jobs  # Dostep wedlug atrybutow 
# ('Adam', ['dev','mgr'])

output = open(r'C:\spam', 'w') # Tworzy plik do zapisu ('w' z ang. write -- zapis)
input = open('data', 'r') # Otwiera plik do odczytu 'r' z ang.read -- odczyt)
input = open('data') # To samo co wyzej ('r' jest trybem domyslnym)
aString = input.read() # Zaladowanie calej zawartosci pliku do jednego lancucha znakow 
aString = input.read(N) # Zaladowanie nastepnych N bajtow (jednego lub wiecej) do lancucha znakow 
aString = input.readline() # Zaladowanie nastepnego wiersza (wraz ze znakami nowego wiersza \n) do lancucha znakow 
aList = input.readlines() # Zaladowanie calej zawartosci pliku do listy lancuchow znakow (wraz ze znakami \n)
output.write(aString) # Zapisanie ciagu znakow (lub bajtow) do pliku 
output.writelines(aList) # Zapisanie wszystkich lancuchow znakow z listy do pliku 
output.close() # Reczne zamkniecie pliku (kiedy konczymy prace z plikiem)
output.flush() # Zapisanie zawartosci bufora wyjsciowego na dysku bez zamykania pliku 
anyFile.seek(N) # Zmiana pozycji w pliku na offset N dla nastepnej operacji 
for wiersz in open ('data'): uzycie wiersza  # iteratory plikow -- wczytywanie zawartosci pliku wiersz po wierszu 
open ('f.txt', encoding='latin-1') # Pliki Unicode w Pythonie 3.x(ciagi typu str)
open('f.bin','rb') # Pliki Unicode w Pythonie 3.x(ciagi typu bytes)
codes.open('f.txt', encoding='utf8') # Pliki Unicode w Pythonie 2.x(ciagi typu unicode)
open('f.bin', 'rb') # Pliki Unicode w Pythonie 2.x(ciagi typu str)

afile = open(nazwa_pliku, tryb_przetwarzania)
afile.metoda()

# Zaawansowane narzedzia do obslugi przechiwywania obiektow (modul pickle) 
# Do obslugi spakowanych danych binarnych w plikach(modul struct) i do przetwarzanie specjalnych typow zawartosci takich jak tekst w formacie JSON XML CSV 

# Pliki wyjsciowe buforowane tekst ktory piszemy nie zawsze prznoszony na dysk po zamknieciu pliku lub wywolanie metody flush wymusza transfer danych na dysk 
# Buforowanie mozna wlaczyc za pomoca open ale moze miec negatywny wpluw na wudajnosc 
# Zapewnia swobodny dostep do zawartosci pliku poprzez okreslenie przesuniecia (offsetu) wzgledem poczatku pliku seek pozwala na odczytywanie i zapisywanie danych w okreslonych pozycjach 

myfile = open('myfile.txt', 'w') # Otwarcie do zapisu tekstowego (tworzy pusty plik)
myfile = ('witaj', 'pliku tekstowy \n') # Zapisanie wiersza tekstu 
# 22
myfile.write('zegnaj, pliku tekstowy\n')
# 23
myfile.close() # Zrzucenie bufora wysciowego na dysk 
myfile = open('myfile.txt') # Otwarcie do odczytu tekstu -- 'r' jest domyslne 
myfile.readline() # Wczytywanie wierszy z powrotem  
# 'witaj, pliku tekstowy \n'
myfile,readline() 
# 'zegnaj ,pliku tekstowy \n'
myfile.readline() 
# ...  -----> pusty lancuch znakow -- koniec pliku 

# Wywolanie metody write odczytuje literke nowego wiersza n teraz pokaze jak zrobic zeby nie odczytywala 
open('myfile.txt').read() # Wczytywanie wszystkiego naraz do lancucha cnakow 
# ' 'witaj, pliku tekstowy \nzegnaj ,pliku tekstowy \n'
print(open('myfile.txt').read()) # Sposob wyswietlania przyjazdy dla uzytkownika 
# witaj, pliku tekstowy 
# zegnaj ,pliku tekstowy

# Natomiast jak chcemy plik tekstowy przeczytac wiersz po wierszu korzystamy z iterawol pliku 
for line in open ('myfile'):  # Uzycie iteratorow plikow , a nie wczytywanie 
    print(line, end='')
...
# witaj, pliku tekstowy 
# zegnaj ,pliku tekstowy

# 345
F = open('data.bin' 'wb') # Otwarcie pliku binarnego do zapisu 
import struct 
data = struct.pack('>i4sh', 7, b'jajo', 8) # Utworzenie spakowanych danych binarnych
data 
# '\x00\x00\x07jajo\x00\x08'
F.write(data)  # Zapisanie lancucha bajtowego 
F.close()

F = open('data.bin', 'rb')
data = F.read()            # Pobranie spakowanych danych binarnych 
data 
# '\x00\x00\x07jajo\x00\x08'
values = struct.unpack('>i4sh', data)  # Konwersja na obiekty pythona 
values 
# (7, b'jajo', 8)

# Typ obiektu                   Kategoria typu                Zmienny ?
# Liczby (wszystkie)            Liczbowy                      Nie
# Lancuchy znakow(wszystkie)    Sekwencja                     Nie
# Listy                         Sekwencja                     Tak
# Slowniki                      Odwzorowanie                  Tak
# Krotki                        Sekwencja                     Nie
# Pliki                         Rozszerenie                   Nie dotyczy 
# Zbiory                        Zbior                         Tak
# Frozenset                     Zbior                         Nie
# bytearray                     Sekwencja                     Tak

# Sekwencja obliczanie dlugosci czy indeksowanie

L1 = [1, ('a', 3)] # Ta sama wartosc unikalne obiekty
L2 = [1, ('a', 3)] 
L1 == L2 , L1 is L2 # Odpowiednik ? Ten sam obiekt ?

# Operator == sprawdza rownosc wartosci . Python wykonuje test rownosci porownujac rekurencyjnie wszystkie zagniezdzone obiekty

# Operator is sprawdza identycznosc obiektow . Python sprawdza czy dwa podane obiekty sa tak naprawde jednym i tym samym obiektem (to znaczy znajduja soe pod jednym adresem w pamieci )
# Jak jest False to sa (referencjami do dwoch roznych obiektow i tym samym dwoch roznych fragmentow pamieci) 

# Jak krotki lancuch 
S1 = 'mielonka'
S2 = 'mielonka'
S1 == S2 , S1 is S2 
# (True, True) # Jak jest krotrzy lancuch znakow 

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)] # Mniejszy , rowny , wiekszy - krotka wynikow 
# (False, False, True)

# Test wielkoszi 
# 1) Python 2x 
# 2) 3.x

# 1)
D1 = {'a':1, 'b':2}
D2 = {'a';1, 'b':3}
D1 == D2  # Test rownosci slownikownwersji 2.x + 3x
# False
D1 < D2   # Test wielkosci slownikow tylko wersja 2.x
# True 

# 2)
list(D1.items())
# [('b', 2), ('a', 1)]
sorted(D1.items())
# [('a', 1), ('b', 2)]
sorted(D1.items()) < sorted(D2.items()) #Test wielkosci w wersji 3.x
# True
sorted(D1.items() > sorted(D2.items()))
# False 

# Obiekt                Wartosc
#  "mielonka"            True
#  ""                    False
# [1, 2]                 True
# []                     False
# {'a':1}                True
# {}                     False
# 1                      True
# 0.0                    False
# None                   False


L = [4, 5, 6]
X =  L * 4
Y = [L] * 4
X 
# [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
Y 
# [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]
L[1] = 0 # Ma wplyw na Y , ale nie na X
X 
# # [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
Y 
# # [[4, 0, 6], [4, 0, 6], [4, 0, 6], [4, 0, 6]]

L = [4, 5, 6]
Y = [list(L) * 4] # Osadzenie wspoldzielnej kopii L
L[1] = 0
Y 
# [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]

Y[0][1] = 99
Y
# [[4, 99, 6], [4, 99, 6], [4, 99, 6], [4, 99, 6]]  # Wszystkie cztery kopie sa nadal takie same 

# # # # # # # # # # # # # # # # # INSTRUKCJE I SKLADNIA # # # # # # # # # # # #  INSTRUKCJE I SKLADNIA
# Instrukcja                      Rola                        Przyklad
# 
# Przypisanie                     Tworzenie referencji        a, b = 'dobry' , 'zly' 
# Wywolania i inne wyrazenia      Wywolywanie funkcji         log.write("mielonka, szynka")
# Wywolania print                 Wyswietlanie obiektow       print('The Killer' , joke)
# if/elif/else                    Wybor dzialania             if "python" in text:
#                                                                 print(text)
# for/else                        Iteracje                    for x in mylist:
#                                                                 print(x)
# while/else                      Ogolne petle                while X > Y:
#                                                                 print('witaj') 
# pass                            Pusta instrukcja zastepcza  while True :
#                                                                 pass
# break                           Wyjscie z petli             while True :
#                                                                 if exittest() : break
# continue                        Kontynuacja petli           while True :
#                                                                 if skiptest(): continue 
# def                             Funkcje i metody            def f(a, b, c=1, *d):  
#                                                                 print(a+b+c+d[0])
# return                          Wynik funkcji               def f(a, b, c=1, *d):  
#                                                                 print(a+b+c+d[0])
# yield                           Funkcje generatora          def gen(n):
#                                                                 for i in n: yield i*2
# global                          Przestrzenie nazw           x = 'stary'
#                                                             def function():
#                                                                 nonlocal x; y; x = 'nowy'
# nonlocal                        Przestrzenie nazw(3.x)      def outer():
#                                                                 x = 'stary'
#                                                             def function():
#                                                                 nonlocal x; x = 'nowy'
# import                          Dostep do modulow           import sys
# from                            Dostep do atrybutow         from sys import stdin
# class                           Budowanie obiektow          class Subclass(Superclass):
#                                                                 staticData = []
#                                                                 def method(self): pass
# try/except/finally              Przechwytywanie wyjatkow    try:
#                                                                 action()
#                                                             except:
#                                                                 print('Blad w akcji')
# raise                           Zglaszanie wyjatkow         raise EndSearch(location)
# assert                          Sprawdzanie w debugowaniu   assert X > Y, 'X jest za male'
# with/as                         Menedzery kontekstu         with open('data') as myfile:
#                                                                 process(myfile)
# del                             Usuwanie referencji         del dane[k]; del[i : j]; del obiekt.atrybut; del zmienna

# Prosta petla interaktywna (odczytaj-oblicz-wyswitl duzymi literami)
while True:
    reply == input("Wpisz dowolny tekst ")
    if reply == 'stop' : break
    print(reply.upper())

# Wpisz tekst : mielonka ---> MIELONKA
# Wpisz tekst : 42 ---> 42
# Wpisz tekst :  stop ---> stop

while True:
    reply == input("Wpisz dowolny tekst ")
    if reply == 'stop' : break
    print(int(reply) ** 2)
print('Koniec')

# Wpisz tekst : 2 ----> 4
# Wpisz tekst : 40 ----> 1600
# Wpisz tekst : stop ---->  Koniec 

# W wersji 2.x Python input to raw_input

while True:
    reply = input("Wpisz dowolny tekst : ")
    if reaply == 'stop' :
        break
    elif not reply.isdigit():
        print('Niepoprawnie' * 3)
    else:
        print(int(reply) ** 2 )
print('Koniec')


# Wpisz tekst : 5 ---> 25
# Wpisz tekst : xyz ---> Niepoprawnie!Niepoprawnie!Niepoprawnie!
# Wpisz tekst : 10 ---> 10
# Wpisz tekst : stop
# Koniec 

# Obsluga bledow za pomoca instrukcji try  to samo co wczesniej tylko z try 
while True:
    reply = input('wpisz tekst:')
    if reply == 'stop' : break 
    try:
        num = int(reply)
    except:
        print('Niepoprawnie!' * 5)
    else:
        print(int(reply) ** 2 )
print('Koniec') 

# Obsluga liczb zmiennoprzecinkowych 
while True:
    reply = input('Wpisz tekst: ')
    if reply == 'stop': break
    try: 
        print(int(reply) ** 2)
    except:
        print('Niepoprawnie' * 8)
print('Koniec')

while True:
    reply = input('Wpisz tekst: ')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2 )
    except:
        print('Niepoprawnie!' * 8)
print('Koniec')

# Wpisz tekst: 50 ----> 2500
# Wpisz tekst: 40.5 ----> 1640.25
# Wpisz tekst 1.23E-100 ----> 1.5129e-200
# Wpisz tekst: spam ----> Niepoprawnie 
# Wpisz tekst : stop ----> Bye

# Kod zagniezdzony na trzy poziomy glebokosci 
while True:
    reply = input('Wpisz tekst: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Niepoprawnie!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('malo')
        else:
            print(num ** 2)
print('Koniec')

# Wpisz tekst: 19 ----> malo 
# Wpisz tekst: 20 ----> 400
# Wpisz tekst: mielonka ----> Niepoprawnie!
# Wpisz tekst: stop ----> Koniec 

# Formy instrukcji przpisania 
spam = 'Mielonka'  # ----> Forma postawowa
spam . ham = 'mniam' , 'MNIAM' # ----> Przypisanie krotki (pozycyjne)
[spam, ham] = ['mniam' , 'MNIAM'] # ----> Przypisanie listy (pozycyjne)
a, b, c, d = 'mielonka' # ----> Przypisanie sekwencji, uogolnione
a, *b = 'mielonka' # ----> Rozszerzone rozpakowanie sekwencji (Python 3.x)
spam = ham = 'lunch' # ----> Przypisanie do wielu celow 
spam += 42 # ----> Przypisanie rozszerzone (odpowiednik spam = spam + 42)

# Przypisanie sekwencji 
% python 
nudge = 1               # Podstawowe przypisanie 
wink = 2     
A, B = nudge, wink      # Przypisanie krotki
A, B                    # Jak A = nudge; B = wink   # (1, 2)
[C, D] = [nudge, wink]  # Przypisanie listy
C, D                    # (1, 2)

nudge = 1
wink = 2
nudge, wink = wink, nudge  # Krotki: zamiana wartosci 
nudge, wink                # Jak T = nudge; nudge = wink; wink = T
nudge, wink                # (2, 1)

[a, b, c] = (1, 2, 3)  # Przypisanie krotki wartosci do listy nazw 
a, c                   # (1, 3)
(a, b, c) = 'ABC'      # Przypisanie lancucha znakow do krotki 
a, c                   # ('A' , 'C')

# Zaawansowane wzorce prypisywania sekwencji 
string = 'JAJO'
a, b, c, d = string     # Ta sama liczba elementow po obu stronach 
a, d                    # ('J' , 'O')
a, b, c = string        # Blad rozna liczba elementow 

a, b, c = string[0], string[1], string[2:]   # Indeksowanie i wycinek
a, b, c    # ('J' , 'A' , 'JO')
a, b, c = list(string[:2] + [string[2:]])    # Wycinek i konkatenacja 
a, b, c    #  ('J' , 'A' , 'JO')
a, b = string[:2]  # To samo w prostrzej formie 
c = string[2:]
a, b, c    # ('J' , 'A' , 'JO')
(a, b), c = string[:2], string[2:]  # Zagniezdzone sokwencje 
a, b, c    # ('J' , 'A' , 'JO')

((a, b), c) = ('JA', 'JO')   # Polaczone w pary zgodnie z ksztaltem i pozycja 
a, b, c # ('J' , 'A' , 'JO')

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ...   # Proste przypisanie do krotki 
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # Zagniezdzone przypisanie do krotki 

red , green , blue = range(3)  # Przypisanie rozpakowujace sekwencje spowodowaly roniez pojawienia sie kolejnej sztuczki programistycznej w Pythonie 
red, blue                      # przypisanie serii liczb calkowitych do zbioru zmiennych 
# (0, 2)

list(range(3)) # [0, 1, 2]

list(zip(range(10))) # otworzy liste z 0 do 9 {}

# Przypadki brzegowe 
seq = [1, 2, 3, 4]
a, b, c, *d = seq 
print (a, b, c, d) # 1 2 3 [4]

a, b , c, d, *e = seq 
print(a, b, c, d, e)
# 1 2 3 [4]

a, b, *e, c, d = seq 
print(a, b, c, d, e)
# 1 2 3 4 [ ]

seq # [1, 2, 3, 4]
a, *b = seq  # Pierwszy pozostale  # (1, [2, 3, 4])
a, b = seq[0], seq[1:] # Pierwszy pozostaly : metoda tradycyjna 
a, b # (1, [2, 3, 4])
*a, b = seq # Poczatek ostatni 
a, b # ([1, 2, 3], 4)
a, b = seq[:-1], seq[-1] # Poczatek, ostatni: metoda tradycyjna 
a, b # ([1, 2, 3], 4)

a = b = c = 'mielonka'
a, b, c # ( 'mielonka' 'mielonka' 'mielonka' )

c = 'mielonka'
b = c
a = b 

a = b = 0
b = b + 1
a, b # ( 0, 1 )

a = b = []
b.append(42)
a, b # ([42], [42])

a = []
b = []       # a i b nie wspoldziela tego samego obiektu 
b.append(42)   
a, b # ([ ], [42])

a, b = [], []  # a i b nie wspoldziela tego samego obiektu 

# Przypisanie rozszerzone 
X = X + Y  # Forma tradycyjna 
X += Y  # Nowsza forma rozszerzona 

X += Y
X *= Y 
X %= Y 
X &= Y 
X ^= Y
X << Y
X -= Y
X /= Y
X ** Y
X |= Y
X >>= Y # przesuwa w prawo i przepisuje 
X //= Y # dzielenie bez reszty 

x = 1 
x = x + 1
x # 2
x += 1 
x # 3 

S = 'mielnka'
S += 'MIELONKA'
S # 'milonkaMIELONKA'

L = L + [5, 6]    # Konkatenacja: wolniej 
L # [1, 2, 3, 4, 5, 6]
L.extend([7, 8])  # Szybciej ale w kiejscu
L # [1, 2, 3, 4, 5, 6, 7, 8]
L += [9, 10] 
L # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slowa zarezerwowane w Python 

False 
None 
True 
and 
as 
assert 
break 
class 
continue 
def 
del 
elif 
else 
except 
finally 
for 
from 
global 
if 
import 
in 
is 
lambda 
nonlocal 
not 
or 
pass 
raise 
return 
try 
while 
with 
yield 

exec # jest sowem zarezerwowanym poniewaz jest instrukcja a nie funkcja wbudowana 
nonlocal # nie jest zarezerwowanym slowem poniewaz ta insteukcja nie jest dostepna 
# Zamiast slowa zarezerwowanego mozna uzyc _ 

# Automatyczne przekierowanie strumienia 
import sys 
temp = sys.stdout # Zapisanie na pozniej 
sys.stdout = open('log.txt' , 'a')  # Przekierowanie do pliku 
print('mielonka') # Wypisuje do pliku , nie na ekran 
print(1, 2, 3)
sys.stdout.close() # Oproznienie bufora zapisu
sys.stdout = temp # Przywrocenia oryginalnego strumienia 

print('znow jestem')  # znow jestem  # Wynik znowu pojawia sie na ekranie
print(open('log.txt').read()) # mielonka   # Rezultat wczesniejszego wypisywania 
#                             # 1 2 3

log = open('log.txt', 'a') # 3x
print(x, y, z, file=log) # Zapis do pliku 
print(a, b, c)  # Zapis do oryginalnego strumienia stdout


X = 1 ; Y = 2
print(X, Y)  # Wyswietlenie metoda standardowa 
import sys 
sys.stdout.write(str(X) + ' ' + str(Y) + '\n') # 1 2    # Wyswietlenie metoda plikowa  
#                                              # 4
print(X, Y, file = open('temp1', 'w')) # Przekierowanie do pliku
open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n') # Bezposredni zapis do pliku 
print(open('temp1', 'rb').read())  # Binarny tryb odczytu  # b'1 2\r\n'
print(open('temp2', 'rb').read())  # b'1 2\r\n'

print('%s %s %s ' % ('mielonka', 'szynka', 'jajka')) # mielonka szynka jajka 
print('{0} {1} {2}'.format('mielonka', 'szynka', 'jajka')) # mielonka szynka jajka 
print('odpowiedz: ' + str(42)) # answer: 42 


if test:            # Test if 
    instrukcje1     # Powiazany blok 
elif test2:         # Opcjonalnie testy elif
    instrukcje2     
else:               # Opcjonalna klauzula else
    instrukcja3


x = 'zabojczy krolik'
if x == 'roger':
    print("gdzie jest Jessie?")
elif x == 'bugs':
    print('co slychac doktorku?')
else:
    print('Uciekaj! Uciekaj!')
# Uciekaj! Uciekaj!

choice = 'szynka'
print({'mielonka': 1,25,         # Instrukcja 'switch' oparta na slowniku
        'szynka': 1.99,          # Wartosc domyslna dzieki has_key lub get 
        'jajka': 0.99,
        'boczek', 1.10}[choice])
    # 1.99

if choice == 'mielonka':
    print(1.25)
elif choice == 'szynka':
    print(1.99)
elif choice == 'jajka':
    print(0.99)
elif choice == 'boczek':
    print(1.10)
else:
    print('Zly wybor')
# 1.99

branch = {'mielonka': 1.25,
           'szynka': 1.99
           'jajka': 0.99}
print(branch.get('mielonka', 'Zly wybor')) # 1.25
print(branch.get('boczek', 'Zly wybor'))   # Zly wybor 

choice = 'boczek'
if choice in branch :
    print(branch[choice])
else:
    print('Zly wybor!')

try:
    print(branch[choice])
except KeyError:
    print('Zly wybor')
# Zly wybor 

x = 1
if x:
    y = 2
    if y:
        print('blok2')
    print('blok1')
print('blok0')

x = 'MIELONKA'
if 'plot' in 'zywoplot':
    print(x * 8)         # Wyswietla 8 razy slowo MIELONKA
    x += 'NI'
    if x.endswitch('NI'):
        x *= 2
        print(x)         # Wyswietla "MIELONKANIMIELONKANI"

X and Y # Wyrazenie jest prawdziwe kiedy zarowno X , jak i Y sa prawdziwe 
X or Y # Wyrazenie jest prawdziwe kiedy X lub Y jest prawdziwe 
not X # Wyrazenie jest prawdziwe , kiedy X jest falszywe (wyrazenie zwraca True lub False)

2 < 3 , 3 < 2 # (True , False)
2 or 3 , 3 or 2 # (2, 3)
[] or 3 # 3
[] or {} # {}

2 and 3 , 3 and 2 # Zwraca operand z lewej strony wyrazenia jezeli jest walszem 
# (3 , 2)         # w przeciwnym wypadku zwraca operand z prawej strony (true false)

A = 't' if  'mielonka' else 'f' # Nie pusty ciag znakow ma wartosc true , czyli prawdza
A # 't'
A = 't' if '' else 'f'
A # 'f'
A = ((X and Y) or Z)
A = Y if X else Z 

while test:        # Warunek petli 
    instrukcje1    # Cialo petli 
else:              # Opcjonalne else 
    insturkcje2    # Wykonane jesli petli nie zakonczymy break 

while True :
    print("Nacisnij kombinacje klawiszy Ctrlq^C, by mnie zatrzynac! ")

x = 'mielonka'   # Python 2x 
while x:
    print(x, end = ' ')
    x = x[1:]   
# mielonka ielonka elonka lonka onka nka ka a

# Ogolny format petli 
while test1:
    instrukcje1   
    if test2; break     # Wyjcie z petli pominiecie reszty 
    if test3; continue  # Przejscie do gory petli do testu1 
else:
    instukcje2          # Wykonywanie jesli nie trafilismy w break 


while True: pass        # Uzyj Ctrl + C by mnie zatrzymac 

def func1():   # Wstawic tu pozniej prawdziwy kod! 
    pass 
def func2():
    pass 

# Do elementow listy + oraz *
sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x 
sum # 10
prod = 1 
for item in [1, 2, 3, 4]: prod *= item
prod # 24 


# Typ sekwencji w petli for 
S = "drwal"
T = ("i", "jestem", "git")
for x in S: print(x, end= ' ')  # Iteracja do lancucha znakow 
# d r w a l
for x in T: print(x, end= '') # Iteracja po krotce 
# i jestem git 


# Przypisanie krotek w petli for 
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:     # Przypisanie krotek 
    print(a, b)

# 1 2
# 3 4
# 5 6

D = {'a':1 , 'b':2, 'c':3}
for key in D:
    print(key, '=>', D[key]) # Uzycie iteratora po kluczach slownika i indeksowania 
# a => 1
# c => 3
# b => 2 

list(D.items())
# [('a', 1), ('c', 3), ('b', 2)]

for (key, value) in D.items():            # Iteracja po kluczach i wartosciach 
    print(sorted(key), ' => ', value)


# Uzycie w naglowku petli 
((a, b), c) = ((1, 2), 3)
a, b, c 
# (1 , 2, 3)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
# 1 2 3
# 1 2 3

for ((a, b), c) in [([1, 2], 3), ['XY', 6]] : print(a, b, c)
# 1 2 3
# X Y 6 

a, b, c = (1, 2, 3) # Przypisanie krotki 
a, b, c
(1, 2, 3)

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: # Wykorzystanie w petli for
    print(a, b, c)
# 1 2 3
# 4 5 6 

a, *b, c = (1, 2, 3, 4) # Rozszerzone przepisanie sekwencji 
a, b, c
# (1, [2, 3], 4)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
# 1 [2, 3] 4
# 5 [6, 7] 8

items = ["aaa", 111, (4, 5), 2.01] # Zbior obiektow 
tests = [(4, 5), 3.14] # Szukane klucze 
for key in tests:  # Dla wszystkich kluczy 
    for item in items: # Dla wszystkich elementow 
        if item == key: # Sprawdzania dopasowania 
            print(key, "znaleziono")
            break 
    else:
        print(key, "nie znaleziono!")
# (4, 5) znaleziono 
# 3.14 nie znaleziono !

# Python wykonuje samodzielna prace 
for key in test:  # Dla wszystkich kluczy 
    if key in items:  # Niech Python sam sprawdza dopasowanie 
        print(key, "znaleziono")
    else:
        print(key,"nie znaleziono!")


# Zamiast wyswietlenia wynikow na ekranie tworzy liste do pozniejszego uzycia 
# res lista zawierajaca wszystkie elementy znalezione na lancuchach seq1 i seq2
seq1 = "mielonka"
seq2 = "biedronka"
res = []                  # Na poczatek pusta lista 
for x in seq1:            # Przeszukanie pierwszej sekwencji 
    if x in seq2:         # Powtarzajacy sie element ?
        res.append(x)     # Dodanie na koncu listy wynikow 
res 
# ['i', 'e', 'o', 'n', 'k', 'a']


# albo w ten sposob 
[x for x in seq1 if x in seq2] # Python zbiera wyniki 
# ['i', 'e', 'o', 'n', 'k', 'a']

# Skanery plikow 
file = open('test.txt', 'r') # Wczytywanie zawartosci do lancucha znakow 
print(file.read())

# zALADOWAC PLIK W MNIEJSZYCH CZESCIACH WHILE I BREAK 
file = open('test.txt')
while True:
    char = file.read(1)  # Wczytywanie znak po znaku 
    if not char: break   # Pusty ciag znakow oznacza koniec pliku 
    print(char)
for char in open('test.txt').read():
    print(char)

# Petrla for tez znak po kolei jednak laduje caly plik do pamieci za jednym razem ( i ze on tam sie zmiesci ) zakladaBy zamiast tego wczytac wiersz po wierszu lub blok po bloku
file = open('test.txt')
while True :
    line = file.readline()     # Wczytanie wiersz po wierszu 
    if not line : break 
    print(line.rstrip())       # Wiersz zawiera juz znak \n
file = open('test.txt', 'rb')
while True :
    chunk = file.read(10)      # Wczytywanie bajtowych fragmentow do 10 bajtow 
    if not chunk: break 
    print(chunk)

# Dane binarne wczytuja sie w blokach Aby wczytac wiersz po wierszu napiszemy kod z petla for i bedzie szybciej sie wykonywal 
for line in open ('test.txt').readlines():
    print(line.rstrip())
for lines in open('test.txt'):  # Uzycie iteratorow -- najlepszego trybu dla tekstowych danych wejsciowych 
    print(line.rstrip())

# Odwrocenie kolejnosci wierszy readlines reversed lista dzila ale obiekt pliku juz nie 
for line in reversed(open('test.txt').readlines()) # : ...

# Wbudowana funkcja range zwraca serie kolejnych coraz wiekszych liczb calkowitych moga byc wykorzystane dle petli for 
# Wbudowana funkcja zip zwraca serie krotek rownoleglych elementow , w petli for moze byc wykorzystana 
# Wbudowana funkcja enumerate (Python 2.3) generuje wartosc jak i indeksy elementow obiektu iterowalnego nie trzeba liczyc recznie 
# Wbudowana funkcja map (Python 1.0) moze miec podobny efekt jak zip w (Python 2.x), ale zostala usunieta w wersji 3.x

list(range(5)), list(range(2, 5)), list(range(0, 10, 2))
# ([0, 1, 2, 3, 4], [2, 3, 4], [0, 2, 4, 6, 8])

list(range( 5, 5))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
list(range(5, 5, 1))
# [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

for i in range(3):
    print(i, 'Python')
# 0 Python
# 1 Python
# 2 Python 


# Skanowanie sekwencji petla while z funkcja range kontra petla for 
X = 'mielonka'
for item in X: print(item, end= '') # Prosta iteracja 
# m i e l o n k a


i = 0 
while i < len(X):
    print(X[i], end = ' ') # Iteracja z petla while 
    i += 1
# m i e l o n k a

X 
# 'mielonka'
len(X)  # Dlugosc lancucha znakow 
# 8
list(range(len(X)))  # Wszystkie poprawne wartosci przesuniecia dla X
# [0, 1, 2, 3, 4, 5, 6, 7]
for i in range(len(X)): print(X[i], end= ' ')  # Recznie indeksowanie za pomoca range/len
# m i e l o n k a

for item in X: print(item, end=' ') # Jezeli mozesz , korzystac z prostej formy iteracji

S = 'mielonka'
for i in range(len(S)):    # Petla wykonuje iteracje dla wartosci z zakresu 
    S = S[1:] + S[:1]      # Przenosi pierwszy element na koniec
    print(S, end= ' ')
#  ielonkam elonkami lonkamie onkamiel nkamielo kamielon amielonk mielonka


S 
# 'mielonka'
for i in range(len(S)):     # Dla pozycji 0.7
    X = S[i:] + S[:i]       # Pozostala czesc + pierwszy znak 
    print(X, end= ' ')
# mielonka ielonam elonkami onkamiel nkamiel kamielon amielonk

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]   # Dziala na dowolnych typach sekwencji 
    print(X, end= ' ')
# [1, 2, 3] [2, 3, 1] [3, 1, 2]

S = 'abcdefghijk'
list(range(0, len(S), 2))
# [0, 2, 4, 6, 8, 10]
for i in range(0, len(S), 2): print(S[i], end= ' ')
# a c e g i k

L = [1, 2, 3, 4, 5]
for x in L:          # Zmienia x, a nie L
    x += 1
L # [1, 2, 3, 4, 5]
x # 6

L = [1, 2, 3, 4, 5]
for i in range(len(L)):    # Dodanie 1 do kazdego elementu listy L
    L[i] += 1              # range i len pozwala uzyskac pozadane indeksy 
L  # [2, 3, 4, 5, 6] 



# To co teraz bedzie nie da sie zrobic za pomoca for x in L przechodzi same elementy listy a nie ich  poizycje .
i = 0
while i <  len(L):
    L[i] += 1
    i += 1
L # [3, 4, 5, 6, 7]

# Przechodzenie rownolegle -- zip oraz map 
# W budowana funkcja zip pozwala na wykorzystanie petli for do rownoleglego przejscia wiekszej liczby sekwencji w tej samej petli bez nakladania sie na siebie w czasie
# w pprostej operacji funkcja przyjmuje jako argument jedna lub wieksza liczbe sekwencji i zwraca serie krotek laczacych w pary rownolegle elementy z tych sekwencji
L1 = [1,2,3,4]
L2 = [5,6,7,8]
# Zeby polaczyc te dwa elementy mozemy wykorzystac funkcje zip 
list(zip(L1, L2))
# [(1, 5), (2, 6), (3, 7), (4, 8)]

for (x, y) in zip(L1, L2):
    print(x, y, ' -- ', x+y)
# 1 5 -- 6
# 2 6 -- 8
# 3 7 -- 10
# 4 8 -- 12 

for (x, y) in zip(L1, L2):
    print(x, y, ' --- ', x+y)

T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
T3 # (7, 8, 9)
list(zip(T1, T2, T3))  # Trzy krotki dla trzech argumentow 
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

S1 = 'abc'
S2 = 'xyz123'
list(zip(S1, S2))    # Odcina krotki do dlugosci najkrotrzego elementu 

S1 = 'abc'
S2 = 'xyz123'
map(None, S1, S2)   
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
list(map(ord, 'mielonka'))
# [109, 205, 101, 108, 111, 110, 107, 97]

res = []
for c in 'mielonka': res.append(ord(c))
res 
# [109, 105, 101, 108, 111, 110, 107, 97]

D1 = {'mielonka':1, 'jajka':3, 'tost':5}
D1 
D1 = {}
D1['mielonka'] = 1
D1['jajka'] = 3
D1['tost'] = 5

keys = ['mielonka', 'jajka', 'tost']
vals = [1, 3, 5]

# Jedna z mozliwosci przeksztalcenia ich w slownik bedzie zastosowanie na listach funkcji zip i rownolegle przejscie ich za pomoca petli for 
list(zip(keys, vals))
# [('mielonka', 1), ('jajka': 3), ('tost': 5)]
D2 = {}
for (k, v) in zip (keys, vals): D2[k] = v 
D2 # {('jajka': 3), ('tost': 5)], ('mielonka', 1)}


import re 
if re.match(" ^ [A-Z][a-z] a* $ ", "Alaaaaaaaa "): # Jednka literka z Z i ile chcemy liter a True False
    print("Dopasowano! ")                          # * nawet jak nie pojawia sie an razu i tak bedzie dopasowane
else:
    print("Nie dopasowano! ")


import re 
if re.match(" ^ [A-Z][a-z] * $ ", "A "):  # Bez literki a wszystko , dopasowano bo wystepuje tylko jedna literka A albo Ala
    print("Dopasowano! ")                          
else:
    print("Nie dopasowano! ")


import re 
if re.match(" ^ [A-Z][a-z]a $ ", "Alaaaaaaaa "): # Jedna literka  z Z 
    print("Dopasowano! ")
else:
    print("Nie dopasowano! ")


import re 
if re.match(" ^ [A-Z][a-z] + $ ", "Ala "):  # Pozwala na nie ograniczona ilosc znakow np [a-z] ale musi wystapic co najmniej raz
    print("Dopasowano! ")                   # +  , True bo mamy 2 literki ze zbioru malych liter , Al tez dziala naley do dwoch grup
else:                                       # Jak jedna literka A to nie dopasowane bo jest tylko z jednego zbioru 
    print("Nie dopasowano! ")


import re 
if re.match(" ^ [A-Z][a-z] ? [A-Z] $ ", "AlA "):  # Dany znak w przedziale [a-z] moze wystapic tylko raz ale moze nie wystapic w cale True 
    print("Dopasowano! ")                                # Bez znaka zapytania to tylko raz ale jak ? to dodaje mozliwosc wystapienia tylko raz
else:                                                    # Ala dopasowano bo jest tylko jedna literka mala l , AA rowniez dopasowana bo mamy symbol ?
    print("Nie dopasowano! ")                            # Alla , nie dopasowane 



import re 
if re.match(" ^ [A-Z][a-z] {2, 5} $ ", "Ala "):  # Dany znak moze powtorzyc sie ile chce i mozna rowniez ograniczyc do minimalnej i max  ilosci jej wystapien 
    print("Dopasowano! ")                           # {} w znaku min wartosc powtorzen tego znaku  , i max wartosc  , jezeli wziac {2, } i 2 pusta wartosc to bedzie dopasowane od 2 do ...
else:                                               # Od poczaatk jedna duza litera i pozniej min 2 i max 5 malych liter , rozniez { , 5} minimum ile chcesz max do 5 np S , Seba , Sebastian juz nie dopasowane 
    print("Nie dopasowano! ")                       # Ala dopasowano , Al nie dopasowano 


# Wyrazenie regularne  dalszy ciag 
import re 
if re.match ( " ko. " , "kotttttt"): # Ma sprawdzac czy dany wzor pasuje do zoru po prawej stronie 
    print("Dopasowano! ")       # Zeby 3 kj. , . oznacza zastapione dowolnym znakiem 
else:                           # kac juz nie dziala bo druga literka to a, kotttttt pasuje ile chcesz 
    print("Nie dopasowano! ")

import re 
if re.match ( " ^ ko. $ " , "kotttt"): # ^ dany wzor musi  rozpoczynac od danych znakow
    print("Dopasowano! ")            # $ zeby na tym znaku byl koniec  kottttttt juz nie bedzie dopaspwywane bo po . wystepuja jakies inne znaki litery 
else:                                # ko0 dziala  
    print("Nie dopasowano! ")

import re 
if re.match ( " [Kk]o. " , "kot"):  # Jezeli dopasowano chociaz jeden znak z [Kk] to bedzie true 
    print("Dopasowano! ")           # Tekstowy tekst moze sie rozpoczyna z malej litery k lub z duzej litery K
else:                           
    print("Nie dopasowano! ")

import re 
if re.match ( " ^ [^A-Za-z]o. $ " , "kot"): # [^A] dany znak nie moze wystapic w tym miejscu na pierwsszej pozycji rok nie dopasowano ^ [A-Za-z] te litery nie moga wystepowac  na poczatku r
    print("Dopasowano! ")           
else:                           
    print("Nie dopasowano! ")

import re 
if re.match ( " ^ [rR]ok [- _ =] [0-9][0-9][0-9][0-9] $ " , "Rok-1995"):  # [0-9] ... cyfr dokladnie 4 ,  ok musi wystapic , - powienien byc i , 4 cyfry 1995
    print("Dopasowano! ")                                                 # Rok-1995 DOPASOWANO BO SPELNIA WSZYSTKIE KRYTERIA 
else:                           
    print("Nie dopasowano! ")

import re  # Wyrazenia regularne 
wzor = r"banan\nbanan\tbanan"  # r anulowac takie znaki r ---> surowy string ignoruje wszystkie znaki specjalne banan\n\banan\tbanan 
tekst = r"gruszkabananjablko"  
print(wzor)

import re  # Wyrazenia regularne 
wzor = r"banan"                 # np wysylanie mejla, albo haslo przechodzimy przez walidacje x musi byc duze ....
tekst = r"gruszkabananjablko"   # Spraqwdzanie czy wzor slowo banan pasuje do tekstu 
print(wzor)                     # mozemy sprawdzic czy wystepuje czy zaczyna sie czy konczy sie slowem banan 

import re  
wzor = r"banan" 
tekst = r"gruszkabananjablko"  
print(re.match(wzor , tekst))               # match dopasowanie   , warosc None kiedy nie udalo nic dopasowac

import re  
wzor = r"banan" 
tekst = r"banangruszkabananjablko"  
print(re.match(wzor, tekst))                # True dopasowuje tylko wylacznie tekst ktory zaczyna sie od danego wzoru 

if re.match(wzor , tekst) :
    print("Dopasowano!")                    # Dopasowano  tekst zaczyna sie od wzoru 
else :
    print("Nie dopasowano !")

if re.match(r" . * " + wzor + r" . * " , tekst) :    # Czy banan znajduje sie w srodku 
    print("Dopasowano!")                   
else :
    print("Nie dopasowano !")

if re.search(wzor, tekst):    # szuka dopasowanie w dowolnym miejscu 
    print("Dopasowano!")                   #    Dopasowano  
else :
    print("Nie dopasowano !")

print(re.findall(wzoer, tekst))  # Wszystkie dopasowania w tekscie jak w tekst wpisac dananjblkobanan wyswietli sie ['banan'] ['banan'] postac zwyklej listy 

dopasowanie = re.search(wzor, tekst)
if dopasowanie :
    print(dopasowanie.group())  # Wskazuje nam wszystkie grupy ktore udalo sie dopasowac 
    print(dopasowanie.start())  # gruszkabananjablko 7 zaczyna sie b 12 zaczyna sie j 
    print(dopasowanie.end())    # wyswietli sie 7 12 
    print(dopasowanie.span())   # Wynnik startu i konca jednoczesnie  poczatek i moniec jako krotki (7 ,12)

tekst2 = re.sub(wzor, r"jagoda", tekst) # zamiana przyjmuje o jeden argument wiecej  , tekst ktory chcemy podmienic zweby zastepowal nam wzor 
print(tekst2)   # gruszkajagodajablko   juz w srodku mamy jagoda , wyszukuje wszystkich dopasowan do wzoru i zastepuje tekstum jako podany drugi argument  
######################################################################################################
# Kontynuacja ksiazki 
# Lambda 

# Lambda to funkcja anonimowa, czyli funkcja, która nie ma nazwy. Jest to krótki i jednorazowy sposób zdefiniowania funkcji w języku Python.
# Oto kilka przykładów zastosowania lambdy w kodzie Python:  

# 1. Funkcja, która zwraca podwojoną wartość argumentu:
f = lambda x: x * 2
print(f(5)) # Output: 10

# 2.  Funkcja, która zwraca sumę dwóch argumentów:
f = lambda x, y: x + y
print(f(3, 4)) # Output: 7

# 3.Sortowanie listy liczb za pomocą funkcji lambda: 
my_list = [5, 2, 8, 1, 9, 3]
sorted_list = sorted(my_list, key=lambda x: x)
print(sorted_list) # Output: [1, 2, 3, 5, 8, 9]

# 4. Użycie lambdy w wyrażeniu listowym:
my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list) # Output: [2, 4, 6, 8, 10]



# Yield 
# yield jest wykorzystywane w funkcjach generatorów w języku Python, które pozwalają na generowanie sekwencji wartości w locie. Zamiast zwracać wartość, funkcja generatora zwraca generator, który może być iterowany, a każde wywołanie generuje kolejną wartość.
 
# 1. Generowanie sekwencji liczb nieparzystych:
def odd_numbers(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            yield i

for num in odd_numbers(10):
    print(num)
# Output: 1 3 5 7 9

# 2. Generowanie sekwencji ciągów Fibonacciego:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))
# Output: 0 1 1 2 3 5 8 13 21 34

# 3. Generowanie sekwencji wartości z listy:
def my_generator(lst):
    for item in lst:
        yield item

gen = my_generator(['apple', 'banana', 'cherry'])
for fruit in gen:
    print(fruit)
# Output: apple banana cherry

# W każdym z powyższych przykładów funkcja zawiera instrukcję yield, która zwraca kolejną wartość sekwencji. yield pozwala na zatrzymanie funkcji w trakcie jej działania i tymczasowe przekazanie wygenerowanej wartości, a następnie kontynuowanie działania funkcji od tego miejsca w kolejnym wywołaniu.
# Funkcje generatorów i yield są przydatne w przypadku generowania dużych ilości danych lub gdy generowanie danych jest złożone obliczeniowo.



# Lambda 
# lambda to instrukcja używana do tworzenia krótkich, anonimowych funkcji w języku Python. Funkcje te są zwykle jednolinijkowe i służą do wykonania jednego konkretnego zadania.

# 1. Zastosowanie do prostych obliczeń matematycznych:
multiply = lambda x, y: x * y
print(multiply(2, 3))
# Output: 6

# 2. Sortowanie listy na podstawie wartości konkretnego klucza:
data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 18}, {'name': 'Bob', 'age': 32}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)
# Output: [{'name': 'Jane', 'age': 18}, {'name': 'John', 'age': 25}, {'name': 'Bob', 'age': 32}]

# 3. Wykorzystanie wraz z funkcją map() do wykonania operacji na każdym elemencie listy:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# Output: [1, 4, 9, 16, 25]

# W każdym z powyższych przykładów lambda służy do definiowania anonimowej funkcji, która jest przypisywana do zmiennej i może być wykorzystywana w dalszej części kodu. lambda zwykle składa się z parametrów oddzielonych przecinkami (jeśli są potrzebne) oraz wyrażenia, które ma zostać zwrócone.
#Użycie lambda jest przydatne w przypadku, gdy potrzebujemy szybko stworzyć i wykorzystać krótką funkcję, bez konieczności definiowania jej w oddzielnej części kodu.



# def
def nazwa(arg1, arg2, argN);
    instrukcje 

def nazwa(arg1, arg2, argN):
    ...
    return wartosc 

# iNSTRUKCJE def urachamiana jest w czasie wykonania 
if test():
    def func()   # ----> Zdefiniowanie funkcji w taki sposob

else test2():
    def func()   # -----> Albo w taki sposob 

fync()   # ----> Wywolanie wybranej i zbudowanej wersji 


# Definicja 
def times(x, y):   # ----> Utworzenie i przypisanie funkcji 
    return x * y   # ----> Cialo fukcji wykonywane po wywolaniu

# Jak teraz napiszemy tak kod bedzie pamietac funkcje def 
times(2, 4) # -----> Wynnik 8 

x = times(3.14, 4) # ----> Zapisanie obiektu wyniku 
x # Pokaze wynnik 12.56 

times('Ni', 4)  # ----> Dla funkcji typ nie ma znaczenia 
# 'NiNiNiNi'


# Funkcja def i w wniej zagniezdona funlcka for oraz if 
# 1. Umieszczenie kodu w funkcji sprawia ze uzyskujemy narzedzie ktore mozna wykonac tyle razy ile nam bedzie sie chcialo 
# 2. Umieszczenie funkcji w pliku modulu oznacza ze mozna ja zaimportowac i ni uzyc jej ponownie w dowolnym programie dzialajacym na naszym komputerze 
def intersect(seq1, seq2):      #  ----->  def i dwa dane
    res = []                    #  -----> Na poczatek pusta lista 
    for x in seq1:              #  -----> Przeszukanie pierwszej sekwencji 
        if x in seq2:           #  -----> Powtarzajacy sie element 
            res.append(x)       #  ----->  Dodanie na koncu listy wynikow 
    return res                  #  ----->  Sprawdzanie wynikow  

# res jest przepisany w jawny sposib dla tego jest lokalna jak rowniez i seq1 i seq2 nazwa x rowniez jest lokalna 
# petla for przepisuje elemnty do zmiennej lokalnej x 

# Wywolania 
s1 = "mielonka"
s2 = "biedronka"

intersect(s1, s2) # Lancuchy znakow 
# ['', '',....'']    # Wspolne literki wyswietli z tych dwoch slow 
# Ta funkcje mozna zastapic prostym wyrazeniem listy skladanej zeby kod dziawal szybciej 
[x for x in s1 if x in s2]  # -----> To samo 

# Polimorfizm nie ten co w kursie oop
# intersect  -----> Pracujemy caly czas z tym co napsalismy z funkcja def if i for 
x = intersect([1, 2, 3], (1, 4)) 
x # ----> 1 
# Dziala rowniez jak na listach z  lancuchem . Funkcja bedzie dziawala na dwoch dowolnych obietkach bez wzgledu na ich typ obejmuje to sekwencje przechowywane fizycznie w pamieci jak i rozniez list i lancuch 

# def 
# 1. Nazwy przisane wewnatrz instrukcji def moga byc widoczne jedynie dla kodu wewnatrz tej instrukcji. Nie mozna sie do nich odnosic w zaden sposob poza ta funkcja 
# 2. Nazwy przypisane wewnatrrz instrukcji def nie wchodza w konflikt ze zmiennymi sposa tej instrukcji nawet jesli tak samo sie nazywaja .Zmienna x przypisana poza definicja funkcji(
# np w innej definicji funkcji lub na najwyzszym poziomie pliku modulu jest czyms zupelnie innym od zmiennej x przypisanej w tej funkcji )

# Zmienne mozna przepisywac w trzech roznych miejscach odpowiadajacym trzem roznym zasiegom :

# 1.
# Jezelei  zmienna zostanie przypisana wewnatrz funkcji def staje zmienna lokalna dla tej funkjci 
# Zmienna lokalna w Pythonie to zmienna, która została zdefiniowana wewnątrz bloku kodu, np. w funkcji, pętli lub instrukcji warunkowej. Tak zdefiniowana zmienna jest dostępna tylko wewnątrz bloku, w którym została zdefiniowana, i nie jest widoczna poza tym blokiem.
def foo():
    x = 5 # zmienna lokalna
    print(x)

foo()
# Output: 5
# W tym przykładzie tworzymy funkcję foo, w której definiujemy zmienną lokalną x i przypisujemy jej wartość 5. Następnie wywołujemy funkcję i otrzymujemy wynik 5. Warto zauważyć, że zmienna x jest widoczna tylko wewnątrz funkcji foo i nie jest dostępna poza nią.
# W przypadku gdy próbujemy odwołać się do zmiennej lokalnej spoza jej bloku, Python zwróci błąd. Przykład:
def foo():
    x = 5 # zmienna lokalna

foo()
print(x)
# Output: NameError: name 'x' is not defined
# BLAD ponieważ zmienna x nie jest widoczna poza blokiem kodu, w którym została zdefiniowana.

# 2.
# Jezeli zmienna przypisana jest wewnatrz instrukcji def zawierajacej inna funkcje staje sie zmienna nielokalna dle tej funkci
# Zmienna nielokalna w Pythonie to zmienna, która jest zdefiniowana w zewnętrznym bloku kodu (np. w funkcji nadrzędnej) i jest używana w bloku kodu wewnętrznego (np. w funkcji podrzędnej).
# W przypadku gdy chcemy odwołać się do zmiennej zdefiniowanej w bloku kodu zewnętrznego, musimy użyć słowa kluczowego nonlocal. Dzięki temu, Python wie, że chodzi nam o zmienną spoza bloku wewnętrznego.
def zewnetrzna():
    x = 5 # zmienna lokalna w zewnętrznym bloku
    def wewnetrzna():
        nonlocal x # deklarujemy x jako nielokalną
        x += 1 # modyfikujemy wartość x
        print(x)
    wewnetrzna()

zewnetrzna()
# Output: 6
# W tym przykładzie, tworzymy funkcję zewnętrzną zewnetrzna, która zawiera zmienną lokalną x o wartości 5. Następnie definiujemy funkcję wewnętrzną wewnetrzna, która używa zmiennej x z funkcji zewnętrznej. Za pomocą słowa kluczowego nonlocal deklarujemy, że chcemy użyć zmiennej x z bloku zewnętrznego. Następnie zwiększamy wartość x o 1 i drukujemy wynik. Wywołanie funkcji zewnetrzna() spowoduje wykonanie funkcji wewnetrzna(), która zmieni wartość x z 5 na 6 i wydrukuje wynik.
# Warto zauważyć, że zmiana wartości zmiennej nielokalnej jest możliwa tylko w funkcji podrzędnej, a nie w funkcji zewnętrznej. Jeśli chcielibyśmy zmienić wartość zmiennej z zewnątrz, musimy użyć innego rodzaju zmiennej, np. zmiennej globalnej.


# 3.
#  Jezeli zmienna przypisana jest poza wszystkii instrukcjami def, staje sie zmienna globalna dla calego pliku 
# bZmienna globalna to zmienna zdefiniowana w najwyższym poziomie kodu, która jest dostępna we wszystkich częściach programu. Zmienna ta może być modyfikowana w dowolnym miejscu programu, co może wpłynąć na działanie całego programu.
x = 10  # zmienna globalna

def foo():
    print(x)

def bar():
    x = 20  # zmienna lokalna, przesłania globalną
    print(x)

foo()  # wynik: 10
bar()  # wynik: 20
foo()  # wynik: 10 (globalna zmienna x nie została zmodyfikowana)
# W powyższym przykładzie zmienna x zdefiniowana na najwyższym poziomie kodu jest zmienną globalną i jest dostępna zarówno w funkcji foo jak i bar. W funkcji bar zmienna x jest przesłonięta przez zmienną lokalną o tej samej nazwie, jednak poza tą funkcją zmienna globalna x pozostaje niezmieniona


# Reguła LEGB to zasada określająca kolejność wyszukiwania nazw zmiennych w Pythonie. Nazwa zmiennej jest poszukiwana w czterech obszarach:
# L (Local) - lokalny zakres - nazwy zmiennych zdefiniowane wewnątrz bieżącej funkcji lub metody.
# E (Enclosing) - zagnieżdżony zakres - nazwy zmiennych zdefiniowane wewnątrz funkcji lub metod otaczających bieżącą funkcję lub metodę (takich jak funkcje zagnieżdżone lub lambda).
# G (Global) - zakres globalny - nazwy zmiennych zdefiniowane na najwyższym poziomie modułu, do którego należy bieżący kod.
# B (Built-in) - zakres wbudowany - nazwy zmiennych wbudowanych w Pythonie, takie jak funkcje wbudowane i wyjątki.
# Kolejność poszukiwania nazw to L -> E -> G -> B. Jeśli nazwa nie zostanie znaleziona w żadnym z tych obszarów, Python zgłosi błąd NameError.

x = 'globalna'

def funkcja1():
    x = 'lokalna'
    print('funkcja1:', x)

    def funkcja2():
        x = 'zagnieżdżona'
        print('funkcja2:', x)

        def funkcja3():
            print('funkcja3:', x)

        funkcja3()

    funkcja2()

funkcja1()
print('global:', x)

#W tym przykładzie zmienna x ma różne wartości w różnych zakresach. W funkcji funkcja3, wartość x jest szukana najpierw w lokalnym zakresie funkcji funkcja3, następnie w zagnieżdżonym zakresie funkcji funkcja2, a na końcu w globalnym zakresie modułu. Wynik działania tego kodu to:
# funkcja1: lokalna
# funkcja2: zagnieżdżona
# funkcja3: zagnieżdżona
# global: globalna
# Jak widać, zmienna x ma różne wartości w różnych zakresach.

X = 88 # ---> zmienna globalna 
def func():
    global X   # ----> zmienna globalna x poza def    
    X = 99 
func()
print(X)  # Wyswietla 99 

# Oba X wskazuja na jedna i ta sama zmienna , stad zmiana wartosci zmiennej X wewnatrz funkcji zmienia rowniez wartosc X na zewnatrz tej funkcji 
# Troche bardziej skomplikowany przyklad GLOBAL 
y, z = 1, 2    # ----> zmienne globalne w module 
def all_global():
    global x      # Deklaracja zmiennych globalnych 
    x = y + z     # Nie trzeba przepisywac y i z ---> dziala regula LEGB 



# Projektowanie pragramow : minimalizowanie modyfikacji dokonywanych pomiedzy plikami 

# Plik first.py
X = 99

# Plik second.py
import first 
print(first.X)    # Ok: referencja do zmiennej w innym pliku 
first.X = 88      # Zmodyfikowanie jej moze byc zbyt subtelne i niejawne 

# Plik first.py 

X = 99 
def setX(new):    # Funkcja akcesora powoduje ze wprowadzone zmiany sa jawne 
    global X      # i pozwala na zarzadzanie dostepem z jednego miejsca 
    X = new 

# Plik second.py
import first
first.setX(88)  # Wywolanie funkcji zamiast bezposredniej zmiany wartosci

# Inne metody dostepu do zmiennych globalnych 
# Mozemy emuowac instrukcje global importujac modul ja zawierajacy i przypisujac wartosci do jego atrybutow 

# plik thismod.py
var = 99           # -----> zmienna globalna == atrybut modulu

def local():       # -----> Modyfikacja zmiennej lokalnej var
    var = 0 

def glob1():
    global var     # -----> Deklaracja zmiennej globalnej (normalnej)
    var +=1        # Modyfikacja zmiennej globalnej var

def glob2():
    var = 0                 # -----> Modyfikacja zmiennej lokalnej var
    import thismod          # Zaimportowanie siebie 
    thismod.var += 1        # Modyfikacja zmiennej globalnej var

def glob3():
    var = 0                                     # -----> Modyfikacja zmiennej lokalnej var
    import sys                                  # Zaimportowanie tabeli systemowej   
    import sysglob = sys.modules['thismod']     # Pobranie obiektu modulu (mozna tez uzyc __name__)
    glob.var += 1                               # Modyfikacja zmiennej globalnej var

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)
# Po wykonaniu tego kodu do zmiennej globalnej dodano 3 (jedynie pierwsza funkcja nie ma wplywu na te zmienna)
import thismod
thismod.test()
# 99 
# 102 
thismod.var 
# 102 

# kontynuacja def
# Podstawy dopasowywania argumentow 


# 1. podstawy dopasowywania argumentów pozycyjne w Python ----> pozycyjne 
# Dopasowywanie argumentów pozycyjnych w Pythonie polega na przekazywaniu argumentów do funkcji w oparciu o ich kolejność. Argumenty przekazywane są w kolejności, w jakiej są zdefiniowane w definicji funkcji. Poniżej przedstawione są podstawy dopasowywania argumentów pozycyjnych w Pythonie:
def my_function(arg1, arg2, arg3):
    # kod funkcji

# W powyższym przykładzie definiujemy funkcję my_function, która przyjmuje trzy argumenty pozycyjne - arg1, arg2, arg3.
# Wywoływanie funkcji z argumentami pozycyjnymi:
my_function('argument 1', 'argument 2', 'argument 3')
# W powyższym przykładzie wywołujemy funkcję my_function z trzema argumentami pozycyjnymi - 'argument 1', 'argument 2', 'argument 3'. Argumenty te zostaną przypisane do odpowiednich argumentów funkcji na podstawie ich kolejności

# Przekazywanie argumentów pozycyjnych z listy lub krotki:
args = ['argument 1', 'argument 2', 'argument 3']
my_function(*args)
# W powyższym przykładzie tworzymy listę args, zawierającą trzy argumenty pozycyjne. Następnie wywołujemy funkcję my_function, przekazując argumenty z listy do funkcji za pomocą operatora *. To oznacza, że argumenty z listy zostaną przypisane do odpowiednich argumentów funkcji na podstawie ich kolejności.

# Przekazywanie argumentów pozycyjnych z krotki:
args = ('argument 1', 'argument 2', 'argument 3')
my_function(*args)
# W powyższym przykładzie tworzymy krotkę args, zawierającą trzy argumenty pozycyjne. Następnie wywołujemy funkcję my_function, przekazując argumenty z krotki do funkcji za pomocą operatora *. To oznacza, że argumenty z krotki zostaną przypisane do odpowiednich argumentów funkcji na podstawie ich kolejności.

# Błąd podczas wywoływania funkcji z niewłaściwą liczbą argumentów:
my_function('argument 1', 'argument 2')
# Jeśli podczas wywoływania funkcji przekażemy niewłaściwą liczbę argumentów, to Python zgłosi błąd i przerwie wykonywanie programu. W powyższym przykładzie wywołujemy funkcję my_function z dwoma argumentami, podczas gdy funkcja ta wymaga trzech argumentów.



# 2. podstawy dopasowywania argumentów Słowa kluczowe po nazwie argumentow w Python ----> Slowa kluczowe 
# Dopasowywanie argumentów słów kluczowych w Pythonie polega na przekazywaniu argumentów do funkcji w oparciu o ich nazwy, a nie ich kolejność. Argumenty te są definiowane w wywołaniu funkcji jako pary nazwa-wartość. Poniżej przedstawione są podstawy dopasowywania argumentów słów kluczowych w Pythonie:
# Definiowanie funkcji z argumentami słów kluczowych:
def my_function(arg1, arg2, arg3):
    # kod funkcji

# Wywoływanie funkcji z argumentami słów kluczowych:
my_function(arg1='value 1', arg2='value 2', arg3='value 3')
# W powyższym przykładzie wywołujemy funkcję my_function z trzema argumentami słów kluczowych - arg1, arg2, arg3. Każdy argument przekazywany jest w postaci pary nazwa-wartość.

# Przekazywanie argumentów słów kluczowych z słownika:
kwargs = {'arg1': 'value 1', 'arg2': 'value 2', 'arg3': 'value 3'}
my_function(**kwargs)
# W powyższym przykładzie tworzymy słownik kwargs, zawierający trzy argumenty słów kluczowych. Następnie wywołujemy funkcję my_function, przekazując argumenty z słownika do funkcji za pomocą operatora **. To oznacza, że argumenty z słownika zostaną przypisane do odpowiednich argumentów funkcji na podstawie ich nazw.

# Przekazywanie argumentów słów kluczowych z jednoczesnym przekazywaniem argumentów pozycyjnych:
my_function('value 1', arg3='value 3', arg2='value 2')
# W powyższym przykładzie przekazujemy pierwszy argument pozycyjny do funkcji my_function oraz dwa argumenty słów kluczowych - arg3 i arg2. Kolejność argumentów nie ma znaczenia, ponieważ argumenty słów kluczowych przekazywane są w postaci par nazwa-wartość.

# Domyślne wartości argumentów:
def my_function(arg1, arg2='default value', arg3='default value'):
    # kod funkcji
# W powyższym przykładzie definiujemy funkcję my_function, która przyjmuje trzy argumenty, z czego dwa mają domyślne wartości. Argumenty arg2 i arg3 mają domyślne wartości 'default value', co oznacza, że jeśli nie zostaną one przekazane podczas wywoływania funkcji, to zostaną one ustawione na wartość domyślną.



# 3. podstawy dopasowywania argumentów wartości domyślne określenie wartości dla argumentów opcjonalnych  w Python ----> Wartosci domyslne 
# W Pythonie wartości domyślne dla argumentów opcjonalnych w funkcji definiuje się w momencie jej tworzenia. W przypadku, gdy wartość dla danego argumentu nie zostanie podana przy wywołaniu funkcji, to zostanie użyta wartość domyślna.

#Poniżej przedstawiamy przykład definiowania funkcji z wartościami domyślnymi argumentów opcjonalnych:
def my_function(arg1, arg2=0, arg3=3.14):
    print(f"arg1={arg1}, arg2={arg2}, arg3={arg3}")
# W powyższym przykładzie definiujemy funkcję my_function, która przyjmuje trzy argumenty, z czego dwa (arg2 i arg3) są opcjonalne i mają wartości domyślne. Jeśli podczas wywołania funkcji zostanie podana tylko wartość dla argumentu arg1, to pozostałe argumenty przyjmą wartości domyślne.

# Przykłady wywołań funkcji:
my_function(1)  # arg1=1, arg2=0, arg3=3.14
my_function(1, 2)  # arg1=1, arg2=2, arg3=3.14
my_function(1, arg3=4.2)  # arg1=1, arg2=0, arg3=4.2
# Warto zauważyć, że wartości domyślne dla argumentów opcjonalnych są przypisywane tylko raz, w momencie tworzenia funkcji. Dlatego, jeśli wartość domyślna jest obiektem zmienialnym (np. lista, słownik), to wartość ta będzie współdzielona przez wszystkie wywołania funkcji. Może to prowadzić do nieoczekiwanych wyników. Aby temu zapobiec, wartości domyślne dla argumentów opcjonalnych powinny być obiektami niemodyfikowalnymi, takimi jak liczby czy ciągi znaków.



# 4. podstawy dopasowywania argumentów zmienna liczba argumentów (zbieranie) przekazywanie dowolnej liczby argumentów  w Python ----> Zmienna liczba argumentow zbieranie
# W Pythonie możliwe jest przekazywanie dowolnej liczby argumentów do funkcji, wykorzystując mechanizm "zbierania" argumentów. W zależności od potrzeb, możemy zebrać argumenty pozycyjne lub nazwane (słownikowe).

# Zbieranie argumentów pozycyjnych:
# Aby zebrać dowolną liczbę argumentów pozycyjnych, używamy gwiazdki * przed nazwą zmiennej. Argumenty zostaną przekazane do funkcji jako krotka.
# Przykład:
def my_function(*args):
    for arg in args:
        print(arg)
# W powyższym przykładzie definiujemy funkcję my_function, która może przyjąć dowolną liczbę argumentów pozycyjnych. Argumenty są zbierane do krotki o nazwie args. W tym przypadku, funkcja wyświetli wartości wszystkich argumentów.

# Zbieranie argumentów nazwanych (słownikowych):
# Aby zebrać dowolną liczbę argumentów nazwanych, używamy podwójnej gwiazdki ** przed nazwą zmiennej. Argumenty zostaną przekazane do funkcji jako słownik, gdzie kluczami będą nazwy argumentów, a wartościami ich wartości.
# Przykład:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
#  powyższym przykładzie definiujemy funkcję my_function, która może przyjąć dowolną liczbę argumentów nazwanych. Argumenty są zbierane do słownika o nazwie kwargs. W tym przypadku, funkcja wyświetli nazwy i wartości wszystkich argumentów.

# Kombinacja zbierania argumentów pozycyjnych i nazwanych:
# Możliwe jest również łączenie zbierania argumentów pozycyjnych i nazwanych w jednej funkcji. W takim przypadku, gwiazdka * służy do zbierania argumentów pozycyjnych, a podwójna gwiazdka ** służy do zbierania argumentów nazwanych.
# Przykład:
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")
# W powyższym przykładzie definiujemy funkcję my_function, która może przyjąć dowolną liczbę argumentów pozycyjnych i nazwanych. Argumenty pozycyjne są zbierane do krotki args, a argumenty nazwane do słownika kwargs. W tym przypadku, funkcja wyświetli wartości wszystkich argumentów pozycyjnych oraz nazwy i wartości wszystkich argumentów nazwanych.



# 5. podstawy dopasowywania argumentów zmienna liczba argumentó\w (rozpakowywanie) przekazywanie dowolnej liczby argumentów zgodnie z pozycja  w Python ----> rozpakowywanie
# Rozpakowywanie argumentów pozycyjnych:
# Jeśli mamy już gotową krotkę lub listę wartości, które chcemy przekazać jako argumenty pozycyjne do funkcji, możemy je "rozpakować" za pomocą gwiazdki * przed nazwą krotki lub listy. W ten sposób wartości zostaną przekazane do funkcji jako osobne argumenty pozycyjne.
# Przykład:
def my_function(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
my_function(*args)
#  powyższym przykładzie definiujemy funkcję my_function, która przyjmuje trzy argumenty pozycyjne. Następnie definiujemy krotkę args z trzema wartościami. W momencie wywoływania funkcji my_function, używamy gwiazdki przed krotką, aby rozpakować wartości i przekazać je jako osobne argumenty. W ten sposób, funkcja wyświetli wartości 1 2 3.
#  Rozpakowywanie argumentów nazwanych:
# Podobnie jak w przypadku argumentów pozycyjnych, możemy "rozpakować" słownik z wartościami, które chcemy przekazać jako argumenty nazwane do funkcji. W tym celu, używamy podwójnej gwiazdki ** przed nazwą słownika. Klucze słownika muszą odpowiadać nazwom argumentów funkcji.
# Przykład:
def my_function(a, b, c):
    print(a, b, c)

kwargs = {'a': 1, 'b': 2, 'c': 3}
my_function(**kwargs)
# W powyższym przykładzie definiujemy funkcję my_function, która przyjmuje trzy argumenty nazwane. Następnie definiujemy słownik kwargs z trzema kluczami odpowiadającymi nazwom argumentów funkcji. W momencie wywoływania funkcji my_function, używamy podwójnej gwiazdki przed słownikiem, aby rozpakować wartości i przekazać je jako osobne argumenty nazwane. W ten sposób, funkcja wyświetli wartości 1 2 3.



# 6. podstawy dopasowywania argumentów będące słowami kluczowymi argumenty które muszą być przekazane przez nazwę  w Python ---> Argumenty przkazane przez nazwe 

# W Pythonie można definiować argumenty, które muszą być przekazywane do funkcji za pomocą słów kluczowych i nazw. Takie argumenty nazywają się argumentami słownikowymi (keyword arguments).
# Aby zdefiniować argument słownikowy, należy podać jego nazwę w definicji funkcji i poprzedzić go znakiem **. W ten sposób argument zostanie traktowany jako słownik, do którego można przekazywać wartości za pomocą słów kluczowych.
# Przykład:
def my_function(a, b, **kwargs):
    print(a, b)
    print(kwargs)

my_function(a=1, b=2, c=3, d=4)
# W powyższym przykładzie definiujemy funkcję my_function, która przyjmuje dwa argumenty pozycyjne a i b, oraz dodatkowe argumenty przekazywane przez słowa kluczowe. Wewnątrz funkcji używamy zmiennej kwargs do odwoływania się do słownika, który zawiera przekazane argumenty słownikowe.
# W momencie wywoływania funkcji, przekazujemy wartości do argumentów słownikowych za pomocą słów kluczowych. W powyższym przykładzie przekazujemy wartości c=3 i d=4. Funkcja wyświetli wartości 1 2 dla argumentów pozycyjnych oraz słownik {'c': 3, 'd': 4} dla argumentów słownikowych.


# Uzycie form *obiekt_iterowalny lub **slownik pokujemy wszystko do srodka tygo 

func(wartosc)  #  ---> wywolujacy ---> normalny argument -- dopasowanie po pozcji 
func(nazwa=wartosc) # Wywolujacy  ---> Slowo kluczowe dopasowanie po nazwie 
func(*obiket_iterowalny) # wywolujacy  ----> Przekazanie wszystkich obiektow iterowalnych jako pojedynczych argumentow pozycyjnych 
func(**slownk) # Wywolujacy ---> Przekazanie wszystkich par klucz-wartosc ze slownika jako pojedynczych argumentow slow kluczowych 
def func(nazwa) # Funkcja ---> Normalny argument - dopasowuje przekazane wartosci po pozycji lub nazwie
def func(nazwa=wartosc) # Funkcja ---> Domysla wartosc argumentow wykorzystana jesli wartosc nie zostala przekazana w wywolaniu
def func(*nazwa) # Funcka ---> Dopasowanie i zbiera pozostale argumenty pozycyjne (w krotce)
def func(**nazwa) # # Funcka ---> Dopasowanie i zbiera pozostale argumenty pozycyjne (w swolniku)
def (*argumenty,nazwa) # Funkcja ---> Argumenty , ktore wywolaniu musza byc przekazane za pomoca slowa kluczowego 
def func(*, nazwa=wartosc) # Funkcja ---> Argumenty ktore w wywolaniu musza byc przekazane za pomoca slowa kluczowego 

def f(a, b=2,c=3): print(a,b,c) # a to argument wymagany b i c sa opcjanalne 
f(1) # 1 2 3               # Uzywamy wartosci domyslnych 
f(a=1) # 1 2 3 
f(1,4) #1 4 5              # Nadpisanie wartosci domyslnych 
f(1,4,5) # 1 4 5
f(1,c=6) # 1 2 6           # Wybieranie wartosci domyslnych 
######################################################################################################
# 31. Kurs Python 3 - Klasy - właściwości (getter, setter)
class KontoBankowe:
    __stan = 0

    def stan_konta(self):
        return self.__stan
    
konto = KontoBankowe()
print(konto.stan_konta())


class KontoBankowe:
    __stan = 0
    
    @property
    def stan_konta(self):
        return self.__stan
    
konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)


class KontoBankowe:
    __stan = 0
    
    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        return "Stan konta: " + str(self.__stan) + "zl" # Stan konta: 0zl
    
    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value
    
konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)
# # Stan konta: 0zl
# # Stan konta: 50zl
konto.stan_konta = 100
print(konto.stan_konta)
# # Stan konta: 150zl 
konto.stan_konta = -150
print(konto.stan_konta)
# # Stan konta: 0




# 30. Kurs Python 3 - Klasy - metody klas oraz statyczne
class Czlowiek:
    
    def __init__(self, imie):
        self.imie = imie
    
    def przedstaw(self):
        print("Nazywam sie " + self.imie) 

    def nowy_czlowiek 

Czlowiek.predstaw()
obj = Czlowiek()
obj.przedstaw()


class Czlowiek:

    
    def __init__(self, imie):
        self.imie = imie
    
    def przedstaw(self):
        print("Nazywam sie " + self.imie) 

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)
    
    @staticmethod
    def przywitaj(arg):
        print("Czesc " + arg)

cz1 = Czlowiek.nowy_czlowiek("Sebastian")
cz1.przedstaw()
# Nazywamy sie Sebastian 

cz2 = cz1.nowy_czlowiek("Adrian")
cz2.przedstaw()
# Czlowiek.przedstaw()
# Nazywam sie Adrian 

Czlowiek.przedstaw("przyjacielu")
# Czesc przyjacielu! 
cz2.przywitaj("czlowieku.")
# Czesc czlowieku.

class Czlowiek:
    def __init__(self, imie):
        self.imie = imie 
    def przedstaw(self):
        print("Nazywa sie " + self.imie)



class Czlowiek: 
def __init__(self,name)
    self.name = imie 
def przedstaw(self):


def Czlowiek:
    dsef __init__ (self, imie:)

# 29. Kurs Python 3 - Klasy - hermetyzacja (ukrywanie danych)
class Test:
    lista = []   # private lista  
    def dodaj(self, arg):
        self.lista.append(arg)
    
    def zdejmij(self):
        if len(self.lista) > 0:
            return self.lista.pop(len(self.lista) -1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
print(obj.zdejmij())
# B
# Process finished with exit code  0
print(obj.lista)
# ['A']

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj.zdejmij())
# C
# Process finished with exit code  0
print(obj.lista)
# ['A', 'B']

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj.lista.append("X")
print(obj.zdejmij())
# X
# Process finished with exit code  0
print(obj.lista)
# ['A', 'B', 'C']


class Test:
    _lista = []   # private lista  
    def dodaj(self, arg):
        self._lista.append(arg)
    
    def zdejmij(self):
        if len(self.lista) > 0:
            return self._lista.pop(len(self._lista) -1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._lista.append("X")
print(obj.zdejmij())
print(obj._lista)
obj.lista.remove


class Test:
    __lista = []   # private lista  
    def dodaj(self, arg):
        self.__lista.append(arg)
    
    def zdejmij(self):
        if len(self.lista) > 0:
            return self.__lista.pop(len(self.__lista) -1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj.Test__lista.append("X")
print(obj.zdejmij())
print(obj.Test_lista)
# X
# ['A', 'B', 'C']


# 28. Kurs Python 3 - Klasy - cykl życia (destruktor)
class Test:
    def __new__(cls):
        print("Hello Class")

obj = Test()


class Test:
    def __del__(self):
        print("Bye Class")

obj = Test()
print("Koniec")
# Koniec 
# Bye Class


obj = Test()
del obj
# Bye Class
# Koniec 


obj = Test()
obj2 = obj
del obj
# Koniec 
# Bye Class


obj = Test()
obj2 = obj
lista = [obj2]
del obj
del obj2
del lista[0]
# Koniec 
# Bye Class


# 27. Kurs Python 3 - Klasy - magiczne metody
import math

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.odleglosc = math.sqrt(x**2 + y**2)
    
    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)

    def __lt__(self, drugi):
        return self.odleglosc < drugi.odleglosc
    
    def __eq__(self, drugi):
        return self.x == drugi.x  self.y == drugi.y

    def __len__(self):
#        return self.odleglosc
        return int(round(self.odleglosc, 0))
    
p1 = Punkt(2, 5)
p2 = Punkt(4, 5)
# p3 = p1 + p2 -----> blad dla tego piszemy drugie def 
p3 = p1 + p2 
# Process finished with exit code 0 

print(p3.x)
print(p3.y)
print(p1 < p2)
# 6 
# 10
# True

print(p1.odleglosc)
print(p2.odleglosc)
# 5.385135342424
# 6.40424342342324
# False

print(p1 == p2)
# False
print(p2 == p2)
# True

print(len(p3))
print(p3.odleglosc)
# 12
# 11.6623824872494297



# 26. Kurs Python 3 - Klasy - dziedziczenie
class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

class Dog(Animal):
    def voice(self):
        print("How How")

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")

class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem")
        super().voice()

dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
# Reksio 
# 10
dog.voice()
# How How 

cat = Cat("Bury", 8)
cat.getVoice()
# Meow Meow

wolf = Wolf("Geralt", 55)
wolf.getVoice()
# Jestem wilkiem, 
# How How 

wolf = Wolf("Geralt", 55)
wolf.getVoice()
print(wilf.name)
# Geralt


# 25. Kurs Python 3 - Klasy i Obiekty (OOP)
class Czlowiek:
    imie = "Sebiastian"

    def przedstawSie (self):
    #   self.imie = 
        return "Czesc, mam na imie " + self.imie
    # def przedstawSie(abc):
    #   abc.imie =


obiekt = Czlowiek()

print(obiekt.imie)
# Sebastian 

print(obiekt.przedstawSie())
# Czesc, mam na imie Sebastian 

obiekt2 = Czlowiek()
obiekt2.imie = "Adrian"
print(obiekt.przedstawSie())
# Czesc mam na imie Adrian 
print(obiekt.przedstawSie())
# Czesc, mam na imie Sebastian 


class Czlowiek:
    imie = "Sebiastian"

    def przedstawSie (self, powitanie = "Czesc"):
        return powitanie + ", mam na imie " + self.imie


obiekt = Czlowiek()
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))
# Witam, mam na imie Sebastian 

obiekt2 = Czlowiek()
obiekt2.imie = "Adrian"
print(obiekt.przedstawSie())
# Czesc, mam na imie Adrian


class Czlowiek:
    
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    
    def przedstawSie (self, powitanie = "Czesc"):
        return powitanie + ", mam na imie " + self.imie + "lat" + str(self.wiek) + " . "


obiekt = Czlowiek("Sebastian", 24)
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))
# Witam, mam na imie Sebastian lat 24

obiekt2 = Czlowiek("Adrian" , 18)
obiekt2.imie = "Adrian"
print(obiekt.przedstawSie())
# Czesc, mam na imie Adrian lat 18

####################################################################
L = [1,2,3,4,5]
for i in range(len(L)):
    L[i] += 10
L
# [11, 12, 13, 14, 15] 


L  = [x + 10 for x in L]
L 
# [21, 22, 23, 24, 25]


L = [x + 10 for x in L]


res = []
for x in L :
    res.append(x + 10)
res
# [31, 32, 33, 34, 35]



####################################################################

# 24. Kurs Python 3 - zbiory (sets) - operacje na zbiorach
liczby1 = {0, 1, 2, 4}
slowa = set(["a", "b", "c"])

print(liczby1)  # {0, 1, 2, 4}
print(slowa)  #  {"a", "b", "c"}

liczby1.add(5)  # {0, 1, 2, 4, 5}
print(liczby1)
liczby1.remove(0)
print(liczby1)  # {1, 2, 4, 5}

liczby1.add(5)
print(liczby1)  # {1, 2, 4, 5}

print(1 in liczby1)  # True
print("a" in liczby1)  # False

liczby1 = {0, 1, 2, 3, 4}
liczby2 = {3, 4, 5, 6}

print(liczby1 | liczby2)  # # {0, 1, 2, 4, 5, 6}

############################################################################
f  = open('script2.py')
lines = f.readlines()
lines 
# ['import sys\n , 'print (sys.path)\n', 'x = 2\n' , ' print (2 ** 32) \n']

# Pozbyc sie sie balych zakow rstrip() albo line[:-1] takie jak \n znak nowego iwrsza 
lines = [line.rstrip() for line in lines]
lines 

lines = [line.rstrip() for line in open('script2.py')]
lines 

[line.upper() for line in open('script2.py')]
[line.rstrip() for line in open ('script2.py') ]
[line.replace(' ', !)  for line in open ('script2.py')]
[('sys' in line, line[0]) for line in open ('script2.py')]

############################################################################
# 23. Kurs Python 3 - dekoratory

def decorator(func):   # wysylamy jeden argument gdzie postac segnatury fukncji 
    def wrapper():     # obwednia , otoczka  ------> opakowanie np prezentu jeszcze inna funkcje 
        print (" --------- ")    # opakowujemy tylko trekst , otwierac polaczenia z baza dantch a pozniej zamykac 
# to co ma raboc wrapper to tylko linijke ------- do gory i na dole i w srodku dynamiczne postac dzialania fukcji  func
        func()  # operacje ktore wykonujemy na bazie danych 
        print(" --------- ")     # zamkniecie bazy danych czy np adapt usera 
    return wrapper # to co chcemy zrwocic to wlasnie nasze opakowanie bez () bo nie chcemy otwierac wrapper , zwracamy funkcje wrapper
# return zwracanie nowej postaci wrapper 
# print( ------ ) przed i po musi byc stale 

def hello(): # funcja hello ktora wypisuje tekst na ekranie konsoli hello world
    print("Hello World")

hello2 = decorator(hello) # dla innej zmiennnej , spelni nowa funcje hello2
hello2()

hello = decorator (hello) # bedzie napisane hello world
# zaczynamy od pisania nazwy chcemy nadpisac jej dzialanie bez () a = i wstawiamy nazwe dekorqatora ktorego uzywamy funkcji zewnetrznej wpisujemy decorator bo def decorator(func
# i to co bedzue w func to zostanie wylowane w wrepper
# argument w func () bedzie srodkiem naszego opakowania 

hello() # jak wylowawamy funckcje hello wypisze nam hello world

@decorator # funkcja musi byc udekorowana i tu nalezy podac tylko nazwe dekoratora ktora chcemy przepisac do funkcji witam
# wwszystko co ponizej bedzie udekorowane 
def witaj():
    print("witaj swiecie")
witaj()
#  --------
#  Witaj Swiecie
#  --------

# jak bedzie zwykle hello()
# wyskoczy bez tego ------
# Hello World

############################################################################
# 22. Kurs Python 3 - generatory (yield)

def gen ():
    i = 0
    while i < 5: # od 0 do 4
        yield i   # nie przerywa dzialania funkcji moze sie wykonac wile razy w funkcji niz return 
        # return i  ----> konczy nam funkcje 
        i += 1
print(gen()) # zwrac TYLKO JEDNA WARTOSC gen() 
# wyswietlono 0 
# <generator object gen at 0x043244243> wynnik 0 jest przechowywany jakis objekt


for i in gen(): # generator mozna wykorzystywac jako obiekt generowania petli obiektowej 
    print(i) # Wyswietli sie wartosc od 0 do 4 w dol 

print(list(gen())) # w nawisach kwadratowych lista

############################################################################
# 21. Kurs Python 3 - mapa i filtr (map & filter)
liczby = [2, 10, 2, 15, 20, 30, 35]

# Mapy zaimplementowana funkcja o nazwie pam
# najpierw trzeba w pierwszym argumencie podaj funkcje i uzyc yield
def funkcja(x):
    return x * 2

wynik = map(funkcja, liczby) # wymaga podania funkcji z jednej funkcji map w druga
# 2 argument liczby na kazda z nich jest operacja przeslania , kazdy element naszej funkcji * 2
print(list(wynik)) 
# wszystkie dane wyswietli w liscie * 2

wynik2 = map(lambda x: x + 2, liczby) # drugi argument pewna kolekcja 
print(list(wynik2))

wynik3 = filter(lambda x: x  % 2 == 0, liczby) # przyjmuje kolekcje jedyna ktora tutaj posiadamy 
# x: -----> liczby po kolei
# czy przeprowaadzony test jest true czy false 
# dzielenie z resta x % 2
# czy warosc jest parzysta 
# == 0 kazda funkcja lambda zwracalo finkcje trrue lub false 
print(list(wynik3))
# 2 10 12 20 30
# jest ograniczona tylko do 5 elementow lambda czy wartosc jest parzysta 

############################################################################
# 20. Kurs Python 3 - funkcje anonimowe (lambda)
def funkcja(f, liczba):
    return f(liczba) 

print(funkcja(lambda x: x * x, 3))

def kwadrat (x):
    return x * x

print(kwadrat(5))

wyn = (lambda x: x * x )(5)
print(wyn)
# 9
# 25
# 25

lam = lambda x: x * x
print(lam(5))  # 25
print(lam(4))  # 16




############################################################################
# ksiazka strona 477 
lines  = (line.rstrip() for line  in open('script2.py') if line[0] == 'p')
lines 
# ['print (sys.path)' , 'print ( 2 ** 32)']

res = []
for line in open('script2.py'):
    if line[0] == 'p':
        res.append(line.rstrip())
res 
# ['print (sys.path)' , 'print (2 ** 32)']

[line.rstrip() for line in open ('script2.py') if line.rstrip() [-1].isdigit()]
# ['x = 2']

fname = r'd:\books\5e\lp5e\draft1typos.txt'
len(open(fname).readlines()) # Wswzystjkie wiersze 
# 263
len ([line for line in open (fname) if line.strip() != ''])   # Wiersze nie puste 

# Ponizszy kod tworzy liste konkatenacji x + y dla kazdego x z jednego lancucha znakow i kazdego y z drugiego. W rezutlacie tworzymy uporzadkowana liste wszystkiech kombinacji znakow z obu lancuchow 
[x + y for x in 'abc' for y in 'lmn']
# ['al', 'am', 'an,'bl','bm','bn','cl','cm','cn']
# TROCHE LATWIEJSZY SPOSOB JEST KONWERSJA DO POSTACI POLECENIA POPRZEZ ODPOWIEDZIE WCIECIE  jego czesci 


sum([3, 2, 4, 1, 5, 0]) # 15
any(['spam', ' ' , 'ni']) # True
all(['spam', ' ', 'ni']) # False 
max([3, 2, 4, 1, 5, 0]) # 5
min([3, 2, 4, 1, 5, ]) # 1


# Specjalna funkcja *arg aby rozpakowaac kolekcje wartosci do postaci poszczegolnych argumentow .Obsluguje dowolne obiekty iterowalne  i pliki 
def f(a, b, c, d): print (a, b, c, d, sep = "&")
f(1, 2, 3, 4) # 1&2&3&4
f(*[1, 2, 3, 4]) # Rozpakowanie listy argumentow # 1&2&3&4
f(*open('script.py'))
# import sys
# &print(sys.path)
# &x = 2
# &print(x ** 32)

# Skladnia akceptuje obiekty iterowalne mozemy uzyc wbudowana funkcje zip do rozpakowania spakwanych krotek lub zagniezdzanie wywolan funkcji zip 
X = (1, 2)
Y = (3, 4)
list(zip(X, Y))   # Pakowanie krotek: zwraca obiekt iterowalny   # [(1, 3), (2, 4)]
A, B = zip(*zip(X, Y)) # Rozpakowaniaa zipa!
A # (1, 2)
B # (3, 4)

# Obbiekt iterowlny range
R = range(10)     # RANGE() zwraca obiket iterowalny a nie liste
R # RANGE(0, 10)
I = iter(R)  # przeksztalcenie obiektu iterowalnego range na iterator
next(I)      # przejscie do nastepnej wartosci
# 0          # petle for rozwiniecie itp wykonuja to w sposob nie jawny 
next(I)
# 1
next(I)
# 2 
list(range(10)) 
# pokaze od 0 do 10

# Obiekty iterowalne map,zip, filter
M = map(abs, (-1, 0 ,1)) # map() zwraca obiekt iterowalny a nie liste 
next(M)
# 1
next(M)
# 0 
next(M)
# 1

for x in M : print(x) # Iterator zwrocony przez funkcje map() jest juz pusty po jednym przejsciu 
M = map(abs, (-1, 0 ,1)) # Ponowna proba wymaga utworzenie nowego obiektu iterowalnego  # oraz iteratora 
for x in M : print(x) # Konteksty iteracyjne automatycznie uwzywaja funkcji next()
# 1
# 0 
# 1
list(map(abs, (-1, 0, 1))) # Iterator mozna przeksztalcic w liste 

Z = zip(1, 2, 3), (10, 20, 30) # zip() dziala tak samo zwraca jednorazowe iteratory
list(Z)
# [(1, 10), (2, 20), (3, 30)]

Z = zip(1, 2, 3), (10, 20, 30)
next(Z) 
# (1, 10)
next(Z)
# (2, 20)

# Zamiast while czy range nalezy uzywac prostych petli for     --->   ( for x in seq: )
# mylist = mylist.append(X) --> otrzymac wynnik zastosowania metody append . Kod ten przypisuje liste mylist do None a nie do zmodyfikowanej listy (i w rezultacie calkowicie  tracimy referencje do listy )




# Strona 547
def maker(N):
    def action(X):         # Utworzenie i zwrocenie funkcji action 
        return X ** N      # Funkcja action zachowuje N z zasiegow funkcji zawierajacej
    return action 

def maker(N):                   # Funkcja lambda rowniez zapamietuja informacje o stanie 
    return lambda x: X ** N 
h = maker(3) 
h(4)   # ponownie 4 ** 3

def f1():
    x = 88
    def f2(x*x):  # Pamieta x z zasiegu funkcji zawierajacej z wartosciami domyslnymi 
        print(x)

def f1():    # Przelazanie x zamiast zagniezdzania 
    X = 88   # Odwowanie z wyprzedzenie jest OK
    F2(X)
def f2(x):   # Plaska struktura jest lepsza niz zagniezdzona 
    print(x)

def func():
    x = 4
    action = (lambda n: x ** n) # x pamieta z zasiegu zawierajacego instrukcje def 
    return action 
x = func()
print(x(2))     # Wyswietla 16 czyli 4 ** 2

def func():
    x = 4
    action = (lambda n, x=x: x ** n)  # Reczne przekazanie x 
    return action 

def makeActions():
    acts = []
    for i in range(5):                   # Probuje zapamietac kazda wartos i 
        acts.append(lambda x: i ** x)    # ..ale wszystkie pamietaja te sama ostatnia wartosc i!
    return acts 
acts = makeActions()
acts[0]
acts[0](2) # wszystkie to 4 ** 2 wartosc ostatniego i = 4
acts[1](2) # Powinno byc 1 ** 2 (1)
acts[2](2) # Powinno byc 2 ** 2 (4)
acts[4](2) # Tylko w tym przypadku wynnik jest poprawny 4 ** 2

def makeActions():
    acts = []
    for i in range(5)                   # Uzycie domyslnej wartosci argumentow 
    acts.append(lambda x, i=i; i ** x)  # Zapamietanie biezacej wartosci zmiennej i
return acts 

acts = makeActions()
acts[0](2) # 0 ** 2
acts[2](2) # 2 ** 2 
acts [4](5)  # 4 ** 5 

def func():
    nonlocal zmienna1, zmienna2   # Tutaj zmienne sa ok 

def tester(start):
    state = start             # Referencja do zmiennej nielokalnej dziala normalnie 
    def nested(label):        
        print(label, state)   # Pamieta stan w zasiegu funkcji zawierajacej 
    return nested
F = tester(0)
F('mielonka')  # mielonka 0
F('szynka') # szynka 0 

def tester(start):
    state = start 
    def nested(label):
        print(label, state)
        state += 1
    return nested
F = tester(0)
F('mielonka')   ###### BLAD 

def tester(start):
    state = start             # Kazde wylowanie otrzymuje wlasna zmienna state
    def nested(label):
        nonlocal state        # Pamieta state z zasiegu funkcji zawierajacej 
        print(label, state)
        state += 1            # Mozna zmienic jesli nonlocal
    return nested
F = tester(0)
F('mielonka')  # mielonka 0
F('szynka')    # szynka 1
F('jajka')     # jajka 2
G = tester(45)
G('mielonka') # mielonka 45 
G('szynka')   # szynka 46

def tester(start):
    def nested(label):
        nonlocal state          # zmienne nonlocal musza juz istniec w zasiegu funkcji zawierajacej 
        state = 0
        print(label, state)
    return nested

def tester(start):
    def nested(label):
        global state        # zmienne globalne nie musza istniec ood czas deklarowania 
        state = 0           # to polecenie tworzy teraz zmienna w module 
        print(label, state)
    return nested 
F = tester(0)
F('aff') # aff 0
state # 0

spam = 99 
def tester():
    def nested():
        nonlocal spam          # Musi byc w instrucji def nie w module 
        print('Aktualna wartosc=', spam)
        spam += 1
    return nested 

def tester (start):
    state = start           # Kazde wywolanie otrzymuje wlasna zmienna stala 
    def nested(label):
        nonlocal state      # Pamieta state z zasiegu funkcji zawierajacej 
        print(label, state)
        state += 1          # Mozna zmienic jesli nonlocal
    return nested 
F = tester(0)
F('mielonka') # spam 0

def tester(start):
    global state            # Przeniesienie do modulu w celu modyfikacji 
    state = start           # zmienne globalne pozwalaja na dokonywanie zmian w modulu
    def nested(label):
        global state 
        print(label, state)
        state += 1
    return nested
F = tester(0)
F('mielonka')   # Mielonka 0
G = tester(42)
G('tost') # tost 42

def tester(start):
    state = start
    def nested(label):
        print(label, state)
        state += 1    # Domyslnie nie moze sie zmienic
    return nested 
F = tester(0)
F('mielonka')

def tester(start):
    state = start              # Kazde wywolanie otrzymuje wlasna zmienna stale 
    def nested(label):
        nonlocal state         # Pamieta state z zasiegu funkcji zawierajacej 
        print(label, state)
        state += 1             # Mozna zmienic jesli nonlocal 
    return nested 
F = tester(0)    # Inkrementacja state z kazdym wywolaniem 
F = ('mielonka') # mielonka 0 
F = ('szynka')   # szynka 1

G = tester(42)  # Utworzenie nowej funkcji tester rozpoczynajacej sie od 42 
G('mieonka')  # mielonka 42 
G('jajka')  # jajka 43 

class Tester:                       # Alternatywa oparta na klasach (patrz czesc 6) 
    def __init__(self, start):      # Przy tworzeniu obiektu stan jest 
        self.state = start          # ...zapisywany w nowym obiekcie w sposob jawny
    def nested(self, label):        # 
        print(label, self.state)    # Jawna referencja do zmiennej state
        self.state += 1             # Modyfikacja jest zawsze dozwolona
F = tester(0)                       # Tworzenie instancji, wywolanie __init__
F.nested('mielonka') # mielonka 0   # F przekazywane jest do self 
F.nested('szynka')  # szynka 1

class tester:
    def __init__(self, start):
        self.state = start 
    def __call__(self, label):      # Przechwycenie bezposrednich wywolan instancji 
        print(label, self.state)    # .nested() nie jest wymagane 
        self.state += 1
H = tester(99)      # Wywolanie metody __call__
H('sok') # sok 99   
H('nalesniki') # nalesniki 100

def tester(start):
    def nested(label):
        print(label, nested.state)      # nested jest w zasiegu funkcji zawierajacej 
        nested.state += 1               # Zmiana atrybutu , a nie samej nested
    nested.state = start                # Poczatkowy stan po zdefiniowaniu funkjci 
    return nested 
F = tester(0)     # F to nested z dolaczonym stanem 
F('mielonka')
F('szynka')       # szynka 1
F.state   # 2 

def tester (start):
    def tester()


def f(*args): print(args)
def f(a, *pargs, **kargs): print(a, pargs, kargs)
f(1, 2, 3, x=1, y=2)
# 1 (2, 3) {'y': 2, 'x': 1}

# Najpierw jednak zobaczmy, co stanie sie kiedy  * oraz ** umieszczone sa w wywolaniach funkcji a nie ich definicjach 
def func(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func(*args)      # To samo co wywolanie func(1, 2, 3, 4)

# ** rozpakowuje slownik par klucz-wartosc na pojedyncze argumenty ze slowami kluczowymi 
args = {'a':1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)   # To samo co wywolanie func(a=1,b=2,c=3,d=4)
# 1 2 3 4

# Wiele sposobow zeby polaczyc normalne argumenty pozycyjne oraz argumenty ze slowami kluczowymi 
func(*(1, 2), **{'d': 4, 'c':4})    # To  samo co wywolanie func(1,2,d=4,c=3)
# 1 2 3 4

func(1, *(2, 3), **{'d':4})     # To samo co wywolanie (1,2,3,d=4)
# 1 2 3 4

func(1, c=3, *(2,), **{'d':4})  # To samo co wywolanie (1,2,c=3,d=4)
# 1 2 3 4

func (1, *(2, 3), d=4)          # To samo co wywolanie (1,2,3,d=4)
# 1 2 3 4

f(1, *(2,), c=3, **{'d':4})     # To samo co wywolanie (1,2,c=3,d=4)
# 1 2 3 4

if dowolnytest:
    action,  args = func1, (1,)   # W tym przypadku wywolanie func1 z 1 argumentem 
else:
    action, args = func2, (1, 2, 3)   # Tutaj wywolanie func2 z 3 argumentami
action(*args)     # Uniswersalne wywolanie 

def kwonly(a, *b, c):
    print(a, b, c)
knowly(1, 2, c=3)
# 1 (2,) 3
knowly(a=1, c=3)
# 1 () 3 
knowly(1,2,3) # Blad nie jest oznaczone c 

def knowly(a, *, b, c):
    print(a,b,c)    # Wszystko po * musi byc oznaczone np b=2 c=3
knowly(1, c=3, b=2)
# 1 2 3 
knowly(c=3,b=2,a=1)
# 1 2 3

def knowly(a, *, b='mielonka', c='szynka'):
    print(a,b,c)
knowly(1)
# 1 mielonka szynka
knowly(1, c=3)
# 1 mielonka 3
knowly (a=1, b=2, c=3)
# 1 2 3
knowly (a=1)
# 1 mielonka szynka



def kwonly(a, *, b, c='mielonka'):
    print(a,b,c)
    kwonly(1, b='jajka')    # Co nie napisze do knowly to musi byc oznaczone b= i cos tam

def kwonly(a, *,b=1,c,d=2):
    print(a,b,c,d)   # c powinno byc oznaczone 
kwonly(3,c=4)
# 3 1 4 2
kwonly(3,c=4,b=5)
# 3 5 4 2


def f(a, *b, **d, c=6): print(a,b,c,d)     # Przed ** tylko argumenty bedace slowami kluczowymi
def f(a, *b, c=6, **d): print(a,b,c,d)     # Zebranie argumentow w naglowku 
f(1, 2, 3, x=4, y=5)    # Uzyte wartosci domyslne 
# 1 (2, 3) 6 {'y':5, 'x':4}
f(1, 2, 3, x=4, y=5, c=7)  # Nadpisanie wartosci domyslnych  # mozemy pisac w dowolnej kolejnosci c a b 
# 1 (2, 3) 7 {'y':5, 'x':4

def f(a, c=6, *b, **d):
    print(a,b,c,d)   # c nie jest argumentem bedacym slowem kluczowym 
f(1, 2, 3, x=4)
# 1 (3,) 2 {'x':4}

def f(a, *b, c=6, **d): print(a, b, c, d)    # Pomiedzy * a ** tylko slowa kluczowe 
f(1, *(2,3), **dict(x=4, y=5))   # Rozpakowanie argumentow przy wywolaniu
# 1 (2, 3) 6 {'y': 5, 'x': 4}
f(1, *(2,3), **dict(x=4, y=5), c=7)   # Blad Slowa kluczowe przed **argumenty! 
f(1, *(2,3), c=7, **dict(x=4, y=5))   # Nadpisanie wartosci domyslnych ----> 1 (2,3) 7 {'y': 5, 'x': 4}
f(1, c=7, *(2,3), **dict(x=4, y=5))   # Przed lub po *  ----> 1 (2,3) 7 {'y': 5, 'x': 4}
f(1, *(2,3), **dict(x=4, y=5, c=7))   # Argument mogacy byc tylko slowem kluczowym w ** ----> 1 (2,3) 7 {'y': 5, 'x': 4}



# 587
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res= arg 
    return res 
def lessthan(x, y): return x < y    # Rowniez moze byc lambda , eval 
def grtrthan(x, y): return x > y 
print(minimax(lessthan, 4, 2, 1, 5, 6, 3)) # Kod samotestu 
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
# %python minmax.py 
# 1 
# 6 

def intersect(*args):
    res[]
    for x in args[0]:                  # Przejrzenie pierwszej sekwencji 
        if x in res: continue          # Pomijamy duplikaty
        for other in args[1:]:         # Dla wszystkich pozostalych argumentow 
            if x not in other: break   # Element w kazdym z nich
        else:                          # Nie wyjscie z petli
            res.append(x)              # Tak dodanie elementu na koncu 
    return res 
 
def union(*args):
    res = []
    for se1 in args:                   # Dla wszystkich argumentow 
        for x in seq:                  # Dla wszystkich wezlow 
            if not x in res:
                res.append(x)          # Dodanie nowych elementow w wynniku
        return res 

from inter2 import intersect, union 
s1, s2, s3 = "Teodor", "Teofil", "Troll"
intersect(s1, s2), union(s1, s2)     # Dwa argumenty 
# (['T' 'e' 'o' 'o'], ['T' 'e' 'o' 'd' 'r' 'f' 'i' 'l'])
intersect([1, 2, 3], (1,4))      # Typy mieszane 
# [1]
intersect(s1, s2, s3)  # Trzy argumenty 
# ['T' 'o' 'o']
union(s1, s2, s3)
# ['T' 'e' 'o' 'd' 'r' 'f' 'i' 'l']

def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

tester(intersect,('a','abcdef','abdst','albmcnd'))

tester (union('a','abcdef','abdst','albmcnd'), False )

tester(intersect('a','abcdef','abdst','albmcnd'), False )
# ['a', 'b'] 
# ['a', 'b'] 
# ['a', 'b'] 
# ['a', 'b'] 

intersect([1, 2, 1, 3], (1, 1, 4))
# [1]

union([1, 2, 1, 3], (1, 1, 4))
# [1, 2, 3, 4]

# Sumowanie z uzyciem rekurencji 
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])    # Wylowanie samej siebie (rekurencja)
mysum([1, 2, 3, 4, 5])
# 15 

def mysum(L):
    print(L)
    if not L:
        return 0 
    else:
        return L[0] + mysum(L[:1]) # Jakby bylo ze napiszemy 1: to naodrot leci kolejnosc 12345 2345 345
mysum([1, 2, 3, 4, 5])
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4]
# [1, 2, 3]
# [1, 2]
# [1]
# []
# 15

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:]) # Uzycie wyrazen trojskladnikowych 

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])  # Dowolny typ, domyslnie wartosc 1 

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)  # Uzycie rozszerzonego przypisania 

mysum([1])   # mysum nie dzilaa dla ostatnich 2 funkcji 
# 1 
mysum([1, 2, 3, 4, 5])
# 15 
mysum(('j', 'a', 'j', 'k', 'o'))   # Ale funkcja dziala dla roznych typow 
# jajko
mysum('mieonka ', 'jajko','szynka ')
# mielonkajajkoszynka 

def mysum(L):
    if not L: return 0
    return nonempty(L)   # Wywoluje funkcje , ktora wywolala mnie 
def nonempty(L):
    return L[0] + mysum(L[1:])    # Rekurencka posrednia 
mysum([1.1, 2.2])
# 3.4

# Petla a rekurenja 
L = [1, 2, ,3 ,4, 5]
sum = 0 
while L :          # WHILE I SUM 
    sum += L[0]
    L = L[1:]
sum 
# 15 


L = [1, 2, , 3, 4]
sum = 0 
for x in L: sum +x     # for i sum   -----> to juz x 
sum
# 15



# Obsluga dowolnych struktur 
def sumtree(L):
    tot = 0
    for x in L :                          # Dla kazdego elementu na tym poziomie 
        if not isinstance(x, list):
            tot +=x                       # Bezposrednie dodawanie liczb 
        else :
            tot += sumtree(x)             # Rekurencja dla podlist
    return tot 
L = [1,[2,[3,4], 5],6,[7,8]]              # Dowolone zagniezdzenie 
print(sumtree(L))                         # Wypisuje 36

# Aby zwiekszyc domyslny rozmiar stosu mozemy uzyc modulu sys:
sys.getrecursionlimit()    # Domyslny limit pozwala na 1000 wylowan rekurencyjnych 
# 1000 
sys.setrecursionlimit(10000)   # Zwiekaszamy limit zagniezdzenia 
help(sys.setrecursionlimit)   # Wyswietlamy wiecej informacji na ten temat 


# Posrednie wywolania funkjci - obiekty pierwszej klasy 
# MOdelem obiektowym pierwszej klasy  first cass object model; FCO   --- FCO sprawia ze Python jest elastyczny 
def echo (message):     # Nazwa echo przypisana do nazwy funkcji 
    print(message)
echo('Wywolanie bezposrednie')   # Wywolanie obiektu przez oryginalna nazwe 
# Direct call 
x = echo                         # Teraz rowniez zmienna x zawiera referencje do funkjci 
x ('Wylowanie beposrednie!')     # Wylowanie obiektu przez nazwe zastosowanie ()

def indirect(func, arg):
    func(arg)
indirect(echo, 'Wylowanie argumetu!')     # Przekazanie funkcji do innej funkcji 
# Wylowanie argumentu 

schedule  = [(echo, 'Mielonka'), (echo, 'Szynka')]
for(func, arg) in shedule:
    func(arg)                                           # Wylowanie funkcji osadzonych w komentarze 
# Mielonka 
# Szynka 

def make(label):
    def echo(message):
        print(label + ':'  + message)
    return echo 
F = make('Mielonka')  # Zostaje zapisana etykieta przekazana do funkcji w wewnetrznym zasiegu 
F('Szynka!')            # Wywolanie funkcji utworzonej w funkcji make 
# Mielonka: Szynka!
F('Jajka')
# Mielonka: Jajka 

# Introspekcja funkcji 
def func(a):
    b = 'mielonka'
    return b * a 
func(5)
# wyswietli mielonka 5razy 

# Atrybuty funkcji 608 strona 

# Adnotacje funkcji 
def func(a, b, c):
    retun a+b+c
func(1, 2, 3)
# 6 

def func( a: 'mielonka', b: 'jajka', c: float) -> int:
    return a + b + c 
func(1, 2, 3)
# 6
func.__annotations__


# Adnotacja dla dwoch trzech argumentow 
def func(a: 'mielonka', b, c: 99):
    return a + b + c
func(1, 2, 3)
# 6
func.__annotations__ 
# (c : 99, a : 'mielonka')

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])
    # c => 99
    # a => mielonka 


# W ponizszym przykladzie a : mielonka = 4 oznacz ze wartoscia domysla argumentu a jest 4 a argument posiada adnotacje 'mielonka' 
def func(a: 'mielonka' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a+b+c 
func(1, 2, 3) 
# 6
func()  # 4 + 5 + 6 (wartosci domyslne)
# 15 
func(1, c = 10) # 1 + 5 + 10  (parametry klucozwe dzilaja standardowo)
# 16



# Lambda  i return roznicz 
def func(x, y, z): return x + y + z 
func(2, 3, 4)
# 9 

f = lambda x, y, z: x+y+z 
f(2, 3, 4)
# 9 

x = (lambda a="raz", b="dwa", c="trzy": a + b + c)
x('las')
# 'lasdwatrzy'

def knight( ):
    title = 'Sir'
    action = (lambda x: title + ' ' + x)  # Tytul w zasiegu instrukcji def zawierajacej wyrazenie 
                                          # lambda
    return action    
msg = act('robin') # # robin przekazano do x
msg # 'Sir robin'


# Jump table 
L = [(lambda x: x**2) # Wewnetrze definicje funkcji 
    (lambda x: x**3)
    (lambda x: x**4)] # Lista trzech wylowanyc funkcji 
for f in L:
    print f(2) # Wyswietla 4 8 16
print L[0](3)  # Wyswietla 9 


# To samo tylko przez def 
def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4 
L = [f1, f2, f3]
for f in L: 
    print(f(2)) # Wyswietla 4 8 16 
print L[0](3)  # Wyswietla 9 

# Wielotorowe rozgaliezienia kodu 
key = 'juz'
{ 'mam' : (lambda: 2 + 2),
'juz': (lambda: 2 * 4),
'jeden': (lambda: 2 ** 6)} [key]()
# 8 

def f1(x): return 2 + 2
def f2(x): return 2 * 4
def f3(x): return 2 ** 6
key = 'jeden'
{'mam': f1, 'juz': f2, 'jeden': f3} [key]()
# 64

# Zasiegi : wyrazenia lambda rowniez mozna zagniezdzac 
def action(x):
    return (lambda y : x + y)   # Utworzenie i zwrocenie funkcji, zapamietanie x 
act = action (99)
act(2)  # Wywolanie wyniku funkcji action 
# 101 

action = (lambda x : (lambda y: x + y))
act = action(99)
act(3)
# 102 
((lambda x : (lambda y: x + y)) (99)(4))
# 103  
# Lepiej unikac zagniezdzanie lambda 

# Odwzorowanie funnkcji na obiekty iterowalne -- map 
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)    # Dodanie 10 do kazdego elementu 
updated# [11 12 13 14]

def inc(x):return x + 10    # Funkcja do wykonania 
map(inc, counters)  # Zbieranie wynikow 
# [11 12 13 14]

list(map(lambda x: x + 3), counters)   # Wyrazenie funkcji 
# [4, 5, 6, 7]

def mymap(func, arg): 
    res = []
    for x in seq : res.append(func(x))
    return res 


pow(3, 4) # 3**3
list(map(pow, [1, 2 ,3], [2, 3, 4])) # 1**2, 2**3, 3**4

list(map(inc, [1, 2, 3, 4]))   
# # [11 12 13 14]
[inc(x) for x in [1, 2, 3 ,4]]
# # [11 12 13 14]

# Wybieranie elementow oniektow iterowalnych -- funkcja filter 
list(range(-5,5))  # od -5 do 5 
list(filter(lambda x: x > 0), range(-5, 5))  
# od 1 do 4 

# Listy skladane kontra funkcja map #################################################

res = []
for x in range(-5, 5):
    if x > 0: 
        res.append(x)
res 
# od 1 do 4 

[x for x in range (5, 5) if x > 0] 
# od 1 do 4 

# Laczenie elementow obiektow iterowalnych -- funkcja reduce 
from functools import reduce 
reduce((lambda x, y: x + y), [1,2,3,4]) # 10
reduce((lambda x, y: x * y), [1,2,3,4]) # 23

L = [1,2,3,4]
res = L[0] # Wartosc poczatkowa 
for x in L[1:]:
    res = res + x 
res # 10

# Modul  operator  ktory udostepnia funkcje odpowidajace wbudowanym wyrazeniom przydatny do wyrazen funkcyjnych 
import operator, functools
functools.reduce(operator.add, [2,4,6])  # Dodawanie oparte na funkcji 12 
functools.reduce (lambda x, y: x + y), [2, 4, 6]


ord ('s')
# Chcemy odzcyztac ASCII wszsytkich
res = []
for x in 'spam' :
    res.append(ord(x))   # Reczne zbieranie wynikow 
res # [115, 112, 97, 109]

# Z funkcja map 
res = list(map(ord, 'spam'))   # Wylowanie funkcji na sekwencji (lub innym obiekcie iterowalnym )
res # [115, 112, 97, 109]

# A teraz lista skladana Funkcja map odwzorowanie funkcji map  na obiekcie iterowalnymm natomiast lista skladana dokonuje odzworowanie wyrazenia na sekwencji 
res  = [ord(x) for x in 'spam']   # Wywolanie wyrazenia na sekwencji (lub innym ...)
res # # [115, 112, 97, 109]

[x ** 2 for x in range(10)]
# [0, 1, 4, 9, i tak do 10 ]

# mOZEMY PRZPISAC DO ZMIENNEJ JEZELI CHCEMY GO ZACHOWAC I UZYWAC W KODZIE , same musimy napisac Jezeli potrzebne tylko w jedny miehsu to lambda 
# lambda 
list(map(lambda x : x ** 2 ), range(10))
# # [0, 1, 4, 9, i tak do 10 ]

[x for x in range(5) if % 2 == 0]
# [0, 2, 4]

list(filter((lambda x : x % 2 == 0), range(5)))
# [0 , 2, 4]

list(filter(lambda x: x % 2 == 0), range(5))
# [0, 2, 4]

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
res 
# [0, 2, 4]

[x ** 2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

list( map ((lambda x : x ** 2), filter((lambda x: x % 2 == 0), range(10) ) ) )
# [ 0, 4, 16, 36, 64 ]

list(map ((lambda x: x**2), filter((lambda x : x ** 2 == 0) range(10) )))
#  [0, 4, 16, 36, 64]

# [wyrazenie for zmienna1 in obiekt_iterowalny1 [if warunek1]
#            for zmienna2 in obiekt_iterowalny1 [if warunek2]
#            for zmienna3 in obiekt_iterowalny1 [if warunek3]]

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
res 
# [100, 200, 300, 101, 201, 301, 102, 202, 302]

res = []
for x in [0, 1, 2]:
    for i in [100, 200, 300]:
        res.append(x + y) 
res 
# # [100, 200, 300, 101, 201, 301, 102, 202, 302]

[x + y for x in 'spam' for y in 'SPAM']
# [ aS sP sA sM pS pP pA pM aS aP aA aM mS mP mA mM ]

# Zastosowanie do obiektow numerycznych a nie jak do tej pory do ciagow 
[(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
# [(0, 1) (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

# Powyzsze wyrazenie zwraca permutacje liczb parzystych z zakresu 0 do 4 z liczbami nieparzystymi 
# z tego zkresu . Warunki if odfiltowuja zbedne elementy w kazdym z podwyrazen 
# Wyrazenie to odpowiada nastepejucemu kodowi  z uzyciem zagniezdzen petli for 
res = []
for x in range(5): 
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append(x, y) 
# [(0, 1) (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

# Przyklda listy skladane macierzy 
M = [[1, 2 ,3 
    4, 5, 6
    7, 8, 9]]

N = [[2, 2, 2
    3, 3, 3
    4, 4, 4]]

M[1] # Wiersz 2 
# [4, 5, 6]

M[1][2] # Wiersz 2 element 3 
# 6 

[row[1] for row in M ]   # Kolumna 2 
# [2, 5, 8]

[M[row[1] for row in (0, 1, 2)]]   # Zastosowanie offsetow 
# [2, 5, 8] 


###############################################################################################################################################################################################################


###############################################################################################################################################################################################################
# Строки в качестве ключей
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# Числа в качестве ключей
my_dict = {1: 'apple', 2: 'banana', 3: 'orange'}

# Кортежи в качестве ключей
my_dict = {('apple', 1): 1, ('banana', 2): 2, ('orange', 3): 3}

# frozenset в качестве ключей
my_dict = {frozenset([1, 2]): 'apple', frozenset([3, 4]): 'banana'}




# Пример импортирования модуля и пакета:
# Импортирование модуля
import my_module

# Импортирование функции из модуля
from my_module import my_function

# Импортирование пакета
import my_package

# Импортирование модуля из пакета
from my_package import my_module

import requests




# что такое синхронный код? Python
# Синхронный код в Python (и в других языках программирования) - это код, который выполняется последовательно и блокирует выполнение программы до завершения текущей операции.
# В синхронном коде каждая операция выполняется последовательно и блокирует выполнение программы до завершения текущей операции. Таким образом, код может выполняться медленно, особенно если он содержит длительные операции ввода-вывода, такие как чтение больших файлов, отправка запросов к базе данных и т.д.
#Пример синхронного кода:
# Синхронный запрос к API
response = requests.get('https://example.com/api/data')
data = response.json()

# Обработка полученных данных
for item in data:
    process_item(item)




# Для чего нужен метод id()? Python
# Метод id() в Python используется для получения уникального идентификатора объекта. Этот идентификатор представляет собой целое число, которое является адресом в памяти, где хранится объект.
# Идентификатор объекта может быть использован для проверки, является ли данный объект ссылкой на тот же объект, что и другой объект. Например, если две переменные ссылаются на один и тот же объект, то их идентификаторы будут равны.
# Пример использования метода id():
x = 10
y = x
z = 10

print(id(x))  # выводит идентификатор объекта, на который ссылается x
print(id(y))  # выводит идентификатор объекта, на который ссылается y (равен идентификатору x)
print(id(z))  # выводит идентификатор объекта, на который ссылается z (может быть равен или не равен идентификатору x)

140713728885168
140713728885168
140713728885168
# Здесь переменные x и y ссылаются на один и тот же объект, поэтому их идентификаторы равны. Переменная z также ссылается на объект со значением 10, но ее идентификатор может быть как равен, так и не равен идентификатору x и y, потому что интерпретатор Python может создавать новые объекты со значением 10 в других областях памяти.




#Для чего в классе используется атрибут __slots__?Python
# ###
#Атрибут __slots__ используется в классах Python для определения набора атрибутов (полей), которые могут быть созданы для экземпляров данного класса. Если __slots__ определен для класса, то экземпляры этого класса могут содержать только те атрибуты, которые перечислены в __slots__.
#Использование __slots__ позволяет сократить потребление памяти, потому что не нужно выделять место для каждого возможного атрибута в экземпляре класса. Кроме того, использование __slots__ также может ускорить доступ к атрибутам экземпляра, так как интерпретатор Python может использовать более эффективные структуры данных для хранения атрибутов.
#Например, следующий код определяет класс Person с использованием __slots__, который позволяет создавать объекты только с атрибутами name и age:
# ###
class Person:
    __slots__ = ('name', 'age')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Теперь экземпляры класса Person могут содержать только атрибуты name и age. Если попытаться добавить другой атрибут, например, gender, будет вызвано исключение AttributeError.



# С помощью каких инструментов можно выполнить статический анализ кода?Python
# В Python существует множество инструментов для выполнения статического анализа кода. Некоторые из них:

# PyLint - это инструмент, который проверяет соответствие кода стандартам PEP 8, выявляет потенциальные ошибки и проблемы в коде.
# Flake8 - это комбинация трех инструментов - PyFlakes, pycodestyle и McCabe - для проверки синтаксиса, соответствия стилю кодирования и выявления неэффективных участков кода.
# Pyright - это быстрый и точный инструмент статического анализа типов для Python, который позволяет проверить соответствие типов и выявить потенциальные ошибки.
# Mypy - это инструмент статической типизации для Python, который позволяет выявлять ошибки связанные с типами данных.
# Bandit - это инструмент для анализа безопасности Python-кода, который помогает обнаруживать потенциальные уязвимости и проблемы безопасности.
# Safety - это инструмент для проверки уязвимостей в зависимостях Python-проектов.
# Coverage - это инструмент для измерения покрытия кода тестами.
# Black - это инструмент для автоматического форматирования кода в соответствии со стандартами PEP 8.




###############################################################################################################################################################################################################


###########################################################################################################################################################################

# 18. Kurs Python 3 - operacje na tekście (String) i listach
print (", ".join(["a","b","b"])) # join przyjmuje liste , a b c kadzy argument ktory wyslemy do join laczy ze soba w soposob ze dokleja je do siebie i rzodziela agrumentem ,
# a, b, c

print("wITAJ SWICIE".replace("wITAJ", "RZEGNAM"))

print("Witaj Swiecie".replace("Witaj", "Czesc")) # Zamiast witaj bedzie czesc swiecie 

print("To jest zdanie".startswitch("To")) # zwraca Prawda lub falsz jezeli to sie zaczyna na To to bedzie --> True 

print("To jest zdanie.".endswitch(".")) # konczy sie . to bedzie True 

print("j" in "To jest zdanie .") # Czy znajduje sie w tym zdaniu j 

print("To jest zdanie.".upper()) # Wszystkie litery robia sie duzymi 

print("To jest zdanie.".lower()) # Wszystkie litery na male 

print(" ------- ")
lista = [10, 20, 25, 35, 40]
if all([i % 2 == 0 for i in lista]): # kazdy argument musi spelniac cgociaz jeden warunek true lub false sprawdzamy czy lsty sa parzyste ==0 sprawdzamy czy jest parzysta 
    print("Wszystkie parzyste") # jAK NIE MAMY ZADNEJ INFORMACJI CZYLI FALSE 

lista = [10, 20, 26, 36, 40]
if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste") # Wszystkie parzyste czyli --> true 

if any([i % 2 == 0 for i in lista]):
    print("Chociaz jedna parzysta") # Chociaz jedna parzysta 

for i in lista:
    print(i)  # liczby z gory w dol 

lista = [15, 25, 25, 35, 45]
for i in enumerate(lista):
    print(i) # Tworzy nowa liste tworzy numeracje od 0 a jao 2 argument na liscie 
# (0, 15)
# (1, 25)
# (2, 25)
# (3, 35)
# (4, 45)


######################################################################################################
# ООП
class Human:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender

    def get_name(self):
        return self.name 
    
    def get_gender(self):
        return self.gender 
    
    def get_age(self):
        return self.age 
person = Human(name='Jaohn',
                age=34,
                gender='male')

            
class Parent:
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        print("Hello, Iam {name}".format(name=self.name))
parent = Parent(name="John")
parent.say_hello()

class Parent:
    def __init__(self,name):
        self.name = name 
    def say_hello(self):
        print("Hello, I am {name}".format(name=self.name))
parent = Parent(name="John")
parent.say_hello()


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age 

    def say_hello(self):
        print(
            "Hello, my name is {name} and Iam {age} years old".format(
                name=self.naame, age=self.age
            )
        )
child = Child(name="Mark", age=25)
child.say_hello()


class A:
    def __init_(self):
        self.a = 10
class B:
     def __init__(self)
     self.b = 25
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
c = C()
print("C class has a={a_vaue} and b={b_value}".format(a_
vaue=c.a, b_value)) 

class Car:
    def __init__(self, brand, color, vol):
        self.brand = brand
        self.color = color
        self.vol = vol

    def drive_forward(self):
        print('Drive forward')
    
    def drive_backward(self):
        print('Drive backward')

Class Car2(Car):
    
    def __init__(self, brand, color, vol):
        super().__init__(brand, color, vol)

    def turn_right(self):
        print("Turn right")
    
    def turn_left(self):
        print("Turn left")

Class Airplane:
    def __init__(self, model):
        self.model = model 
    def fly(self):
        print("Start the flight")

class FlyingCar(Car2, Airplane):
    def __init__(self, brand, color, vol, model):
        Car2.__init__(self, brand, color, vol)
        Airplane.__init__(self, model)

flying_car = FlyingCar(
    brand='Tesla',
    color='black',
    vol=4.5,
    model='F'
)
flying_car.fly()



class Human:
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print("Hello, I am {}".format(self.age))


human = Human(age=35)
human.say_hello()


class HumanExtended(Human):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def say_hello(self):
        print("Hello, I am {} and I am {}".format(
            self.name, self.age
        ))


human2 = HumanExtended(age=56, name='John')
human2.say_hello()


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 5


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()
print(c.a)
print(c.b)



class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age_and_name(self):
        return self.age, self.get_name()


human_1 = Human(age=25, name='John', gender='male')
print(human_1.get_age_and_name())
#########################################################################################################################################
# Інкапсуляція 
class TextProcessor:
    def __init__(self):
        self._punktuation = '.,!?;:*'

    def __is_punktuation(self, char):
        return char in self._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punktuation(char):
                continue
            clean_text += char
        return clean_text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is: {}".format(self.__clean_string))
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ['Hello, I am John *', 'Hey, what is the weather today ?']
ct = di.process_texts(t)



class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


# user = User(name='Alex')
# user.name = 'Bob'
# print(user.name)

class User2:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Property was called")
        return self.__name


u2 = User2(name='Mike')
print(u2.name)


class Worker:
    RIGHTS = "Equal"
    SALARY_MAP = {
        "A": 100,
        "B": 200,
        "C": 500
    }

    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)

    @staticmethod
    def __get_salary(working_class):
        return Worker.SALARY_MAP.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


w1 = Worker('A')
print(w1.salary)

w2 = Worker('D')
print(w2.salary)


# program to illustrate protected access modifier in a class

class edpresso:
    def __init__(self, name, project):
        self._name = name
        self._project = project

# creating object of the class 
edp = edpresso("TeamPhoenix", 2)

# direct access of protected member
print("Name:",edp._name)
print("project:",edp._project)

# Name: TeamPhoenix
# # project: 2


# Private members 
# program to illustrate private access modifier in a class

class edpresso:
   def __init__(self, name, project):
      # public variable
      self.name = name
      # private variable
      self.__project = project

# creating an instance of the class Sample
edp = edpresso('TeamPhoenix', 3)

# accessing public variable name
print("Name:",edp.name)

# accessing private variable __project using 
# _Edpresso__project name
print("Project:",edp._edpresso__project)




# Python program to
# demonstrate protected members
# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

# Calling protected member of base class:  2
# Calling modified protected member outside class:  3
# Accessing protected member of obj1:  3
# Accessing protected member of obj2:  2




# Python program to
# demonstrate private members
# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

# BLAD

####################################################################################################################################################################
# Поліморфізм   #############################################

# 1. Перевантаження 
# 2. Перепизначення 

# Zadania 
class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length


    def get_area(self):
        return self._width * self._length


class Square(Parallelogram):
    def get_area(self):
        return self._width * self._length


def function(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


print(function('{1, 5, 3}', '4'))


# Polymorphizm_overriding.py 
class Multiplier:
    def __init__(self, a):
        self._a = a

    def print_a(self, x):
        print(self._a * x)


m = Multiplier(5)
m.print_a(2)


class Exponent(Multiplier):
    def print_a(self, x):
        print(self._a ** x)


e = Exponent(4)
e.print_a(2)


# polymorphizm_overlad.py 
class Base:
    def __init__(self, a):
        self.__a = a

    def print_a(self, square=False, multiplier=None):
        if square and not multiplier:
            print(self.__a ** 2)
        elif not square and multiplier:
            print(self.__a * multiplier)
        elif square and multiplier:
            print((self.__a ** 2) * multiplier)
        else:
            print(self.__a)


base = Base(4)
base.print_a()


# polymorphizm_examples.py  
class Car:
    def __init__(self, name):
        self._speed_name_map = {
            "BMW": 250,
            "Mercedes": 350
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self._speed_name_map.get(name, 0)

    def distance_on_max_speed(self, distance):
        if self._max_speed == 0:
            print(
                "Speed = 0, select valid car brand: {}".format(
                    list(self._speed_name_map.keys())
                )
            )
            return 0
        return distance / self._max_speed


car1 = Car('BMW')
car2 = Car('Mercedes')
car3 = Car('ABC')

print(car1.distance_on_max_speed(100))
print(car2.distance_on_max_speed(100))
print(car3.distance_on_max_speed(100))


class Animal:
    def __init__(self, name):
        self._name = name

    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("Meow")



class Dog(Animal):
    def voice(self):
        print("Bark")


animal = Animal('?')
animal.voice()

cat = Cat('Sarah')
cat.voice()
dog = Dog('Rex')
dog.voice()


class Animal2:
    def __init__(self, name):
        self._name = name

    def voice(self):
        if self._name == 'cat':
            print('Meow')
        elif self._name == "dog":
            print('Bark')
        else:
            print("...")


a1 = Animal2('cat')
a2 = Animal2('dog')
a3 = Animal2('dinosaur')
a1.voice()
a2.voice()
a3.voice()


# Bad_example.py 
class Messenger:
    def __init__(self, connection):
        self._connection = connection

    def send_message(self, text, option=None):
        self._connection.send(text)


class ExtendedMessenger(Messenger):  # Bad example !
    def send_message(self, text, option=None):
        if option == 'message':
            self._connection.send(text)
        elif option == 'image':
            self._connection.send(text)
        elif option == 'math':
            print('2+2=4')hh
        else:
            print('...')


####################################################################################################################################################################
# Абстракція 

# simple-calculator.py
class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __convert_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        packed_values = tuple(expression.split(' '))
        if len(packed_values) < 3:
            print("Wrong indentation, check your expression")
            return 0, 0, '+'
        a, op, b = packed_values
        return self.__convert_type(a), self.__convert_type(b), op


class Core:
    def __init__(self):
        self._parser = Parser()
        self._functions = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }

    def calculate(self, expression):
        a, b, op = self._parser.parse(expression)
        result = self._functions.get(op)(a, b)
        return result


class Interface:
    def __init__(self):
        self._core = Core()

    def run_calculator(self):
        while True:
            print("Enter your expression: eg. '2 + 2' ")
            expression = input()
            result = self._core.calculate(expression)
            print("Result: {}".format(result))
            print("=" * 10)


if __name__ == "__main__":
    calculator = Interface()
    calculator.run_calculator()



# abstraction_example.py    #  ----> Деталі реалізації
class Core:
    def __init__(self):
        self._types = {
            "A": 100,
            "B": 300
        }

    #def get_salary(self, worker_type):
        #return self._types.get(worker_type, 0)
    
    def get_salary(self, class_name):
        return self._types.get(class_name, 0)  #  ----> Деталі реалізації


class AccountingInterface:       #  ----> Інтерфейс
    def __init__(self, data):
        self._core = Core()
        self._database = data

    #def get_person_salary(self, name):
        #person_class = self._people_class_dict.get(name)
        #return self._core.get_salary(person_class)         #  ----> Інтерфейс 

    def get_salary(self, name):
        class_of_employee = self._database.get(name)
        salary = self._core.get_salary(class_of_employee)
        return salary


db = {"John": "A", "Mike": "B"}
interface = AccountingInterface(data=db)
print("John's salary is: {}".format(interface.get_salary(name="John")))

#################################################################################################################################################################

# Робота з рекурсією
# http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad6.html

# https://www.w3schools.com/python/gloss_python_function_recursion.asp#%3A%7E%3Atext%3DPython%20also%20accepts%20function%20recursion%2Cthat%20a%20function%20calls%20itself.%26text%3DThe%20recursion%20ends%20when%20the%2Ci.e.%20when%20it%20is%200)
# https://pythonru.com/osnovy/rekursiya-python

# https://www.codecamp.ru/blog/python-recursion/  ----> codecamp 
# https://www.datacamp.com/tutorial/understanding-recursive-functions-python  ----> datacamp 

# tasks.py 
def values(n, current=1):
    if current <= n:
        print(current)
        values(current=current + 1, n=n)


# values(20)

def check_pow_2(n):
    if n == 1:
        print("YES")
    else:
        if n % 2 == 0:
            check_pow_2(n // 2)
        else:
            print("NO")


# check_pow_2(16)

def sum_val(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_val(num, res)
# print(sum_val(345))



# simple_recursion.py 
a = [4, 5, 6, 3, 2]


def iter_arr(array):
    for elem in array:
        print(elem)


def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


# def rec_count(index):
#     print(index)
#     index += 1
#     rec_count(index)
#
#
# rec_count(1)



# binary_seach_tree.py 
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data):
        if data == self.data:
            print("{} in tree".format(data))
            return True
        if data < self.data:
            if self.left is None:
                print("{} not in tree".format(data))
                return False
            return self.left.search(data)
        if self.right is None:
            print("{} not in tree".format(data))
            return False
        return self.right.search(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


a = [4, 5, 1, 3, 2, 8, 0]
for i in range(len(a)):
    if i == 0:
        root = Node(a[i])
    else:
        root.insert(a[i])

root.search(2)


##########################################################################################################################################################################

# Структури даних  (6)

# complex_objects.py ---->  Складні обєкти 
user = {
    "name": "JohnDoe",
    "info": {
        "basic": {
            "age": 25,
            "salary": 5000
        },
        "additional": {
            "study": "mathematics",
            "family": "married"
        },
        "special": {
            "projects": [
                {"name": "quantum_computer", "stage": "in_progress"},
                {"name": "laser_gun", "stage": "in_production"}
            ]
        }
    }
}


def get_data(data_dict, keys):
    data = data_dict
    for key in keys:
        data = data[key]
    return data


def get_data_rec(data_dict, keys, index=0):
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index + 1)
    return data_dict


print(get_data(user, ['info', 'special', 'projects', 0, 'name']))
print(get_data_rec(user, ['info', 'special', 'projects', 0, 'name']))


# comprehensions.py 
# chars = []
# for char in "abcde":
#     chars.append(char)
# print(chars)
chars = [char for char in "abcde"]
print(chars)

names = ['make', 'john', 'sally']
names = [name.capitalize() for name in names]
print(names)

numbers = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

unique_values = {value ** 2 for value in [1, 3, 5, 5, 2, 2, 1, 7]}
print(unique_values)

data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)

values_squares = {value: value ** 2 for value in range(10)}
print(values_squares)

m = tuple(n for n in range(12))
print(m)


# flattening.py 
matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)


# tasks-2.py
def func(index, count):
    return {
        "ID": index,
        "values": ["{}_{}".format(index, value) for value in range(count)]
    }


def generate(count):
    return [func(i, j) for i, j in zip(range(count), list(range(count))[::-1])]


r = generate(10)
# print(r)
f = [value for sublist in r for value in sublist['values']]
print(f)


######################################### Kontynuacja Структури даних  (6)
# Python Nested Dictionary 
# In Python, a dictionary is an unordered collection of items. For example:
dictionary = {'key' : 'value',
'key_2': 'value_2'}


# What is Nested Dictionary in Python?
nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}

# Create a Nested Dictionary 
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)
# {1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}


# Example 2: Access the elements using the [] syntax
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
# John
# 27
# Male


# Add element to a Nested Dictionary
# Example 3: How to change or add elements in a nested dictionary?
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])
# {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}


# Example 4: Add another dictionary to the nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])
# {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}


# Example 5: How to delete elements from a nested dictionary?
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

del people[3]['married']
del people[4]['married']
del people[2]['married']

print(people[3])
print(people[4])
# {'name': 'Luna', 'age': '24', 'sex': 'Female'}
# {'name': 'Peter', 'age': '29', 'sex': 'Male'}


# Example 6: How to delete dictionary from a nested dictionary?
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

del people[3], people[4]
print(people)
# {1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}


# Example 7: How to iterate through a Nested dictionary?
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])
# Person ID: 1
# Name: John
# Age: 27
# Sex: Male

# Person ID: 2
# Name: Marie
# Age: 22
# Sex: Female

# Comprehensions 
chars = [char for char in "abcde"]  # ['a','b','c','d','e']
names = ['mike', 'john','sally','mary','kate','robert']       # ------> List comprehension
names = [name.capitalize() for name in names]   # ['Mike','John',...]

evan_nums = [num for num in [1, 2, 3, 4, 5, 6, 7, 8] if num % 2 == 0] # [2, 4, 6, 8]
unique_values = {value**2 for value in [1,3, 5, 5, 2, 1, 7, 3]}  #  {1, 4, 9 ,49, 25}  # -----> Set comprehension


data = ["John_25", "Sally_19", "Susan_35", "Jack_16"] # #
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data} # # 
print(name_age_dict)  # {'John': '25', 'Sally': '19',...}    # #

values_squares = {value: value ** 2 for value in range(10)}  # #---->     Dict
print(values_squares) # {0: 0,1: 1,2: 4,3: 9,...}            # #---->  comprehension

months = (num for num in range(12))    # ---->      Tuple 
print(months)  # (0, 1, 2, 3,...)      # ---->    comprehension

# "Double Comprehension" i "flattening"
matrix = [[j for j in range(2)]for i in range(2)]
print(matrix) # [[0, 1], [0, 1]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix) # [0, 1, 0, 1]
# 1. Вкладені структури   ----> https://dvmn.org/encyclopedia/python_intermediate/multistructures/
# 2. Comprehensions ----> https://www.datacamp.com/tutorial/python-list-comprehension  ---------------> wazne 
# 3. List comprehensions ----> https://www.w3schools.com/python/python_lists_comprehension.asp
# 4. Double comprehension ----> https://www.adamsmith.haus/python/answers/how-to-do-a-double-iteration-with-a-list-comprehension-in-python 

# uslowie = True
# x = 1 if uslowie == True else 0 
# print(x)

# --------------> to przeczytac 


# # 2. Comprehensions ----> https://www.datacamp.com/tutorial/python-list-comprehension  ---------------> wazne 
# 2. 1)
list_variable = [x for x in iterable]
# 2) list Comprehension in Python: The Mathematics ----> Zrozumienie listy w Pythonie: Matematyka
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}

S = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
V = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}
M = {0, 4, 16, 36, 64}

# 3) Podsumowanie i praktyka 
# Krótko mówiąc, widać, że istnieje kilka elementów powracających we wszystkich tych wierszach kodu:
# Nawiasy kwadratowe, które są sygnaturą list Pythona;
# Słowo kluczowe for, po którym następuje zmienna, która symbolizuje element listy; i.
# Słowo kluczowe IN, po którym następuje sekwencja (która może być listą!).
list_variable = [x for x in iterable]


# Initialize `numbers`
numbers = range(10)


# Jeśli teraz chcesz wykonać operację na każdym elemencie w liczbach, możesz to zrobić za pomocą pętli FOR, tak jak ten:
# Initialize `new_list`
new_list = []


# Add values to `new_list`
for n in numbers:
    if n%2==0:
        new_list.append(n**2)

# Print `new_list`
print(new_list)
# [0, 4, 16, 36, 64]


# To wszystko jest ładne i dobrze, ale teraz rozważ następujący przykład zrozumienia listy, gdzie w zasadzie zrobić to samo z bardziej zwartą notacją:
# Create `new_list` 
new_list = [n**2 for n in numbers if n%2==0]


# Print `new_list`
print(new_list)
# [0, 4, 16, 36, 64]


# # Import `timeit`
import timeit


# Print the execution time
print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))
# 0.05234622399802902


# Define `power_two()` 
def power_two(numbers):
    for n in numbers:
        if n%2==0:
            new_list.append(n**2)
    return new_list

# Print the execution time 
print(timeit.timeit('power_two(numbers)', globals=globals(), number=10000))
# 0.07795589299712447


# 3) Funkcje lambda z map(), filter() i reduce()
# Jak zastąpić MAP() w połączeniu z Funkcjami Lambda
# Możesz przepisać kombinację map() i funkcji lambda tak jak w poniższym przykładzie:
# Initialize the `kilometer` list 
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)

# Print `feet` as a list 
print(list(feet))
# [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]


# Convert `kilometer` to `feet` 
feet = [float(3280.8399)*x for x in kilometer]

# Print `feet`
print(feet)
# [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]


# Teraz, gdy już wiesz, jak łatwo można przekonwertować funkcję map() w połączeniu z funkcją lambda, można również zająć się kodem, który zawiera funkcję Python filter() z funkcjami lambda i przepisać go również.
# Map the values of `feet` to integers 
feet = list(map(int, feet))

# Filter `feet` to only include uneven distances 
uneven = filter(lambda x: x%2, feet)

# Check the type of `uneven`
type(uneven)

# Print `uneven` as a list
print(list(uneven))
# [122375, 124015]


# Najpierw przepisujesz funkcję map(), której używasz do konwersji elementów listy stóp na liczby całkowite. Następnie, można zająć się funkcją filter(): Wziąć ciało funkcji lambda, użyć for i słowa kluczowe, aby logicznie połączyć x i stopy:
# Constructing `feet` 
feet = [int(x) for x in feet]

# Print `feet`
print(feet)

# Get all uneven distances
uneven = [x%2 for x in feet]

# Print `uneven`
print(uneven)
# [128608, 119750, 122375, 124015]
# [0, 0, 1, 1]


# 4) Reduce reduce() and Lambda Functions in Python
# Wreszcie, można również przepisać funkcje lambda, które są używane z funkcją reduce() do bardziej kompaktowych linii kodu. Spójrz na następujący przykład:
# Import `reduce` from `functools` 
from functools import reduce

# Reduce `feet` to `reduced_feet`
reduced_feet = reduce(lambda x,y: x+y, feet)

# Print `reduced_feet`
print(reduced_feet)
# [128608, 119750, 122375, 124015]
# 494748


# Construct `reduced_feet`
reduced_feet = sum([x for x in feet])

# Print `reduced_feet`
print(reduced_feet)
# 494748


# 5) Lista pojęć z warunkami 
# Define `uneven`
uneven = [x/2 for x in feet if x%2==0]

# Print `uneven` 
print(uneven)
# [64304.0, 59875.0]


# Initialize and empty list `uneven` 
uneven = []

# Add values to `uneven` 
for x in feet:
    if x % 2 == 0:
        x = x / 2
        uneven.append(x)

# Print `uneven` 
print(uneven)
# [64304.0, 59875.0]


# 6) Multiple If Conditions
# Teraz, gdy już zrozumieliście, jak można dodać warunki, nadszedł czas, aby przekształcić następujące dla pętli do zrozumienia listy z warunkami
divided = []

for x in range(100):
    if x%2 == 0 :
        if x%6 == 0:
            divided.append(x)

# Uważaj, widzisz, że poniższe dla pętli zawiera dwa warunki! Zastanów się dokładnie, jak zamierzasz to rozwiązać.
divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]

print(divided)
# [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]


# 7) If-Else Conditions
[x+1 if x >= 120000 else x+5 for x in feet]
# [128609, 119755, 122376, 124016]


# Przyjrzyjmy się teraz następującym fragmentom kodu, który jest przepisem powyższego fragmentu kodu:
for x in feet:  
    if x >= 120000:
        x + 1
    else: 
        x+5


# 8) Zagnieżdżone rozumienie listy
list_of_list = [[1,2,3],[4,5,6],[7,8]]

# Flatten `list_of_list`
[y for x in list_of_list for y in x]
# [1, 2, 3, 4, 5, 6, 7, 8]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
[[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


transposed = []

for i in range(3):
     transposed_row = []
     for row in matrix:
            transposed_row.append(row[i])
     transposed.append(transposed_row)



matrix = [[0 for col in range(4)] for row in range(3)]
matrix
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


for x in range(3):
    nested = []
    matrix.append(nested)
    for row in range(4):
        nested.append(0)


x = 0
matrix =[]
while x < 3:
    nested = []
    y = 0
    matrix.append(nested)
    x = x+1
    while y < 4:
        nested.append(0)
        y= y+1



[[int(x) for x in feet] for x in feet]
#* [[128608, 119750, 122375, 124015],
#  [128608, 119750, 122375, 124015],
#  [128608, 119750, 122375, 124015],
#  [128608, 119750, 122375, 124015]]



# 3 List comprehensions ----> https://www.w3schools.com/python/python_lists_comprehension.asp      -----> wazne
newlist = [expression for item in iterable if condition == True]

# Warunek
# Warunek jest jak filtr, który akceptuje tylko elementy, które mają wartość True.
#newlist = [x for x in fruits if x != "apple"]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# ['banana', 'cherry', 'kiwi', 'mango']
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# Warunek, jeśli x != "jabłko" powróci prawda dla wszystkich elementów innych niż "jabłko", dzięki czemu nowa lista zawiera wszystkie owoce z wyjątkiem "jabłko".

# Warunek jest opcjonalny i można go pominąć:
# newlist = [x for x in fruits]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
# ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Iterable 
# Iterable może być dowolnym obiektem iteralnym, takim jak lista, krotka, zestaw itp.
# Możesz użyć funkcji range(), aby utworzyć iteralną:
newlist = [x for x in range(10)]
print(newlist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ten sam przykład, ale z warunkiem:
# Akceptuj tylko liczby mniejsze niż 5:
# newlist = [x for x in range(10) if x < 5]
newlist = [x for x in range(10) if x < 5]
print(newlist)
# [0, 1, 2, 3, 4]

# Wyrażenie jest aktualnym elementem w iteracji, ale jest również wynikiem, który można manipulować zanim skończy się jak element listy na nowej liście:
# newlist = [x.upper() for x in fruits]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# Możesz ustawić wynik na cokolwiek chcesz:
# Set all values in the new list to 'hello':
# newlist = ['hello' for x in fruits]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
# ['hello', 'hello', 'hello', 'hello', 'hello']

# Wyrażenie może również zawierać warunki, nie takie jak filtr, ale jako sposób na manipulowanie wynikiem:
# Return "orange" instead of "banana":
# newlist = [x if x != "banana" else "orange" for x in fruits]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']


# # 4. Double comprehension ----> https://www.adamsmith.haus/python/answers/how-to-do-a-double-iteration-with-a-list-comprehension-in-python  
text = [["Hello", "World!"], ["Lets", "Eat!"]]
double_comprehension = [word for words in text for word in words]
print(double_comprehension)
# ['Hello', 'World!', 'Lets', 'Eat!']

#################################################################################################
# Модулі Python

# 1. Написати функцію process, яка на вхід приймає рядок. Насамперед усередині функції знайдіть найчастіше слово (модуль combinations) і винесіть код в окремий метод get_max_count_word.
import collections
import itertools
import random


def get_max_count_word(counts_dict):
    max_count = 0
    max_count_word = None
    for word, count in counts_dict.items():
        if count > max_count:
            max_count = count
            max_count_word = word
    return max_count_word


def get_max_count_word_combinations(words, max_count_word):
    combinations = itertools.combinations(words, 2)
    max_count_word_combinations = [comb for comb in combinations if max_count_word in comb]
    return max_count_word_combinations


def process(text):
    words = text.split(' ')
    counts = collections.Counter(words)
    max_count_word = get_max_count_word(counts)
    max_count_word_combinations = get_max_count_word_combinations(words, max_count_word)
    random_combination = max_count_word_combinations[random.randint(0, len(max_count_word_combinations)-1)]
    return random_combination


text = "blue cat is parked right behind the blue building with blue walls and red door"
rc = process(text)
print(rc)



# 2. Знайдіть в тексті всі комбінації (пари по 2 слова) із словом, що найчастіше зустрічається. Винесіть код окремим методом get_max_count_word_combinations, який поверне список кортежів.

import re
import math
import datetime

t = "I want to be a professor, but only one thing I can solve is x=exp(8)+sqrt(17)+log(5)"


def process(text):
    re_match = re.search('x=', text)
    equation = text[re_match.span()[1]:]
    ops = {'exp': math.exp, 'sqrt': math.sqrt, 'log': math.log}
    actions = equation.split('+')
    result = 0
    for action in actions:
        action = action.replace('(', ' ').replace(')', '')
        op, value = action.split(' ')
        result += ops[op](int(value))
    report = "Result = {response}; Date {date}".format(
        response=result,
        date=datetime.datetime.now().strftime('%d/%m/%y')
    )
    print(report)


process(t)


# Modul re 
import re

text = "Hi @mr_alex ! My name is John and I love coffee. #coffeelover #2021"

print(re.sub(r"[.!?\\-]", '', text))
print([e for e in re.finditer(r"#[A-Za-z0-9]*", text)])
print(re.split(r"[.!?\\-]", text))


# Modul math
import math

print(math.sqrt(16))
print(math.pi)
print(math.e)
print(round(2.1))
print(math.ceil(2.1))
print(math.floor(2.99999))
print(math.isnan(math.nan))
print(math.exp(2))
print(math.log(8, 2))

# Modul random 
import random

print(random.random())
print(random.randint(0, 10))
print(random.choice([1, 2, 3, 4, 5]))
random.seed(3)
seq = [1, 2, 3, 4, 6]
random.shuffle(seq)
print(seq)


#  Modul itertools
import itertools

combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))
permutations = itertools.permutations([1, 2, 3, 4], 2)
print(list(permutations))
print(list(itertools.combinations_with_replacement([1, 2, 3], 2)))
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda a, b: a - b)))
print(list(itertools.filterfalse(lambda x: x % 2, range(11))))


# Modul datetime
from datetime import datetime

now = datetime.now()
print(now)
print(datetime.time(now))
print(now.year, now.month, now.day)

date_string = "21 June, 2018"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)


# Modul collections
import collections

a = [1, 1, 2, 3, 3, 3]
counts = collections.Counter(a)
print(counts)

dict_of_lists = collections.defaultdict(list)
for value in range(1, 11):
    if value % 2 == 0:
        dict_of_lists['even'].append(value)
    else:
        dict_of_lists['odd'].append(value)
print(dict(dict_of_lists))

counts = collections.defaultdict(int)
for value in a:
    counts[value] += 1
print(counts)

d = collections.deque([1, 2, 3])
d.popleft()
d.append(4)
d.appendleft(6)
d.pop()
print(d)


#  Class Processor
class Processor:
    def __init__(self):
        pass

    def process(self):
        print('Process')

# Moja funkcja 
def my_function():
    print('Hello world')

#  Funkcja 
from lessons.L7.custom_module_example.my_module import my_function
from lessons.L7.custom_module_example.my_module_2.processors import Processor

my_function()
p = Processor()
p.process()


import collections
a = [1, 1, 2, 3, 3, 3]
counts = collections.Counter(a)
print(counts)

dict_of_lists = collections.defaultdict(list)
for value in range(1, 11):
    if value % 2 == 0:
        dict_of_lists['even'].append(value)
    else:
        dict_of_lists['odd'].append(value)
print(dict(dict_of_lists))

counts = collections.defaultdict(int)
for value in a:
    counts[value] += 1
print(counts)

d = collections.deque([1, 2, 3])
d.popleft()
d.append(4)
d.appendleft(6)
d.pop()
print(d)


#############################################################################################################################################################
# 008_Читання_та_запис_файлів_(Presentation) 
from xml.dom import minidom
from xml.etree import ElementTree

# my_doc = minidom.parse('my_file.xml')
#
# items = my_doc.getElementsByTagName('item')
# print(items)

data = ElementTree.Element('data')
items = ElementTree.SubElement(data, 'items')
item1 = ElementTree.SubElement(items, 'item')
item2 = ElementTree.SubElement(items, 'item')
item1.set('name', 'item1')
item2.set('name', 'item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

my_data = ElementTree.tostring(data)
with open('items2.xml', 'wb') as my_file:
    my_file.write(my_data)



{"data": [{"name": "Arthur", "age": 31}, {"name": "Kate", "age": 84}, {"name": "Alice", "age": 64}, {"name": "Mike", "age": 30}], "current_date": "12;05;21"}



[{"name":  "John", "age":  25}]



import json
filename = 'my_file.json'
with open(filename, 'r') as file:
    data = json.load(file)
data.append({"name": 'Alex', "age": 45})
print(data)
with open('my_file2.json', 'w') as file:
    json.dump(data, file)



import csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv_reader]
data.append(['Mike', '35', 'male'])
print(data)
with open('data.csv', 'w') as data_file:
    csv_writer = csv.writer(
        data_file,
        delimiter=','
    )
    for row in data:
        csv_writer.writerow(row)

import csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv_reader]
print(data)


text = "hello world"
print(text)
print(type(text))
b_text = text.encode(encoding='utf-8')
print(b_text)
print(type(b_text))

with open("test", "wb") as file:
    file.write(b_text)

with open("test", "rb") as file:
    t = file.read()
    print(t)
    print(type(t))



# Читання та запис файлів XML
# Читання 
from xml.etre import minidom 
my_doc = minidom.parse('items.xml')
items = my_doc.getElementsByTagName('item')
print(items)

# Запис 
from xml.etree import ElementTree
data = ElementTree.Element('data')
items = ElementTree.SubElement(data, 'items')
items1 = ElementTree.SubElement(data, 'items')
items2 = ElementTree.SubElement(data, 'items')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'
my_data = ElementTree.tostring(data)
with open("items2.xml","wb") as my_file:
    my_file.write(my_data)


<data> 
    <items> # trzeba dopisac 
        <item name='item1'>item1abc</item>
        <item name="item2">item2abc</item>
    </items>
</data>

import csv 
with open('data.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimeter=',')
    data = [row for row in csv_reader]
print(data)


# Читання та запис файлів CSV
import csv 
columns name = ['Name','Age','Gender'] 
data = [
    columns_names,
    ['John', 25, 'male'],
    ['Sally', 37, 'female'],
    ['Sarah', 19,'female'],
    ['Alex', 48,'male']
]
with open('data.csv', mode='w') as data_file:
    csv_writer = csv.writer(
        data_file,
        delimiter=','
    )
    for row in data:
        csv_writer.writerow(row) 
# Name, Age, Gender
# John,25,male
# Salle,37,female
# Sarah,19,female
# Alex,48,male

import random 
latters = 'fdsfsdfdsgsgqss' 
random_letters = ""
random_count = 25 
while len(random_letters) < random_count:
    random_letters = letters[random.randint(0,len(letters)-1)]
    random_letters += random_letter
with open('random_string','w') as text_file:
    text_file.write(random_letters)

import random 
import datetime
import json 
users = ['Artur','Kate','Alice','Mike']
users_list = []
for user in users :
    user_list.append({'name': user,'age': random.randint(1, 99)})
data = {
    'data':users_list,
    'current_date': datetime.datetime.now().strftime('%d;%m';%y)
}
filename = 'users_data_{current_date.json'.format(current_date=data['current_date'])
with open(filename, 'w') as json_file:
    json.dump(data, json_file)

import json 
import csv
with open('users_data_06;04;21.json','r') os file:
    data = json.load(file)
rows = []
for user in data ['data']:
    rows.append(list(user.values()))
rows = [list(data['data'][0].keys())]  + rows
with open ('users_data_{date}.csv'.format(date=data[current_date]), 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for row in rows:
        csv_writer.writerow(row) 


from xml.etree import ElementTree
import csv  

with open('users_data_06;04;21.csv', 'r') as file :
    reader = csv.reader(file, delimiter = ',')
    data = [row for row in reader]
columnw = data[0]
users = data[1:]
xml_data = ElementTree.Element('data')
items_data = ElementTree.SubElement(xml_data,'users')
items = [ElementTree.SubElement(items_holder, 'user') for i in range(len(users))]
for j in range(len(users)):
    item = items[j]
    for k in range(len(columns)):
        item.set(columns[k], users[j][k])
xml_file = ElementTree.tostring(xml_data)
with open('users.xml','wb') as file :
    file.write(xml_file)

# Read files: https://www.w3schools.com/python/python_file_open.asp
f = open("demofile.txt", "r")
print(f.read())

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))

f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Write files: https://www.w3schools.com/python/python_file_write.asp 
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())



f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())



# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
f = open("myfile.txt", "x")

f = open("myfile.txt", "w")



# JSON in Python: https://www.w3schools.com/python/python_json.asp 

import json
# Convert from JSON to Python:
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


# Convert from Python to JSON:
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# Working with JSON in Python: https://realpython.com/python-json/

#############################################################################################################################################################

#  #argument order.py
def printCar(brand,name = "concept",year = 1960 ,color="black"):
    print(brand,name,year,color)

printCar(name = "T",brand = "Ford",)
####################################################################################################

#Organiczenia sposobu przekazywania danych do fukcji - programista za pomocą / oraz *
# może okrelic dopuszczalne sposoby przekazywania argumentów do funkcji.

#Slash oznacza parametry tylko pozycyjne , ważna jest koejność tych parametrów i nie mogą być przekazywane
# jako argumenty nazwane.Uwaga parametry tylko pozycyjne umieszczane są przed / dzięki temu rozdziela para
# metry tylko pozycyjne od reszty parametrów.

def printData(string,number = 10 , /):
    print(string,number);
printData("Test",5) #działa prawidłowo,argumenty pozycyjne : Test 5

printData(string = "Test",number = 11) #bład nie mozna uzywac argumentów nazwanych'
####################################################################################################

#Gwiazdka oznacza argumenty nazwane ,musi byc umieszczona przed pierwszym parametrem ktory ma byc tak 
#przekazany

def printData(*,string,number = 10):
    print(string,number);
printData(string = "Test",number = 11) #działą prawidłowo : Test 11
printData("Test",5) #bład oa mają być przekaane jako nazwane

#parametry po gwiazdce muszą być przekazane jako argumenty nazwane
#parametry przed gwiazdką mogą być przekazane jako nazwane albo pozycyjne
def printData(float,bool,*,string,number = 10):
    print(float,bool,string,number);
printData(12.5,bool = True , string = "Test" , number = 11)      #12.5 True Test 11
printData(float = 12.5,bool=False,number = 11,string = "Test")   #12.5 False Test 11
printData(20.3,False,number=11,string = "Test")  #20.3 False Test 11
####################################################################################################

def printCar(brand, / ,name = "concept", * ,year = 1960 ,color="black"):
    print(brand,name,year,color)
#printCar(brand = "Ford","Mustang",color = "blue",year = 1974) -blad
printCar("Ford","Mustang",year = 1974,color = "blue")
#printCar("Ford",name="Mustang","blue",year = 1974) -blad

######################################################################################################

#operatory przy należności
#lista elementów (albo czy isnieją w tej liscie elementy)

data = [0,1,2,3,4,5]

print(-1 in data) #False nie isnieje tej liczby
print(3 in data ) #True istnieje 3
print("3" in ("3", "4")) #True

print(10 not in data) #pytamy czy 10 jest True bo niema
print(1 not in data)  #False poniewaz jest 1

######################################################################################################
#  #argument order.py
def printCar(brand,name = "concept",year = 1960 ,color="black"):
    print(brand,name,year,color)

printCar(name = "T",brand = "Ford",)
####################################################################################################

#Organiczenia sposobu przekazywania danych do fukcji - programista za pomocą / oraz *
# może okrelic dopuszczalne sposoby przekazywania argumentów do funkcji.

#Slash oznacza parametry tylko pozycyjne , ważna jest koejność tych parametrów i nie mogą być przekazywane
# jako argumenty nazwane.Uwaga parametry tylko pozycyjne umieszczane są przed / dzięki temu rozdziela para
# metry tylko pozycyjne od reszty parametrów.

def printData(string,number = 10 , /):
    print(string,number);
printData("Test",5) #działa prawidłowo,argumenty pozycyjne : Test 5

printData(string = "Test",number = 11) #bład nie mozna uzywac argumentów nazwanych'
####################################################################################################

#Gwiazdka oznacza argumenty nazwane ,musi byc umieszczona przed pierwszym parametrem ktory ma byc tak 
#przekazany

def printData(*,string,number = 10):
    print(string,number);
printData(string = "Test",number = 11) #działą prawidłowo : Test 11
printData("Test",5) #bład oa mają być przekaane jako nazwane

#parametry po gwiazdce muszą być przekazane jako argumenty nazwane
#parametry przed gwiazdką mogą być przekazane jako nazwane albo pozycyjne
def printData(float,bool,*,string,number = 10):
    print(float,bool,string,number);
printData(12.5,bool = True , string = "Test" , number = 11)      #12.5 True Test 11
printData(float = 12.5,bool=False,number = 11,string = "Test")   #12.5 False Test 11
printData(20.3,False,number=11,string = "Test")  #20.3 False Test 11
####################################################################################################

def printCar(brand, / ,name = "concept", * ,year = 1960 ,color="black"):
    print(brand,name,year,color)
#printCar(brand = "Ford","Mustang",color = "blue",year = 1974) -blad
printCar("Ford","Mustang",year = 1974,color = "blue")
#printCar("Ford",name="Mustang","blue",year = 1974) -blad



####################################################################################################

#pętla zagnieżdzona 
#Python pozwala na zagnieżdżone pętle

i = 0                                      #wyswietli się 0 1 2
while(i < 3):                                           # 0 1 2
    strData = ""                                        # 0 1 2
    j = 0
    while(j < 3):
        strData += " " + str(j)
        j += 1
    print(strData)
    i += 1


listsData = [                             #wpisac nie listData tylko listsData
    [0,1,2,3,4]
    ["Ola","Ala","Adam"]    
    [ 10, "Adam", 20 ,"Ania" ]
]
for listData in listsData :       #pobieramy jedną  listę ze wszystkich list (listsData)
    for v in listData:            #bedzie wyswietlone , od 0 od 4, , ola ala adam ,10 adam 20 ania z gory w dol
        print(v)   
    
####################################################################################################



