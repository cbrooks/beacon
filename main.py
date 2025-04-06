from ota import OTAUpdater
from screen_saver_balls import *
from screen_saver_cubes import *
from weather_main import ShowWeather
from num_pad_v2 import * # Lo res 240x240

SSID = ""
PASSWORD = ""
firmware_url = "https://raw.githubusercontent.com/cbrooks/beacon/main"

#from num_pad_v3 import * # Hi res 480x480
# version 1.1 - yeah, it worked!
if __name__ == "__main__":
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")
    ota_updater.download_and_install_update_if_available()
    print("**BEGIN**")
    ScreenSaverCubes()
    ScreenSaverBalls()
#     digs = get_digs("test")
#     print(digs)
    ShowWeather()

    print("END!")

