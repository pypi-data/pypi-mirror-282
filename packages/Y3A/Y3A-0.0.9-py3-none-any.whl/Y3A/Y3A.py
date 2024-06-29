"""
AWS Classes Module

This module provides a classes representing a behaivour of AWS objects

Classes:

Methods:

Usage:
- ...

Author: Pavel ERESKO
"""

import boto3
from arnparse import arnparse
from botocore.exceptions import ClientError

import io
import zipfile
import json
import stat
import time

from ObjectModelFramework import *

import importlib.resources

# id parameter passing
class PAR:
    ''' Identyfiers for the param way '''
    PAR    = 0
    LIST   = 1
    FILTER = 2
    STRING = 3

# id parameter passing
class COLOR:
    ''' Identyfiers for the param way '''
    ORANGE    = "#FFC18A"
    RED       = "#F9BBD9"
    RED_DARK  = "#FF99CC"
    LILA      = "#f2c4f4"
    BLUE      = "#d7c1ff"
    BLUE_DARK = "#c19fff"
    CRIMSON   = "#F2B3BC"

def bt(aws_service):
    if getattr(Y3A, "CLIENTS", None) == None:
        setattr(Y3A, "CLIENTS", {})
    
    if not aws_service in Y3A.CLIENTS:
        client = boto3.Session(
            profile_name = Y3A.PROFILE
        ).client(
            aws_service
        )
        Y3A.CLIENTS[aws_service] = client

    else:
        client = Y3A.CLIENTS[aws_service]

    return client

def Id17(id):
    return id[-17:]

def str_to_class(strtype):
    clss = strtype.replace('AWS::', "")
    clss = clss.replace('::', "_")
    clss = globals()[clss] if clss in globals() else None
    return clss

def idpar(id, ParType = PAR.PAR):
    if id is None:
        flt = {}
    elif isinstance(id, str): # obsolete
        field = None
        flt = {field : (id, ParType)}
    elif isinstance(id, tuple):
        flt = {id[0] : (id[1], ParType)}
    # elif isinstance(id, list): ?
    else:
        flt = id
    
    params = {}
    for key, val in flt.items():
        if isinstance(val, tuple):
            i_val, i_type = val
        else:
            i_val = val
            i_type = ParType

        if i_val == None:
            continue

        if   i_type == PAR.PAR:
            params[key] = i_val

        elif i_type == PAR.LIST:
            params[key] = [i_val]

        elif i_type == PAR.FILTER:
            if "Filters" not in params:
                params["Filters"] = []

            params["Filters"].append({
                'Name': key,
                'Values': i_val
            })

        elif i_type == PAR.STRING:
            params["Filter"] = f'{key}="{i_val}"'

    return params

def get_resource_path(path, file):
    with importlib.resources.path(path, file) as res_path:
        return str(res_path)

def Wait(service_name, waiter_name, resource_param, resource_id):
    waiter = bt(service_name).get_waiter(waiter_name)

    waiter.wait(
        **{f"{resource_param}": resource_id},
        WaiterConfig={
            'Delay': 3,
            'MaxAttempts': 100
        }
    )


class awsObject(ObjectModelItem):
    Icon = "AWS"
    Prefix = ""

    @classmethod
    def get_objects(cls, filter=None):
        try:
            return cls.aws_get_objects(filter)
        except Exception as e:
            ErrorCode = e.response['Error']['Code'] if hasattr(e, "response") else ""
            if ErrorCode[-9:] == '.NotFound' or ErrorCode == "AccessDenied":
                return []
            else:
                print(f"{cls.get_class_view()}.get_objects: {e.args[0]}")
                raise


    def get_view(self):
        '''Getting view of object'''

        view = f"{getattr(self, 'Tag_Name', super().get_view())}"
        return view
    
    def get_href(self):
        try:
            wrap = self.html_wrap()
        except Exception as e:
            print(f"get_href: An exception occurred: {type(e).__name__} - {e}")
            wrap = ""

        if wrap == "":
            return ""
        
        url  = wrap.format(self = self, region = "eu-central-1") # TODO region
        href = f'HREF="{url}" TARGET="_blank"'
        return href

    def html_wrap(self):
        return ""

    @classmethod
    def html_root(cls):
        return "https://{region}.console.aws.amazon.com/"

    @classmethod
    def html_home(cls, client):
        return awsObject.html_root() + "{client}/home?region={region}#".format(client = client, region = "{region}")

    def get_icon(self):
        icon = super().get_icon()
        path = get_resource_path('Y3A.icons', icon + '.png').replace("\\", "/")
        return path

class Tag(awsObject):
    @staticmethod
    def create(id, name, Value):
        bt('ec2').create_tags(
            Resources=[id],
            Tags=[
                {
                    'Key': name,
                    'Value': Value
                },
            ]
        )

    @staticmethod
    def delete(id, name):
        bt('ec2').delete_tags(
            Resources=[id],
            Tags=[
                {'Key': name}
            ]
        )

    @staticmethod
    def cli_add(name):
        return f""

    @staticmethod
    def cli_del(id, name):
        return f"aws ec2 delete-tags --resources {id} --tags Key={name}"


class EC2_Reservation(awsObject): 
    Icon = "Res_Amazon-Instance_48"
    Show = False
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
                    "ReservationId" : (EC2_Reservation, FIELD.ID),
                    "OwnerId"       : str,
                    "Groups"        : ([str]), # !!!
                    "Instances"     : ([EC2_Instance]),
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        resp = bt('ec2').describe_instances(**idpar(('reservation-id', id), PAR.FILTER))
        return resp['Reservations']


class EC2_SecurityGroup(awsObject):
    ListName = "SecurityGroups"

    @staticmethod
    def fields():
        return {
                    "_parent" : (EC2_Instance, FIELD.LIST_ITEM),
                    "ListName" : (str, FIELD.LIST_NAME),
                    "GroupName" : (str, FIELD.VIEW),
                    'GroupId': (EC2_SecurityGroup, FIELD.LINK_IN),
                }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["GroupId"]}"

    @staticmethod
    def aws_get_objects(id=None):
        return EC2_Instance.get_objects_by_index(id, "SecurityGroups", "GroupId")

class EC2_Instance(awsObject): 
    Prefix = "i"
    Draw = DRAW.ALL
    Icon = "Arch_Amazon-EC2_48"
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
                    "_parent" : (EC2_Reservation, FIELD.LINK),
                    "InstanceId" : (EC2_Instance, FIELD.ID),
                    "SubnetId" : (EC2_Subnet, FIELD.OWNER),
                    'Tags' : ({"Key" : "Value"}),
                    'VpcId': EC2_VPC,
                    'KeyPairId': (EC2_KeyPair, FIELD.LINK_IN),
                    # 'SecurityGroups': [EC2_SecurityGroupSecurityGroups]  ToDo
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        resp = bt('ec2').describe_instances(**idpar(('InstanceIds', id), PAR.LIST))
        res = []
        for reservation in resp['Reservations']:
            for inst in reservation["Instances"]:
                inst["_parent"] = reservation["ReservationId"]
                res.append(inst)
        return res

    def get_ext(self):
        return f"{getattr(self, 'PlatformDetails', '-')}"

    @staticmethod
    def create(name, ImageId, InstanceType, KeyPairId, SubnetId, Groups=[], PrivateIpAddress=None, UserData=""):
        id = bt('ec2').run_instances(
            ImageId = ImageId,
            InstanceType = InstanceType,
            KeyName = EC2_KeyPair.IdToName(KeyPairId),
            NetworkInterfaces=[
                {
                    'SubnetId': SubnetId,
                    'DeviceIndex': 0,
                    'AssociatePublicIpAddress': True if PrivateIpAddress is not None else False,
                    'PrivateIpAddress': PrivateIpAddress, # todo - PrivateIpAddress vs PublicIpAddress
                    'Groups': Groups,
                }
            ],
            UserData = UserData,
            MinCount = 1,
            MaxCount = 1
        )['Instances'][0]['InstanceId']

        Tag.create(id, "Name", f"{EC2_Instance.Prefix}-{name}")

        return id
    
    @staticmethod
    def delete(id):
        bt('ec2').terminate_instances(
            InstanceIds=[id]
        )

        Wait('ec2', 'instance_terminated', "InstanceIds", [id])

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)

        if hasattr(self, "KeyName"):
            setattr(self, "KeyPairId", EC2_KeyPair.NameToId(self.KeyName))


class EC2_Instance_NetworkInterface(awsObject):
    ListName = "Network Interfaces"

    @staticmethod
    def fields():
        return {
            "ListName" : (str, FIELD.LIST_NAME),
            '_parent': (EC2_Instance, FIELD.LIST_ITEM),
            'View': (str, FIELD.VIEW),
            'NetworkInterfaceId': (EC2_NetworkInterface, FIELD.LINK_IN),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["NetworkInterfaceId"]}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.View = f"{self.NetworkInterfaceId}"

    @staticmethod
    def aws_get_objects(id = None):
        return EC2_Instance.get_objects_by_index(id, "NetworkInterfaces", "NetworkInterfaceId")


