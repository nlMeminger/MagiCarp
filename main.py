import gui
import btdevice
import systemhost
import media_control

def main():
    sys = systemhost.SystemHost()
    sys.setVolume(25)
    sys.setBrightness(50)
   
   
    
    #bluetoothDev = btdevice.BtDevice(macAddress= 'A0:56:F3:60:8C:D8')
    #bluetoothDev.connectToPlayer()

    mainGui = gui.Gui(sysHost = sys)

if __name__ == "__main__":  

    try:
        main()
    except KeyboardInterrupt:
        exit(0)