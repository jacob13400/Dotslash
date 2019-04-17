f = open("Write.py", "r+")
s = "\t" + f.read()
f.close()
s1 = "try:\n"
s2 = "except:\n \tprint(\"Syntax error\")"
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
import Run
Run.main()