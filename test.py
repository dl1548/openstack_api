#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   get_instance_data.py
@Time    :   2019/01/23 16:12:15
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

auth = v3.Password(
    user_domain_name='Default',
    username='admin',
    password='65c8fc5137d945f1',
    project_domain_name='Default',
    project_name='admin',
    auth_url='http://192.168.1.131:5000/v3'
)
sess = session.Session(auth=auth, verify=False)

novac =  nova_client.Client(2,session=sess)


neutronc = neutron_client.Client(session=sess)


novac = nova_client.Client(2, session=sess)
# 获取所有实例信息
# instance_list = novac.servers.list(detailed=True) 
# print(instance_list)    # [<Server: zili-instance02>, <Server: zili-instance01>]

# 获取镜像
image_list=novac.glance.list()
print(image_list)   # [<Image: CentOS-7-x86_64>, <Image: cirros>]

# print(dir(novac.glance))
# print(novac.glance.find_image('cirros'))
# image = novac.glance.find_image('cirros')


# 查找实例类型
# f1 = novac.flavors.find(ram=512)
# print(f1)

# instance_type_list = novac.flavors.list()
# print(instance_type_list) # [<Flavor: m1.tiny>, <Flavor: m1.small>, <Flavor: m1.medium>, <Flavor: m1.large>, <Flavor: m1.xlarge>] 


# print(dir(novac.flavors))
# print(novac.flavors.find(name='zili-insType'))
# print('---------')



# 密钥列表
# key_list = novac.keypairs.list()
# key_name = (key_list[0].name)
# print('key_name: '+key_name)

# keyc = key_client.Client(session=sess)
# key_list = keyc.projects.list() 
# print(key_list)


# 网络信息
# 查找网络
# net = novac.neutron.find_network('demo-network')
# print(dir(net))
# print(net.id)

# 获取网络信息
# neutronc = neutron_client.Client(session=sess)

# net_dict = neutronc.list_networks()  # 'networks': [{ }]
# net_id = net_dict['networks'][0]['id']
# print('net_id: '+net_id)

# # 可用区
# ava_zone = novac.availability_zones.list()
# ava_name = ava_zone[1].zoneName
# print('ava_name: '+ava_name)


# # 安全组
# sec_dict = neutronc.list_security_groups()




# # 创建实例
# sss = novac.servers.create("my-server", image=image_list[1],flavor=fl,nics=[{'net-id':net.id}])
# # sss = novac.servers.create("my-server", image=image_list[1],flavor=fl,nics=[{'net-id':net.id}],key_name=key_list[0])
# print(sss)

# # 
# sss = novac.servers.create("my-server-zili-03", image=image,flavor=instance_type_list[5], \
#     nics=[{'net-id':net_id}],key_name=key_name,security_groups=['ssh-icmp'],availability_zone=ava_name)
# print(sss)




    # # # 实例开机  需要实例id
    # # start_instance = novac.servers.start('237568a6-256f-411c-aa36-318bf43d5651')

