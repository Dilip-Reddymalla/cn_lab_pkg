# cn-lab

A ready-to-use Computer Networks (CN) Lab Python package that bundles real socket programs and C++ NS-3 network simulations, making them installable and downloadable on **any computer** with a single command.

---

## 📦 What's Included?

When this package is installed, the following real lab experiment files are included:
* **`client.py`**: TCP Chat Client using Python sockets
* **`server.py`**: TCP Chat Server using Python sockets
* **`gobackn.cc`**: Go-Back-N Sliding Window Protocol simulation for NS-3 with NetAnim support
* **`stopandwait.cc`**: Stop-and-Wait ARQ Protocol simulation for NS-3 with NetAnim support
* **`star.cc`**: Star Topology CSMA Ethernet Switch simulation for NS-3 with NetAnim
* **`smtp.cc`**: Direct SMTP client protocol implementation in C (raw sockets)

---

## 🚀 Installation

Install this package directly from GitHub onto **any computer or OS** (Windows, Linux, macOS) by opening a terminal/command prompt and running:

```bash
pip install git+https://github.com/Dilip-Reddymalla/cn_lab_pkg.git
```

> **Note**: Requires Python 3.7+ and Git installed on the system.

---

## 📥 How to Download / Extract the Files

Once installed, navigate to the folder where you want your lab files and run:

### Command:
```bash
cn-download
```
*(or `cn-extract`)*

All 6 lab files will immediately be extracted to your current working directory:
```text
Downloading/Extracting 6 CN lab files to: C:\Users\Username\Documents\CN_Lab
  -> client.py
  -> gobackn.cc
  -> server.py
  -> smtp.cc
  -> star.cc
  -> stopandwait.cc

All files successfully saved in: C:\Users\Username\Documents\CN_Lab
```

### Specifying a target directory:
You can also provide a target folder path:
```bash
cn-download "D:\College\CN_Lab"
```

---

## 💻 Running the Programs

### 1. Python TCP Chat (Client & Server)
Open two separate terminals:

* **Terminal 1 (Server):**
  ```bash
  python server.py
  ```
* **Terminal 2 (Client):**
  ```bash
  python client.py
  ```
  Enter `127.0.0.1` (or server IP) and port `12345` when prompted.

---

### 2. NS-3 Simulations (`gobackn.cc`, `stopandwait.cc`, `star.cc`)
Copy the `.cc` files to your NS-3 `scratch/` directory:
```bash
cp gobackn.cc ~/ns-allinone-3.x/ns-3.x/scratch/
cd ~/ns-allinone-3.x/ns-3.x/
./ns3 run scratch/gobackn.cc
```
Open the generated `.xml` trace files (`go-back-n-animation.xml`, `star-topology.xml`, etc.) using **NetAnim** for visual playback.

---

### 3. SMTP Mail Client (`smtp.cc`)
Compile with GCC/G++ on Linux:
```bash
g++ smtp.cc -o smtp_client
./smtp_client
```

---

## 🐍 Python Import API

You can also interact with the package inside Python scripts:

```python
import cn_lab

# 1. Download all files to current directory
cn_lab.export_all_files(".")

# 2. List all bundled files
print(cn_lab.list_files())

# 3. Find the exact path where files are installed on your system
print(cn_lab.get_bundle_dir())

# 4. Networking utility: check local IP
print("My IP:", cn_lab.get_local_ip())
```
