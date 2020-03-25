import winreg
from getTime import dt_from_win32_ts

hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\Explorer\RunMRU")
print("Key Name: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU")
subkeyCnt, valuesCnt, modtime = winreg.QueryInfoKey(hkey)

dt = dt_from_win32_ts(modtime)
print('Last Modified Time: ', dt.strftime('%Y-%m-%d %H:%M:%S.%f'))
  

for n in range(valuesCnt):
	value = winreg.EnumValue(hkey,n)
	print(value[1])
winreg.CloseKey(hkey)
