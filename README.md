# SuperCount

> Analyze word count and character frequency for any text file — books, articles, scripts, and more.

[![Latest Release](https://img.shields.io/github/v/release/VarunRazdan/SuperCount)](https://github.com/VarunRazdan/SuperCount/releases)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Features

- Word count and character frequency for any `.txt` file
- Analyze multiple files at once
- Glob pattern support (e.g. `*.txt`)
- No dependencies — pure Python standard library

---

## Getting Started

### Option 1: Download the binary (no Python needed)

1. Go to the [Releases page](https://github.com/VarunRazdan/SuperCount/releases)
2. Download the file for your OS:

| OS      | File                     |
|---------|--------------------------|
| macOS   | `supercount-macos`       |
| Linux   | `supercount-linux`       |
| Windows | `supercount-windows.exe` |

3. Run it:

**macOS / Linux** — open a terminal in the folder where you downloaded it:
```bash
chmod +x supercount-macos
./supercount-macos myfile.txt
```

**Windows** — open Command Prompt in the folder where you downloaded it:
```
supercount-windows.exe myfile.txt
```

> Don't have a file handy? Just run the binary with no arguments and it will prompt you to enter a path.

---

### Option 2: Run from source (requires Python 3)

```bash
git clone https://github.com/VarunRazdan/SuperCount.git
cd SuperCount
python3 main.py myfile.txt
```

---

## Usage Examples

**Single file:**
```bash
./supercount-macos myfile.txt
```

**Multiple files:**
```bash
./supercount-macos file1.txt file2.txt
```

**All `.txt` files in a folder:**
```bash
./supercount-macos books/*.txt
```

---

## Sample Output

```
=========== SUPERCOUNT ===========
Analyzing: frankenstein.txt
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
