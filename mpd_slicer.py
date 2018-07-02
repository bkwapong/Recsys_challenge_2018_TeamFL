def write_file(f_name, lines, count):
	#print (count)
	file = open(f_name, "w")
	file.write("{")
	file.write("\n")
	for line in lines[:]:
		file.write(line)
		#file.write("\n")
	file.write("}")
	file.close()
	

if __name__ == '__main__':
	count = 0
	file_name = ""
	lines = []
	with open('mpd.txt', 'r') as mpd_file:
		while True:
			line = mpd_file.readline()
			# check if it is the end of the file
			if line == "":
				write_file(file_name, lines, count)
				lines = []
				break
			elif "./data/mpd.slice" in line:
				# remove all null characters
				line = line.replace("\00", "")
				if line[0] == "}":
					#print (len(lines))
					write_file(file_name, lines, count)
					lines = []
					sub_line = line[8:40].split(".")
					file_name = "1000_Playlists/mpd.slice."+str(sub_line[2])+".json"
				elif count == 0: # if it is the first time
					#print ("I'm here")
					file_name = "1000_Playlists/mpd.slice.315000-315999.json"
				count += 1
				#if count == 2:
				#	break
			else:
				if count > 0:
					lines.append(line)
	#print (len(lines))
	#print (count)

#mpd_file.close()
