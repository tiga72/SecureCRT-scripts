# $language = "python"
# $interface = "1.0"

# PasteWithEchoFlowControl.py
# For every line sent, script checks for the last word in line, use str[-1]
# this acts as a form of over flow control

import SecureCRT
import time

SCRIPT_TAB = crt.GetScriptTab()

def main():

	nStartTime = time.time()
	
	SCRIPT_TAB.Screen.Synchronous = True
	
	for line in open("C:\\Users\\engseng.lim\\Desktop\\Apps\\Scripts for CRT\\RW\\ilo-push.txt", "r"):
		SCRIPT_TAB.Screen.Send(line + '\r')

		if line != "":
			checkLastWord = line[-1]
			SCRIPT_TAB.Screen.WaitForString(checkLastWord, 3)		
		
		else:
			continue
		
#		SCRIPT_TAB.Screen.WaitForString('\r', 1)
#		SCRIPT_TAB.Screen.WaitForString('\n', 1)		
			
	SCRIPT_TAB.Screen.Synchronous = False

	crt.Sleep(2500)
	nTimeElapsed = time.time() - nStartTime
	timeSec = (nTimeElapsed/60)
	timeTook = (str(timeSec))[:4]
	crt.Dialog.MessageBox("Time took %s minutes" % timeTook)
	
main()
