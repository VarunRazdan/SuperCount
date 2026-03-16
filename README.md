# 📚 SuperCount

> Analyze word count and character frequency for any text file — books, articles, scripts, and more.

[![Latest Release](https://img.shields.io/github/v/release/VarunRazdan/SuperCount)](https://github.com/VarunRazdan/SuperCount/releases)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/VarunRazdan/supercount/pulls)

---

## Demo

<!-- TODO: Record a demo GIF with `asciinema` or `terminalizer` and embed it here -->

```
=========== SUPERCOUNT ===========
Analyzing: books/frankenstein.txt
----------- Word Count -----------
Found 78094 total words
--------- Character Count --------
e: 46043
t: 30365
a: 26743
o: 25985
i: 25226
n: 24433
s: 23110
...
============== END ===============
```

---

## Features

- **Word count** — total words in any `.txt` file
- **Character frequency** — sorted breakdown of all alphabetic characters
- **Multi-file support** — analyze several files in one command
- **Glob patterns** — use `books/*.txt` to process entire directories at once
- **Zero dependencies** — pure Python standard library, no installs needed beyond Python itself
- **Fast** — processes full-length novels in milliseconds

---

## Installation

### Download a pre-built binary (no Python needed)

Go to the [Releases page](https://github.com/VarunRazdan/SuperCount/releases) and download the binary for your OS:

| Platform | File |
|----------|------|
| macOS    | `supercount-macos` |
| Linux    | `supercount-linux` |
| Windows  | `supercount-windows.exe` |

**macOS/Linux:** make it executable first:
```bash
chmod +x supercount-macos  # or supercount-linux
./supercount-macos <file.txt>
```

### Python users (clone & run)
```bash
git clone https://github.com/VarunRazdan/SuperCount.git
cd SuperCount
python3 main.py <file.txt>
```

---

## Usage

### Single file

```bash
supercount <file.txt>
```

### Multiple files

```bash
supercount <file1.txt> <file2.txt>
```

### Glob pattern

```bash
supercount <dir>/*.txt
```

### Recursive glob

```bash
supercount "<dir>/**/*.txt"
```

---

## Sample Output

```
=========== SUPERCOUNT ===========
Analyzing: books/frankenstein.txt
----------- Word Count -----------
Found 78094 total words
--------- Character Count --------
e: 46043
t: 30365
a: 26743
o: 25985
i: 25226
n: 24433
s: 23110
r: 21631
h: 20092
l: 14580
...
============== END ===============
```

---

## Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

[MIT](LICENSE) © 2026 VarunRazdan
