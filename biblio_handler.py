import win32gui
import math
import time
from ctypes import Structure, c_long, byref
import ctypes
import os
import sys
user32=ctypes.WinDLL("user32")
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
def callback(hwnd, extra):
    nazwa = win32gui.GetWindowText(hwnd)
    chain = str(hwnd) + "; " + nazwa
    handler.append(chain)
    #ZWRACA HWND I NAZWA OKNA
def main():
    global handler
    handler = []
    win32gui.EnumWindows(callback, None)
#opcje
def rozpoznaj_wymiar(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = int(rect[0]) #x lewego gornego rogu okna
    y = int(rect[1]) #y lewego gornego rogu okna
    w = int(rect[2]) #x prawego dolnego rogu okna
    h = int(rect[3]) #y prawego dolnego rogu okna
    return x,y,w,h
#znajdz item wyswietl i pokaz miejsce
def f(name):
    for item in handler:
        if item.find(name)>0:
            print(item,"index na liscie:", handler.index(item))
            #chain = item +";" + "index na liscie:" + str(handler.index(item))
#znajdz item i zwroc hwnd
def fhwnd(name):
    for item in handler:
        if item.find(name)>0:
            i=item.split(";")
            ret=int(i[0])
            return ret
def pokieruj(name):
    hwnd = fhwnd(name)
    user32.ShowWindow(hwnd,3)#zmniejsza do wartosci default
    time.sleep(1)
    user32.SetForegroundWindow(hwnd)#ustawia pozycje okna na widoczna
    x,y,h,w = rozpoznaj_wymiar(hwnd)
    z=int((h-x)/2)
    user32.SetCursorPos(x+z,y+10)
def move(x,y,krok):
    pt=POINT()
    pt.x=0
    pt.y=0
    ix=0
    iy=0
    maxx=0
    maxy=0
    wspolczynnik=0
    user32.GetCursorPos(byref(pt))
    wx = int(pt.x)
    wy = int(pt.y)
    maxx = int(math.fabs(x-wx)**2)
    maxy = int(math.fabs(y-wy)**2)
    kroky=krok
    if wy>y:
        kroky=kroky*-1
    if wx>x:
        krok=krok*-1
    print("max:",maxx,
          "may:",maxy,
          "wx:",wx,
          "wy:",wy,
          "krok:",krok,
          )
    wukong=1
    zrob_tak=1
    if (not maxx==0 and not maxx==-1 and not maxx==1) and zrob_tak==1:
        wspolczynnik=float(y-wy)/float(x-wx)
        for ix in range(1, x-wx,krok):
            iy=wy + int(wspolczynnik*ix)
            if wukong==1:
                time.sleep(0.001)
                wukong=0
            else:
                time.sleep(0.0)
                wukong=1
                zrob_tak=0
            user32.SetCursorPos(wx+ix,iy)  
    if (not maxy==0 and not maxy==-1 and not maxy==1) and zrob_tak==1:
        wspolczynnik=float(x-wx)/float(y-wy)
        for iy in range(1, y-wy,kroky):
            ix=wx + int(wspolczynnik*iy)
            if wukong==1:
                time.sleep(0.001)
                wukong=0
            else:
                zrob_tak=0
                time.sleep(0.0)
                wukong=1
            user32.SetCursorPos(ix,wy+iy)
def grab_window(name,x,y):
    main()
    pokieruj(name)
def play(input):
    string="!@#$%^&*()"
    wix=list(input)
    
    steps.insert(253, "257, 13, 0")
    steps.insert(253, "256, 13, 0")
    for char in reversed(wix):
        chain_down = "256,  "+str(ord(char.upper()))+", 0"
        chain_up = "257,  "+str(ord(char.upper()))+", 0"
        if char.isupper():
            steps.insert(253,"257, 161, 0")
            steps.insert(253,chain_up)
            steps.insert(253,chain_down)
            steps.insert(253,"256, 161, 0")
        elif string.find(char)>=0:
            chain_down = "256,  "+str(ord(str(string.find(char)+1)))+", 0"
            chain_up = "257,  "+str(ord(str(string.find(char)+1)))+", 0"
            steps.insert(253,"257, 161, 0")
            steps.insert(253,chain_up)
            steps.insert(253,chain_down)
            steps.insert(253,"256, 161, 0")
        else:
            steps.insert(253, chain_up)
            steps.insert(253, chain_down)    
    wukong=1
    for step in steps[:-1]:
        s = step.split(", ")
        what = int(s[0])
        x = int(s[1])
        y = int(s[2])
        #print (opozniacz)
        #myszka dziala w grach
        #problem polegal na zlym okresleniu eventu myszy zamiast 0x10 bylo po prostu 10
        if what == 512:
            ctypes.windll.user32.SetCursorPos(x,y)
        if what == 513:# mouse left_down
            ctypes.windll.user32.SetCursorPos(x,y)
            ctypes.windll.user32.mouse_event(0x02,x,y,0,0)
        if what == 514:# mouse left_up        
            ctypes.windll.user32.SetCursorPos(x,y)
            ctypes.windll.user32.mouse_event(0x04,x,y,0,0)
        if what == 516:# mouse right down
            ctypes.windll.user32.SetCursorPos(x,y)
            ctypes.windll.user32.mouse_event(0x08,x,y,0,0)
        if what == 517:# mouse right up
            ctypes.windll.user32.SetCursorPos(x,y)
            ctypes.windll.user32.mouse_event(0x10,x,y,0,0)
        #klawiatura nie dziala w grach
        #dla DirectX sa inne oznaczenia
        #nalezy dodac funkcje sprawdzajaca jaki to rodzaj aplikacji czy korzysta z directx
        #nalezy dodac tablice konwersji znakow na directx
        #http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
        if what == 256 or what == 260:# keyboard down
            ctypes.windll.user32.keybd_event(x, 0, 0, 0)
        if what == 257:# keyboard up
            ctypes.windll.user32.keybd_event(x, 0, 0x0002, 0)
        if wukong==1:
            time.sleep(0.015)
            wukong=0
        else:
            time.sleep(0.0)
            wukong=1
    ctypes.windll.user32.SetCursorPos(810,545)
