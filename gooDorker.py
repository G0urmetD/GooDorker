import argparse
import random
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
{Fore.RED}version: 1.2                                          
"""

# Function to read user agents from file
def read_user_agents(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

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

   # Search for public available sql stuff - still in test
    sql_dorks = [
        f'site:{domain} intitle:"index of" "/etc/mysql/"',
        f'site:{domain} intitle:"index of" "postgresql.conf"',
        f'site:{domain} intitle:"index of" "mysql.log" | "mysql.logs"',
        f'site:{domain} intext:backup.sql intitle:index.of'
    ]
    dorks.extend(sql_dorks)

   # Search for pages that have login/admin/password in title
    pages_dorks = [
        f'site:{domain} inurl:"login"',
        f'site:{domain} inurl:"admin"',
        f'site:{domain} inurl:"password"'
    ]
    dorks.extend(pages_dorks)

    # Search for pages that have login/admin/password in URL
    urlpages_dorks = [
        f'site:{domain} intitle:"login"',
        f'site:{domain} intitle:"admin"',
        f'site:{domain} intitle:"password"'
    ]
    dorks.extend(urlpages_dorks)

    # Search for information out of sql database files containing username password
    sqldatabasefiles_dorks = [
        f'site:{domain} filetype:sql intext:username password'
    ]
    dorks.extend(sqldatabasefiles_dorks)

    # Search for security cameras access
    securitycams_dorks = [
        f'site:{domain} inurl:/view/viewer_index.shtml'
    ]
    dorks.extend(securitycams_dorks)

    # Search for phpMyAdmin panels
    phpMyAdmin_dorks = [
        f'site:{domain} inurl:"/phpmyadmin/"'
    ]
    dorks.extend(phpMyAdmin_dorks)

    # Search for cacti device monitoring panels
    cactimonitoring_dorks = [
        f'site:{domain} inurl:"/cacti/"'
    ]
    dorks.extend(cactimonitoring_dorks)

    # Search for Cisco WebVPN services
    ciscowebvpn_dorks = [
        f'site:{domain} inurl:webvpn.html'
    ]
    dorks.extend(ciscowebvpn_dorks)

    # Search for .htpasswd files
    htpasswdfiles_dorks = [
        f'site:{domain} inurl:.htpasswd'
    ]
    dorks.extend(htpasswdfiles_dorks)

    # Search for PHP info pages
    phpinfopages_dorks = [
        f'site:{domain} inurl:"/phpinfo.php"'
    ]
    dorks.extend(phpinfopages_dorks)

    # Search for apache server status pages
    apacheserverstatus_dorks = [
        f'site:{domain} inurl:"server-status"'
    ]
    dorks.extend(apacheserverstatus_dorks)

    # Search for Jenkins script consoles
    jenkinsscriptconsole_dorks = [
        f'site:{domain} inurl:"/jenkins/script"'
    ]
    dorks.extend(jenkinsscriptconsole_dorks)

    # Search for zabbix monitoring software
    zabbixmonitoring_dorks = [
        f'site:{domain} inurl:"/zabbix/"'
    ]
    dorks.extend(zabbixmonitoring_dorks)

    # Search for wp-admin panel
    wpadminpanel_dorks = [
        f'site:{domain} intitle:"index of" "wp-admin"'
    ]
    dorks.extend(wpadminpanel_dorks)

    # Search for WordPress configuration files
    wpconfigurationfiles_dorks = [
        f'site:{domain} ext:conf inurl:wp-'
    ]
    dorks.extend(wpconfigurationfiles_dorks)

    # Search for ftp addresses
    ftpaddresses_dorks = [
        f'site:{domain} inurl:ftp://'
    ]
    dorks.extend(ftpaddresses_dorks)

    return dorks

# Function to perform Google search with a random user-agent
def perform_search(domain, rate_limit, user_agents):
    dorks = generate_dorks(domain)

    # Perform searches
    for dork in dorks:
        user_agent = random.choice(user_agents)
        print(f"{Fore.GREEN}[*] Searching for: {dork}")
        for url in google_search(dork, num=10, stop=10, pause=rate_limit, user_agent=user_agent):
            print(f"{Fore.YELLOW}{url}")
        print()  # Empty line between search results

if __name__ == "__main__":
    # Print ASCII banner
    print(ascii_banner)

    # Parse arguments
    parser = argparse.ArgumentParser(description='Google Dorking Tool')
    parser.add_argument('-d', '--domain', type=str, required=True, help='Domain to search for')
    parser.add_argument('-r', '--rate-limit', type=float, default=5.0, help='Rate limit in seconds between searches')
    parser.add_argument('--random', action='store_true', help='Use random user agents')
    parser.add_argument('-u', '--user-agents-file', type=str, default='user_agents.txt', help='File containing user agents')
    args = parser.parse_args()

    # Read user agents from file
    if args.random:
        user_agents = read_user_agents(args.user_agents_file)
    else:
        user_agents = None

    # Perform searches and output results in command line
    perform_search(args.domain, args.rate_limit, user_agents)
