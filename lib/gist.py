from PythonGists import PythonGists

def CreateGist(id:int,content:str,username:str,password:str):
    if type(id)!=int or type(content)!=str or type(username)!=str or type(password)!=str:
        raise TypeError
    try:
        Gist=PythonGists(username=username,password=password)
        url=Gist.createGist(description='GuOJ Pastebin', content=content, name='GuOJ-Pastebin-'+str(id)+'.md')
    except Exception as error:
        raise error
    return url