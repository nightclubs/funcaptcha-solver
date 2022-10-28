# FunCaptcha Solver
## Credits
[`AcierP`](https://github.com/acierp) is the original creator, I just fixed the module so that it would actually solve.


## Installation

download the funcapsolver folder and audios folder, and make a new file with those folders in the same directory. Then input  
```python
from funcapsolver import *
``` 
at the top of your brand new file. Congrats now you just initiated the solver (read the examples below on how to solve).

## Examples (all taken straight from acier's github repo!)

#### Obtaining an unsolved captcha token
```python
token = funcapsolver.get_token(host='api.funcaptcha.com', pkey='69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC')
```

#### Solving a captcha and returning the captcha response
```python
token = funcapsolver.get_token('api.funcaptcha.com', '69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC')
solved = funcapsolver.solveCaptcha(token)
print(solved)
``` 

##### If you want to use threading, I suggest you ignore all exceptions due to rate limits and shit.

## Updates
1. full requests-based python funcaptcha solver using images instead of audio!! (working on this rn!)
2. update this and add google speech to text api.
