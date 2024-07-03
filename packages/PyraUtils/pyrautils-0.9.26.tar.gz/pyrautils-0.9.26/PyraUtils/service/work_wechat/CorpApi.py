# -*- coding: utf-8 -*-

from .AbstractApi import AbstractApi
from .CorpApiType import *


class CorpApi(AbstractApi) :
    def __init__(self, corpid, corpsecret):
        """初始化企业API，设置企业ID和秘钥"""
        super().__init__()
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.access_token = None

    async def refreshAccessToken(self) :
        """刷新访问令牌"""
        parms = dict(
            corpid=self.corpid,
            corpsecret=self.corpsecret,
        )
        response = await self.httpCall(CORP_API_TYPE['GET_ACCESS_TOKEN'], parms)
        self.access_token = response.get('access_token')

    async def getAccessToken(self) :
        """获取访问令牌，如果没有则刷新"""
        if self.access_token is None:
            await self.refreshAccessToken()
        return self.access_token

    async def get_user(self, access_token, userid):
        """
        读取成员信息
        文档链接：https://work.weixin.qq.com/api/doc/90000/90135/90196
        """
        params = dict(
            access_token=access_token,
            userid=userid
        )

        response = await self.httpCall(CORP_API_TYPE['USER_GET'], params)
        return response

    async def get_userid_by_email(self, access_token, email, email_type=1):
        """
        功能： 邮箱获取userid。
        email_type: 邮箱类型：1-企业邮箱（默认）, 2-个人邮箱

        https://developer.work.weixin.qq.com/document/path/95895
        """
        params = dict(
            access_token=access_token
        )

        body = dict(
            email=email,
            email_type=email_type
        )

        response = self.httpCall(CORP_API_TYPE['USERID_BY_EMAIL_POST'], params, req_body=body)
        return response


    async def get_user_list_id(self, access_token):
        """
        获取成员ID列表
        文档链接：https://developer.work.weixin.qq.com/document/path/96067
        """
        params = dict(
            access_token=access_token
        )

        response = await self.httpCall(CORP_API_TYPE['USER_LIST_ID'], params)
        return response

    async def get_userid_by_email(self, access_token, email, email_type=1):
        """
        通过邮箱获取userid
        文档链接：https://developer.work.weixin.qq.com/document/path/95895
        email_type: 邮箱类型：1-企业邮箱（默认）, 2-个人邮箱
        """
        params = dict(
            access_token=access_token
        )

        body = dict(
            email=email,
            email_type=email_type
        )

        response = await self.httpCall(CORP_API_TYPE['USERID_BY_EMAIL_POST'], params, req_body=body)
        return response


    async def get_approval_detail(self, access_token, sp_no):
        """
        查询审批申请详情
        功能：企业可通过审批应用或自建应用Secret调用本接口，根据审批单号查询企业微信“审批应用”的审批申请详情。
        """

        params = dict(
            access_token=access_token
        )

        body = dict(
            sp_no=sp_no
        )

        response = await self.httpCall(CORP_API_TYPE['APPROVAL_DETAIL'], params, req_body=body)
        return response

    async def sendMessage(self, access_token, touser, agentid,  msgtype="text", safe=0, **kwargs):
        """消息发送"""
        params = dict(
            access_token=access_token
        )

        body = dict(
            touser=touser,
            msgtype=msgtype,
            agentid=agentid,
            safe=safe,
            enable_duplicate_check=0,
            duplicate_check_interval=1800
        )

        if msgtype == "text":
            body['text'] = {'content': kwargs['msg_content']}
        elif msgtype == "markdown":
            body['markdown'] = {'content': kwargs['msg_content']}
        elif msgtype == "textcard":
            body['textcard'] = {
                'title': kwargs['msg_title'],
                'description': kwargs['msg_content'],
                'url': kwargs['msg_url'],
                'btntxt': '详情'
            }
        elif msgtype == "template_card":
            pass
        response = await self.httpCall(CORP_API_TYPE['MESSAGE_SEND'], params, req_body=body)
        return response

