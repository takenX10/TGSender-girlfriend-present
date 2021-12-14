# TGSender-girlfriend-present
A telegram bot to send pictures and videos automatically. It sends all the pictures/videos taken in a month, starting from a date, and every day it sends all the pictures/videos of the next month. 

> e.g. you start the bot on the first  of november 2021 (1-11-2021), and the oldest image you uploaded was taken on april 2017 (4-2017), then the bot on first of november 2021 (1-11-2021) sends all the pictures from april 2017 (4-2017), on second of november 2021 (2-11-2021) sends all the pictures from may 2017 (5-2017), ....


I made this to make a present for my girlfriend, we have been together for 5 years and I wanted to do something a little bit special for the 5th anniversary, and I thought it could be useful for someone else.

The code is a little bit crappy cuz I didn't have a lot of time to implement it, but it works, so yay don't flame me plz.

P.S.
She liked it a lot!! XD


## How to use
First of all you should install all the requirements.txt, it's only telepot so
- `sudo python3 -m pip install telepot`
or
- `sudo python3 -m pip install -r requirements.txt`

then you should install imagemagick and exiftool, on debian:
- `sudo apt install imagemagick`
- `sudo apt-get install libimage-exiftool-perl`

then:
1. cd inside the directory of the sources
2. Create a folder and name it `images`
3. Upload all the images inside `images` folder
4. cd inside the directory of the sources again
5. run runme.sh `sudo ./runme.sh` (its going to take a little bit of time depending on how many images you have)
6. add runme_crontab.sh to your crontab, once a day. (btw a good time to send all the pictures of the day for me and my girlfriend was 9am)
7. edit `variables.py` with your api key, telegram chat id and starting date of the script
   1. If you don't know how to create a telegram bot go [here](https://core.telegram.org/bots)
   2. If you don't know how to get the api key of a group chat go [here](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
8. That's it !

