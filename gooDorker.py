import argparse
from googlesearch import search as google_search
from colorama import init, Fore, Style

# Initialize Colorama for Windows
init()

# ASCII Banner
ascii_banner = f"""
{Fore.CYAN}
   _____             _____             _             
  / ____|           |  __ \           | |            
 | |  __  ___   ___ | |  | | ___  _ __| | _____ _ __ 
 | | |_ |/ _ \ / _ \| |  | |/ _ \| '__| |/ / _ \ '__|
 | |__| | (_) | (_) | |__| | (_) | |  |   <  __/ |   
  \_____|\___/ \___/|_____/ \___/|_|  |_|\_\___|_|   
                                                     
                                                     
{Fore.RED}Author: G0urmetD (403 - Forbidden)
{Fore.RED}version: 1.0                                          
"""

# Function to generate Google Dorks
def generate_dorks(domain):
    dorks = []

    # Search for subdomains
    subdomain_dorks = [
        f'site:*.{domain} -www',
        f'site:*.*.{domain} -www',
        f'site:*.*.*.{domain} -www'
    ]
    dorks.extend(subdomain_dorks)

    # Search for typical file extensions
    file_dorks = [
        f'site:{domain} (filetype:pdf OR filetype:doc OR filetype:docx OR filetype:xls OR filetype:xlsx OR filetype:ppt OR filetype:txt OR filetype:odt OR filetype:pps OR filetype:xml)',
        f'site:{domain} (filetype:asp OR filetype:aspx OR filetype:php OR filetype:py OR filetype:bak OR filetype:conf OR filetype:eml OR filetype:log OR filetype:ps1 OR filetype:reg OR filetype:sql)'
    ]
    dorks.extend(file_dorks)

    return dorks

# Function to perform Google search and output results in the command line
def perform_search(domain, rate_limit):
    dorks = generate_dorks(domain)

    # Perform searches
    for dork in dorks:
        print(f"{Fore.GREEN}[*] Searching for: {dork}")
        for url in google_search(dork, num=10, stop=10, pause=rate_limit):
            print(f"{Fore.YELLOW}{url}")
        print()  # Empty line between search results

if __name__ == "__main__":
    # Print ASCII banner
    print(ascii_banner)

    # Parse arguments
    parser = argparse.ArgumentParser(description='Google Dorking Tool')
    parser.add_argument('-d', '--domain', type=str, required=True, help='Domain to search for')
    parser.add_argument('-r', '--rate-limit', type=float, default=5.0, help='Rate limit in seconds between searches')
    args = parser.parse_args()

    # Perform searches and output results in command line
    perform_search(args.domain, args.rate_limit)