class EC2_InternetGateway(awsObject): 
    Prefix = "igw"
    Icon = "Arch_Amazon-API-Gateway_48"
    Color = COLOR.RED

    @staticmethod
    def fields():
        return {
                    "InternetGatewayId" : (EC2_InternetGateway, FIELD.ID),
                    'Attachments' : ([EC2_VPCGatewayAttachment]),
                    'Tags' : ({"Key" : "Value"}),
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        resp = bt('ec2').describe_internet_gateways(**idpar(('InternetGatewayIds', id), PAR.LIST))
        return resp['InternetGateways']


    @staticmethod
    def create(name):
        id = bt('ec2').create_internet_gateway()['EC2_InternetGateway']['InternetGatewayId']
        Tag.create(id, "Name", f"{EC2_InternetGateway.Prefix}-{name}")
        return id

    @staticmethod
    def delete(id):
        bt('ec2').delete_internet_gateway(
            InternetGatewayId = id
        )


class EC2_VPCGatewayAttachment(awsObject): 
    Prefix = "igw-attach"
    Draw = DRAW.VIEW
    DoNotFetch = True
    ListName = "Attachments"

    @staticmethod
    def fields():
        return {
                    "_parent" : (EC2_InternetGateway, FIELD.LIST_ITEM),
                    "ListName" : (str, FIELD.LIST_NAME),
                    "VpcId" : (EC2_VPC, FIELD.LINK_IN),
                }
    
    def get_view(self):
        return f"{Id17(self.VpcId)}"

    @staticmethod
    def aws_get_objects(id=None):
        return EC2_InternetGateway.get_objects_by_index(id, "Attachments", "VpcId")
    
    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["VpcId"]}"

    @staticmethod
    def create(InternetGatewayId, VpcId):
        resp = bt('ec2').attach_internet_gateway(InternetGatewayId=InternetGatewayId, VpcId=VpcId)
        return f"{InternetGatewayId}{ID_DV}{VpcId}"

    @staticmethod
    def delete(id):
        InternetGatewayId, _, VpcId = id.rpartition(ID_DV)
        bt('ec2').detach_internet_gateway(InternetGatewayId=InternetGatewayId, VpcId=VpcId)


class EC2_NatGateway(awsObject): 
    Prefix = "nat"
    Icon = "NATGateWay"
    Color = COLOR.BLUE_DARK

    @staticmethod
    def fields():
        return {
                    "NatGatewayId"        : (EC2_NatGateway, FIELD.ID),
                    "SubnetId"            : (EC2_Subnet    , FIELD.OWNER),
                    'Tags'                : ({"Key" : "Value"}),
                    "NatGatewayAddresses" : ([EC2_EIPAssociation], FIELD.LINK_IN),
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        resp = bt('ec2').describe_nat_gateways(**idpar(('NatGatewayIds', id), PAR.LIST))
        return resp['NatGateways']
    
    def get_view(self):
        return f"NAT"

    @staticmethod
    def create(name, SubnetId, AllocationId):
        id = bt('ec2').create_nat_gateway(SubnetId = SubnetId, AllocationId = AllocationId)['NatGateway']['NatGatewayId']

        Tag.create(id, "Name", f"{EC2_NatGateway.Prefix}-{name}")

        Wait('ec2', 'nat_gateway_available', "NatGatewayIds", [id])

        return id
    
    @staticmethod
    def delete(id):
        bt('ec2').delete_nat_gateway(NatGatewayId = id)

        Wait('ec2', 'nat_gateway_deleted', "NatGatewayIds", [id])


class EC2_EIPAssociation(awsObject): 
    DoNotFetch = True
    ListName = "Addresses"

    @staticmethod
    def fields():
        return {
                    '_parent'           : (EC2_NatGateway, FIELD.LIST_ITEM),
                    'ListName'           : (str, FIELD.LIST_NAME),
                    "View"               : (str, FIELD.VIEW),
                    "AllocationId"       : (EC2_EIP, FIELD.LINK),
                    "NetworkInterfaceId" : (EC2_NetworkInterface, FIELD.LINK_IN),
                    'Tags'               : ({"Key" : "Value"}),
                }
    
    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["AssociationId"]}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.View = f"{getattr(self, 'AssociationId', '-')}"

    @staticmethod
    def aws_get_objects(id=None):
        filters = []
        if id:
            filters.append({
                'Name': 'association-id',
                'Values': [id]
            })

        resp = bt('ec2').describe_addresses(Filters=filters)
        return resp["Addresses"]

    @staticmethod
    def create(allocation_id, instance_id):
        resp = bt('ec2').associate_address(AllocationId=allocation_id, InstanceId=instance_id)
        return f"{resp['AssociationId']}"

    @staticmethod
    def delete(id):
        RouteTableId, _, AssociationId = id.rpartition(ID_DV)
        bt('ec2').disassociate_address(AssociationId = AssociationId)

class EC2_SecurityGroup(awsObject):
    Prefix = "sg"
    Icon = "SecurityGroup"
    Color = COLOR.RED

    @staticmethod
    def fields():
        return {
                    "GroupId"    : (str , FIELD.ID),
                    "VpcId"      : (EC2_VPC, FIELD.OWNER),
#                    "IpPermissions"       : ([EC2_SecurityGroup_Rule]),
#                    "IpPermissionsEgress" : ([EC2_SecurityGroup_Rule]),
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        return bt('ec2').describe_security_groups(**idpar(('GroupIds', id), PAR.LIST))['SecurityGroups']

    def get_view(self):
        return f"{self.GroupName}"

    @staticmethod
    def create(name, Description, EC2_VPC):
        sgName = f"{EC2_SecurityGroup.Prefix}-{name}"

        id = bt('ec2').create_security_group(
            GroupName = name,
            Description = Description,
            VpcId = EC2_VPC
        )['GroupId']

        Tag.create(id, "Name", sgName)

        return id
    
    @staticmethod
    def delete(id):
        bt('ec2').delete_security_group(
            GroupId=id
        )

class EC2_SecurityGroup_Rule(awsObject):
    Prefix = "sgr"
    ListName = "Rules"

    @staticmethod
    def fields():
        return {
                    'SecurityGroupRuleId': EC2_SecurityGroup_Rule,
                    'GroupId': (EC2_SecurityGroup, FIELD.LIST_ITEM),
                    'ListName': (str, FIELD.LIST_NAME),
                }
    
    @staticmethod
    def create(GroupId, IpProtocol, FromToPort, CidrIp):
        id = bt('ec2').authorize_security_group_ingress(
            GroupId=GroupId,
            IpPermissions=[
                {
                    'IpProtocol': IpProtocol,
                    'FromPort': FromToPort,
                    'ToPort': FromToPort,
                    'IpRanges': [{'CidrIp': CidrIp}]
                }
            ]
        )["SecurityGroupRules"][0]["SecurityGroupRuleId"]

        return f"{GroupId}{ID_DV}{id}"
        
    @staticmethod
    def delete(id):
        security_group_id, _, security_group_rule_id = id.rpartition(ID_DV)
        bt('ec2').revoke_security_group_ingress(
            GroupId=security_group_id,
            SecurityGroupRuleIds=[security_group_rule_id]
        )

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["GroupId"]}{ID_DV}{resp["SecurityGroupRuleId"]}"

    @staticmethod
    def aws_get_objects(id=None):
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_security_group_rules.html
        # security-group-rule-id - The ID of the security group rule.
        # group-id - The ID of the security group.

        flt = {}
        if id == None:
            pass

        elif isinstance(id, str):
            par_id = None; cur_id = None
            if id is not None:
                par_id, _, cur_id = id.rpartition(ID_DV)

            if par_id:
                flt["group-id"] = ([par_id], PAR.FILTER)

            if cur_id and cur_id != "*":
                flt["SecurityGroupRuleIds"] = (cur_id, PAR.LIST)
        
        else:
            flt = id

        id_par_res = idpar(flt)
        resp = bt('ec2').describe_security_group_rules(**id_par_res)
        return resp['SecurityGroupRules']

    def get_view(self):
        res = ""
        res = f"{res}{getattr(self, 'IpProtocol', '')}"
        if hasattr(self, "FromPort"):
            ips = f"{self.FromPort}"
            if self.FromPort != self.ToPort:
                ips = f"{ips} - {self.ToPort}"
            res = f"{res}({ips})"
            
        return res


class EC2_Subnet(awsObject): 
    Prefix = "subnet"
    Draw = DRAW.ALL
    Icon = "Subnet"
    Color = COLOR.BLUE_DARK

    @staticmethod
    def fields():
        return {
                    "SubnetId" : (EC2_Subnet, FIELD.ID),
                    "VpcId" : (EC2_VPC, FIELD.OWNER),
                    'Tags' : ({"Key" : "Value"}),
                    'AvailabilityZoneId' : (AWS_AvailabilityZone, FIELD.LINK),
                }

    @staticmethod
    def aws_get_objects(id=None):
        response = bt('ec2').describe_subnets(**idpar(('SubnetIds', id), PAR.LIST))['Subnets']
        return response
    
    def get_ext(self):
        return f"{getattr(self, 'CidrBlock', '-')}"

    @staticmethod
    def create(name, EC2_VPC, CidrBlock):
        id = bt('ec2').create_subnet(
            VpcId = EC2_VPC,
            CidrBlock = CidrBlock
        )["EC2_Subnet"]["SubnetId"]

        Tag.create(id, "Name", f"{EC2_Subnet.Prefix}-{name}")

        return id
    
    @staticmethod
    def delete(id):
        bt('ec2').delete_subnet(
            SubnetId = id
        )

    

