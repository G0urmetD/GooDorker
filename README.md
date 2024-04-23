# GooDorker
Small tool to automate google dorks search with one input parameter for the domain.

## Installation
```Bash
pip3 install -r requirements.txt
```

## Usage
```Bash
# start google dork search with domain input (rate limit default = 5 seconds)
python3 gooDorker.py -d example.com

# start google dork search with domain input and rate limit to 10 seconds
python3 gooDorker.py -d example.com -r 10
```
