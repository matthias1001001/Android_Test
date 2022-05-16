import subprocess
import time

def step(action):
    subprocess.call(["adb","shell","input","keyevent",action])

def wait():
    time.sleep(3)

def home():
    step("3")
    step("3")

def suche():
    home()
    wait()
    step("84")
    wait()
    step("44")
    step("47")
    step("51")
    step("66")
    wait()
    wait()
    home()

def camera():
    home()
    wait()
    step("27")
    step("66")
    step("66")
    step("22")
    step("66")
    wait()
    step("4")
    wait()
    home()

def maps():
    home()
    wait()
    step("22")
    step("22")
    step("22")
    step("66")
    step("22")
    step("22")
    step("22")
    step("66")
    wait()
    step("22")
    step("29")
    step("21")
    step("21")
    step("66")
    step("37")
    step("42")
    step("35")
    step("43")
    step("40")
    step("47")
    step("48")
    step("29")
    step("32")
    step("48")
    step("66")
    wait()
    wait()
    home()

def taschenrechner():
    home()
    step("93")
    step("19")
    step("66")
    wait()
    step("10")
    step("81")
    step("10")
    step("66")
    wait()
    home()

#taschenrechner()
suche()
#camera()
