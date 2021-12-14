#!/usr/bin/env python3
####################
# Author: takenX10 #
#	   ( )   _     #
#	  (_` )_('>    #
#	  (__,~_)8     #
#	    _YY_       #
####################


import os
import sys
import json


imgfolder = ''
json_name = ''

# Returns the date of the image
# Date format YYYY:MM:DD
def image_data(image_name):
	# sudo apt install imagemagick
    # sudo apt-get install libimage-exiftool-perl
	
	if(".mp4" in image_name):
		cmd = os.popen(f'exiftool {image_name}')
		output = cmd.read()
		return output.split("File Modification Date/Time     : ")[1][:10]
	else:
		cmd = os.popen(f'identify -verbose {image_name}')
		output = cmd.read()
	if 'DateTime:' in output:
		return output.split('DateTime: ')[1][:10]
	elif 'modify:' in output:
		return output.split('modify: ')[1][:10].replace('-',':')
	else:
		print("ERROR: Can't find image data of image: "+image_name)
		return '0001:01:01'

# List all the images inside the imgfolder
def list_images():
	images = []
	for i in os.listdir(imgfolder):
		images.append(i)
	images_number = len(images)
	return images, images_number

# Returns the sorted json with all the parsed dates and names
def create_json(images_list, number_of_images):
	images_json_list = {'val':[]}
	j = 1
	for i in images_list:
		print('current image: '+str(j)+'/'+str(number_of_images)+'\t\t'+i)
		data = {
			"name": i,
			"date": image_data(imgfolder+'/'+i)
		}
		j += 1
		images_json_list['val'].append(data)

	images_json_list['val'].sort(key=lambda x: x['date'])
	return images_json_list


def main():
	# Getting arguments
	global imgfolder
	global json_name
	
	if(len(sys.argv) < 2):
		print("Usage: python3 imgparser.py <root directory>")
		return
	
	imgfolder = sys.argv[1] + "/images"
	json_name = sys.argv[1] + "/parsed_images.json"

	images_list, number_of_images = list_images()

	json_list = create_json(images_list, number_of_images)

	with open(json_name, 'w') as json_file:
		json.dump(json_list, json_file)

if __name__ == '__main__':
	main()
