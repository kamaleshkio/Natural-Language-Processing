import re
def extract_domain(email):
    pattern = r"@([A-Za-z0-9]+)\.com"
    match = re.sub(pattern," ", email)
    print(match)

email = "manjeet@gfg.com"
print(extract_domain(email))