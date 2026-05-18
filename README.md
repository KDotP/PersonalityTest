# Personality Test

This is a python-based personality test.

Personality question and type sources are listed below. List is neither exhaustive nor exclusive as many questions and types have been determined by the developer.

This is the source code. If you wish to run yourself, see below. Otherwise, a prebuilt verison should be provided.

---

## Spoilers

Since this is the bare code, if you are planning on taking the test you are highly advised **against** checking through files.

Several small hints and details are contained in the code which may deminish the suprise associated with coming upon them naturally.

---

## Excluded Files

In order to run this program, a `SECRETS.py` file is required. In this file, there must be a string variable called `WEBHOOK`.

WEBHOOK can be an empty string, or can be linked to your own Discord Webhook.

---

## How to Run
 
**Note that this version is the source code. A prebuilt version should be provided to you. Ensure you know what you are doing before using the terminal or running any files.**

This program runs in Python. Follow the steps below for your operating system.

*If you already have Python installed and know how to launch Python files, you may choose to skip to Step 4*
 
---
 
### Step 1 — Install Python
 
**Before Installing**
1. Open a terminal for your operating system.
2. Run the command `python --version` on Windows, or `python3 --version` on any other platform.
3. If a valid response returns, skip this section. If it returns an error, continue to the install steps below.

**Windows**
1. Go to [python.org/downloads](https://www.python.org/downloads/) and click the yellow **Download Python** button.
2. Run the installer. On the first screen, check the box that says **"Add Python to PATH"** before clicking Install — this is easy to miss and important.
3. Click **Install Now** and let it finish.
**macOS**
1. Go to [python.org/downloads](https://www.python.org/downloads/) and click the yellow **Download Python** button.
2. Open the downloaded `.pkg` file and follow the installer steps.
**Linux**
Python is likely already installed. You can check by opening a terminal and typing:
```
python3 --version
```
If you see a version number, you're good. If not, run:
```
sudo apt install python3
```
 
---
 
### Step 2 — Download the program
 
1. Navigate to the `<> Code` section in the top right of the Github page.
2. From the dropdown menu, select `Download ZIP`
3. To run files, unzip the downloaded program to an accessable location such as your desktop.
 
---
 
### Step 3 — Open a terminal

**Windows**
1. Open the folder where you saved `main.py`.
2. Click the address bar at the top of the File Explorer window, type `cmd`, and press Enter. A terminal window will open already pointed at the right folder.
**macOS**
1. Open the folder where you saved `main.py` in Finder.
2. Right-click (or Control-click) the folder and select **New Terminal at Folder**. If you don't see that option, open Terminal from Applications → Utilities, then type `cd ` (with a space), drag the folder into the terminal window, and press Enter.
**Linux**
Open a terminal and navigate to the folder with:
```
cd /path/to/your/folder
```
 
---
 
### Step 4 — Run the program
 
In the terminal, type the following and press Enter:
 
**Windows:**
```
python main.py
```
 
**macOS / Linux:**
```
python3 main.py
```
 
The test will start in the terminal window. Type the number of your answer and press Enter to respond to each question.
 
---
 
### Troubleshooting
 
**"Python is not recognized" (Windows)** — You likely missed the "Add Python to PATH" checkbox during installation. Uninstall Python and reinstall it, making sure to check that box.
 
**"No module named 'X'" (all platforms)** — This is expected if you're running the program outside of its intended environment. Let whoever gave you this know.
 
**The terminal closes immediately** — You probably double-clicked `main.py`, you may have to run it through the terminal instead. Go back to Step 3.
 
---
 
## Works Cited

* Goldberg, L. R. (1992). The development of markers for the Big-Five factor structure. Psychological Assessment, 4(1), 26–42. https://doi.org/10.1037/1040-3590.4.1.26
* Goldberg, L. R., et al. (2006). The International Personality Item Pool and the future of public-domain personality measures. Journal of Research in Personality, 40(1), 84–96. https://doi.org/10.1016/j.jrp.2005.08.007
* Donnellan, M.B. and Robins, R.W. (2010), Resilient, Overcontrolled, and Undercontrolled Personality Types: Issues and Controversies. Social and Personality Psychology Compass, 4: 1070-1083. https://doi.org/10.1111/j.1751-9004.2010.00313.x
* Costa, P.T., Jr., Herbst, J.H., McCrae, R.R., Samuels, J. and Ozer, D.J. (2002), The replicability and utility of three personality types. Eur. J. Pers., 16: S73-S87. https://doi.org/10.1002/per.448