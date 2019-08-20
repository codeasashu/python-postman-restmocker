class pmrequest(object):

    def __init__(self, request, name=None):
        self.request = request
        self.name = name
    
    def getName(self):
        return self.name

    def getMethod(self):
        return self.request['method'] if 'method' in self.request else None

    def getUri(self):
        urldict = self.request['url']
        protocol = urldict['protocol'] if 'protocol' in urldict else 'http'
        host = urldict['host'][0] if 'host' in urldict and len(urldict['host']) > 0 else None
        if host:
            host = host + '/' if host[-1] != '/' else host
            path = '/'.join(urldict['path'] if 'path' in urldict else [])
            query_params = []
            if 'query' in urldict:
                for query in urldict['query']:
                    if 'disabled' not in query or (query['disabled'] == False):
                        param = query['key'] + '=' + query['value']
                        query_params.append(param)            
            query_params = ('?' if len(query_params) else '') + '&'.join(query_params)
            url = ('https://' if (protocol == 'https') else 'http://') + host + path + query_params
            return url
        else:
            return None
