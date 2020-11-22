.PHONY: clean all test

all: README.html test

test: tests/test_LaTeXDatax.py LaTeXDatax/datax.py
	pip install .
	python $<

README.html : README.md
	md2html --github $< -o $@

clean :
	rm -f __pycache__ README.html
