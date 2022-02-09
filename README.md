# LaTeXDatax.py

Import calculated values from a python script into a LaTeX document. This is a
python interface for [the datax LaTeX package
[ctan]](https://ctan.org/pkg/datax).

## Installation
```
pip install LaTeXDatax
```

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

## Pint integration
```python
from pint import Quantity
from LaTeXDatax import datax
datax(filename = "data.tex", E = Quantity(24,"kg m / s^2"))
```

Works as you would hope, in large part because of how well
[pint](https://pint.readthedocs.io/) implements siunitx strings. Hat off.

## Looking for contributors
I don't know python very well. This package works, but if you have ideas for
how to improve it, or you spot some python faux pas, feel free to make a PR or
get in touch!

