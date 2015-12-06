#!/usr/bin/env python3
# coding=utf-8

class Athlete:
    def __init__(self, a_name, a_dob=None, a_time=[]):
        #the code will initialize a "Athlete" class
        self.name = a_name
        self.dob = a_dob
        self.times = a_time
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
        return (sorted(set([self.sanitize(t) for t in self.times]))[0:3])
    def add_time(self, time_valve):
        self.times.append(time_valve)
    def add_times(self, list_of_times):
        self.tiems.extend(list_of_times)
        
def get_coach_data(filename):
    try:
        with open(filename)as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return Athlete(temp1.pop(0),temp1.pop(0),temp1)
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return None

james = get_coach_data('james.txt')
print(james.name + "s fastest times are: " + str(james.top3()))

