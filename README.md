# mkpass

A small, dependency-free command-line password generator.

Built on Python's [`secrets`](https://docs.python.org/3/library/secrets.html)
module for cryptographically strong randomness. Standard library only — no
`pip install`, just run the script.

## Requirements

- Python 3.8+

## Usage

```console
$ python3 mkpass.py                  # one 16-char password
$ python3 mkpass.py -l 24            # 24 chars long
$ python3 mkpass.py -n 5             # five passwords
$ python3 mkpass.py -l 20 -s        # include symbols
$ python3 mkpass.py -l 20 -s -e     # also print estimated entropy
```

## Options

| Flag                | Description                          |
| ------------------- | ------------------------------------ |
| `-l, --length N`    | password length (default: 16)        |
| `-n, --count N`     | how many to generate (default: 1)    |
| `--no-lower`        | exclude lowercase letters            |
| `--no-upper`        | exclude uppercase letters            |
| `--no-digits`       | exclude digits                       |
| `-s, --symbols`     | include punctuation symbols          |
| `-e, --entropy`     | print estimated entropy to stderr    |

The entropy line is written to stderr, so stdout stays clean for piping:

```console
$ python3 mkpass.py -l 32 -s | pbcopy
```

## License

[MIT](LICENSE)
