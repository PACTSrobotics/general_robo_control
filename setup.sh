sudo apt install supervisor
git pull
sudo ln -s /home/pi/general_robo_control/general_robo_control.conf /etc/supervisor/conf.d/ 
sudo pip3 install -r requirements.txt
sudo supervisorctl update
sudo supervisorctl reread 
