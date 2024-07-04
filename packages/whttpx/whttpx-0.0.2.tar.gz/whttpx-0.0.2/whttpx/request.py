import json

from httpx import AsyncClient, Timeout
from datetime import datetime, timedelta

from wellog import loggen
from envOS import server_env

from .Error import Error_Auth, Error_Server

wdai = {
  "authorization": None,
  "expiration": None,
}

class Request:
  def __init__(self, verify=None):    
    self._SERVER=[
      'WELLDOCS_INTER',
      'WELLDOCS_PUBLIC',
      'PYVERT_INTER',
      'PYVERT_PUBLIC',
      'WDAI_PUBLIC'
    ]
    params = { "verify":verify}
    if not verify:
      params['verify']=True if server_env.ENVIROMENT == 1 else False
    self.client = AsyncClient(**params)
    self._WDAI_KEY:dict={'username':'', 'password':''}

  async def get(self, id_server=int, server:str=None, url:str='', timeout:int=60):
    '''
    Modulo para realizar peticiones, los servidores validos son:
    - 0.`WELLDOCS_INTER`
    - 1.`WELLDOCS_PUBLIC`
    - 2.`PYVERT_INTER`
    - 3.`PYVERT_PUBLIC`
    - 4.`WDAI_PUBLIC`
    '''
    start = datetime.now()
    host_server = self.server(id_server, server)
    data = {
      "url": host_server + url,
      "timeout":Timeout(timeout)
    }

    if id_server == 4:
      auth = await self.prepare_wdai(host_server)
      data.update(auth)

    response = await self.client.get(**data)
    loggen.info(f"{data['url']} - {response.status_code} - {(datetime.now() - start).total_seconds():.2f}s")
    
    return self.prepare_response(id_server=id_server, data=response)
  
  async def post(self, id_server:int, server:str=None, url:str='', appJson:dict=None, FormData:dict=None, Files=None, timeout:int=60):
    '''
    Modulo para realizar peticiones, los servidores validos son:
    - 0.`WELLDOCS_INTER`
    - 1.`WELLDOCS_PUBLIC`
    - 2.`PYVERT_INTER`
    - 3.`PYVERT_PUBLIC`
    - 4.`WDAI_PUBLIC`
    '''
    start = datetime.now()
    host_server = self.server(id_server, server)
    data = {
      "url": host_server + url,
      "timeout":Timeout(timeout)
    }

    if id_server == 4:
      auth = await self.prepare_wdai(host_server)
      data.update(auth)

    if appJson: data['json']=appJson
    else:
      data['data']=FormData
      if Files: data['files']=Files
    
    response = await self.client.post(**data)
    loggen.info(f"{data['url']} - {response.status_code} - {(datetime.now() - start).total_seconds():.2f}s")

    return self.prepare_response(id_server=id_server, data=response)

  def server(self, id_server:int, server:str=None):
    if server:
      loggen.info('WARNING: Unregistered domain')
      return server
    if id_server > len(self._SERVER):
      raise Error_Server('There is no server with that id')
    name = self._SERVER[id_server]
    server = server_env.URL_SERVER[name]
    if not server:
      raise Error_Server('No se encuentra el server')
    
    return server

  def prepare_response(self, id_server:int, data):
    if id_server == 0 or id_server == 1:
      body = json.loads(data.text)
      response = {
        'result':body['result'],
        'message':body['message'],
        'data': body['data']
      }    
    elif id_server == 4:
      response = data.json()
      if "detail" in response:
        raise Error_Auth('Could not validate Token')
    else: 
      try:
        response = data.json()
      except Exception:
        response = {}
    return response

  async def prepare_wdai(self, BASE_URL):
    data = {}    
    if not wdai['expiration'] or datetime.now() > wdai['expiration']:
      wdai['expiration'] = None
      data = {
        "url": f"{BASE_URL}auth",
        "json":self._WDAI_KEY
      }
      response = await self.client.post(**data)
      loggen.info(f"{data['url']} - {response.status_code}")
      auth = response.json()
      
      if 'access_token' not in auth or 'token_type' not in auth: raise Error_Auth("Could not validate credentials")
      data = {}
      wdai['expiration'] = datetime.now() + timedelta(hours=11, minutes=59, seconds=30)
      wdai['authorization'] = auth['token_type'] + " " + auth['access_token']
    data['headers']={
        "Authorization": wdai['authorization']
      }
    return data
  
  def setKeyWDAI(self, key:dict):
    self._WDAI_KEY.update(key)