class EC2_NetworkAcl(awsObject): 
    Prefix = "nacl"
    Icon = "NACL"
    Color = COLOR.BLUE_DARK

    @staticmethod
    def fields():
        return {
                    "NetworkAclId" : (EC2_NetworkAcl, FIELD.ID),
                    'VpcId': (EC2_VPC, FIELD.OWNER),
                    'OwnerId': (str, FIELD.OWNER),
                    'Entries': ([EC2_NetworkAclEntry], FIELD.OWNER),
                    'Tags' : ({"Key" : "Value"}),
                    #),[{'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': True, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'allow', 'RuleNumber': 100}, {'CidrBlock': '0.0.0.0/0', 'Egress': False, 'Protocol': '-1', 'RuleAction': 'deny', 'RuleNumber': 32767}]
                    # 'Associations': [{'NetworkAclAssociationId': 'aclassoc-0c867a11b811c5be1', 'NetworkAclId': 'acl-0334606b00fe7551c', 'SubnetId': 'subnet-06678d33e23eba72f'}]
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        return bt('ec2').describe_network_acls(**idpar(('NetworkAclIds', id), PAR.LIST))['NetworkAcls']


class EC2_NetworkAclEntry(awsObject): 
    Prefix = "nacle"
    Icon = "NetworkAccessControlList"
    Color = COLOR.BLUE_DARK
    ListName = "Entries"

    @staticmethod
    def fields():
        return {
            "_parent": (EC2_NetworkAcl, FIELD.LIST_ITEM),
            "ListName": (EC2_NetworkAcl, FIELD.LIST_NAME),
            "Ext"     : (str, FIELD.EXT ),
            "View"    : (str, FIELD.VIEW),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["RuleNumber"]}"

    @staticmethod
    def aws_get_objects(id=None):
        return EC2_NetworkAcl.get_objects_by_index(id, "Entries", "RuleNumber")
    
    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.View = f"{self.RuleAction} - {getattr(self, 'CidrBlock', '*')}- {self.RuleNumber}:{self.Protocol} {getattr(self, 'PortRange', '')}"


class EC2_RouteTable(awsObject): 
    Prefix = "rtb"
    Icon = "RouteTable"
    Color = COLOR.BLUE_DARK

    @staticmethod
    def fields():
        return {
                    "RouteTableId" : (EC2_RouteTable, FIELD.ID),
                    "VpcId" : (EC2_VPC, FIELD.OWNER),
                    "Routes" : ([EC2_Route]),
                    "Associations" : ([EC2_RouteTable_Association]),
                    'OwnerId': (str, FIELD.OWNER),
                    'Tags' : ({"Key" : "Value"}),
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        return bt('ec2').describe_route_tables(**idpar(('RouteTableIds', id), PAR.LIST))['RouteTables']

    @staticmethod
    def create(name, VpcId):
        id = bt('ec2').create_route_table(VpcId = VpcId)['EC2_RouteTable']['RouteTableId']

        Tag.create(id, "Name", f"{EC2_RouteTable.Prefix}-{name}")
        return id

    @staticmethod
    def delete(id):
        bt('ec2').delete_route_table(
            RouteTableId = id
        )

class EC2_RouteTable_Association(awsObject):
    Prefix = "rtba"
    Draw = DRAW.ALL
    Color = COLOR.BLUE_DARK
    ListName = "Associations"
    UseIndex = True

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["RouteTableId"]}{ID_DV}{resp["RouteTableAssociationId"]}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.View = f"{Id17(self.SubnetId)}" if hasattr(self, "SubnetId") else "-"
        self.Ext  = f"{Id17(self.SubnetId)}" if hasattr(self, "SubnetId") else "-"

    @staticmethod
    def fields():
        return {
                    'Ext' : (str, FIELD.EXT),
                    'View': (str, FIELD.VIEW),
                    'RouteTableId'           : (EC2_RouteTable, FIELD.LIST_ITEM),
                    'ListName'               : (EC2_RouteTable, FIELD.LIST_NAME),
                    'SubnetId'               : (EC2_Subnet, FIELD.LINK_IN),
                }

    @staticmethod
    def aws_get_objects(id=None):
        return EC2_RouteTable.get_objects_by_index(id, "Associations", 'RouteTableAssociationId')

    @staticmethod
    def create(RouteTableId, SubnetId):
        resp = bt('ec2').associate_route_table(SubnetId = SubnetId, RouteTableId = RouteTableId)
        return f"{RouteTableId}{ID_DV}{resp['AssociationId']}"

    @staticmethod
    def delete(id):
        RouteTableId, _, AssociationId = id.rpartition(ID_DV)
        bt('ec2').disassociate_route_table(AssociationId = AssociationId)


class EC2_Route(awsObject):
    Prefix = "route"
    Draw = DRAW.ALL-DRAW.ID
    Icon = "Route"
    Color = COLOR.BLUE_DARK
    UseIndex = True
    ListName = "Routes"

    @staticmethod
    def fields():
        return {
                    'ListName'             : (EC2_RouteTable      , FIELD.LIST_NAME),
                    "_parent"              : (EC2_RouteTable      , FIELD.LIST_ITEM),
                    "GatewayId"            : (EC2_InternetGateway , FIELD.LINK),
                    "InstanceId"           : (EC2_Instance        , FIELD.LINK),
                    "NatGatewayId"         : (EC2_NatGateway      , FIELD.LINK),
                    "NetworkInterfaceId"   : (EC2_NetworkInterface, FIELD.LINK),
                }

    @staticmethod
    def aws_get_objects(id=None):
        return EC2_RouteTable.get_objects_by_index(id, "Routes", int)
    
    @staticmethod
    def destination(resp):
        for attr in ["DestinationCidrBlock", "DestinationPrefixListId"]:
            if type(resp) is dict:
                if attr in resp:
                    return (attr, resp[attr])
            else: # class
                if hasattr(resp, attr):
                    return (attr, getattr(resp, attr))

        print(f"EC2_Route.destination: {resp}")
        return ("-", "-")

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{EC2_Route.destination(resp)[1]}"

    def get_view(self):
        if hasattr(self, "GatewayId_local"):
            return 'local'

        return EC2_Route.destination(self)[1]

    def get_ext(self):
        return EC2_Route.destination(self)[1]

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)

        if hasattr(self, "GatewayId") and self.GatewayId == "local":
            self.GatewayId = None
            setattr(self, "GatewayId_local", True)

    @staticmethod
    def create(RouteTableId, DestinationCidrBlock, GatewayId = None, NatGatewayId = None):
        args = {
            "RouteTableId": RouteTableId,
            "DestinationCidrBlock": DestinationCidrBlock,
        }

        if GatewayId is not None:
            args["GatewayId"] = GatewayId
        
        if NatGatewayId is not None:
            args["NatGatewayId"] = NatGatewayId

        resp = bt('ec2').create_route(**args)

        return f"{RouteTableId}{ID_DV}{DestinationCidrBlock}"
    
    @staticmethod
    def delete(id):
        RouteTableId, _, DestinationCidrBlock = id.rpartition(ID_DV)

        try:
            bt('ec2').delete_route(
                RouteTableId = RouteTableId,
                DestinationCidrBlock = DestinationCidrBlock
            )
        except ClientError as e:
            if e.response['Error']['Message'][:25] == 'cannot remove local route':
                pass  # it is kinda ok
            else:
                raise # all other are not


