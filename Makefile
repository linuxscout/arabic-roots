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
	

# Publish to github
publish:
	git push origin master 

khoja:DATA=khoja
khoja:
	# look for inexistant roots in our data base
	cat docs/khoja/quad_roots.txt docs/khoja/tri_roots.txt >/tmp/${DATA}.txt
	tokenize.sh /tmp/${DATA}.txt >output/${DATA}.txt

	python python/compare.py -f output/${DATA}.txt > output/${DATA}.diff

sarfbase:DATA=sarfbase
sarfbase:
	# look for inexistant roots in our data base
	cat docs/khoja/quad_roots.txt docs/khoja/tri_roots.txt >/tmp/${DATA}.txt
	tokenize.sh docs/sarfbase/${DATA}.txt >output/${DATA}.txt

	python python/compare.py -f output/${DATA}.txt > output/${DATA}.diff
merge:DATA=merge
merge:
	# look for inexistant roots in our data base
	cat output/khoja.diff output/sarfbase.diff >output/${DATA}.txt

	python python/compare.py -f output/${DATA}.txt > output/${DATA}.diff
merge_all:
	cat output/merge.diff data/roots.txt > output/roots.txt.new
	echo "If it's ok, copy output/roots.txt.new"
