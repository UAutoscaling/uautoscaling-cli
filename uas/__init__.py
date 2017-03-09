import os, sys, json, time
BASE = os.path.join(os.path.dirname(os.path.join(__file__)), '..', 'libs')
sys.path.append(BASE)
import argparse
from api import requestToAPI

def createRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "RuleName": args.name,
            "ScaleDirection": args.scale_diretion,
            "ScaleStep": args.scale_step,
            "CooldownTime": 300,
            "CheckPeriod": 1,
            "MetricType": args.metric_type,
            "ConditionType": args.condition_type,
            "ConsecutivePeriods": args.consecutiveperiods,
            "Thresholds": args.thresholds,
            "Action": 'CreateASPolicyRule'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))


def modifyRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "RuleId": args.rule_id,
            "RuleName": args.name,
            "ScaleDirection": args.scale_diretion,
            "ScaleStep": args.scale_step,
            "CooldownTime": 300,
            "CheckPeriod": 1,
            "MetricType": args.metric_type,
            "ConditionType": args.condition_type,
            "ConsecutivePeriods": args.consecutiveperiods,
            "Thresholds": args.thresholds,
            "Action": 'ModifyASPolicyRule'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def listRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "Action": 'GetASPolicyRules'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def delRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "RuleId": args.rule_id,
            "Action": 'DeleteASPolicyRule'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

