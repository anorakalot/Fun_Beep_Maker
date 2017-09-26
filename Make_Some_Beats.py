import os
cmd_1 = "beep -f 32.70"
cmd_2 = "beep -f 261.63"
cmd_3 = "beep -f 4000"
check = True

while check:
	a = raw_input("1,2,3 to play notes, 0 to quit")
	if a == "1":
		os.system(cmd_1)
	elif a == "2":
		os.system(cmd_2)
	elif a == "3":
		os.system(cmd_3)
	elif a == "0":	
		check = False
	else:
		None

