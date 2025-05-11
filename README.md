# AutoSearch for Microsoft Rewards

**AutoSearch** is a Python-based automation script that simulates random searches on Bing using Selenium WebDriver. It opens a new browser tab for each search to mimic natural user behavior and helps users passively collect Microsoft Rewards points.

> ⚠️ This tool is for educational purposes only. Automating searches may violate Microsoft's terms of service. Use responsibly.

---

## 🔧 Features

- Automates Microsoft Bing searches
- Randomized search queries to mimic human behavior
- Opens each search in a new browser tab
- Customizable number of searches and delays
- Supports Microsoft Edge or Chrome (with WebDriver)

---

## 🧰 Requirements

- Python 3.x
- Selenium library
- Microsoft Edge 
- Corresponding WebDriver (`msedgedriver.exe` )

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/auto-search-rewards.git
   cd auto-search-rewards
   ```
2. **Install dependencies**
   ```bash
   pip install selenium
   ```
3. **Download WebDriver**
   - For Edge: Download msedgedriver
   - Make sure the version matches your browser version
   - Place the .exe in the project folder
## 🚀 Usage

1. **Edit the script if needed**
   - Modify the list of search terms in the script.
   - Change the number of searches as needed.
   - Ensure the correct path to your WebDriver is set (e.g., `./msedgedriver.exe`).

2. **Run the script**
   ```bash
   python bing_automation.py
   ```