class EC2_VPC(awsObject): 
    Prefix = "vpc"
    Draw = DRAW.ALL
    Icon = "Arch_Amazon-Virtual-Private-Cloud_48"
    Color = COLOR.BLUE

    @staticmethod
    def fields():
        return {
                    "VpcId"           : (EC2_VPC, FIELD.ID),
                    "NetworkAclId"    : (EC2_NetworkAcl),
                    'Tags'            : ({"Key" : "Value"})
#                    'CidrBlockAssociationSet' : [{'AssociationId': 'vpc-cidr-assoc-070bb...bcc9c9695b', 'CidrBlock': '10.222.0.0/16', 'CidrBlockState': {...}}],
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        resp = bt('ec2').describe_vpcs(**idpar(('VpcIds', id), PAR.LIST))
        return resp['Vpcs']
    
    def get_ext(self):
        return f"{getattr(self, 'CidrBlock', '-')}"
    
    @staticmethod
    def create(name, CidrBlock):
        id = bt('ec2').create_vpc(CidrBlock=CidrBlock)['EC2_VPC']['VpcId']
        Tag.create(id, "Name", f"{EC2_VPC.Prefix}-{name}")
        return id
    
    @staticmethod
    def delete(id):
        bt('ec2').delete_vpc(
            VpcId = id
        )
    
    @staticmethod
    def cli_add(name, CidrBlock):
        return f"id000000001"

class EC2_NetworkInterface(awsObject): 
    Prefix = "ni"
    Icon = "VPCElasticNetworkInterface"
    Color = COLOR.BLUE_DARK
    ListName = "NetworkInterfaces"

    @staticmethod
    def fields():
        return {
                    "NetworkInterfaceId" : (EC2_NetworkInterface, FIELD.ID),
                    "VpcId"              : EC2_VPC,
                    "SubnetId"           : (EC2_Subnet, FIELD.LIST_ITEM),
                    "ListName"           : (str, FIELD.LIST_NAME),
#                    "PrivateIpAddresses" : str, # print("Private IP Addresses:", [private_ip['PrivateIpAddress'] for private_ip in network_interface['PrivateIpAddresses']])
#                    "Attachment"         : str, #    print("Attachment ID:", network_interface['Attachment']['AttachmentId'])
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        return bt('ec2').describe_network_interfaces(**idpar(('NetworkInterfaceIds', id), PAR.LIST))['NetworkInterfaces']


class S3_Bucket(awsObject): 
    Prefix = "s3"
    Icon = "Arch_Amazon-Simple-Storage-Service_48"

    @staticmethod
    def fields():
        return {
                    "Name" : (S3_Bucket, FIELD.ID),
                }
    
    @staticmethod
    def aws_get_objects(id=None):
        if id is None:
            response = bt('s3').list_buckets()
            return response['Buckets']
        else:
            # response = bt('s3').head_bucket(Bucket=id)
            return [{ "Name" : id }]

    def upload_file(id, s3_key, file_path):
        response = bt('s3').upload_file(file_path, id, s3_key, ExtraArgs={'ContentType': 'text/html'})

    def put_object_acl(id, s3_key, acl):
        response = bt('s3').put_object_acl(ACL=acl, Bucket=id, Key=s3_key)


    def clear_bucket(id):
        s3 = bt('s3')
        response = s3.list_objects_v2(Bucket=id)

        if 'Contents' in response:
            for obj in response['Contents']:
                s3.delete_object(Bucket=id, Key=obj['Key'])

    def html_wrap(self):
        region = "{region}"
        return awsObject.html_root() + f"s3/buckets/{self.Name}" # ?region={region}&bucketType=general&tab=objects


class EC2_EIP(awsObject):
    Prefix = "eipassoc"
    Icon = "ElasticIP"
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
                    'AllocationId': (EC2_EIP, FIELD.ID),
                    'Tags': ({"Key" : "Value"}),
                }
    
    @staticmethod
    def create(name):
        id = bt('ec2').allocate_address(Domain='vpc')['AllocationId']
        Tag.create(id, "Name", f"{EC2_EIP.Prefix}-{name}")
        return id
    
    @staticmethod
    def delete(id):
        bt('ec2').release_address(
            AllocationId = id
        )

    @staticmethod
    def aws_get_objects(id=None):
        resp = bt('ec2').describe_addresses(**idpar(('AllocationIds', id), PAR.LIST))
        return resp['Addresses']


class EC2_KeyPair(awsObject):
    Prefix = "key"
    Icon = "KeyPair"
    
    @staticmethod
    def fields():
        return {
                    'KeyPairId': (EC2_KeyPair, FIELD.ID),
                    'Tags': ({"Key" : "Value"}),
                }
    
    def Destroy(id):
        bt('ec2').delete_key_pair(KeyPairId = id)

    @staticmethod
    def cli_add(name):
        return f"aws ec2 create-key-pair --key-name {name} --query 'KeyMaterial' --output text > {name}.pem"

    @staticmethod
    def cli_del(name):
        return f"aws ec2 delete-key-pair --key-name {name}"

    @staticmethod
    def aws_get_objects(id=None):
        response = bt('ec2').describe_key_pairs(**idpar(('KeyPairIds', id), PAR.LIST))
        return response['KeyPairs']

    def get_view(self):
        return f"{self.KeyName}"


    @staticmethod
    def create(name, path):
        # KeyName = f"{EC2_KeyPair.Prefix}-{name}"

        resp = bt('ec2').create_key_pair(KeyName=name)
        private_key = resp['KeyMaterial']

        try:
            with open(path, 'w') as key_file: key_file.write(private_key)
        except Exception as e:
            print(f"EC2_KeyPair.create: An exception occurred: {type(e).__name__} - {e}")

        id = resp['KeyPairId']
        return id
    
    @staticmethod
    def delete(id, path):
        bt('ec2').delete_key_pair(KeyPairId = id)

        try:
            if os.path.exists(path):
                os.remove(path)
        except Exception as e:
            print(f"EC2_KeyPair.delete: An exception occurred: {type(e).__name__} - {e}")


    @staticmethod
    def IdToName(KeyPairId):
    #   KeyName = bt('ec2').EC2_KeyPair(KeyPairId).key_name # does not work
        resp = bt('ec2').describe_key_pairs(KeyPairIds=[KeyPairId])
        KeyName = resp['KeyPairs'][0]['KeyName']
        return KeyName
    
    @staticmethod
    def NameToId(name):
        resp = bt('ec2').describe_key_pairs(KeyNames=[name])
        KeyPairId = resp['KeyPairs'][0]['KeyPairId']
        return KeyPairId


class SNS_Topic(awsObject):
    Color = COLOR.RED
    Icon = "Arch_Amazon-Simple-Notification-Service_48"

    @staticmethod
    def create(name):
        resp = bt('sns').create_topic(Name=name)
        return resp['TopicArn']
    
    @staticmethod
    def form_id(resp, id_field):
        topic_arn = resp["TopicArn"]
        name = topic_arn.split(':')[-1]
        return name

    @staticmethod
    def aws_get_objects(id=None):
        topics = bt('sns').list_topics()['Topics']

        if id == None:
            return topics
        
        for topic in topics:
            if topic == 0:
                return [topic]

        return []
    
    def html_wrap(self):
        return awsObject.html_home("sns") + f"/topic/{self.TopicArn}"



class CloudTrail_Trail(awsObject):
    Color = COLOR.RED
    Icon = "Arch_AWS-CloudTrail_48"

    @staticmethod
    def fields():
        return {
                    'Name': (CloudTrail_Trail, FIELD.ID),
                    'S3BucketName': (S3_Bucket, FIELD.LINK),
                    'KmsKeyId_Local': (KMS_Key, FIELD.LINK),
                }

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        
        self.KmsKeyId_Local = self.KmsKeyId.split('/')[-1]

    @staticmethod
    def aws_get_objects(id=None):
        response = bt('cloudtrail').describe_trails(**idpar(('trailNameList', id), PAR.LIST))
        return response['trailList']

    def html_wrap(self):
        return awsObject.html_home("cloudtrailv2") + f"/trails/{self.TrailARN}"


class KMS_Key(awsObject):
    Color = COLOR.CRIMSON
    Icon = "Arch_AWS-Key-Management-Service_48"

    @staticmethod
    def fields():
        return {
                    'KeyId': (KMS_Key, FIELD.ID),
                }

    @staticmethod
    def aws_get_objects(id=None):
        if id==None:
            response = bt('kms').list_keys()
            return response['Keys']
        else:
            response = bt('kms').describe_key(KeyId=id)
            return [response['KeyMetadata']]

    def html_wrap(self):
        return awsObject.html_home("kms") + f"/kms/keys/{self.KeyId}"


class IAM_User(awsObject):
    Icon = "Res_User_48_Light"

    @staticmethod
    def fields():
        return {
                    'UserName': (IAM_User, FIELD.ID),
                    'AttachedPolicies': ((IAM_Policy,), FIELD.LINK_IN),
                }

    @staticmethod
    def aws_get_objects(id=None):
        btiam = bt('iam')

        if id is None:
            response = btiam.list_users()
            items = response['Users']
        
        else:
            response = btiam.get_user(UserName=id)
            items = [response['User']]

        for item in items:
            attached_policies = btiam.list_attached_user_policies(UserName=item["UserName"])['AttachedPolicies']
            item["AttachedPolicies"] = [item["PolicyArn"].replace(":", "-") for item in attached_policies]

        return items

    def html_wrap(self):
        return awsObject.html_home("iam") + f"/users/details/{self.UserName}"



class IAM_Group(awsObject):
    Icon = "Res_Users_48_Light"

    @staticmethod
    def fields():
        return {
                    'GroupName': (IAM_Group, FIELD.ID),
                    'Users': ((IAM_User,), FIELD.LINK_IN),
                    'AttachedPolicies': ((IAM_Policy,), FIELD.LINK_IN),
                }

    @staticmethod
    def aws_get_objects(id=None):
        btiam = bt('iam')

        if id is None:
            response = btiam.list_groups()
            items = response['Groups']
        
        else:
            response = btiam.get_group(GroupName=id)
            items = [response['Group']]
        
        for item in items:
            response = btiam.get_group(GroupName=item["GroupName"])
            item["Users"] = [user["UserName"] for user in response["Users"]]

            attached_policies = btiam.list_attached_group_policies(GroupName=item["GroupName"])['AttachedPolicies']
            item["AttachedPolicies"] = [item["PolicyArn"].replace(":", "-") for item in attached_policies]

        return items

    def html_wrap(self):
        return awsObject.html_home("iam") + f"/groups/details/{self.GroupName}"


class IAM_Role(awsObject):
    Icon = "IAMRole"

    @staticmethod
    def fields():
        return {
               'RoleName': (IAM_Role, FIELD.ID),
               'AttachedPolicies': ((IAM_Policy,), FIELD.LINK_IN),
            }

    @staticmethod
    def aws_get_objects(id = None):
        btiam = bt('iam')

        if id is None:
            response = btiam.list_roles()
            items = response['Roles']
        
        else:
            response = btiam.get_role(RoleName=id)
            items = [response['Role']]

        for item in items:
            attached_policies = btiam.list_attached_role_policies(RoleName=item["RoleName"])['AttachedPolicies']
            item["AttachedPolicies"] = [item["PolicyArn"].replace(":", "-") for item in attached_policies]

        return items

    @staticmethod
    def create(name):
        btaim = bt('iam')

        role_policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }

        resp = btaim.create_role(
            RoleName=name,
            AssumeRolePolicyDocument=json.dumps(role_policy_document),
            Description='Role to execute my Lambda function'
        )

        btaim.attach_role_policy(
            RoleName = name,
            PolicyArn = 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )

        return resp['Role']['RoleName']
    
    def html_wrap(self):
        # "https://us-east-1.console.aws.amazon.com/iam/home?region=eu-central-1#/roles/details/management-events-cloud-trail-role?section=permissions"
        return awsObject.html_home("iam") + f"/roles/details/{self.RoleName}"

    
    @staticmethod
    def delete(id):
        btiam = bt('iam')

        attached_policies = btiam.list_attached_role_policies(RoleName = id)['AttachedPolicies']
        for policy in attached_policies:
            btiam.detach_role_policy(RoleName = id, PolicyArn=policy['PolicyArn'])

        btiam.delete_role(RoleName = id)


