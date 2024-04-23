# GooDorker
Small tool to automate google dorks search with one input parameter for the domain.

## Installation
```Bash
pip3 install -r requirements.txt
```

## gooDorker.py
```Bash
# start google dork search with domain input (rate limit default = 5 seconds)
python3 gooDorker.py -d example.com

# start google dork search with domain input and rate limit to 10 seconds
python3 gooDorker.py -d example.com -r 10
```

## gooDorker-api.py
1. Open up (https://developers.google.com/custom-search/v1/overview) and follow the instructions to activate a Google Custom Search JSON API for a new/current project
2. Create a new API key under "APIs & Servcices" -> "Credentials" in the Google Cloud console
3. Create a new programmable search engine (https://programmablesearchengine.google.com)
4. use the API key with the -k/--api-key parameter
5. use the programmable search engine id with the -c/--cse-id parameter

```Bash
# start google dork search with domain input (rate limit default = 5 seconds)
python3 gooDorker-api.py -d example.com -k <API-KEY> -c <Search-Engine-ID>

# start google dork search with domain input and rate limit to 10 seconds
python3 gooDorker-api.py -d example.com -k <API-KEY> -c <Search-Engine-ID> -r 10
```

## Known Issues
- the rate limit can be very annoying. Play around with the rate-limit parameter. If you had to many requests, grab a cup of coffee and wait.
