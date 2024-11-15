
upgrade:
	pip wheel gls
	pip install --upgrade .



c: clean

clean:
	rm -f *~ .*~
	rm -f ./gls/*~
	rm -rf ./gls/__pycache__
	rm -f ./gls-*.whl
	rm -rf ./build
	rm -rf ./gls.egg-info
