# install: generate_help
install: download generate_help
	cd /tmp/ && \
		git clone https://github.com/Suyash458/WiktionaryParser && \
		cd WiktionaryParser && \
		git checkout 72e5f74 && \
		sudo -H python3 ./setup.py install
	sudo -H pip3 install -e ".[all]"

download: download/websters_unabridged_dictionary_by_various.txt.utf-8
	:

download/websters_unabridged_dictionary_by_various.txt.utf-8:
	python3 ./vim_dictionary/download_dictionary.py
	touch download/websters_unabridged_dictionary_by_various.txt.utf-8

generate_help: doc/tags
	:

doc/tags:
	vim -i NONE -u NONE --cmd "helptags ./doc/" --cmd "q!"

clean: backup
	find . -iname "__pycache__" -print0 | xargs -0 rm -rf
	find . -iname "*.pyc" -print0 | xargs -0 rm -rf
	rm -rf /tmp/WiktionaryParser || true
	rm -rf ./vim_dictionary.egg-info ./doc/tags ./download/* ./dist ./build || true

backup:
	cp -rf ./download/ /tmp

test: download
	bash -x ./tests/test.sh
