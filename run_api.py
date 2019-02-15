#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   run_api.py
@Time    :   2019/01/23 13:49:32
@Author  :   Li Zili 
@Version :   1.0
@Contact :   cn.zili.lee@gmail.com
'''

from instance_data_api import GetInstanceData
from create_instance_api import CreateInstance
import json


class RunOpenstackApi(object):
    """
    :user_domain_name:
    :username:
    :password:
    :project_domain_name:
    :project_name:
    :auth_url:
    """
    def __init__(self,**kwargs):
        self.user_domain_name=kwargs.get('user_domain_name','')
        self.username=kwargs.get('username','')
        self.password=kwargs.get('password','')
        self.project_domain_name=kwargs.get('project_domain_name','')
        self.project_name=kwargs.get('project_name','')
        self.auth_url=kwargs.get('auth_url','')

    def get_create_instance_data(self,**kwargs):

        instance_data = GetInstanceData(
            user_domain_name=self.user_domain_name,
            username=self.username,
            password=self.password,
            project_domain_name=self.project_domain_name,
            project_name=self.project_name,
            auth_url=self.auth_url,
        )

        novac = instance_data.nova_login()
        neutronc = instance_data.neutron_login()
        all_data = dict()

        # 获取可用区
        ava_zone_list = list()
        ava_zone_data = instance_data.get_availability_zones(novac=novac)
        for num, zone in enumerate(ava_zone_data):
            num = dict()
            num['name']=zone.zoneName
            num['value']=zone.zoneName
            ava_zone_list.append(num)
        all_data['availability_zone']=ava_zone_list

        # 获取镜像
        image_list = list()
        image_data = instance_data.get_images(novac=novac)
        for num,image in enumerate(image_data):
            num = dict()
            num['name']=image.name
            num['value']=image.name
            image_list.append(num)
        all_data['images']=image_list

        # 获取实例类型
        flavor_list= list()
        flavor_data = instance_data.get_flavors(novac=novac)
        for num,flavor in enumerate(flavor_data):
            num = dict()
            num['name']=flavor.name
            num['value']=flavor.name
            flavor_list.append(num)
        all_data['flavors']=flavor_list

        #获取密钥
        key_list= list()
        key_data = instance_data.get_keys(novac=novac)
        for num,key in enumerate(key_data):
            num = dict()
            num['name']=key.name
            num['value']=key.name
            key_list.append(num)
        all_data['keys']=key_list

        # 网络信息
        nic_data = instance_data.get_nics(neutronc=neutronc)
        nic_list = list()
        for num, net in enumerate(nic_data['networks']):
            num = dict()
            num['name'] = net['name']
            num['value'] = net['id']
            nic_list.append(num)
        all_data['network']=nic_list

        # 获取安全组
        security_group_data = instance_data.get_security_groups(neutronc=neutronc)
        security_group_list = list()
        for num, group in enumerate(security_group_data['security_groups']):
            num = dict()
            num['name'] = group['name']
            num['value'] = group['name']
            security_group_list.append(num)
        all_data['security_group']=security_group_list


        return all_data


    def create_instance(self,**kwargs):
        instance = CreateInstance(
            user_domain_name=self.user_domain_name,
            username=self.username,
            password=self.password,
            project_domain_name=self.project_domain_name,
            project_name=self.project_name,
            auth_url=self.auth_url,
        )
        name=kwargs.get('name','')
        image=kwargs.get('image','')
        flavor=kwargs.get('flavor','')
        nics=kwargs.get('nics','')
        key_name=kwargs.get('key_name','')
        security_groups=kwargs.get('security_groups','')
        availability_zone=kwargs.get('availability_zone','')

        ins = instance.create(
                name=name,
                image=image,
                flavor=flavor,
                nics=nics,
                key_name=key_name,
                security_groups=security_groups,
                availability_zone=availability_zone
        )

        return ins

if __name__ == "__main__":
    test = RunOpenstackApi(
        user_domain_name='Default',
        username='admin',
        password='65c8fc5137d945f1',
        project_domain_name='Default',
        project_name='admin',
        auth_url='http://192.168.1.131:5000/v3'
    )

    res = test.get_create_instance_data()
    print(res)

    # inst=test.create_instance(
        
    # )