class IAM_Policy(awsObject):
    Icon = "IAMRole"

    @staticmethod
    def form_id(resp, id_field):
        arn = resp["Arn"]
        arn = arn.replace(":", "-")
        return arn

    @staticmethod
    def aws_get_objects(id = None, scope = 'All', only_attached = True):
        btiam = bt('iam')
        if id is None:
            response = btiam.list_policies(
                Scope=scope, # 'All'|'AWS'|'Local',
                OnlyAttached=only_attached,
                #PolicyUsageFilter = 'PermissionsPolicy'|'PermissionsBoundary'
            )
            return response['Policies']
        
        else:
            # owner, name = s.split('-', 1)
            # PolicyArn=f"arn:aws:iam::'{owner}':policy/service-role/{name}"

            response = btaim.get_policy(PolicyArn=id)
            return [response['Policy']]


class Lambda_Function(awsObject):
    Icon = "Arch_AWS-Lambda_48"
    Color = COLOR.ORANGE
    Draw = DRAW.DEF - DRAW.ID

    @staticmethod
    def fields():
        return {
                    'FunctionName': (Lambda_Function, FIELD.ID),
                    'Tags': ({"Key" : "Value"}),
                    'LogGroup': (Logs_LogGroup, FIELD.LINK),   
                }

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        
        self.LogGroup = self['LoggingConfig']['LogGroup']

    @staticmethod
    def aws_get_objects(id=None):
        if id is None:
            response = bt('lambda').list_functions()
            return response['Functions']
        else:
            response = bt('lambda').get_function(FunctionName=id)
            return [response["Configuration"]] 
        
    @staticmethod
    def str_to_zipped_data(Code):
        data_bytes = Code.encode()
        with io.BytesIO() as zip_buffer:
            with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
                zip_file.writestr('lambda_function.py', data_bytes)

                file_info = zip_file.getinfo('lambda_function.py')
                unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH
                file_info.external_attr = unix_st_mode << 16 

            return zip_buffer.getvalue()

    @staticmethod
    def create(name, code, role_arn = None):
        handler = 'lambda_function.lambda_handler'
        runtime = 'python3.12'
        zipped_data = Lambda_Function.str_to_zipped_data(code)

        params = {
            "FunctionName": name,
            "Runtime": runtime,
            "Handler": handler,
            "Code": {'ZipFile': zipped_data},
            "Timeout": 30,
            "MemorySize": 128,
            "Role": role_arn
        }

        response = bt('lambda').create_function(**params)
        return response['FunctionName']
    
    def wait_for_update(self, delay=1, max_attempts=15):
        btlambda = bt('lambda')

        attempts = 0
        while attempts < max_attempts:
            response = btlambda.get_function(FunctionName=self.FunctionName)
            status = response['Configuration']['LastUpdateStatus']
            if status == 'Successful':
                return
            elif status == 'Failed':
                raise Exception("Function update failed.")
            else:
                time.sleep(delay)
                attempts += 1
        raise Exception("Function update did not complete within the expected time.")        

    def update_code(self, code):
        zipped_data = Lambda_Function.str_to_zipped_data(code)

        response = bt('lambda').update_function_code(
            FunctionName=self.FunctionName,
            ZipFile=zipped_data,
            Publish=True  # Set to True to publish a new version of the Lambda function
        )

        self.wait_for_update()

    def invoke(self, payload):
        response = bt('lambda').invoke(
            FunctionName=self.FunctionName,
            InvocationType='RequestResponse',  # or 'Event' for async call
            Payload=str(payload).replace("'",'"')
        )

        result = response['Payload'].read().decode('utf-8')
        result = json.loads(result)
        return result
    
    @staticmethod
    def delete(id):
        bt('lambda').delete_function(FunctionName=id)

    def html_wrap(self):
        return awsObject.html_home("lambda") + f"/functions/{self.FunctionName}"


class RDS_DBInstance(awsObject):
    Icon = "Arch_Amazon-RDS_48"
    Color = COLOR.LILA

    @staticmethod
    def fields():
        return {
                    'DBInstanceIdentifier': (RDS_DBInstance, FIELD.ID),
                    'DBSubnetGroupName': (RDS_DBSubnetGroup, FIELD.OWNER),
                    'Tags': ({"Key" : "Value"}),
                }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('rds').describe_db_instances(**idpar(('DBInstanceIdentifier', id)))
        return response['DBInstances']

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)

        if hasattr(self, "DBSubnetGroup"):
            setattr(self, "DBSubnetGroupName", self.DBSubnetGroup["DBSubnetGroupName"])
    
    @staticmethod
    def create(name, DBSubnetGroupName, IAM_User, Pass):
        response = bt('rds').create_db_instance(
            DBInstanceIdentifier = name,
            DBInstanceClass = Y3A.Const['RDS.InstanceType'],
            Engine = Y3A.Const['RDS.Engine'],
            MasterUsername=IAM_User,
            MasterUserPassword=Pass,
            AllocatedStorage=20,
            DBSubnetGroupName=DBSubnetGroupName,
            MultiAZ=False,
            PubliclyAccessible=True,
        )

        return response['RDS_DBInstance']['DBInstanceIdentifier']

    @staticmethod
    def delete(id, SkipFinalSnapshot = True):
        bt('rds').delete_db_instance(
            DBInstanceIdentifier = id,
            SkipFinalSnapshot = SkipFinalSnapshot
        )        
    
class RDS_DBSubnetGroup(awsObject):
    Icon = "Arch_Amazon-RDS_48"
    Color = COLOR.LILA

    @staticmethod
    def fields():
        return {
                    'DBSubnetGroupName': (RDS_DBSubnetGroup, FIELD.ID),
                    'VpcId': (EC2_VPC, FIELD.OWNER),
                    'Subnets': [RDS_DBSubnetGroup_Subnet],
                }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('rds').describe_db_subnet_groups(**idpar(('DBSubnetGroupName', id)))
        return response['DBSubnetGroups']
    
    @staticmethod
    def create(name, DBSubnetGroupDescription, SubnetIds):
        response = bt('rds').create_db_subnet_group(
            DBSubnetGroupName = name,
            DBSubnetGroupDescription=DBSubnetGroupDescription,
            SubnetIds = SubnetIds
        )
        return response['DBSubnetGroup']['DBSubnetGroupName']

    @staticmethod
    def delete(id):
        response = bt('rds').delete_db_subnet_group(DBSubnetGroupName=id)
        return

class RDS_DBSubnetGroup_Subnet(awsObject):
    UseIndex = True
    ListName = "Subnets"
    DoNotFetch = True

    @staticmethod
    def fields():
        return {
                    'SubnetIdentifier': (EC2_Subnet, FIELD.LINK_IN),
                    '_parent': (RDS_DBSubnetGroup, FIELD.LIST_ITEM),
                    'ListName': (str, FIELD.LIST_NAME),
                    'View': (str, FIELD.VIEW),
                }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["SubnetIdentifier"]}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.View = f"{self.SubnetIdentifier}"

    @staticmethod
    def aws_get_objects(id = None):
        return RDS_DBSubnetGroup.get_objects_by_index(id, "Subnets", 'SubnetIdentifier')

class DynamoDB_Table(awsObject):
    Icon = "Arch_Amazon-DynamoDB_48"
    Color = COLOR.LILA

    @staticmethod
    def fields():
        return {
                    'TableName': (DynamoDB_Table, FIELD.ID),
                }

    @staticmethod
    def aws_get_objects(id = None):
        if id is None:
            response = bt('dynamodb').list_tables()
            res = []
            for curid in response["TableNames"]:
                res += DynamoDB_Table.aws_get_objects(curid)
            return res
        
        else:
            response = bt('dynamodb').describe_table(TableName = id)
            return [response["Table"]]

    @staticmethod
    def create(id):
        attribute_definitions = [
            {'AttributeName': 'id', 'AttributeType': 'N'}, # Add other attribute definitions as needed
        ]
        key_schema = [
            {'AttributeName': 'id', 'KeyType': 'HASH'}, # Add other key schema elements as needed
        ]
        provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}

        response = bt('dynamodb').create_table(
            TableName=id,
            AttributeDefinitions=attribute_definitions,
            KeySchema=key_schema,
            ProvisionedThroughput=provisioned_throughput
        )
        return id

    @staticmethod
    def delete(id):
        response = bt('dynamodb').delete_table(TableName=id)
        return


class AWS_AMI(awsObject):
    Icon = "Res_Amazon-EC2_Instance_48"
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
                    'ImageId': (AWS_AMI, FIELD.ID),
                }

    @staticmethod
    def aws_get_objects(id = None):
        # filters = [
        #     {'Name': 'owner-id', 'Values': ['your_account_id']},
        #     {'Name': 'state', 'Values': ['available']}
        # ]
        response = bt('ec2').describe_images(**idpar([('ImageIds', id), ('owner-id', "1234")], PAR.LIST))  # todo 
        return response["Images"]


