# datax.py
import sys

def printvariable(tag,variable,f):
    """
    Prints variable named "tag" with value "variable" to an iostream "f",
    as a pgfkey, so that it can easily be read by the datax LaTeX package.

    Parameters
    ----------
    tag : str
        The name of the variable, by which it will be called in the tex source.
    variable :
        Either a naked string, which will be stored as is,
        a naked number, which will be wrapped in siunitx's `\\num`,
        or a tuple with 2 or 3 members:
        (number, unit, format),
        (number, unit) or
        (number, format);
        which will be wrapped in siunitx's `\\SI` or `\\num`.

        number :
            the numeric value of the variable
        unit : str
            a string on `\\SI` format, so `\\joule\\per\\meter\\cubed`
        format : str
            a C-style format string for the number, by default `%.4g`

        In a two member tuple, the second argument will be assumed to be the format
        if it contains a '%' (the unit '%' is written as `\\percent`).
    """
    if not isinstance(variable,tuple):
        if isinstance(variable,str):
            print('\\pgfkeyssetvalue{/datax/%s}{%s}'%(tag,variable),file=f)
            return
        if 'pint' in sys.modules: # Is this entire block an illegal waste of resources? Maybe. Will it cause more overhead time than I have already spent seeking a better solution? No.
            from pint import Quantity
            if isinstance(variable, Quantity):
                print('\\pgfkeyssetvalue{{/datax/{}}}{{{:Lx}}}'.format(tag,variable),file=f) # ignores format specification
                return
        number = variable
        unit = ''
        form = '%.4g'
    else: # variable is tuple
        if len(variable) == 3:
            number = variable[0]
            unit = variable[1] # Assumes number, unit, format
            form = variable[2]
        else:
            if '%' in variable[1]:
                number = variable[0]
                unit = ''
                form = variable[1]
            else:
                number = variable[0]
                unit = variable[1]
                form = '%.4g'
    if len(unit)==0:
        formatstring = '\\pgfkeyssetvalue{/datax/%s}{\\num{'+form+'}}' 
        print(formatstring%(tag,number),file=f)
        return
    formatstring = '\\pgfkeyssetvalue{/datax/%s}{\\SI{'+form+'}{%s}}'
    print(formatstring%(tag,number,unit),file=f)

def printvariables(filename,**variables):
    """
    Do `printvariable` for each of the given keyword arguments.

    NB! filename is not a string, but an iostream. It is named thusly to minimize the number of names unavailable to the user.
    """
    print('% File auto-generated by LaTeXDatax.py. Will be overwritten.',file=filename)
    for tag,variable in variables.items():
        printvariable(tag,variable,filename)

def datax(filename="data.tex",**variables):
    """
    Print the given variables to a file to be read by the `datax` LaTeX package.
    """
    with open(filename, "w", encoding="utf-8") as f:
        printvariables(f,**variables)
