import urllib.request
import settings
# noinspection PyBroadExceptio

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
def try_connection():
    if connect():
        pass
    else:
        if 'on' in settings.debug_mode:
            pass
        elif 'off' in settings.debug_mode:

            print("no internet,please try again or try again")
            exit()
        else:
            print("error on mode'",settings.debug_mode,"'")
            print("ERROR:you con only set debug_mode in on and off")
            exit()