class AWS_AvailabilityZone(awsObject):
    @staticmethod
    def fields():
        return {
                    'ZoneId': (AWS_AvailabilityZone, FIELD.ID),
                    'ZoneName': (str, FIELD.VIEW),
                    'RegionName': (AWS_Region, FIELD.OWNER),
                }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('ec2').describe_availability_zones()

        if id == None:
            return response["AvailabilityZones"]

        return [next((zone for zone in response['AvailabilityZones'] if zone['ZoneId'] == id), None)]


class AWS_Region(awsObject):
    @staticmethod
    def fields():
        return {
                    'RegionId': (AWS_Region, FIELD.ID),
                }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('ec2').describe_availability_zones()

        if id != None:
            return [{"RegionId" : id}]

        keys = []
        regions = []
        for az in response["AvailabilityZones"]:
            reg = az["RegionName"]
            if not reg in keys:
                regions.append({"RegionId" : reg})
                keys.append(reg)

        return regions


class ELB_LoadBalancer(awsObject):
    Icon = "Arch_Elastic-Load-Balancing_48"
    Color = COLOR.BLUE

    @staticmethod
    def fields():
        return {
                    'DNSName': str,
                    'LoadBalancerArn': str,
                    'LoadBalancerName': (ELB_LoadBalancer, FIELD.ID),
                    'VpcId': (EC2_VPC, FIELD.OWNER),
                    'AvailabilityZones': [ELB_LoadBalancer_AvailabilityZone],
                    # 'SecurityGroups': ['sg-0cd135d2e4a0df03e']
                }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('elbv2').describe_load_balancers(**idpar(('Names', id), PAR.LIST))
        return response['LoadBalancers']


class ELB_LoadBalancer_AvailabilityZone(awsObject):
    @staticmethod
    def fields():
        return {
                    'ZoneName': 'eu-central-1a',
                    'SubnetId': (EC2_Subnet, FIELD.LINK),
                    # 'LoadBalancerAddresses': [],
                    '_parent': (ELB_LoadBalancer, FIELD.OWNER),
                }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["SubnetId"]}"

    @staticmethod
    def aws_get_objects(id = None):
        response = ELB_LoadBalancer.get_objects_by_index(id, "AvailabilityZones", 'SubnetIdentifier')
        return response


class ELB_TargetGroup(awsObject):
    @staticmethod
    def fields():
        return {
            'TargetGroupName': (ELB_TargetGroup, FIELD.ID),
            'VpcId': (EC2_VPC, FIELD.LINK),
            # 'LoadBalancerArns': ['arn:aws:elasticloadbalancing:eu-central-1:047989593255:loadbalancer/app/ALB-Frederick/211b0083ba139ccd']
        }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('elbv2').describe_target_groups(**idpar(('Names', id), PAR.LIST))
        return response['TargetGroups']


class ELB_Listener(awsObject):
    @staticmethod
    def fields():
        return {
            'ListenerArn': (ELB_Listener, FIELD.ID),
            "LoadBalancerName": (ELB_LoadBalancer, FIELD.OWNER),
        }

    @staticmethod
    def aws_get_objects(id = None):
        if id == None:
            lbs = ELB_LoadBalancer.aws_get_objects()
            res = []
            for lb in lbs:
                response = bt('elbv2').describe_listeners(LoadBalancerArn = lb["LoadBalancerArn"])["Listeners"]

                for ls in response:
                    ls["LoadBalancerName"] = lb["LoadBalancerName"]

                res += response

        else:
            res = bt('elbv2').describe_listeners(ListenerArns = [id])["Listeners"]

            lb = ELB_LoadBalancer.get_objects({'LoadBalancerArns': (res[0]["LoadBalancerArn"], PAR.LIST)})

            res[0]["LoadBalancerName"] = lb[0]["LoadBalancerName"]

        return res


class AutoScaling_LaunchConfiguration(awsObject):
    Icon = "Arch_Elastic-Load-Balancing_48"
    Color = COLOR.BLUE

    @staticmethod
    def fields():
        return {
            'LaunchTemplateId': (AutoScaling_LaunchConfiguration, FIELD.ID),
            'LaunchTemplateName': (str, FIELD.VIEW),
            'CreatedBy': (IAM_User, FIELD.LINK_IN),
        }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('ec2').describe_launch_templates(**idpar(('LaunchTemplateIds', id), PAR.LIST))
        return response['LaunchTemplates']


class AutoScaling_AutoScalingGroup(awsObject):
    Icon = "Arch_Elastic-Load-Balancing_48"
    Color = COLOR.BLUE

    @staticmethod
    def fields():
        return {
            'AutoScalingGroupName': (AutoScaling_AutoScalingGroup, FIELD.ID),
        }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('autoscaling').describe_auto_scaling_groups(**idpar(('AutoScalingGroupNames', id), PAR.LIST))
        return response['AutoScalingGroups']


class CloudFormation_Stack(awsObject):
    Icon = "Arch_AWS-CloudFormation_48"
    Color = COLOR.RED

    @staticmethod
    def fields():
        return {
            'StackName': (CloudFormation_Stack, FIELD.ID),
            'Tags': ({"Key" : "Value"}),
        }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('cloudformation').describe_stacks(**idpar(('StackName', id)))
        return response['Stacks']
    
    @staticmethod
    def create(stack_name, template_body, parameters = None):
        cf_pars = [{'ParameterKey': key, 'ParameterValue': value} for key, value in parameters.items()] if parameters != None else []
        response = bt('cloudformation').create_stack(StackName=stack_name, TemplateBody=template_body, Parameters=cf_pars, Capabilities=['CAPABILITY_IAM'])

        Wait('cloudformation', 'stack_create_complete', "StackName", stack_name)

        return stack_name
    
    @staticmethod
    def update(stack_name, template_body, parameters = None):
        cf_pars = [{'ParameterKey': key, 'ParameterValue': value} for key, value in parameters.items()] if parameters != None else []
        response = bt('cloudformation').update_stack(StackName=stack_name, TemplateBody=template_body, Parameters=cf_pars, Capabilities=['CAPABILITY_IAM'])

        Wait('cloudformation', 'stack_update_complete', "StackName", stack_name)

        return stack_name

    @staticmethod
    def delete(StackName):
        response = bt('cloudformation').delete_stack(StackName=StackName)

        Wait('cloudformation', 'stack_delete_complete', "StackName", StackName)

        return

    def html_wrap(self):
        return awsObject.html_home("cloudformation") + f"/stacks/stackinfo?stackId={self.StackId}"
    

class CloudFormation_StackResource(awsObject):
    ListName = "Resources"

    @staticmethod
    def fields():
        return {
            'StackName': (CloudFormation_Stack, FIELD.LIST_ITEM),
            "ListName" : (str, FIELD.LIST_NAME),
            'View': (CloudFormation_StackResource, FIELD.VIEW),
            'PhysicalResourceId': (None, FIELD.LINK),
        }

    @staticmethod
    def form_id(resp, id_field):
        PhysicalResourceId = resp["PhysicalResourceId"] if "PhysicalResourceId" in resp else ""
        PhysicalResourceId = PhysicalResourceId.replace(ID_DV, "_")
        PhysicalResourceId = PhysicalResourceId.replace(":", "_")
        return f"{resp["StackName"]}{ID_DV}{PhysicalResourceId}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)

        PhysicalResourceId = resp["PhysicalResourceId"] if "PhysicalResourceId" in resp else ""

        self.View = f"{self.ResourceType.replace('AWS::', '')}::{PhysicalResourceId}"

        self.ResourceType = str_to_class(self.ResourceType)

        if self.ResourceType == ECS_Service:
            parts = PhysicalResourceId.split('/')
            self.PhysicalResourceId = f"{parts[-2]}|{parts[-1]}"

    def get_actual_field_type(self, field):
        if field == 'PhysicalResourceId':
            return self.ResourceType

        return super().get_actual_field_type(field)

    @staticmethod
    def aws_get_objects(id = None):
        StackId = None
        StackResourceId = None
        if id:
            StackId, _, StackResourceId = id.rpartition(ID_DV)

        res = []
        for stack in CloudFormation_Stack.aws_get_objects(StackId):
            for resource in bt('cloudformation').describe_stack_resources(**idpar(('StackName', stack['StackName'])))['StackResources']:
                if StackResourceId and StackResourceId != "*" and resource['PhysicalResourceId'] != StackResourceId:
                    continue
                res.append(resource)

        return res
    

class ApiGateway_RestApi(awsObject):
    Icon = "Arch_Amazon-API-Gateway_48"
    Color = COLOR.RED

    @staticmethod
    def fields():
        return {
            'id': (ApiGateway_RestApi, FIELD.ID),
            'name': (str, FIELD.VIEW),
            'Tags': ({"Key" : "Value"}),
        }

    @staticmethod
    def aws_get_objects(id = None):
        if id == None:
            return bt('apigateway').get_rest_apis()['items']
        else:
            response = bt('apigateway').get_rest_api(restApiId = id)
            del response['ResponseMetadata']
            return [response]
        
    def html_wrap(self):
        return awsObject.html_root() + f"/apigateway/main/apis/{self.id}"


class ApiGateway_Resource(awsObject):
    Icon = "Arch_Amazon-API-Gateway_48-Resource"
    Color = COLOR.RED_DARK

    @staticmethod
    def fields():
        return {
            '_parent': (ApiGateway_RestApi, FIELD.OWNER),
            'path': (str, FIELD.VIEW),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["id"]}"

    @staticmethod
    def aws_get_objects(id = None):
        return ApiGateway_RestApi.get_objects_by_index(id, ApiGateway_Resource, "id")

    @staticmethod
    def get_objects_of_parent(parent, id):
        if id == None:
            return bt('apigateway').get_resources(restApiId=parent)["items"]
        else:
            response = bt('apigateway').get_resource(restApiId=parent, resourceId=id)
            del response['ResponseMetadata']
            return [response]


