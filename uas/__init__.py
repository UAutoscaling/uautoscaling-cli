import os, sys, json
BASE = os.path.join(os.path.dirname(os.path.join(__file__)), '..', 'libs')
sys.path.append(BASE)
import argparse
from api import requestToAPI

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

def listInstanceGroup(args):
    params = {
            "Region": args.region,
            "Action": 'GetASPolicyList'
            }
    r = requestToAPI(args.publicKey, args.privateKey, params)
    r = json.loads(r)
    print(json.dumps(r, indent=4))

def createRule(args):
    params = {
            "Region": args.region,
            "PolicyId": args.group_id,
            "RuleName": args.name,
            "ScaleDirection": args.scale_diretion,
            "ScaleStep": args.scale_step,
            "CooldownTime": 300,
            "CheckPeriod": 1,
            "MetricType": 101,
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
            "MetricType": 101,
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
            "IsBindEIP": args.eip,
            "Action": 'CreateASInstanceGroup'
            }
    if args.ulb:
        params['UlbId'] = args.ulb
        for v,i in zip(args.vserver, xrange(0, len(args.vserver))):
            params['VServerConfigs.%d' %i] = v
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

def addInstanceToGroup(args):
    params = {
            "InstanceId": args.instanceId,
            "GroupId": args.groupId,
            "Region": args.region,
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

def modifyTimer(args):
    params = {
            "Region": args.region,
            "Name": args.name,
            "TaskId": args.id,
            "Period": args.period,
            "NotificationId": args.notification_id,
            "StartTime": args.start_time,
            "EndTime": args.end_time,
            "TimerActionURL": 'uas_scanner',
            "TimerActionPath": args.policy_id,
            "Action": 'ModifyASTimer'
            }
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


def runAddRule(subparsers):
    createParser = subparsers.add_parser('add-rule', help='moify instance group')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the group')
    createParser.add_argument('group_id', help='the group id to modify')
    createParser.add_argument('name', help='Name of the rule')
    createParser.add_argument('scale_step', help='scale step')
    createParser.add_argument('scale_diretion', help='scale direction, ADD or MINUS')
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
    createParser.add_argument('condition_type', help='condition type, LT or GT')
    createParser.add_argument('consecutiveperiods', help='consecutive periods means , range 1-10')
    createParser.add_argument('thresholds', help='thresholds, e.g. 90 means 90% of cpu')
    createParser.set_defaults(func=modifyRule)



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
    createParser.add_argument('--eip', help='is bind eip yes or no')
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
    createParser.add_argument('--eip', help='is bind eip yes or no')
    createParser.set_defaults(func=createInstanceGroup)
    
def runGetInstanceGroup(subparsers):
    parser = subparsers.add_parser('get', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.set_defaults(func=getInstanceGroup)

def runGetPolicyList(subparsers):
    parser = subparsers.add_parser('list', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.set_defaults(func=listInstanceGroup)

def runAddInstanceToGroup(subparsers):
    parser = subparsers.add_parser('add-instance', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.set_defaults(func=addInstanceToGroup)

def runRemoveInstanceFropGroup(subparsers):
    parser = subparsers.add_parser('remove-instance', help='get instance group')
    parser.add_argument('publicKey', help='public key')
    parser.add_argument('privateKey', help='private key')
    parser.add_argument('region', help='Region of the group')
    parser.add_argument('groupId', help='group id')
    parser.add_argument('instanceId', help='instance id')
    parser.set_defaults(func=removeInstanceFromGroup)

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

def runModifyTimer(subparsers):
    createParser = subparsers.add_parser('modify-timer', help='create a timer')
    createParser.add_argument('publicKey', help='public key')
    createParser.add_argument('privateKey', help='private key')
    createParser.add_argument('region', help='Region of the policy')
    createParser.add_argument('id', help='id for timer')
    createParser.add_argument('name', help='Name of the timer')
    createParser.add_argument('start_time', help='start time for timer')
    createParser.add_argument('end_time', help='end time for timer')
    createParser.add_argument('period', help='period for timer')
    createParser.add_argument('policy_id', help='policy id for timer')
    createParser.add_argument('notification_id', help='Notification id')
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

def main():
    parser = argparse.ArgumentParser(description="client for managing the CodePush Server")
    subparsers = parser.add_subparsers(help='subcommand')
    runCreateInstanceGroup(subparsers)
    runGetInstanceGroup(subparsers)
    runGetPolicyList(subparsers)
    runModifyInstanceGroup(subparsers)
    runAddRule(subparsers)
    runModifyRule(subparsers)
    runGetRuleList(subparsers)
    runDelRule(subparsers)
    runAddInstanceToGroup(subparsers)
    runRemoveInstanceFropGroup(subparsers)
    runCreateTimerPolicy(subparsers)
    runCreateBootupConfigBandwidthPackage(subparsers)
    runModifyTimerPolicy(subparsers)
    runCreateTimer(subparsers)
    runModifyTimer(subparsers)
    runUpdateTimerStatus(subparsers)
    runNewTimer(subparsers)
    args = parser.parse_args()
    args.func(args)

__all__ = ['main']
