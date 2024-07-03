import httpx
import json

class AbstractApi(object) :
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def getAccessToken(self):
        """获取访问令牌，需在子类中实现"""
        raise NotImplementedError

    async def refreshAccessToken(self):
        """刷新访问令牌，需在子类中实现"""
        raise NotImplementedError

    async def getSuiteAccessToken(self):
        """获取套件访问令牌，需在子类中实现"""
        raise NotImplementedError

    async def refreshSuiteAccessToken(self):
        """刷新套件访问令牌，需在子类中实现"""
        raise NotImplementedError

    async def getProviderAccessToken(self):
        """获取服务提供商访问令牌，需在子类中实现"""
        raise NotImplementedError

    async def refreshProviderAccessToken(self):
        """刷新服务提供商访问令牌，需在子类中实现"""
        raise NotImplementedError

    @staticmethod
    def __tokenExpired(errCode):
        """检查令牌是否过期"""
        return errCode in [40014, 42001, 42007, 42009]

    async def __refreshToken(self, url):
        """根据URL中的关键字刷新相应的令牌"""
        if 'SUITE_ACCESS_TOKEN' in url :
            self.refreshSuiteAccessToken()
        elif 'PROVIDER_ACCESS_TOKEN' in url :
            self.refreshProviderAccessToken()
        elif 'ACCESS_TOKEN' in url :
            self.refreshAccessToken()

    @staticmethod
    def __checkResponse(response):
        """检查API响应，若有错误则抛出异常"""
        errCode = response.get('errcode')
        errMsg = response.get('errmsg')

        if errCode == 0:
            return response 
        else:
            raise RuntimeError(errCode, errMsg)

    async def httpCall(self, urlType, params:dict, req_body=None, **kwargs) -> json:
        """执行HTTP调用，支持自动重试和令牌刷新"""
        url, method = urlType
        response = {}
        retry_cnt = 0
        max_retries = 3  # 最大重试次数

        while retry_cnt < max_retries:
            # if 'POST' == method and req_body is not None:
            if method == 'POST':
                if req_body is None:
                    req_body = {}  # 确保请求体不为空
                response = await self.__httpPost(url, params, req_body, **kwargs)
            elif method == 'GET':
                response = await self.__httpGet(url, params, **kwargs)

            # check if token expired
            if self.__tokenExpired(response.get('errcode')) :
                await self.__refreshToken(url)
                retry_cnt += 1
                continue
            else :
                break
        return self.__checkResponse(response) 

    async def __httpPost(self, url:str, params:dict, req_body, **kwargs) -> json:
        """执行HTTP POST请求"""
        try:
            response = await self.client.post(url, params=params, json=req_body, **kwargs)
            json_data = response.json()
        except (httpx.HTTPError, httpx.RequestError) as err:
            raise RuntimeError("error", err)
        return json_data

    async def __httpGet(self, url:str, params:dict, **kwargs) -> json:
        """执行HTTP GET请求"""
        try:
            response = await self.client.get(url, params=params, **kwargs)
            json_data = response.json()
        except (httpx.HTTPError, httpx.RequestError) as err:
            raise RuntimeError("error", err)

        return json_data

    async def __post_file(self, url, media_file):
        """执行文件上传的POST请求"""
        response = await self.client.post(url, file=media_file)
        return response.json()
