#/usr/bin/sh
# Build arabic-roots package

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 

# convert roots.txt into programming language tables:
#python
build:
	echo "#!/usr/bin/env python" > output/roots_const.py
	echo "# -*- coding: utf-8 -*-" >> output/roots_const.py
	scripts/makelist.sh data/roots.txt >> output/roots_const.py
	cp python/roots_const.py python/roots_const.py.bak
	cp output/roots_const.py roots_const.py
	

install:
	sudo python setup.py install
install3:
	sudo python3 setup.py install
# Publish to github
publish:
	git push origin master 

wheel:
	sudo python setup.py bdist_wheel
wheel3:
	sudo python3 setup.py bdist_wheel
sdist:
	sudo python setup.py sdist
upload:
	echo "use twine upload dist/PyArabic-0.6.1.tar.gz"
	
test:
	pytest pyarabic/test_araby.py
doc:
	epydoc -v --config epydoc.conf
