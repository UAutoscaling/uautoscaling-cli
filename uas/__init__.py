import os, sys, json, time
BASE = os.path.join(os.path.dirname(os.path.join(__file__)), '..', 'libs')
sys.path.append(BASE)
import argparse
from api import requestToAPI

def formatTime(ts):
    arr = time.localtime(ts)
    return time.strftime("%Y-%m-%d %H:%M:%S", arr)

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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def listRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "Action": 'GetASPolicyRules'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def delRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "RuleId": args.rule_id,
            "Action": 'DeleteASPolicyRule'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def getInstanceGroupList(args):
    params = {
            "Region": args.region,
            "Action": 'GetASInstanceGroupList'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def getInstanceGroup(args):
    params = {
            "GroupId": args.groupId,
            "Region": args.region,
            "Action": 'GetASInstanceGroupDetail'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyInstanceGroup(args):
    params = {
            "Region": args.region,
            "GroupId": args.group_id,
            "GroupName": args.name,
            "NotificationId": args.notification_id,
            "ScaleMax": args.scale_max,
            "ScaleMin": args.scale_min,
            "BootupConfig": args.bootup_config,
            "RemovePolicy": args.remove_policy,
            "IsBindEIP": args.eip,
            "Action": 'ModifyASInstanceGroup'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def delInstanceGroup(args):
    params = {
            "GroupId": args.groupId,
            "Region": args.region,
            "Action": 'DeleteASInstanceGroup'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def removeInstanceFromGroup(args):
    params = {
            "InstanceId": args.instanceId,
            "GroupId": args.groupId,
            "Region": args.region,
            "Action": 'RemoveInstanceFromGroup'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def createTimer(args):
    params = {
            "Region": args.region,
            "Name": args.name,
            "Period": args.period,
            "NotificationId": args.notification_id,
            "StartTime": args.start_time,
            "EndTime": args.end_time,
            "TimerActionURL": 'uas_scanner',
            "TimerActionPath": args.policy_id,
            "Action": 'CreateASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def getTimer(args):
    params = {
            "Region": args.region,
            "TaskId": args.id,
            "Action": 'GetASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def listTimer(args):
    params = {
            "Region": args.region,
            "Action": 'GetASTimerList'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def modifyTimer(args):
    params = {
            "Region": args.region,
            "TaskId": args.id,
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
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
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def newTimer(args):
    with open(args.config, 'r') as f:
        config = json.load(f)

    params_b = {
            "Region": args.region,
            "Name": config['Name'],
            "Bandwidth": config['Bandwidth'],
            "TimeRange": config['TimeRange'],
            "Action": 'CreateASBootupConfigBandwidthPackage'
            }
    r_b = requestToAPI(args.publicKey, args.privateKey, params_b)
    r_b = json.loads(r_b)
    print(json.dumps(r_b, indent=4))

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
    r_p = requestToAPI(args.publicKey, args.privateKey, params_p)
    r_p = json.loads(r_p)
    print(json.dumps(r_p, indent=4))

    if r_p['RetCode'] != 0 :
        return

    params = {
            "Region": args.region,
            "Name": config['Name'],
            "Period": config['Period'],
            "NotificationId": config['NotificationId'],
            "StartTime": config['StartTime'],
            "EndTime": config['EndTime'],
            "TimerActionURL": 'uas_scanner',
            "TimerActionPath": r_p["PolicyId"],
            "Action": 'CreateASTimer'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def getTimerDetail(args):

    result = {}

    params_b = {
            "Region": args.region,
            "TaskId": args.id,
            "Action": 'GetASTimer'
            }
    r_b = requestToAPI(args.publicKey, args.privateKey, params_b)
    r_b = json.loads(r_b)
    print(json.dumps(r_b, indent=4))

    if r_b['RetCode'] != 0 :
        return

    result['Name'] = r_b['Name']
    result['Status'] = r_b['Status']
    result['Period'] = r_b['Period']
    result['StartTime'] = formatTime(r_b['StartTime'])
    result['EndTime'] = formatTime(r_b['EndTime'])
    result['NotificationId'] = r_b['NotificationId']

    params_p = {
            "Region": args.region,
            "PolicyId": r_b['TimerActionPath'],
            "Action": 'GetASPolicyDetail'
            }
    r_p = requestToAPI(args.publicKey, args.privateKey, params_p)
    r_p = json.loads(r_p)
    print(json.dumps(r_p, indent=4))

    if r_p['RetCode'] != 0 :
        return

    result['EIPID'] = r_p['EIPID']

    params = {
            "Region": args.region,
            "ConfigId": r_p['BootupConfig'],
            "Action": 'GetASBootupConfigBandwidthPackage'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

    result['Bandwidth'] = r['Bandwidth']
    result['TimeRange'] = r['TimeRange']

    print(json.dumps(result, indent=4))


### rule
def runAddRule(subparsers):
    createParser = subparsers.add_parser('add-rule', help='moify instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('group_id', help='the group id to modify')
    createParser.add_argument('name', help='Name of the rule')
    createParser.add_argument('scale_step', help='scale step')
    createParser.add_argument('scale_diretion', help='scale direction, ADD or MINUS')
    createParser.add_argument('metric_type', help='metric type, 101 : CPU CPUUtilization / 102 : NetPacketIn')
    createParser.add_argument('condition_type', help='condition type, LT or GT')
    createParser.add_argument('consecutiveperiods', help='consecutive periods means , range 1-10')
    createParser.add_argument('thresholds', help='thresholds, e.g. 90 means 90% of cpu')
    createParser.set_defaults(func=createRule)

def runGetRuleList(subparsers):
    createParser = subparsers.add_parser('list-rule', help='moify instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('group_id', help='the group id to modify')
    createParser.set_defaults(func=listRule)

def runDelRule(subparsers):
    createParser = subparsers.add_parser('del-rule', help='moify instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('group_id', help='the group id to modify')
    createParser.add_argument('rule_id', help='the rule id to modify')
    createParser.set_defaults(func=delRule)

def runModifyRule(subparsers):
    createParser = subparsers.add_parser('modify-rule', help='moify instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('group_id', help='the group id to modify')
    createParser.add_argument('rule_id', help='the rule id to modify')
    createParser.add_argument('name', help='Name of the rule')
    createParser.add_argument('scale_step', help='scale step')
    createParser.add_argument('scale_diretion', help='scale direction, ADD or MINUS')
    createParser.add_argument('metric_type', help='metric type, 101 : CPU / 102 : NetPacketIn')
    createParser.add_argument('condition_type', help='condition type, LT or GT')
    createParser.add_argument('consecutiveperiods', help='consecutive periods means , range 1-10')
    createParser.add_argument('thresholds', help='thresholds, e.g. 90 means 90% of cpu')
    createParser.set_defaults(func=modifyRule)


### instance group
def runModifyInstanceGroup(subparsers):
    createParser = subparsers.add_parser('modify', help='moify instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('group_id', help='the group id to modify')
    createParser.add_argument('name', help='Name of the group')
    createParser.add_argument('notification_id', help='Notification id')
    createParser.add_argument('scale_max', help='Max of scale')
    createParser.add_argument('scale_min', help='Min of scale')
    createParser.add_argument('bootup_config', help='The id of bootup config')
    createParser.add_argument('remove_policy', help='first or last')
    createParser.add_argument('--eip', help='is bind eip YES or NO')
    createParser.set_defaults(func=modifyInstanceGroup)

def runCreateInstanceGroup(subparsers):
    createParser = subparsers.add_parser('create', help='create instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('name', help='Name of the group')
    createParser.add_argument('notification_id', help='Notification id')
    createParser.add_argument('scale_max', help='Max of scale')
    createParser.add_argument('scale_min', help='Min of scale')
    createParser.add_argument('bootup_config', help='The id of bootup config')
    createParser.add_argument('remove_policy', help='first or last')
    createParser.add_argument('desired_amount', help='The desired amount')
    createParser.add_argument('-u', '--ulb', help='uld id')
    createParser.add_argument('--vserver', nargs='+', help='config of vserver, e.g. vserver-quklv4:9000')
    createParser.add_argument('--eip', help='is bind eip YES or NO')
    createParser.set_defaults(func=createInstanceGroup)

def runGetInstanceGroup(subparsers):
    parser = subparsers.add_parser('get', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.set_defaults(func=getInstanceGroup)

def runGetInstanceGroupList(subparsers):
    parser = subparsers.add_parser('list', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.set_defaults(func=getInstanceGroupList)

def runDeleteInstanceGroup(subparsers):
    parser = subparsers.add_parser('delete', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.set_defaults(func=delInstanceGroup)

def runAddVServer(subparsers):
    createParser = subparsers.add_parser('add-vserver', help='add a vserver to instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('groupId', help='instance group id')
    createParser.add_argument('ulbId', help='ULB ID')
    createParser.add_argument('vserverConfig', help='vserver config VServerId:Port')
    createParser.set_defaults(func=addVServer)

def runDeleteVServer(subparsers):
    createParser = subparsers.add_parser('delete-vserver', help='delete a vserver to instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('groupId', help='instance group id')
    createParser.add_argument('ulbId', help='ULB ID')
    createParser.add_argument('vserverConfig', help='vserver config VServerId:Port')
    createParser.set_defaults(func=deleteVServer)


### instance
def runAddInstanceToGroup(subparsers):
    parser = subparsers.add_parser('add-instance', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.add_argument('isLock', help='lock state YES or NO')
    parser.set_defaults(func=addInstanceToGroup)

def runRemoveInstanceFropGroup(subparsers):
    parser = subparsers.add_parser('remove-instance', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.set_defaults(func=removeInstanceFromGroup)

def runUpdateInstanceLockState(subparsers):
    parser = subparsers.add_parser('update-instance-lock-state', help='update instance lock state')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.add_argument('state', help='lock state YES or NO')
    parser.set_defaults(func=updateInstanceLockState)

def runCreateTimerPolicy(subparsers):
    createParser = subparsers.add_parser('create-timer-policy', help='create a timer task policy')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('name', help='Name of the policy')
    createParser.add_argument('notification_id', help='Notification id')
    createParser.add_argument('bootup_config', help='The eip id for bandwidth package')
    createParser.add_argument('eip_id', help='The eip id for bandwidth package')
    createParser.set_defaults(func=createTimerPolicy)

def runModifyTimerPolicy(subparsers):
    createParser = subparsers.add_parser('modify-timer-policy', help='modify a timer task policy')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='ID of the policy')
    createParser.add_argument('bootup_config', help='The bootup_config id for bandwidth package')
    createParser.add_argument('eip_id', help='The eip id for bandwidth package')
    createParser.set_defaults(func=modifyTimerPolicy)

def runCreateBootupConfigBandwidthPackage(subparsers):
    createParser = subparsers.add_parser('create-bootup-config-bandwidth-package', help='create a bootup config for bandwidth package')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('name', help='Name of the bootup config')
    createParser.add_argument('bandwidth', help='bandwidth of bandwidth package M')
    createParser.add_argument('time_range', help='time range of bandwidth package Hour')
    createParser.set_defaults(func=createBootupConfigBandwidthPackage)

def runModifyBootupConfigBandwidthPackage(subparsers):
    createParser = subparsers.add_parser('modify-bootup-config-bandwidth-package', help='create a bootup config for bandwidth package')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='BandwidthPackage BootupConfig id')
    createParser.add_argument('--name', help='Name of the bootup config')
    createParser.add_argument('--bandwidth', help='bandwidth of bandwidth package M')
    createParser.add_argument('--time_range', help='time range of bandwidth package Hour')
    createParser.set_defaults(func=modifyBootupConfigBandwidthPackage)

def runCreateTimer(subparsers):
    createParser = subparsers.add_parser('create-timer', help='create a timer')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('name', help='Name for name')
    createParser.add_argument('start_time', help='start time for timer')
    createParser.add_argument('end_time', help='end time for timer')
    createParser.add_argument('period', help='period for timer')
    createParser.add_argument('policy_id', help='policy id for timer')
    createParser.add_argument('notification_id', help='Notification id')
    createParser.set_defaults(func=createTimer)

def runGetTimer(subparsers):
    createParser = subparsers.add_parser('get-timer', help='create a timer')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='id for timer')
    createParser.set_defaults(func=getTimer)

def runListTimer(subparsers):
    createParser = subparsers.add_parser('list-timer', help='create a timer')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.set_defaults(func=listTimer)

def runModifyTimer(subparsers):
    createParser = subparsers.add_parser('modify-timer', help='create a timer')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='id for timer')
    createParser.add_argument('--name', help='Name of the timer')
    createParser.add_argument('--start_time', help='start time for timer')
    createParser.add_argument('--end_time', help='end time for timer')
    createParser.add_argument('--period', help='period for timer')
    createParser.add_argument('--policy_id', help='policy id for timer')
    createParser.add_argument('--notification_id', help='Notification id')
    createParser.set_defaults(func=modifyTimer)

def runUpdateTimerStatus(subparsers):
    createParser = subparsers.add_parser('update-timer-status', help='create a timer with config')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='id for timer')
    createParser.add_argument('status', help='status for timer, ON or OFF')
    createParser.set_defaults(func=updateTimerStatus)

def runNewTimer(subparsers):
    createParser = subparsers.add_parser('new-timer', help='create a timer with config')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('config', help='config dir for timer')
    createParser.set_defaults(func=newTimer)

def runGetTimerDetail(subparsers):
    createParser = subparsers.add_parser('get-timer-detail', help='create a timer with config')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='id for timer')
    createParser.set_defaults(func=getTimerDetail)

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
    runCreateTimer(subparsers)
    runGetTimer(subparsers)
    runListTimer(subparsers)
    runModifyTimer(subparsers)
    runUpdateTimerStatus(subparsers)
    runNewTimer(subparsers)
    runGetTimerDetail(subparsers)
    args = parser.parse_args()
    args.func(args)

__all__ = ['main']
