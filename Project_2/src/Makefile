DESTDIR = $(HOME)
SHELL = /bin/bash

###############################################################################
.PHONY: all clean install

all:
	apt update
	apt install python3-pip doxygen graphviz
	pip3 install -r requirements

pack:
	sh script.sh
	doxygen
	rm -rf ../xducho07_xjudaj00_xnedel09* ../repo
	mkdir ../repo
	cd .. && zip -r ./repo/xducho07_xjudaj00_xnedel09.zip ./ -x "*__pycache__*" "*doc*" "*install*" "*repo*"
	cd ../repo && unzip xducho07_xjudaj00_xnedel09.zip && rm xducho07_xjudaj00_xnedel09.zip
	mkdir -p ../xducho07_xjudaj00_xnedel09/install 2>/dev/null
	cd .. && mv repo doc xducho07_xjudaj00_xnedel09
	cd .. && mv install/install.deb xducho07_xjudaj00_xnedel09/install/install.deb
	cd .. && zip -r xducho07_xjudaj00_xnedel09.zip xducho07_xjudaj00_xnedel09 && rm -rf xducho07_xjudaj00_xnedel09

clean:
	rm -rf ../doc ../install/install.deb ../install/usr ../install/tmp

test:
	python3 test.py

doc:
	doxygen

run:
	python3 calcmain.py

profile:
	python3 deviation.py < input10.txt
	python3 deviation.py < input100.txt
	python3 deviation.py < input1000.txt

install:
	sh script.sh
