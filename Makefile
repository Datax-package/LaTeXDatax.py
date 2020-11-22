.PHONY: clean all

all: README.html

README.html : README.md
	md2html --github $< -o $@

clean :
	rm -f __pycache__ README.html
