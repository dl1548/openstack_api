#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_instance_api.py
@Time    :   2019/01/23 16:13:18
@Author  :   Li Zili 
@Version :   1.0
@Contact :   cn.zili.lee@gmail.com
'''


from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as nova_client
#from neutronclient import client as neutron_client
from neutronclient.v2_0 import client as neutron_client
from keystoneclient.v3 import client as key_client
import requests
# disbled warning
requests.packages.urllib3.disable_warnings()

"""
Keystone(身份认证)
Nova(计算)
Neutron(网络)
Glance(镜像存储)
Cinder(块存储)
Swift(对象存储)
Horizon(dashboard)
Ceilometer(计量)
Heat(部署编排)
Trove(数据库)
"""

class CreateInstance(object):
    def __init__(self,**kwargs):
        self.user_domain_name=kwargs.get('user_domain_name','')
        self.username=kwargs.get('username','')
        self.password=kwargs.get('password','')
        self.project_domain_name=kwargs.get('project_domain_name','')
        self.project_name=kwargs.get('project_name','')
        self.auth_url=kwargs.get('auth_url','')


    def auth_sess(self):
        auth = v3.Password(
            user_domain_name=self.user_domain_name,
            username=self.username,
            password=self.password,
            project_domain_name=self.project_domain_name,
            project_name=self.project_name,
            auth_url=self.auth_url
                )
        sess = session.Session(auth=auth, verify=False)
        
        return sess
    
    def nova_login(self):
        novac =  nova_client.Client(2,session=self.auth_sess())

        return novac
    
    def neutron_login(self):
        neutronc = neutron_client.Client(session=self.auth_sess())

        return neutronc

    # 创建实例
    def find_image(self,**kwargs):
        """
        : novac: nova_client.Client(2,session)
        : images_name: 镜像名
        """
        novac=kwargs.get('novac','')
        image_name=kwargs.get('images_name')
        image = novac.glance.find_image(image_name)

        return image

    def create(self,**kwargs):
        """
        创建实例所需要的参数
        
        :name:  实例名 .
        :image: 镜像名 .
        :flavor: 实例类型 .
        :nic: 网路名.
        :key_name: 密钥名 .
        :security_groups: 安全组 .
        :availability_zone: 可用区 .

        """
        novac=self.nova_login()

        name=kwargs.get('name','')
        image=novac.glance.find_image(kwargs.get('image',''))
        flavor=novac.flavors.find(name=kwargs.get('flavor',''))
        nics=kwargs.get('nics','')
        key_name=kwargs.get('key_name','')
        security_groups=kwargs.get('security_groups','')
        availability_zone=kwargs.get('availability_zone','')

        instance = novac.servers.create(
                name=name,
                image=image,
                flavor=flavor,
                nics=[{'net-id':nics}],
                key_name=key_name,
                security_groups=[security_groups],
                availability_zone=availability_zone
                )
                
        return instance





# # 实例开机  需要实例id
# start_instance = novac.servers.start('237568a6-256f-411c-aa36-318bf43d5651')

