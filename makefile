# TODO: automatically generate help files.
install: download
	:

download: download/websters_unabridged_dictionary_by_various.txt.utf-8
	:

download/websters_unabridged_dictionary_by_various.txt.utf-8:
	python3 ./vim_dictionary/download_dictionary.py
	touch download/websters_unabridged_dictionary_by_various.txt.utf-8:

clean: backup
	find . -iname "__pycache__" -print0 | xargs -0 rm -rf
	find . -iname "*.pyc" -print0 | xargs -0 rm -rf
	rm ./download/*

backup:
	cp -rf ./download/ /tmp

test: download
	bash ./tests/test.sh
