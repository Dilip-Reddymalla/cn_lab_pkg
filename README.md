# cn-lab

A ready-to-use Computer Networks (CN) Lab package designed for **Ubuntu / Linux**. It bundles real socket programs and NS-3 network simulations, making them installable and downloadable with a single command.

---

## 📦 What's Included?

When this package is installed, the following 6 lab files are ready to extract:
* **`client.py`**: TCP Chat Client (Python sockets)
* **`server.py`**: TCP Chat Server (Python sockets)
* **`gobackn.cc`**: Go-Back-N Sliding Window Protocol simulation for NS-3 with NetAnim XML output
* **`stopandwait.cc`**: Stop-and-Wait ARQ Protocol simulation for NS-3 with NetAnim XML output
* **`star.cc`**: Star Topology CSMA Ethernet Switch simulation for NS-3 with NetAnim
* **`smtp.cc`**: Direct SMTP client protocol implementation in C using POSIX sockets

---

## 🐧 Installation on Ubuntu

Ubuntu 20.04, 22.04, and 24.04 include Python 3 by default. Open a terminal (`Ctrl+Alt+T`) and run:

### 1. Ensure `pip` and `git` are installed:
```bash
sudo apt update
sudo apt install python3-pip git -y
```

### 2. Install the package:
```bash
pip3 install git+https://github.com/Dilip-Reddymalla/cn_lab_pkg.git
```
*(On Ubuntu 24.04+ or if you see an `externally-managed-environment` warning, add `--break-system-packages` or use a venv)*:
```bash
pip3 install git+https://github.com/Dilip-Reddymalla/cn_lab_pkg.git --break-system-packages
```

---

## 📥 Downloading / Extracting the Lab Files

In Ubuntu, open terminal in any folder where you want your lab experiments and run:

```bash
cn-download
```
*(or `cn-extract`)*

If `~/.local/bin` is not yet in your `$PATH`, you can also run:
```bash
python3 -m cn_lab.downloader
```

All 6 files will immediately be saved into your current folder:
```text
Downloading/Extracting 6 CN lab files to: /home/ubuntu/cn_lab
  -> client.py
  -> gobackn.cc
  -> server.py
  -> smtp.cc
  -> star.cc
  -> stopandwait.cc

All files successfully saved in: /home/ubuntu/cn_lab
```

---

## 🚀 Running on Ubuntu

### 1. Python TCP Chat (`server.py` & `client.py`)
Open two terminal tabs:

* **Tab 1 (Server):**
  ```bash
  python3 server.py
  ```
* **Tab 2 (Client):**
  ```bash
  python3 client.py
  ```
  Type `127.0.0.1` and port `12345`.

---

### 2. NS-3 Simulations (`gobackn.cc`, `stopandwait.cc`, `star.cc`)
NS-3 runs natively on Ubuntu.

1. Copy the `.cc` file to your NS-3 `scratch` folder:
   ```bash
   cp gobackn.cc ~/ns-allinone-3.*/ns-3.*/scratch/
   cp stopandwait.cc ~/ns-allinone-3.*/ns-3.*/scratch/
   cp star.cc ~/ns-allinone-3.*/ns-3.*/scratch/
   ```

2. Run the simulation:
   ```bash
   cd ~/ns-allinone-3.*/ns-3.*/
   ./ns3 run scratch/gobackn.cc
   ```

3. View animation in **NetAnim**:
   ```bash
   cd ~/ns-allinone-3.*/netanim-*/
   ./NetAnim
   ```
   Open the generated XML file (`go-back-n-animation.xml` or `star-topology.xml`).

---

### 3. SMTP Mail Client (`smtp.cc`)
Compile and run with `g++` (uses standard Linux POSIX headers `<sys/socket.h>`, `<arpa/inet.h>`, `<unistd.h>`):

```bash
g++ smtp.cc -o smtp_client
./smtp_client
```

---

## 🐍 Python API Usage

You can also use it inside any Python script on Ubuntu:

```python
import cn_lab

# Extract all files into current directory
cn_lab.export_all_files(".")

# List all bundled files
print(cn_lab.list_files())

# Get your local IP address
print("Local IP:", cn_lab.get_local_ip())
```
