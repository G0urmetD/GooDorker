import argparse
from googlesearch import search as google_search
from colorama import init, Fore, Style

# Initialisiere Colorama für Windows
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

# Funktion zur Generierung der Google Dorks
def generate_dorks(domain):
    dorks = []

    # Suche nach Subdomains
    subdomain_dorks = [
        f'site:*.{domain} -www',
        f'site:*.*.{domain} -www',
        f'site:*.*.*.{domain} -www'
    ]
    dorks.extend(subdomain_dorks)

    # Suche nach typischen Dateiendungen
    file_dorks = [
        f'site:{domain} (filetype:pdf OR filetype:doc OR filetype:docx OR filetype:xls OR filetype:xlsx OR filetype:ppt OR filetype:txt OR filetype:odt OR filetype:pps OR filetype:xml)',
        f'site:{domain} (filetype:asp OR filetype:aspx OR filetype:php OR filetype:py OR filetype:bak OR filetype:conf OR filetype:eml OR filetype:log OR filetype:ps1 OR filetype:reg OR filetype:sql)'
    ]
    dorks.extend(file_dorks)

    return dorks

# Funktion zur Durchführung der Google-Suche und Ausgabe der Ergebnisse in der Kommandozeile
def perform_search(domain, rate_limit):
    dorks = generate_dorks(domain)

    # Suchanfragen durchführen
    for dork in dorks:
        print(f"{Fore.GREEN}[*] Searching for: {dork}")
        for url in google_search(dork, num=10, stop=10, pause=rate_limit):
            print(f"{Fore.YELLOW}{url}")
        print()  # Leere Zeile zwischen den Suchergebnissen

if __name__ == "__main__":
    # ASCII Banner ausgeben
    print(ascii_banner)

    # Argumente parsen
    parser = argparse.ArgumentParser(description='Google Dorking Tool')
    parser.add_argument('-d', '--domain', type=str, required=True, help='Domain to search for')
    parser.add_argument('-r', '--rate-limit', type=float, default=5.0, help='Rate limit in seconds between searches')
    args = parser.parse_args()

    # Suchen durchführen und Ergebnisse in Kommandozeile ausgeben
    perform_search(args.domain, args.rate_limit)
