from datetime import datetime

#To input the program number
n=input()
sz="Pg1.txt"
sz=sz[:2]+n+sz[3:]

f = open(sz, "r+")
s = "\t" + f.read()
f.close()
s1 = "try:\n"
s2 = "\nexcept :\n \tprint(\"Syntax error, mate. Check again. In the meantime, here's a fun fact to keep you occupied: \")\n \tprint(\"One of the guys in charge here, is definitely trying to kill you. Good luck figuring out who it is.\")"
s3 = ""
s4 = ""
s5 = "def main():\n"
s_final = "\t"
c = -1
l = len(s)
for i in range(l):
	if s[i] == "\n" and i != l-1:
		s3 = s3 + s[c+1:i+1] + "\t" 
		c = i
s3 = s3 + s[c+1:] + "\n"
s4 = s1 + s3 + s2
l = len(s4)
c = -1
for i in range(l):
	if s4[i] == "\n" and i != l-1:
		s_final = s_final + s4[c+1:i+1] + "\t"
		c = i
s_final = s_final + s4[c+1:]
s_final = s5 + s_final
f1 = open("Run.py", "w+")
f1.write(s_final)
f1.close()


try:
	import Run

except:
	print("Syntax error, mate. Check again. In the meantime, here's a fun fact to keep you occupied: ")
	print("One of the guys in charge here, is definitely trying to kill you. Good luck figuring out who it is.")

else :
	Run.main()

f=open("log.txt","a")
utc_time = datetime.utcnow()
f.write("\n")
f.write(str(sz)+"\tBUFFER\t")
f.write(str(utc_time))
