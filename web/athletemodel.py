#!/usr/bin/env python3
# coding=utf-8

import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		temp1 = data.strip().split(',')
		return AthleteList(temp1.pop(0),temp1.pop(0),temp1)
	except IOError as ioerr:
		print('File Error: ' + str(ioerr))
		return None

def put_to_store(file_list):
	all_athletes = {}
	for each_file in file_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle','wb') as athf:
			pickle.dump(all_athletes,athf)
	except IOError as ioerr:
		print('file error (put_to_store):' + str(ioerr))
	return (all_athletes)
def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle','rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('file error (get_from_store)' + str(ioerr))
	return (all_athletes)

if __name__ == '__main__':
	the_files = ['james.txt','bran.txt']
	data = put_to_store(the_files)
	print(data)