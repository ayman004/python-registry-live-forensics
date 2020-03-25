import winreg
from getTime import dt_from_win32_ts

def subkeys(key):
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            yield subkey
            i+=1
        except WindowsError as e:
            break

def traverse_registry_tree(hkey, keypath, tabs=0):
	key = winreg.OpenKey(hkey, keypath, 0, winreg.KEY_READ)
	subkeyCnt, valuesCnt, modtime = winreg.QueryInfoKey(hkey)
	for subkeyname in subkeys(key):
		path ="%s\\%s" % (keypath, subkeyname)
		mykey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
		subkeyCnt, valuesCnt, modtime = winreg.QueryInfoKey(mykey)
		
		for n in range(valuesCnt):
			value = winreg.EnumValue(mykey,n)
			if value[0] == 'Debugger':
				dt = dt_from_win32_ts(modtime)
				print('Last Modified Time: ', dt.strftime('%Y-%m-%d %H:%M:%S.%f'))
				print('Imagefile Execution Manipulation detected!!!')
				print('Application used:',path.split('\\')[-1])
				print('Path:',path)
				print('Application attacked:',value[1])
			

		subkeypath = "%s\\%s" % (keypath, subkeyname)
		traverse_registry_tree(hkey, subkeypath, tabs+1)

keypath = r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options"
print("key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options")
traverse_registry_tree(winreg.HKEY_LOCAL_MACHINE, keypath)