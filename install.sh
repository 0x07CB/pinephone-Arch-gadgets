#!/bin/bash
echo "installation de rush-script..."
sudo cp gadgets/rush-script/rush-script /usr/bin/rush-script
sudo chmod a+x /usr/bin/rush-script

echo "installation des backlight-hack..."
sudo mkdir -p /etc/pinephone-gadgets
sudo cp gadgets/backlight-hack/*.py /etc/pinephone-gadgets/
echo " --- installation de strobe..."
sudo ln -s /etc/pinephone-gadgets/strobe.py /usr/bin/strobe
sudo chmod a+x /etc/pinephone-gadgets/strobe.py
sudo chmod a+x /usr/bin/strobe
echo " --- installation de blink..."
sudo ln -s /etc/pinephone-gadgets/blink.py /usr/bin/blink
sudo chmod a+x /etc/pinephone-gadgets/blink.py
sudo chmod a+x /usr/bin/blink
echo " --- installation de zrandef..."
sudo ln -s /etc/pinephone-gadgets/zrandef.py /usr/bin/zrandef
sudo chmod a+x /etc/pinephone-gadgets/zrandef.py
sudo chmod a+x /usr/bin/zrandef

