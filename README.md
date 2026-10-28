# cn-lab

Computer Networks Lab Suite bundling all real client, server, and C++ NS-3 simulation files.

## Bundled Real Files Included in this Package:
* `client.py` - Real socket client chat code
* `server.py` - Real socket server chat code
* `gobackn.cc` - Go-Back-N sliding window protocol simulation (NS-3)
* `stopandwait.cc` - Stop-and-Wait protocol simulation (NS-3)
* `star.cc` - CSMA star topology simulation (NS-3)
* `smtp.cc` - Raw C socket SMTP mail sender client

---

## Installation on Any System

### From GitHub (One single command on any machine):
```bash
pip install git+https://github.com/<your-username>/<repo-name>.git#subdirectory=cn_lab_pkg
```

### Or Local Folder Installation:
```bash
cd cn_lab_pkg
pip install .
```

---

## How to Download / Extract the Files on Any System

Once installed, anyone on any machine can run:

```bash
cn-download
```
or:
```bash
cn-extract
```
This instantly copies all 6 real files (`client.py`, `server.py`, `gobackn.cc`, `stopandwait.cc`, `star.cc`, `smtp.cc`) into their current folder!

You can also specify a folder destination:
```bash
cn-download "C:\my_cn_lab"
```

---

## Python Usage

You can also access or extract them within Python:

```python
import cn_lab

# List all bundled real files
print(cn_lab.list_files())

# Extract all files into the current folder or a specific directory
cn_lab.export_all_files("./lab_codes")

# Get path where files are installed inside site-packages
print(cn_lab.get_bundle_dir())
```
