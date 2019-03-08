import urllib.request
import urllib.parse

# response = urllib.request.urlopen('https://www.python.org')

# print(type(response))
#
# print(response.read().decode('utf-8'))
#
# print(response.status)
#
# print(response.getheaders())
#
# print(response.getheader('Server'))


# data 参数
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data = data)
print(response.read())


# timeout 参数
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

