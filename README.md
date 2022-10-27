# FunCaptcha Solver
## Credits
[`AcierP`](https://github.com/acierp) is the original creator, I just fixed the module so that it would actually solve.

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
