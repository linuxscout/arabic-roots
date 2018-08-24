# Arabic Roots List

## Description

Arabic roots List is a resource needed by many deveopers and researchers, here we provide this resource as a separate data, with usefull scripts.

###Citation
If you would cite it in academic work, can you use this citation

	Taha Zerrouki‏, Arabic roots list,  http://github.com/linuxscout/arabic-roots, 2018

or in bibtex format

	@misc{zerrouki2018arabicroots,
	  title={Arabic roots list},
	  author={Zerrouki, Taha},
	  url={http://github.com/linuxscout/arabic-roots},
	  year={2018}
	}


## Statistics 
All roots: 7504
3 letters roots: 5674
4 letters roots: 1830
## Files
* data/ : contains  data of roots
* scripts: scripts used to provide tools

## Data Structure
--------------
A text with one root by line.
The root is normalized which means all Hamzat are normalize to Hamza on line ء.

## How to update data

* check if the word doesn't exist in the minimal form data file ( classified/stopwords.ods)
* add affixation information
* run 
```
make
```
* catch the output of script in releases folder.

Thanks
 
