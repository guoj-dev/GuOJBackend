from PythonGists.PythonGists import PythonGists,Gist

def CreateGist(uuid:str,content:str,username:str,password:str):
    if type(uuid)!=str or type(content)!=str or type(username)!=str or type(password)!=str:
        raise TypeError
    try:
        Gist=PythonGists(username=username,password=password)
        url=Gist.createGist(description='GuOJ Pastebin', content=content, name='GuOJ-Pastebin-'+uuid+'.md')
    except Exception as error:
        raise error
    return url

def GetGist(url:str):
    if type(url)!=str:
        raise TypeError
    try:
        gist=Gist(url)
        Content=gist.getFileContent()
    except Exception as error:
        raise error
    return Content