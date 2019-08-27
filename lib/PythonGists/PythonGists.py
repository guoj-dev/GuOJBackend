import requests

try:
	import simplejson as json
except ImportError:
	import json
try:
	from .access import main as login 

except:
	from access import main as login 

API_URL='https://api.github.com'

class Gist(object):
	def __init__(self,url):
		self.gistUrl = url
		self.gistId = url.split('/')[-1]
	def __repr__(self):
		return '<Gist Object at {0}>'.format(self.gistUrl)
	def getRawJSON(self):
		return requests.get('{0}/gists/{1}'.format(API_URL,self.gistId)).json()
	def getFileContent(self):
		files = self.getRawJSON()['files']
		return dict([(key,files[key]['content']) for key in files.keys()])
		
class PythonGists(object):
	def __init__(self,username,password):
		self.accessToken=login(username,password)
	
	@staticmethod
	def Gist(description,content,name,token=None):
		public=True
		url=API_URL+'/gists'

		if token is None:
			authtoken=None
		else:
			authtoken=token
		token='token {0}'.format(authtoken)
		data=json.dumps({"description":description,"public":False,"files":{name:{"content":content}}})

		if authtoken is None:
			r=requests.post(url,data=data)
		else:
			r=requests.post(url,headers={'Authorization':token},data=data)
		
		uniqueID=r.json()['url']
		gistLink="http://gist.github.com/{0}".format(uniqueID.split('/')[-1])
		return gistLink
	@staticmethod
	def GistFromFile(description,file):
		with open(file,'r') as f:
			content=f.read()
		return PythonGists.Gist(description,content,file)
	def createGist(self,description,content,name):
		return self.Gist(description,content,name,self.accessToken)
	def createGistFromFile(self,description,file):
		with open(file,'r') as f:
			content=f.read()
		return self.Gist(description,content,file,self.accessToken)
	@staticmethod
	def getGistsLinks(username):
		url='{0}/users/{1}/gists'.format(API_URL,username)
		data=requests.get(url).json()
		return [a['url'] for a in data]
	@staticmethod
	def getGists(username):
		url='{0}/users/{1}/gists'.format(API_URL,username)
		data=requests.get(url).json()
		return [Gist(a['url']) for a in data]
		
if __name__=='__main__':
	
	print('Welcome to PythonGists. Please check out the docs first at GitHub and then use')
	
