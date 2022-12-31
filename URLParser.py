# classe que analisa parametros de uma url
# do 5o curso de python da alura
import re

class URLParser:
    pass
class URLParser:
    def __init__(self, url:str) -> None:
        self.validate(url)
        self.__url = self.sanitize(url)

        self.__url_base, self.__url_param = self.spliturl(url)

    def sanitize(self, url:str):
        return url.strip()

    def validate(self, url):
        #if not url: #mais elegante que url == ''
        #regex mais elegante ainda
        if not re.match(r'(http(s)?://)?(www.)?\w+.com(.br)?', url):
            raise ValueError('A URL é invalida!')

    def spliturl(self, url:str):
        indice = url.find('?')
        return url[0:indice], url[indice+1:]

    @property
    def url(self):
        return self.__url

    @property
    def url_base(self):
        return self.__url_base

    @property
    def url_param(self):
        return self.__url_param

    def __str__(self) -> str:
        return f'''| {self.__url}
| Base: {self.__url_base}
| Params: {self.__url_param}
| Chaves: {self.keys()}
| Valores: {self.values()}'''

    def __len__(self):
        return len(self.url)

    # __o convenção pra "outro objeto" i guess
    def __eq__(self, __o: object) -> bool: 
        # if type(__o) == URLParser: # leva em conta só a mesma classe
        if isinstance(__o, URLParser): # considera classes filhas como iguais tb
            return self.url == __o.url
        else:
            return False

    def keys(self):
        
        regex = re.findall(r'\w+=', self.__url_param)
        return [i[:-1] for i in regex]


    def value(self, parametro):
        param_indice = self.__url_param.find(parametro) 

        indice_e = self.__url_param.find('&', param_indice) 

        if indice_e != -1:
            param_valor = self.__url_param[param_indice+len(parametro)+1:indice_e]
        else:
            param_valor = self.__url_param[param_indice+len(parametro)+1:]

        return param_valor

    def values(self):
        return [self.value(i) for i in self.keys()]
