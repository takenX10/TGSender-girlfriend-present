#!/usr/bin/env python3
####################
# Author: takenX10 #
#	   ( )   _     #
#	  (_` )_('>    #
#	  (__,~_)8     #
#	    _YY_       #
####################

import os
import json
import sys
import telepot
import time
from variables import *
from datetime import date
from dateutil.relativedelta import relativedelta

imgfolder = ''
json_name = ''

bot = telepot.Bot(api_token)

def parse_json(filename):
	with open(filename) as f:
		data = json.load(f)
	return data


# Date format: YYYY:MM:DD
def get_current_date():
	today = date.today()
	return today.strftime("%Y:%m:%d")

# return absolute distance in days from two dates formatted in my string format
def subtract_dates(d1, d2):
	d1 = [int(a) for a in d1.split(':')]
	d2 = [int(a) for a in d2.split(':')]
	date1 = date(d1[0],d1[1],d1[2])
	date2 = date(d2[0],d2[1],d2[2])
	return abs((date2 - date1).days)

# return the right year and month of the images you want to send today
def right_date(starting_date, current_date, starting_year):
	diff = subtract_dates(starting_date,current_date)
	d = [int(a) for a in starting_year.split(':')]
	sy = date(d[0],d[1],d[2])
	right = sy + relativedelta(months=+diff) 
	return (right.year, right.month)

def list_images():
	images = []
	for i in os.listdir(imgfolder):
		images.append(i)
	return images

def send_image(img, date):
	# print(f'Sending {img} (date = {date})...')
	if('.mp4' in img):
		bot.sendVideo(chat_id, open(imgfolder+'/'+img, 'rb'), caption=date)
	else:
		bot.sendPhoto(chat_id, photo=open(imgfolder+'/'+img,'rb'), caption=date)

# True -> the current date is before the start -> you shouldn't send anything
def test_current_date(current, start):
	d1 = [int(a) for a in current.split(':')]
	d2 = [int(a) for a in start.split(':')]
	date1 = date(d1[0],d1[1],d1[2])
	date2 = date(d2[0],d2[1],d2[2])
	if((date1 - date2).days < 0):
		return True
	return False

def main():
	# Getting arguments
	global imgfolder
	global json_name
	
	if(len(sys.argv) < 2):
		print("Usage: python3 telegram_sender.py <root directory>")
		return
	
	imgfolder = sys.argv[1] + "/images"
	json_name = sys.argv[1] + "/parsed_images.json"

	current_date = get_current_date()

	if(test_current_date(current_date, starting_date)):
		# print(str(subtract_dates(current_date,starting_date) + " left until start!"))
		return
	else:
		pass
		# print("Day "+str(subtract_dates(current_date,starting_date)))

	images_json = parse_json(json_name)
	starting_year = images_json['val'][0]['date']
	year, month = right_date(starting_date, current_date, starting_year)
	# print('Sending photos from '+str(year)+'/'+str(month))
	acc = 0
	for i in images_json['val']:
		data = i['date']
		data = [int(a) for a in data.split(':')]
		if(data[0] == year and data[1] == month):
			acc += 1
			data = i['date'].split(':')
			data = data[2]+'/'+data[1]+'/'+data[0]
			send_image(i['name'],data)
			time.sleep(1)
			if(acc == 20):
				# Necessary otherwise the script gets blocked
				time.sleep(35)
				acc = 0

if __name__ == '__main__':
	main()


