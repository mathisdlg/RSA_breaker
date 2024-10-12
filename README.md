# RSA_breaker

A small tool to show how it's simple to break small rsa key

## Usage

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install sympy pycryptodome
```
Run those command or execute `nix-shell`(if you have nix package manager)

Next you need to run `python3 break_rsa.py` and follow the instruction

# Example

You can try the code with public_128.key and try to found the private message encrypt with this key.  
Good luck!