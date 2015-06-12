# beleza
PyQt4 application for the bagtrekkin school project

## Getting started

Python version used : 2.7

#### Clone the repo

```bash
$ git clone git@github.com:yourusername/beleza.git
````

#### Set the virtual environment 

*this way to avoid /usr/include/python symlinking*.
Then activate it.

```bash
$ virtualenv --always-copy venv
$ source venv/bin/activate
```

#### Download and install sip (PyQt requirement) 


[`Download sip`](http://www.riverbankcomputing.com/software/sip/download) into your beleza folder


Then unpack and install it : 
```bash
$ tar zxvf sip-version.tar.gz
$ cd sip-version
$ python configure.py --incdir=../venv/include/python2.7
$ make
$ make install
$ cd ..
```

You can check ['sip documentation'](http://pyqt.sourceforge.net/Docs/sip4/) to get more infos.


#### Download and install PyQt4


[`Download PyQt4`](http://www.riverbankcomputing.com/software/pyqt/download) into your beleza folder


Then unpack and install it : 
```bash
$ tar zxvf PyQt-blablaversion.tar.gz
$ cd PyQt-blablaversion
$ python configure.py 
$ make
$ make install
```


You can check [`PyQt4 documentation`](http://pyqt.sourceforge.net/Docs/PyQt4/) to get more infos.

#### You're done !

You can check everything's well by trying to import some Qt modules :

```bash
$ python
````
```python
>>> from PyQt4 import QtCore, QtGui
>>> type(QtCore)
<type 'module'>
>>>
```

If you get this, everything's OK. Let's make a procrastinating pause !



