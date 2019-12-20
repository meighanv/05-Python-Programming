# # Request Library
# import requests
link = 'http://www.github.com'
# r = requests.get(link)
# print(r.status_code) #status
# #print(r.content[0:400])#actual content [0:400] prints the first 401 bytes in bytes
# print(r.url) #The URL queried
# print(r.history) #Shows historical r codes
# print(r.headers) # Provides server information as a dictionary ; r.headers['<Category>']
# print(r.request.headers) # provides client header infor as dict including cookie info
# print(r.encoding) #Provides page encoding
# #print(r.text) #prints content as string
# # r = requests.get(link, stream=True) #raw r 
# # r.raw.read(100) #shows the first 100 bytes in hex
# # There Doesn't appear any parsing in this library

"""
urllib module
"""
# Any of the following libraries can be passed by name into dir() to get info
import urllib.request as request
import urllib.error as error
import urllib.parse as urlparse
import urllib.robotparser as robot

dir(request) # list of the features
r = request.urlopen(link) #open link
c = request.urlopen(link).read() #open link and read content (in bytes) could have also done r.read()
r.getcode() # Obtain the response status code
r.code # same as above
r.geturl # states what was requested
r._method # shows the request method
r.getheaders() #Gets the response headers (server info)
r.getheader()['Content-Type'] #get a value for a specific key in head dict
r.info()['Content-Type'] # Same as above

# TRY EXCEPT FOR OPENING A URL
try:
    request.urlopen("https://www.pyrthon.ogr")
except error.URLError as e:
    print(e.reason)

### PARSING ###
amazon = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3dstripbooks-intl-ship&field-keywords=Pearson+Books"
print(urlparse.urlsplit(amazon))
# prints the output: SplitResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', query='url=search-alias%3dstripbooks-intl-ship&field-keywords=Pearson+Books', fragment='')
print(urlparse.urlparse(amazon)) #basically same as above

data = {'param1':'value1','param2':'value2'}
urlparse.urlencode(data)
# Output 'param1=value1&param2=value2'
urlparse.parse_qs(urlparse.urlencode(data))
# Output: {'param1': ['value1'], 'param2': ['value2']}
urlparse.urlencode(data).encode('UTF-8')
# Output: b'param1=value1&param2=value2'
urlparse.urljoin('http://localhost:8080/~cache/', 'data file') #create a url
# Output: 'http://localhost:8080/~cache/data file'
par = robot.RobotFileParser()
par.set_url('https://www.samsclub.com/robots.txt')
par.read() #reading the URL content
print(par)
# User-agent: *
# Allow: /ads.txt
# Allow: /sams/account/signin/createSession.jsp
# Disallow: /cgi-bin/
# Disallow: /sams/checkout/
# Disallow: /sams/account/
# Disallow: /sams/cart/
# Disallow: /sams/search/
# Disallow: /sams/eValues/clubInsiderOffers.jsp
# Disallow: /friend
# Disallow: /s/
# Disallow: /%2ASCDC%3D1%2A
# Allow: /sams/account/referal/
par.can_fetch('*','https://www.samsclub.com/friend/')
