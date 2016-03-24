# $language = "python"
# $interface = "1.0"

def main():

#	shCmdList = crt.Dialog.Prompt("Enter log file name:")

	crt.Screen.Synchronous = True

	shCmdList = crt.Dialog.FileOpenDialog(title="slect file",filter="Text Files(*.txt)|*.txt||")
	cmd = open(shCmdList, "r")
	
	for line in cmd:
		crt.Screen.Send(line + '\r')
		crt.Screen.WaitForString("#")
		crt.Sleep(1200)
		
	crt.Screen.Synchronous = False		
main()
