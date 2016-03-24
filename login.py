# $language = "python"
# $interface = "1.0"

# To use, please change "PIN" value
# Automated script to login F5, cyclades, Cisco, Nexus, Juniper and A10 devices
# "Enter Destination" accepts hostname or ips
# Tab Name feature: Changes current Securecrt's tab name to the device's hostname you are connecting to automatically
# Improvements from v4: 
#	- Shorter and more efficient script than previous (window caption is changed globally instead of basing it on device type)
#	- Able to detect Nexus or devices already in enable mode and not send enable to Screen
# Improvements from v5: able to login automically to F5s and Cyclades

import re

def main():
	
	PIN = str(1572)
	objTab = crt.GetScriptTab()  #Returns the tab from which the script was started.
	tab = objTab.Screen  #Allows us to type "tab.xxx" instead of "objTab.Screen.xxx"
	global dest
	unixID = "elim2"
	
	def setTabName():
		global index
		global rawResult
		tab.WaitForCursor() # readstring captures all string in rawResult after cursor position change is detected
		rawResult = tab.ReadString(["#", ">"])# Stops reading when it sees # or >
		index = tab.MatchIndex	# MatchIndex is a property of ReadString. Returns integer. Here, "#" is 1; ">" is 2	
		tmpResult = rawResult.split()# rawResult is split and gets the last line of capture using [-1]
		result = tmpResult[-1]
		crt.Window.Caption = result.replace("elim2@","")# Juniper hostname contains "elim2@", display only the hostname using replace
		return;
		
	def chkDigit():
		rdest = dest.replace(".","")
		boolean_dest = rdest.isdigit()
		return boolean_dest;
	
	def testF5():
		sdest = dest.split(".")
		iSF5 = (sdest[0] == "10") and (sdest[1] == "251")
		return iSF5;
		
	def testCyc():
		chkResult = re.search('.CAS', dest, re.IGNORECASE)
		return chkResult;
		
	tab.Synchronous = True
	dest = str(crt.Dialog.Prompt("Enter Destination"))
###############################
	if dest == "":
		crt.Dialog.MessageBox("Please enter an ip or hostname")
		return
###############################
	if testCyc():
		crt.Window.Caption = str(dest)
		crt.Screen.Send("ssh root@" + dest + "\n")
		nIndex = crt.Screen.WaitForStrings(["yes/no", "password"], 6, False)
		if nIndex == 1:
			crt.Screen.Send("yes" + "\n")
			crt.Screen.WaitForString("password", 6, False)
			crt.Screen.Send("~p8/gPK" + "\n")
		else:
			crt.Screen.Send("~p8/gPK" + "\n")
		return
###############################
	if (chkDigit()) and (testF5()):
		crt.Screen.Send("ssh root@" + dest + "\n")
		nIndex = crt.Screen.WaitForStrings(["yes/no", "password"], 6, False)
		if nIndex == 1:
			crt.Screen.Send("yes" + "\n")
			crt.Screen.WaitForString("password", 6, False)
			crt.Screen.Send("st4nh0l3" + "\n")
		else:
			crt.Screen.Send("st4nh0l3" + "\n")		
		crt.Screen.WaitForString("root@")
		szResult = crt.Screen.ReadString(":")
		crt.Window.Caption = szResult
		return
###############################
	rsa = str(crt.Dialog.Prompt("Enter RSA Passcode Only"))
	code = (PIN + rsa)
	tab.Send("ssh " + unixID + "@" + dest + "\n")
	nIndex = crt.Screen.WaitForStrings(["yes/no", "password"], 6, False)
	if nIndex == 1:
		crt.Screen.Send("yes" + "\n")
		crt.Screen.WaitForString("password", 6, False)
		crt.Screen.Send(code + "\n")
	else:
		crt.Screen.Send(code + "\n")
	setTabName()

# Sends 'enable' if and only if the hostname ends with '>' AND it is not a Juniper device
	if ((index == 2) and not("JUNOS" in rawResult)): 
		tab.Send("enable" + "\n")
		tab.WaitForString("password", 3, False)
		crt.Sleep(50)
		tab.Send(code + "\n")
	else:
		return
		
	tab.Synchronous = False
	
main()