class ApiGateway_Method(awsObject):
    ListName = "Methods"

    @staticmethod
    def fields():
        return {
            "ListName" : (str, FIELD.LIST_NAME),
            '_parent': (ApiGateway_Resource, FIELD.LIST_ITEM),
            'View': (str, FIELD.VIEW),
            'Link': (None, FIELD.LINK),
        }

    def get_actual_field_type(self, field):
        if field == 'Link':
            return self.LinkType

        return super().get_actual_field_type(field)

    @staticmethod
    def aws_get_objects(id = None):
        client = bt('apigateway')

        par_query = None
        kind_query = None
        if id is not None:
            par_query, _, kind_query = id.rpartition(ID_DV)

        resources = ApiGateway_Resource.get_objects(par_query)

        result = []
        for resource in resources:
            if "resourceMethods" in resource:
                for method, _ in resource["resourceMethods"].items():

                    response = client.get_method(
                        restApiId  = resource['_parent'],
                        resourceId = resource['id'],
                        httpMethod = method
                    )
                    
                    del response['ResponseMetadata']
                    response["_parent"] = f"{resource['_parent']}{ID_DV}{resource['id']}"
                    response["_id"] = f"{resource['_parent']}{ID_DV}{resource['id']}{ID_DV}{method}"

                    response["View"] = response['httpMethod']
                    if 'uri' in response['methodIntegration']:
                        arn = response['methodIntegration']['uri']
                        arn_components = arnparse(arn)
                        parts = arn_components.resource.split('/')

                        arn = parts[3]
                        arn_components = arnparse(arn)

                        response["Link"] = arn_components.resource
                        response["LinkType"] = str_to_class(f"{arn_components.partition.upper()}::{arn_components.service.capitalize()}::{arn_components.resource_type.capitalize()}")

                        response["View"] += ": " + arn_components.resource

                    result.append(response)

        return result


class ApiGateway_DomainName(awsObject):
    Icon = "domain_name"
    Color = COLOR.RED
    Draw = DRAW.DEF - DRAW.ID

    @staticmethod
    def fields():
        return {
            'domainName': (ApiGateway_DomainName, FIELD.ID),
            'Tags': ({"Key" : "Value"}),
        }

    @staticmethod
    def aws_get_objects(id = None):
        response = bt('apigateway').get_domain_names()['items']
        if id != None:
            for domainName in response:
                if domainName['domainName'] == id:
                    return [domainName]
            return []
        else:
            return response


class ApiGateway_BasePathMapping(awsObject):
    ListName = "API mappings"

    @staticmethod
    def fields():
        return {
            "ListName" : (str, FIELD.LIST_NAME),
            '_parent': (ApiGateway_DomainName, FIELD.LIST_ITEM),
            'restApiId': (ApiGateway_RestApi, FIELD.LINK),
            'View': (str, FIELD.VIEW),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["restApiId"]}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.View = self.restApiId

    @staticmethod
    def aws_get_objects(id = None):
        return ApiGateway_DomainName.get_objects_by_index(id, ApiGateway_BasePathMapping, "restApiId")

    @staticmethod
    def get_objects_of_parent(parent, id):
        return bt('apigateway').get_base_path_mappings(**idpar({"domainName": parent}))["items"]
    

class Route53_HostedZone(awsObject):
    Icon = "Arch_Amazon-Route-53_48"
    Color = COLOR.BLUE

    @staticmethod
    def fields():
        return {
            'Id': (Route53_HostedZone, FIELD.ID),
            'Name': (str, FIELD.VIEW),
            'Tags': ({"Key" : "Value"}),
        }

    @staticmethod
    def aws_get_objects(id = None):
        if id == None:
            return bt('route53').list_hosted_zones()['HostedZones']
        
        else:
            response = bt('route53').get_hosted_zone(Id=id)
            return [response['HostedZone']]


class Route53_RecordSet(awsObject):
    ListName = "Records"

    @staticmethod
    def fields():
        return {
            "ListName" : (str, FIELD.LIST_NAME),
            '_parent': (Route53_HostedZone, FIELD.LIST_ITEM),
            'Name': (str, FIELD.VIEW),
            'Link': (ApiGateway_DomainName, FIELD.LINK),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["Name"]}"

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.Link = self.Name[:-1]

    @staticmethod
    def aws_get_objects(id = None):
        return Route53_HostedZone.get_objects_by_index(id, Route53_RecordSet, "Name")

    @staticmethod
    def get_objects_of_parent(parent, id):
        return bt('route53').list_resource_record_sets(**idpar({"HostedZoneId": parent}))["ResourceRecordSets"]


class Logs_LogGroup(awsObject):
    Icon = "Arch_Amazon-CloudWatch_48"
    Color = COLOR.RED
    Draw = DRAW.DEF - DRAW.ID

    @staticmethod
    def fields():
        return {
            'logGroupName': (Logs_LogGroup, FIELD.ID),
        }

    @staticmethod
    def aws_get_objects(id = None):
        return bt('logs').describe_log_groups(**idpar(('logGroupNamePrefix', id)))['logGroups']


