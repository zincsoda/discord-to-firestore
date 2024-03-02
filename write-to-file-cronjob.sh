# Added this to crontab 
# 0 * * * * ~/write_file.sh
cd ~/discord-to-firestore
. ./venv/bin/activate
python scheduled-date-to-firebase.py | tee ~/tmp/$(date '+%Y-%m-%d_%H-%M-%S').txt
