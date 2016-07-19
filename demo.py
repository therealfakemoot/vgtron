import requests

def post(url, d):
    r = requests.post(url, data=d)
    return r

def write(url, d):
    d['write'] = 'true'
    d['key'] = '1234'
    d['value'] = '1234'
    return requests.post(url, d)

def read(url, d):
    d['read'] = 'true'
    return requests.post(url, d)


def main(url, test):
    data = {'loadtest':'true'}
    if test == 'w':
        r = write(url, data)
    elif test == 'r':
        r = read(url, data)

    with open('/home/ndumas5/public_html/results.html', 'w') as f:
        f.write(r.text)

if __name__ == '__main__':
    main('http://ndumas.com/', 'w')
