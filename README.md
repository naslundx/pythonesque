# pythonesque - Write code in other languages in python-style syntax!

Have you ever wished you could write C++ like follows:

```
def main():
  i = 0
  j = 5
  while i < j:
    i += 1
```

No? That means you're a sane person. But if you feel a bit more crazy, try this!

## How to test

1. Clone this repo (`git clone https://github.com/naslundx/pythonesque`) and enter it (`cd pythonesque`)

2. Check out the example (`cat test.cpp`)

3. Run the script (`python3 test.cpp`)

4. Check the generated file (`cat outtest.cpp`)

5. Compile and see it run! (`g++ outtest.cpp -std=-std=c++1y && ./a.out`)
