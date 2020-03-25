import winreg
from getTime import dt_from_win32_ts
	
hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
print("Key Name: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
subkeyCnt, valuesCnt, modtime = winreg.QueryInfoKey(hkey)

dt = dt_from_win32_ts(modtime)
print('Last Modified Time: ', dt.strftime('%Y-%m-%d %H:%M:%S.%f'))
 
# Retrieve the value tuples (name, value, type).
print('Program Name \t\t Path')
print('==============  \t ====')
for n in range(valuesCnt):
	value = winreg.EnumValue(hkey,n)
	print(value[0],'\t\t', value[1])
winreg.CloseKey(hkey)