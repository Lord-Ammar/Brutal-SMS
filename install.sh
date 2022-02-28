#!usr/bin/bash
#ini cuma buat install module yg eror
echo -e "[•] Installing Data..."
pkg update &> /dev//null
pkg upgrade &> /dev//null
pkg install git &> /dev//null
pkg install bash &> /dev//null
pkg install python &> /dev//null
pkg install python2 &> /dev//null
pip install requests &> /dev//null
pip2 install requests &> /dev//null
pip install bs4 &> /dev//null
pip2 install bs4 &> /dev//null
pip install colorama &> /dev//null
pip2 install colorama &> /dev/null
echo -e "[•] Done Installing Data..."
