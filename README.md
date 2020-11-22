# LaTeXDatax.py
Import calculated values from a python script into a LaTeX document.
This is a python interface for [the datax LaTeX package [ctan]](https://ctan.org/pkg/datax).

## Installation
One method that works, though it may not be *the way* in python, is downloading the repo, and running `pip install .` in the root directory of it.

## Usage
In a python script:
```python
from LaTeXDatax import datax
datax(
		filename = "data.tex",
		a = "Literal string",
		b = 3.141592,
		c = (3.141592,"\\meter"),
		d = (3.141592,"\\meter","%.2g"),
		e = (3.141592,"%.2g"),
     )
```

In the LaTeX document:
```tex
\documentclass{article}
\usepackage{siunitx}
\usepackage{datax}
\begin{document}
	The length was measured as \(d=\datax{d}\).
\end{document}
```

## Looking for contributors
I don't know python very well. This should be a working package, but it would probably be better in more comfortable hands.
Specifically, I'm not sure how to distribute packages in the python ecosystem.

