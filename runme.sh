echo "/usr/bin/env python3 $(pwd)/telegram_sender.py $(pwd)" > runme_crontab.sh
chmod +x runme_crontab.sh
/usr/bin/env python3 $(pwd)/imgparser.py $(pwd)