#!/usr/bin/env python3
# coding=utf-8

import cgi
import athletemodel
import yate
import cgitb

cgitb.enable()

athletes = athletemodel.get_from_store()

from_data = cgi.FieldStorage()
athlete_name = from_data['Which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("athlete: " + athlete_name + " DOB " + 
		athletes[athlete_name].dob + "."))
print(yate.u_list(athletes[athlete_name].top3()))
print(yate.include_footer({"Home":"/index.html",
		"Select another athlete":"generate_list.py"}))