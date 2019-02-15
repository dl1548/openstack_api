#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   view.Py
@Time    :   2019/01/24 09:52:08
@Author  :   Li Zili 
@Version :   1.0
@Contact :   cn.zili.lee@gmail.com
'''

from run_api import RunOpenstackApi

openstack_client =  RunOpenstackApi(
        user_domain_name='Default',
        username='admin',
        password='65c8fc5137d945f1',
        project_domain_name='Default',
        project_name='admin',
        auth_url='http://192.168.1.131:5000/v3'
)

instance_data=openstack_client.get_create_instance_data()

print(instance_data)

# instance = openstack_client.create_instance(
#         name="my-api-test",
#         image='cirros',
#         flavor='zili-insType',
#         nics='0b7c1579-e6eb-4f2e-bf02-4519aee697f5',
#         key_name='zili-miyue-01',
#         security_groups='ssh-icmp',
#         availability_zone='nova'
# )
# print(instance)