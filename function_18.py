url = input()

def get_domain_name(url):
    url = url.replace('http://', '').replace('https://', '').replace('www.', '')
    url = url.split('.')
    return url[0]
#
# get_domain_name(url)

# url = url.replace('http://', '').replace('https://', '').replace('www.', '')
# url = url.split('.')
# print(url[0])
