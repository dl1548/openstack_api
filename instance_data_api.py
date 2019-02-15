#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   instance_data_api.py
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



class GetInstanceData(object):
    
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

    def get_instances(self,**kwargs):
        """
        : novac: nova_client.Client(2,session)
        """
        novac=kwargs.get('novac','')
        instance_list = novac.servers.list(detailed=True)

        return instance_list   # instance_list[0].name
    
    def get_availability_zones(self,**kwargs):
        """
        : novac: nova_client.Client(2,session)
        """
        novac=kwargs.get('novac','')
        zone_list = novac.availability_zones.list()

        return zone_list    #  zone_list[1].zoneName

    def get_images(self,**kwargs):
        """
        : novac: nova_client.Client(2,session)
        """
        novac=kwargs.get('novac','')
        images_list=novac.glance.list()

        return images_list  # name=images_list[0].name

    def get_flavors(self,**kwargs):
        """
        : novac: nova_client.Client(2,session)
        """
        novac=kwargs.get('novac','')
        instance_type_list = novac.flavors.list()

        return instance_type_list   # instance_type_list[0].name

    def get_keys(self,**kwargs):
        """
        : novac: nova_client.Client(2,session)
        """
        novac=kwargs.get('novac','')
        key_list = novac.keypairs.list()

        return key_list     # key_list[0].name


    def get_nics(self,**kwargs):
        """
        : neutronc: neutron_client.Client(2,session)
        """
        neutronc=kwargs.get('neutronc','')
        nic_dict = neutronc.list_networks()
        return nic_dict

    def get_security_groups(self,**kwargs):
        """
        : neutronc: neutron_client.Client(2,session)
        """
        neutronc=kwargs.get('neutronc','')
        sec_dict = neutronc.list_security_groups()

        return sec_dict