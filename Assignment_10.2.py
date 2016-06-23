# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Desired Output:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)
dic = {}
for line in fhandle:
	if line.startswith("From "):
		hour = line.split()[5].split(":")[0]
		dic[hour]=dic.get(hour,0) + 1

lst = dic.items()
lst.sort()
for v,k in lst:
	print v, k