import winreg
import re
from getTime import dt_from_win32_ts

main_sub_key = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\Explorer\RecentDocs\\"
hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, main_sub_key)
subkeys = []
try:
    i = 0
    while True:
        asubkey = winreg.EnumKey(hkey, i)
        subkeys.append(main_sub_key+asubkey)
        i += 1
except WindowsError:
    pass


search = re.compile('[A-Za-z1-9._%+-]{4,}')
for key in subkeys:
	print()	
	print("""############################################################################""")
	print(key)
	print("""############################################################################""")
	hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
	
	subkeyCnt, valuesCnt, modtime = winreg.QueryInfoKey(hkey)
	dt = dt_from_win32_ts(modtime)
	print('Last Modified Time: ', dt.strftime('%Y-%m-%d %H:%M:%S.%f'))
  
	for n in range(valuesCnt):
		value = winreg.EnumValue(hkey,n)
		#print((value[1]).decode('cp850', errors='replace')[:70])
		wanted = str(value[1])
		found = re.findall(search, wanted)
		if found:
			print(str(n)+'. '+' '.join(x for x in found))
		
winreg.CloseKey(hkey)
