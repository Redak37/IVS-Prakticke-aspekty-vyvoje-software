mkdir -p ../install/usr/share/calcmain 2>/dev/null
mkdir -p ../install/usr/local/bin 2>/dev/null
mkdir -p ../install/tmp 2>/dev/null
cp requirements ../install/tmp/requirements.txt
cp calcmain-icon.png ../install/usr/share/calcmain/calcmain-icon.png
cp -t ../install/usr/share/calcmain/ *.py
ln -sf /usr/share/calcmain/calcmain.py ../install/usr/local/bin/calcmain
chmod a+x ../install/usr/share/
chmod a+x ../install/DEBIAN/postinst
dpkg-deb --build ../install ../install/install.deb
rm -rf ../install/tmp ../install/usr