# instance group
def createInstanceGroup(args):
    params = {
            "Region": args.region,
            "GroupName": args.name,
            "NotificationId": args.notification_id,
            "ScaleMax": args.scale_max,
            "ScaleMin": args.scale_min,
            "BootupConfig": args.bootup_config,
            "RemovePolicy": args.remove_policy,
            "DesiredAmount": args.desired_amount,
            "Action": 'CreateASInstanceGroup'
            }
    if args.ulb:
        params['UlbId'] = args.ulb
        for v,i in zip(args.vserver, xrange(0, len(args.vserver))):
            params['VServerConfigs.%d' %i] = v
    if args.eip:
        params['IsBindEIP'] = args.eip
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def getInstanceGroupList(args):
    params = {
            "Region": args.region,
            "Action": 'GetASInstanceGroupList'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def getInstanceGroup(args):
    params = {
            "GroupId": args.groupId,
            "Region": args.region,
            "Action": 'GetASInstanceGroupDetail'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyInstanceGroup(args):
    params = {
            "Region": args.region,
            "GroupId": args.group_id,
            "Action": 'ModifyASInstanceGroup'
            }
    if args.name:
        params["GroupName"] = args.name
    if args.notification_id:
        params["NotificationId"] = args.notification_id
    if args.scale_max:
        params["ScaleMax"] = args.scale_max
    if args.scale_min:
        params["ScaleMin"] = args.scale_min
    if args.bootup_config:
        params["BootupConfig"] = args.bootup_config
    if args.remove_policy:
        params["RemovePolicy"] = args.remove_policy
    if args.eip:
        params["IsBindEIP"] = args.eip

    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def delInstanceGroup(args):
    params = {
            "GroupId": args.groupId,
            "Region": args.region,
            "Action": 'DeleteASInstanceGroup'
            }
    if args.isKeepInstances:
       params["KeepInstances"] = args.isKeepInstances
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def addVServer(args):
    params = {
            "GroupId": args.groupId,
            "ULBId": args.ulbId,
            "VServerConfig": args.vserverConfig,
            "Region": args.region,
            "Action": 'AddASVServer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def deleteVServer(args):
    params = {
            "GroupId": args.groupId,
            "ULBId": args.ulbId,
            "VServerConfig": args.vserverConfig,
            "Region": args.region,
            "Action": 'DeleteASVServer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))


# instance
def addInstanceToGroup(args):
    params = {
            "InstanceId": args.instanceId,
            "GroupId": args.groupId,
            "Region": args.region,
            "IsLock": args.isLock,
            "Action": 'AddInstanceToGroup'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def removeInstanceFromGroup(args):
    params = {
            "InstanceId": args.instanceId,
            "GroupId": args.groupId,
            "Region": args.region,
            "Action": 'RemoveInstanceFromGroup'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def updateInstanceLockState(args):
    params = {
            "InstanceId": args.instanceId,
            "GroupId": args.groupId,
            "State": args.state,
            "Region": args.region,
            "Action": 'UpdateInstanceLockState'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def createTimerPolicy(args):
    params = {
            "Region": args.region,
            "PolicyName": args.name,
            "PolicyType": 5,
            "ResourceId": 'BandwidthPackage',
            "NotificationId": args.notification_id,
            "ScaleMax": 0,
            "ScaleMin": 0,
            "BootupConfig": args.bootup_config,
            "EIPID": args.eip_id,
            "Action": 'CreateASPolicy'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyTimerPolicy(args):
    params = {
            "Region": args.region,
            "PolicyId": args.id,
            "BootupConfig": args.bootup_config,
            "EIPID": args.eip_id,
            "Action": 'ModifyASPolicy'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def createBootupConfigBandwidthPackage(args):
    params = {
            "Region": args.region,
            "Name": args.name,
            "Bandwidth": args.bandwidth,
            "TimeRange": args.time_range,
            "Action": 'CreateASBootupConfigBandwidthPackage'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyBootupConfigBandwidthPackage(args):
    params = {
            "Region": args.region,
            "ConfigId": args.id,
            "Action": 'ModifyASBootupConfigBandwidthPackage'
            }
    if args.name:
        params["Name"] = args.name
    if args.bandwidth:
        params["Bandwidth"] = args.bandwidth
    if args.time_range:
        params["TimeRange"] = args.time_range
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))



def getBWTimerDetail(policyId, publicKey, privateKey, projectId, region):
    result = {}
    params_p = {
            "Region": region,
            "PolicyId": policyId,
            "Action": 'GetASPolicyDetail'
            }
    r_p = requestToAPI(publicKey, privateKey, projectId, params_p)
    r_p = json.loads(r_p)
    if r_p['RetCode'] != 0 :
        print(json.dumps(r_p, indent=4))
        return result

    result['EIPID'] = r_p['EIPID']

    params = {
            "Region": region,
            "ConfigId": r_p['BootupConfig'],
            "Action": 'GetASBootupConfigBandwidthPackage'
            }
    r = requestToAPI(publicKey, privateKey, projectId, params)
    r = json.loads(r)
    if r['RetCode'] != 0 :
        print(json.dumps(r, indent=4))
        return result

    result['Bandwidth'] = r['Bandwidth']
    result['TimeRange'] = r['TimeRange']
    return result

def getIGTimerDetail(path):
    result = {}
    ps = path.split('?')
    result["GroupId"] = ps[0]
    res = ps[1].split('&')
    result["ScaleMax"] = res[0].split("=")[1]
    result["ScaleMin"] = res[1].split("=")[1]
    return result

def getTimer(args):
    params = {
            "Region": args.region,
            "TaskId": args.id,
            "Action": 'GetASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)

    if r['RetCode'] != 0 :
        print(json.dumps(result, indent=4))
        return

    result = {}
    result['Name'] = r['Name']
    result['Status'] = r['Status']
    result['Period'] = r['Period']
    result['StartTime'] = r['StartTime']
    result['EndTime'] = r['EndTime']
    result['TimerType'] = r['TimerType']
    result['NotificationId'] = r['NotificationId']

    path = {}
    if(r["TimerType"] == "INSTANCE_GROUP"):
        path = getIGTimerDetail(r["TimerActionPath"])
    elif(r["TimerType"] == "BANDWIDTH_PACKAGE"):
        path = getBWTimerDetail(r["TimerActionPath"], args.publicKey, args.privateKey, args.projectId, args.region)
    else:
        print('unkown type', r["TimerType"])
    result = dict(result, **path)
    print(json.dumps(result, indent=4))

def listTimer(args):
    params = {
            "Region": args.region,
            "Action": 'GetASTimerList'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def updateTimerStatus(args):
    if (args.status != 'ON' and args.status != 'OFF') :
        print('status must be ON or OFF')
        return
    params = {
            "Region": args.region,
            "TaskId": args.id,
            "Status": args.status,
            "Action": 'UpdateASTimerStatus'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def createBandwidthPackageTimer(args):
    with open(args.config, 'r') as f:
        config = json.load(f)

    params_b = {
            "Region": args.region,
            "Name": config['Name'],
            "Bandwidth": config['Bandwidth'],
            "TimeRange": config['TimeRange'],
            "Action": 'CreateASBootupConfigBandwidthPackage'
            }
    r_b = requestToAPI(args.publicKey, args.privateKey, args.projectId, params_b)
    r_b = json.loads(r_b)
    # print(json.dumps(r_b, indent=4))

    if r_b['RetCode'] != 0 :
        return

    params_p = {
            "Region": args.region,
            "PolicyName": config['Name'],
            "PolicyType": 5,
            "ResourceId": 'BandwidthPackage',
            "NotificationId": config['NotificationId'],
            "ScaleMax": 0,
            "ScaleMin": 0,
            "BootupConfig": r_b["ConfigId"],
            "EIPID": config['EIPID'],
            "Action": 'CreateASPolicy'
            }
    r_p = requestToAPI(args.publicKey, args.privateKey, args.projectId, params_p)
    r_p = json.loads(r_p)
    # print(json.dumps(r_p, indent=4))

    if r_p['RetCode'] != 0 :
        return

    params = {
            "Region": args.region,
            "Name": config['Name'],
            "Period": config['Period'],
            "NotificationId": config['NotificationId'],
            "StartTime": config["StartTime"],
            "EndTime": config["EndTime"],
            "TimerType": "BANDWIDTH_PACKAGE",
            "TimerActionURL": 'uas_scanner',
            "TimerActionPath": r_p["PolicyId"],
            "Action": 'CreateASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyBandwidthPackageTimer(args):
    params = {
        "Region": args.region,
        "TaskId": args.id,
        "TimerType": "BANDWIDTH_PACKAGE",
        "Action": 'ModifyASTimer'
        }
    if args.name:
        params["Name"] = args.name
    if args.period:
        params["Period"] = args.period
    if args.notification_id:
        params["NotificationId"] = args.notification_id
    if args.start_time:
        params["StartTime"] = args.start_time
    if args.end_time:
        params["EndTime"] = args.end_time
    if args.policy_id:
        params["TimerActionURL"] = 'uas_scanner'
        params["TimerActionPath"] = args.policy_id
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def createInstanceGroupTimer(args):
    with open(args.config, 'r') as f:
        config = json.load(f)
    params = {
            "Region": args.region,
            "Name": config["Name"],
            "Period": config["Period"],
            "StartTime": config["StartTime"],
            "EndTime": config["EndTime"],
            "NotificationId": config["NotificationId"],
            "TimerType": "INSTANCE_GROUP",
            "TimerActionURL": 'uas_scanner',
            "TimerActionPath": config["GroupId"] + '?max=' + str(config["ScaleMax"]) + '&min=' + str(config["ScaleMin"]),
            "Action": 'CreateASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyInstanceGroupTimer(args):
    with open(args.config, 'r') as f:
        config = json.load(f)
    params = {
            "Region": args.region,
            "TaskId": args.id,
            "Name": config["Name"],
            "Period": config["Period"],
            "StartTime": config["StartTime"],
            "EndTime": config["EndTime"],
            "NotificationId": config["NotificationId"],
            "TimerType": "INSTANCE_GROUP",
            "TimerActionURL": 'uas_scanner',
            "TimerActionPath": config["GroupId"] + '?max=' + str(config["ScaleMax"]) + '&min=' + str(config["ScaleMin"]),
            "Action": 'ModifyASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, args.projectId, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

### rule
def runAddRule(subparsers):
    parser = subparsers.add_parser('add-rule', help='moify instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('group_id', help='the group id to modify')
    parser.add_argument('name', help='Name of the rule')
    parser.add_argument('scale_step', help='scale step')
    parser.add_argument('scale_diretion', help='scale direction, ADD or MINUS')
    parser.add_argument('metric_type', help='metric type, 101 : CPU CPUUtilization / 102 : NetPacketIn')
    parser.add_argument('condition_type', help='condition type, LT or GT')
    parser.add_argument('consecutiveperiods', help='consecutive periods means , range 1-10')
    parser.add_argument('thresholds', help='thresholds, e.g. 90 means 90% of cpu')
    parser.set_defaults(func=createRule)

def runGetRuleList(subparsers):
    parser = subparsers.add_parser('list-rule', help='moify instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('group_id', help='the group id to modify')
    parser.set_defaults(func=listRule)

def runDelRule(subparsers):
    parser = subparsers.add_parser('del-rule', help='moify instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('group_id', help='the group id to modify')
    parser.add_argument('rule_id', help='the rule id to modify')
    parser.set_defaults(func=delRule)

def runModifyRule(subparsers):
    parser = subparsers.add_parser('modify-rule', help='moify instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('group_id', help='the group id to modify')
    parser.add_argument('rule_id', help='the rule id to modify')
    parser.add_argument('name', help='Name of the rule')
    parser.add_argument('scale_step', help='scale step')
    parser.add_argument('scale_diretion', help='scale direction, ADD or MINUS')
    parser.add_argument('metric_type', help='metric type, 101 : CPU / 102 : NetPacketIn')
    parser.add_argument('condition_type', help='condition type, LT or GT')
    parser.add_argument('consecutiveperiods', help='consecutive periods means , range 1-10')
    parser.add_argument('thresholds', help='thresholds, e.g. 90 means 90% of cpu')
    parser.set_defaults(func=modifyRule)


### instance group
def runModifyInstanceGroup(subparsers):
    parser = subparsers.add_parser('modify', help='moify instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('group_id', help='the group id to modify')
    parser.add_argument('--name', help='Name of the group')
    parser.add_argument('--notification_id', help='Notification id')
    parser.add_argument('--scale_max', help='Max of scale')
    parser.add_argument('--scale_min', help='Min of scale')
    parser.add_argument('--bootup_config', help='The id of bootup config')
    parser.add_argument('--remove_policy', help='first or last')
    parser.add_argument('--eip', help='is bind eip YES or NO')
    parser.set_defaults(func=modifyInstanceGroup)

def runCreateInstanceGroup(subparsers):
    parser = subparsers.add_parser('create', help='create instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('name', help='Name of the group')
    parser.add_argument('notification_id', help='Notification id')
    parser.add_argument('scale_max', help='Max of scale')
    parser.add_argument('scale_min', help='Min of scale')
    parser.add_argument('bootup_config', help='The id of bootup config')
    parser.add_argument('remove_policy', help='first or last')
    parser.add_argument('desired_amount', help='The desired amount')
    parser.add_argument('-u', '--ulb', help='uld id')
    parser.add_argument('--vserver', nargs='+', help='config of vserver, e.g. vserver-quklv4:9000')
    parser.add_argument('--eip', help='is bind eip YES or NO')
    parser.set_defaults(func=createInstanceGroup)

def runGetInstanceGroup(subparsers):
    parser = subparsers.add_parser('get', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.set_defaults(func=getInstanceGroup)

def runGetInstanceGroupList(subparsers):
    parser = subparsers.add_parser('list', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.set_defaults(func=getInstanceGroupList)

def runDeleteInstanceGroup(subparsers):
    parser = subparsers.add_parser('delete', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('--isKeepInstances', help='is keep instances YES or NO')
    parser.set_defaults(func=delInstanceGroup)

def runAddVServer(subparsers):
    parser = subparsers.add_parser('add-vserver', help='add a vserver to instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('groupId', help='instance group id')
    parser.add_argument('ulbId', help='ULB ID')
    parser.add_argument('vserverConfig', help='vserver config VServerId:Port')
    parser.set_defaults(func=addVServer)

def runDeleteVServer(subparsers):
    parser = subparsers.add_parser('delete-vserver', help='delete a vserver to instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('groupId', help='instance group id')
    parser.add_argument('ulbId', help='ULB ID')
    parser.add_argument('vserverConfig', help='vserver config VServerId:Port')
    parser.set_defaults(func=deleteVServer)


### instance
def runAddInstanceToGroup(subparsers):
    parser = subparsers.add_parser('add-instance', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.add_argument('isLock', help='lock state YES or NO')
    parser.set_defaults(func=addInstanceToGroup)

def runRemoveInstanceFropGroup(subparsers):
    parser = subparsers.add_parser('remove-instance', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.set_defaults(func=removeInstanceFromGroup)

def runUpdateInstanceLockState(subparsers):
    parser = subparsers.add_parser('update-instance-lock-state', help='update instance lock state')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.add_argument('state', help='lock state YES or NO')
    parser.set_defaults(func=updateInstanceLockState)

def runCreateTimerPolicy(subparsers):
    parser = subparsers.add_parser('create-timer-policy', help='create a timer task policy')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('name', help='Name of the policy')
    parser.add_argument('notification_id', help='Notification id')
    parser.add_argument('bootup_config', help='The eip id for bandwidth package')
    parser.add_argument('eip_id', help='The eip id for bandwidth package')
    parser.set_defaults(func=createTimerPolicy)

def runModifyTimerPolicy(subparsers):
    parser = subparsers.add_parser('modify-timer-policy', help='modify a timer task policy')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('id', help='ID of the policy')
    parser.add_argument('bootup_config', help='The bootup_config id for bandwidth package')
    parser.add_argument('eip_id', help='The eip id for bandwidth package')
    parser.set_defaults(func=modifyTimerPolicy)

def runCreateBootupConfigBandwidthPackage(subparsers):
    parser = subparsers.add_parser('create-bootup-config-bandwidth-package', help='create a bootup config for bandwidth package')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('name', help='Name of the bootup config')
    parser.add_argument('bandwidth', help='bandwidth of bandwidth package M')
    parser.add_argument('time_range', help='time range of bandwidth package Hour')
    parser.set_defaults(func=createBootupConfigBandwidthPackage)

def runModifyBootupConfigBandwidthPackage(subparsers):
    parser = subparsers.add_parser('modify-bootup-config-bandwidth-package', help='create a bootup config for bandwidth package')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('id', help='BandwidthPackage BootupConfig id')
    parser.add_argument('--name', help='Name of the bootup config')
    parser.add_argument('--bandwidth', help='bandwidth of bandwidth package M')
    parser.add_argument('--time_range', help='time range of bandwidth package Hour')
    parser.set_defaults(func=modifyBootupConfigBandwidthPackage)

def runGetTimer(subparsers):
    parser = subparsers.add_parser('get-timer', help='create a timer')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('id', help='id for timer')
    parser.set_defaults(func=getTimer)

def runListTimer(subparsers):
    parser = subparsers.add_parser('list-timer', help='create a timer')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.set_defaults(func=listTimer)

def runUpdateTimerStatus(subparsers):
    parser = subparsers.add_parser('update-timer-status', help='create a timer with config')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('id', help='id for timer')
    parser.add_argument('status', help='status for timer, ON or OFF')
    parser.set_defaults(func=updateTimerStatus)

def runCreateBandwidthPackageTimer(subparsers):
    parser = subparsers.add_parser('create-bw-timer', help='create a timer with config')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('config', help='config dir for timer')
    parser.set_defaults(func=createBandwidthPackageTimer)

def runModifyBandwidthPackageTimer(subparsers):
    parser = subparsers.add_parser('modify-bw-timer', help='modify a bandwidth package timer')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('id', help='id for timer')
    parser.add_argument('--name', help='Name of the timer')
    parser.add_argument('--start_time', help='start time for timer')
    parser.add_argument('--end_time', help='end time for timer')
    parser.add_argument('--period', help='period for timer')
    parser.add_argument('--policy_id', help='policy id for timer')
    parser.add_argument('--notification_id', help='Notification id')
    parser.set_defaults(func=modifyBandwidthPackageTimer)

def runCreateInstanceGroupTimer(subparsers):
    parser = subparsers.add_parser('create-ig-timer', help='create a instance group timer with config')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('config', help='config dir for timer')
    parser.set_defaults(func=createInstanceGroupTimer)

def runModifyInstanceGroupTimer(subparsers):
    parser = subparsers.add_parser('modify-ig-timer', help='modify a instance group timer with config')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('projectId', help='project id')
    parser.add_argument('region', help='Region of the policy')
    parser.add_argument('id', help='id for timer')
    parser.add_argument('config', help='config dir for timer')
    parser.set_defaults(func=modifyInstanceGroupTimer)

def main():
    parser = argparse.ArgumentParser(description="client for managing the CodePush Server")
    subparsers = parser.add_subparsers(help='subcommand')
    runCreateInstanceGroup(subparsers)
    runGetInstanceGroup(subparsers)
    runGetInstanceGroupList(subparsers)
    runModifyInstanceGroup(subparsers)
    runDeleteInstanceGroup(subparsers)
    runAddRule(subparsers)
    runModifyRule(subparsers)
    runGetRuleList(subparsers)
    runDelRule(subparsers)
    runAddInstanceToGroup(subparsers)
    runRemoveInstanceFropGroup(subparsers)
    runUpdateInstanceLockState(subparsers)
    runAddVServer(subparsers)
    runDeleteVServer(subparsers)
    runCreateTimerPolicy(subparsers)
    runCreateBootupConfigBandwidthPackage(subparsers)
    runModifyBootupConfigBandwidthPackage(subparsers)
    runModifyTimerPolicy(subparsers)
    runGetTimer(subparsers)
    runListTimer(subparsers)
    runUpdateTimerStatus(subparsers)
    runCreateBandwidthPackageTimer(subparsers)
    runModifyBandwidthPackageTimer(subparsers)
    runCreateInstanceGroupTimer(subparsers)
    runModifyInstanceGroupTimer(subparsers)
    args = parser.parse_args()
    args.func(args)

__all__ = ['main']
