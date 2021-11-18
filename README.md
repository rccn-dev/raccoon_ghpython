## Raccoon GHPython

Load py functions from GitHub.

Add a new Grasshopper Python component and add the following code:

```python
import urllib2
response = urllib2.urlopen('https://raw.githubusercontent.com/raccoon-ncku/raccoon_ghpython/master/{}.py'.format(func))
code = response.read()
```

Add an input with name `func` and an output named `code`