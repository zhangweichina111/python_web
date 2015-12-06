#!/usr/bin/env python3
# coding=utf-8

class AthleteList(list):
	"""docstring for AthleteList"""
	def __init__(self, a_name, a_dob=None, a_times=[]):
		super(AthleteList, self).__init__()
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	def sanitize(self, time_string):
		if '-' in time_string:
			splitter = '-'
		elif ':' in time_string:
			splitter = ':'
		else:
			return time_string
		(mins,secs) = time_string.split(splitter)
		return (mins + '.' + secs)
	def top3(self):
		return (sorted(set([self.sanitize(t) for t in self]))[0:3])
def get_coach_data(filename):
	try:
		with open(filename)as f:
			data = f.readline()
		temp1 = data.strip().split(',')
		return AthleteList(temp1.pop(0),temp1.pop(0),temp1)
	except IOError as ioerr:
		print('File Error: ' + str(ioerr))
		return None
if __name__ == '__main__':
	james = get_coach_data("james.txt")
	print(james.name + "s fastest times are: " + str(james.top3()))