class ECR_Repository(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Registry_48"
    Color = COLOR.ORANGE
    Draw = DRAW.DEF

    @staticmethod
    def fields():
        return {
            'repositoryName': (ECR_Repository, FIELD.ID),
        }

    @staticmethod
    def aws_get_objects(id = None):
        return bt('ecr').describe_repositories(**idpar({"repositoryNames": id}, PAR.LIST))['repositories']


class ECR_Repository_Image(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Registry_48"
    Color = COLOR.ORANGE
    ListName = "Images"

    @staticmethod
    def fields():
        return {
            "ListName" : (str, FIELD.LIST_NAME),
            '_parent': (ECR_Repository, FIELD.LIST_ITEM),
            'imageTag': (str, FIELD.VIEW),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["imageDigest"].replace(":", "_")}"

    @staticmethod
    def aws_get_objects(id = None):
        return ECR_Repository.get_objects_by_index(id, ECR_Repository_Image, "imageTag")

    @staticmethod
    def get_objects_of_parent(parent, id):
        resp = bt('ecr').list_images(**idpar({"repositoryName": parent}))
        return resp["imageIds"]


class ECS_Cluster(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Service_48"
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
            'clusterName': (ECS_Cluster, FIELD.ID),
        }

    @staticmethod
    def aws_get_objects(id = None):
        if id == None:
            resp = bt('ecs').list_clusters()
            ids = [cluster_arn.split('/')[-1] for cluster_arn in resp["clusterArns"]]
            return ECS_Cluster.aws_get_objects(ids)
            
        else:
            return bt('ecs').describe_clusters(**idpar({ "clusters": id if isinstance(id, list) else [id] }))['clusters']

    def html_wrap(self):
        res = awsObject.html_root() + f"/ecs/v2/clusters/{self.clusterName}"
        return res


class ECS_Service(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Service_48"
    Color = COLOR.ORANGE

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["_parent"]}{ID_DV}{resp["serviceName"]}"

    @staticmethod
    def fields():
        return {
            '_parent': (ECS_Cluster, FIELD.OWNER),
            'serviceName': (str, FIELD.VIEW),
        }

    @staticmethod
    def aws_get_objects(id = None):
        return ECS_Cluster.get_objects_by_index(id, ECS_Service, "serviceName")

    @staticmethod
    def get_objects_of_parent(parent, id):
        srv = bt('ecs')

        if id == None:
            resp = srv.list_services(**idpar({"cluster": parent}))
            ids = [service_arn.split('/')[-1] for service_arn in resp["serviceArns"]]
        else:
            ids = [id]

        resp = srv.describe_services(cluster=parent, services=ids)

        return resp["services"]
    
    def html_wrap(self):
        res = awsObject.html_root() + f"/ecs/v2/clusters/{self._parent}/services/{self.serviceName}"
        return res


class ECS_TaskDefinition_Family(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Service_48"
    Color = COLOR.ORANGE

    @staticmethod
    def aws_get_objects(id = None):
        if id != None:
            return [{"_id": id}]

        task_defs = ECS_TaskDefinition.aws_get_objects(None)

        exist = {}
        res = []
        for curid in task_defs:
            family = curid["family"]
            if family in exist:
                continue

            exist[family] = True
            res.append({"_id": family})

        return res


class ECS_TaskDefinition(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Service_48"
    Color = COLOR.ORANGE
    ListName = "Tasks"

    @staticmethod
    def fields():
        return {
            "ListName" : (str, FIELD.LIST_NAME),
            'family': (ECS_TaskDefinition_Family, FIELD.LIST_ITEM),
        }

    @staticmethod
    def form_id(resp, id_field):
        return f"{resp["family"]}:{resp["revision"]}"

    @staticmethod
    def aws_get_objects(id = None):
        btecs = bt('ecs')
        if id == None:
            resp = btecs.list_task_definitions()
            ids = [service_arn.split('/')[-1] for service_arn in resp["taskDefinitionArns"]]
        else:
            ids = [id]

        res = []
        for curid in ids:
            resp = btecs.describe_task_definition(taskDefinition=curid)
            res.append(resp['taskDefinition'])
        return res


class ECS_Task(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Service_48"
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
            '_parent': (ECS_Service, FIELD.OWNER),
            '_view': (str, FIELD.VIEW),
            '_taskDefinition': (ECS_TaskDefinition, FIELD.LINK_IN),
            '_subnet': (EC2_Subnet, FIELD.LINK_IN),
            '_network_interface': (EC2_NetworkInterface, FIELD.LINK_IN),
        }

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self._view = self.taskArn.split('/')[-1]
        self._taskDefinition = self.taskDefinitionArn.split('/')[-1]

        if len(self.attachments) > 0: # todo ECS_Task_Attachments ??
            att = self.attachments[0]["details"]
            self._subnet            = att[0]["value"]
            self._network_interface = att[1]["value"]

    @staticmethod
    def form_id(resp, id_field):
        return resp["_parent"] + ID_DV + resp["taskArn"].split('/')[-1]

    @staticmethod
    def aws_get_objects(id = None):
        return ECS_Service.get_objects_by_index(id, ECS_Task, "_id")

    @staticmethod
    def get_objects_of_parent(parent, id):
        srv = bt('ecs')

        cluster, serviceName = parent.split('|')

        if id == None:
            resp = srv.list_tasks(
                cluster=cluster,
                serviceName=serviceName
            )
            ids = [service_arn.split('/')[-1] for service_arn in resp["taskArns"]]
        else:
            ids = [id]

        if len(ids) == 0:
            return []

        resp = srv.describe_tasks(
            cluster=cluster,
            tasks=ids
        )

        return resp["tasks"]
    
    def html_wrap(self):
        "wind/services/wind-service/tasks?region=eu-central-1"
        res = awsObject.html_home("kms") + f"/ecs/v2/clusters/"
        return "" # TODO


class ECS_Task_Container(awsObject):
    Icon = "Arch_Amazon-Elastic-Container-Registry_48"
    Color = COLOR.ORANGE

    @staticmethod
    def fields():
        return {
            '_parent': (ECS_Task, FIELD.OWNER),
            'name': (ECS_Task, FIELD.VIEW),
            "_image": (ECR_Repository_Image, FIELD.LINK_IN),
        }

    @staticmethod
    def form_id(resp, id_field):
        return resp["_parent"] + ID_DV + resp["name"].split('/')[-1]

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self._image = self.image.split('/')[-1].replace(":", ID_DV)

    @staticmethod
    def aws_get_objects(id = None):
        return ECS_Task.get_objects_by_index(id, "containers", "name")


class EC2_VPCPeeringConnection(awsObject):
    Prefix = "pcx"
    Color = COLOR.BLUE_DARK
    Icon = "EC2_VPCPeeringConnection"

    @staticmethod
    def fields():
        return {
            'VpcPeeringConnectionId': (EC2_VPCPeeringConnection, FIELD.ID),
            'AccepterVpc': (EC2_VPC, FIELD.LINK_IN),
            'RequesterVpc': (EC2_VPC, FIELD.LINK_IN),
        }

    def __init__(self, aws, id_query, index, resp, do_auto_save=True):
        super().__init__(aws, id_query, index, resp, do_auto_save)
        self.AccepterVpc  = self.AccepterVpcInfo ["VpcId"]
        self.RequesterVpc = self.RequesterVpcInfo["VpcId"]

    @staticmethod
    def aws_get_objects(id = None):
        resp = bt('ec2').describe_vpc_peering_connections(**idpar({"VpcPeeringConnectionIds": id}, PAR.LIST))
        return resp["VpcPeeringConnections"]

    @staticmethod
    def create(VpcId, PeerVpcId, name):
        id = bt('ec2').create_vpc_peering_connection(VpcId=VpcId, PeerVpcId=PeerVpcId)['VpcPeeringConnection']["VpcPeeringConnectionId"]
        Tag.create(id, "Name", f"{EC2_VPCPeeringConnection.Prefix}-{name}")
        return id
    
    @staticmethod
    def delete(id):
        resp = bt('ec2').delete_vpc_peering_connection(VpcPeeringConnectionId=id)
        return
    

class EC2_VPCEndpoint(awsObject):
    Icon = "EC2_VPCEndpoint"
    Color = COLOR.BLUE_DARK

    @staticmethod
    def fields():
        return {
            'VpcEndpointId': (EC2_VPCEndpoint, FIELD.ID),
            'VpcId': (EC2_VPC, FIELD.LINK_IN),
        }

    @staticmethod
    def aws_get_objects(id = None):
        resp = bt('ec2').describe_vpc_endpoints(**idpar({"VpcEndpointIds": id}, PAR.LIST))
        return resp['VpcEndpoints']

    @staticmethod
    def create(VpcId, RouteTableId, VpcEndpointType, ServiceName):
        try:
            response = bt('ec2').create_vpc_endpoint(
                VpcEndpointType=VpcEndpointType, # 'Gateway'/'Interface'
                VpcId=VpcId,
                ServiceName=ServiceName,
                RouteTableIds=[RouteTableId],
            )
        except Exception as e:
            print(f"Cannot create endpoint: {e}")

    @staticmethod
    def delete(id):
        resp = bt('ec2').delete_vpc_endpoints(
                VpcEndpointIds=[id]
            )
        
    def html_wrap(self):
        url = awsObject.html_home("vpcconsole") + f"EndpointDetails:vpcEndpointId={self.VpcEndpointId}"
        return url


class Y3A(ObjectModel):
    def fetch_cf_res_list(self, stack):
        do_auto_save_after = self.do_auto_save
        self.do_auto_save = False

        result = []
        for res in self.CloudFormation_StackResource.fetch(f"{stack}|*"):
            if res.ResourceType == None:
                continue
            try: # to do ..
                result.append(self[res.ResourceType].fetch(res.PhysicalResourceId)[0])
            except Exception as e:
                print(f"Cannot get object: {res.ResourceType} - {res.PhysicalResourceId} - {e}")

        self.save()
        self.do_auto_save = do_auto_save_after

        return result

    def get_cf_res(self, listname, criteria, par = None) -> str:
        list = listname
        if type(list) is str:
            list = self.fetch_cf_res_list(list)

        for res in list:
            if criteria(self, res, par):
                return res
        
        return None

    def __init__(self, profile, path, do_auto_load = True, do_auto_save = True):

        setattr(Y3A, "PROFILE", profile)

        super().__init__(
            path,
            do_auto_load,
            do_auto_save, 
            {
                'EC2.UserData.Apache' : ""\
                                + "#!/bin/bash\n"\
                                + "yum update -y\n"\
                                + "yum install httpd -y\n"\
                                + "systemctl start httpd\n"\
                                + "systemctl enable httpd\n"\
                                + 'echo "<html><body><h1>[Starting page]</h1></body></html>" > /var/www/html/index.html'\
                            ,
                'EC2.InstanceType' : 't2.micro',
                'EC2.ImageId.Linux' : 'ami-0669b163befffbdfc',

                'RDS.InstanceType' : 'db.t3.micro',
                'RDS.Engine' : 'mysql',
                'DrawRDS' : 'EC2_VPC, EC2_Subnet, RDS'
            },
            {
                'IAM'     : [IAM_User, IAM_Group, IAM_Role, IAM_Policy],
                'VPC'     : [EC2_KeyPair, EC2_VPC, EC2_InternetGateway, EC2_VPCGatewayAttachment],
                'SN'      : [EC2_Subnet],
                'RT'      : [EC2_RouteTable, EC2_Route, EC2_RouteTable_Association],
                'EIP'     : [EC2_EIP, EC2_EIPAssociation],
                'NW'      : [EC2_NatGateway, EC2_VPCEndpoint, EC2_VPCPeeringConnection],
                'SG'      : [EC2_SecurityGroup, EC2_SecurityGroup_Rule],
                'NACL'    : [EC2_NetworkAcl, EC2_NetworkAclEntry],
                'EC2'     : [EC2_Instance, EC2_Reservation, EC2_NetworkInterface, EC2_Instance_NetworkInterface], # AWS_AMI, 
                'RDS'     : [RDS_DBSubnetGroup, RDS_DBSubnetGroup_Subnet, RDS_DBInstance, DynamoDB_Table],
                'ELB'     : [ELB_LoadBalancer, ELB_LoadBalancer_AvailabilityZone, ELB_TargetGroup, ELB_Listener, AutoScaling_LaunchConfiguration, AutoScaling_AutoScalingGroup],
                'RAZ'     : [AWS_Region, AWS_AvailabilityZone],
                'CF'      : [CloudFormation_Stack, CloudFormation_StackResource],
                'API'     : [ApiGateway_RestApi, ApiGateway_Resource, ApiGateway_Method, ApiGateway_DomainName, ApiGateway_BasePathMapping],
                'Route53' : [Route53_HostedZone, Route53_RecordSet],
                'S3'      : [S3_Bucket],
                'Lambda'  : [Lambda_Function],
                'SNS'     : [SNS_Topic],
                'LOG'     : [Logs_LogGroup],
                'EC'      : [ECR_Repository, ECR_Repository_Image, ECS_Cluster, ECS_Service, ECS_TaskDefinition_Family, ECS_TaskDefinition, ECS_Task, ECS_Task_Container],
                'CT'      : [CloudTrail_Trail],
                'KMS'     : [KMS_Key],
            }
        )

        self.Classes["All"] = [x for x in self.Classes["ALL"] if x not in [IAM_User, IAM_Group, IAM_Role, EC2_Reservation, AWS_AMI, AWS_Region, AWS_AvailabilityZone]]
        self.Classes["TS" ] = [x for x in self.Classes["All"] if x not in [EC2_KeyPair, EC2_SecurityGroup, EC2_SecurityGroup_Rule, Logs_LogGroup]]

    # DoNotFetch = True TODO remove it!
