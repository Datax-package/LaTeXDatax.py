.PHONY: clean all test publish

all: README.html test dist/

dist/ : setup.py LaTeXDatax/datax.py
	python $< sdist bdist_wheel

test: tests/test_LaTeXDatax.py LaTeXDatax/datax.py
	pip install .
	python $<

README.html : README.md
	md2html --github $< -o $@

publish : clean dist/
	python -m twine upload dist/*

clean :
	rm -rf __pycache__/ LateXDatax/__pycache__/ README.html LaTeXDatax.egg-info/ build/ dist/
