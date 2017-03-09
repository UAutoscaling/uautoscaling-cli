# 依赖
* python 2.7 +

# 使用

通用参数说明：

* PublicKey 账户公钥 [API密钥](https://consolev3.ucloud.cn/apikey)
* PrivateKey 账户私钥 [API密钥](https://consolev3.ucloud.cn/apikey)
* ProjectId 项目ID [项目概况](https://consolev3.ucloud.cn/dashboard)
* Region [区域ID][https://docs.ucloud.cn/api/summary/regionlist]

通用输出说明：

* RetCode 用来表示API请求的返回值 ，当retcode = 0时表示API请求正常， retcode != 0时表示API请求错误。
* Action 指令名称 返回所调用的指令名称。 例如 DescribeUHostInstanceResponse
* Message API返回错误信息

## 创建一个Instance Group

`./autoscaling create $PublicKey $PrivateKey $ProjectId $Region $Name $NotificationId $ScaleMax $ScaleMin $BootupConfig $RemovePolicy $DesiredAmount --eip $IsBindEIP -u $ULB_ID --vserver $VServerConfig $VServerConfig ...`

参数说明：

* Name Group的名称
* NotificationId 通知组ID
* ScaleMax 伸缩组的最大值
* ScaleMin 伸缩组最小值
* BootupConfig 启动配置ID（到启动配置那一页下参看)
* RemovePolicy 移出策略 （FIRST | LAST)
* DesiredAmount 期望实例数
* IsBindEIP 实例是否绑定EIP (YES | NO). optional, default NO
* ULB_ID ULB的ID
* VServerConfig VServer配置 "$VServerID:$Port" 例如 vserver-quklv4:9000

例如：`./autoscaling create 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 test_multiple_vserver 60092 2 2 uabc-nylrb4 LAST 2 --eip 'YES' -u ulb-w0x3bn --vserver 'vserver-quklv4:9000' 'vserver-eraha3:8000'`

## 获取Instance Group List

`./autoscaling list $PublicKey $PrivateKey $ProjectId $Region`

例如：`./autoscaling list 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2` 

## 修改一个Instance Group

`./autoscaling modify $PublicKey $PrivateKey $ProjectId $Region $GroupId --name $Name --notification_id $NotificationId --scale_max $ScaleMax --scale_min $ScaleMin --bootup_config $BootupConfig --remove_policy $RemovePolicy --eip $IsBindEIP`

参数说明：

* GroupId Instance Group ID
* Name Group的名称
* NotificationId 通知组ID
* ScaleMax 伸缩组的最大值
* ScaleMin 伸缩组最小值
* BootupConfig 启动配置ID（到启动配置那一页下参看)
* RemovePolicy 移出策略 （FIRST | LAST)
* IsBindEIP 实例是否绑定EIP (YES | NO). optional, default NO

例如：`./autoscaling modify 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-f0ogue --name test_multiple_vserver --notification_id 60092 --scale_max 2 --scale_min 2 --bootup_config uabc-nylrb4 --remove_policy LAST --eip YES`


## 获取一个Instance Group

`./autoscaling get  $PublicKey $PrivateKey $ProjectId $Region $GroupId`

参数说明：

* GroupId 查找的GroupId

例如：`./autoscaling get 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku`


## 删除一个Instance Group

`./autoscaling delete $PublicKey $PrivateKey $ProjectId $Region $GroupId --isKeepInstances $isKeepInstances`

参数说明：

* GroupId 查找的GroupId
* isKeepInstances 是否保留实例 YES | NO

例如：`./autoscaling delete 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku --isKeepInstances=NO`


## 增加伸缩策略

`./autoscaling add-rule $PublicKey $PrivateKey $ProjectId $Region $GroupId $Name $ScaleStep $ScaleDirection $MetricType $ConditionType $ConsecutivePeriods $Thresholds`

参数说明：

* GroupId 查找的GroupId
* Name 策略名称
* ScaleStep 伸缩步长 例如1就是增加或者删除1台机器
* ScaleDirection 伸缩方向 (ADD|MINUS)
* MetricType 监控类型 101 : CPU CPU使用率 / 102 : NetPacketIn 网卡入包量
* ConditionType 条件类型 (LT 小于, GT 大于)
* ConsecutivePeriods 连续周期 (连续几个周期)
* Thresholds 阈值

说明:
监控都是1分钟为一个监控点，假如 ConsecutivePeriods 为 5， Thresholds 为 60， ConditionType 为 GT，表示 5个周期的监控指标超过60%

例如：`./autoscaling add-rule 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku test-rule 1 ADD 101 LT 1 20`

## 修改伸缩策略

`./autoscaling modify-rule $PublicKey $PrivateKey $ProjectId $Region $GroupId $RuleId $Name $ScaleStep $ScaleDirection $ConditionType $ConsecutivePeriods $Thresholds`

参数说明：

* RuleId 修改的Rule的ID

其它参数同 add-rule

说明:
监控都是1分钟为一个监控点，假如 ConsecutivePeriods 为 5， Thresholds 为 60， ConditionType 为 GT，表示 5个周期的监控指标超过60%

例如：`./autoscaling modify-rule 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku uapr-355y11 test-rule  1 ADD 101 LT 1 20`


## 获取伸缩策略列表

`./autoscaling list-rule $PublicKey $PrivateKey $ProjectId $Region $GroupId`

参数说明：

* GroupId 对应的Instance Group ID

例如：`./autoscaling list-rule 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku`

## 删除策略

`./autoscaling del-rule $PublicKey $PrivateKey $ProjectId $Region $GroupId $RuleId`

参数说明：

* GroupId 对应的Instance Group ID
* RuleId 对应的策略ID

例如：`./autoscaling del-rule 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku uapr-355y11`


## 为伸缩组增加一个实例

`./autoscaling add-instance $PublicKey $PrivateKey $ProjectId $Region $GroupId $InstanceId $IsLock`

参数说明：

* GroupId 对应的Instance Group ID
* InstanceId 要增加的uhost ID
* IsLock 实例是否锁定 YES or NO

例如：`./autoscaling add-instance 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku uhost-ubc51v YES`


## 从伸缩组删除一个实例

`./autoscaling remove-instance $PublicKey $PrivateKey $ProjectId $Region $GroupId $InstanceId`

参数说明：

* GroupId 对应的Instance Group ID
* InstanceId 要删除的uhost ID

例如：`./autoscaling remove-instance 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku uhost-ubc51v`

## 更新实例锁定状态

`./autoscaling update-instance-lock-state $PublicKey $PrivateKey $ProjectId $Region $GroupId $InstanceId $State`

参数说明：

* GroupId 对应的Instance Group ID
* InstanceId 要删除的uhost ID
* State 实例是否锁定 YES or NO

例如：`./autoscaling update-instance-lock-state 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku uhost-ubc51v YES`

## 向伸缩组添加一个VServer

`./autoscaling add-vserver 'PublicKey' 'PrivateKey' 'ProjectId' $Region $GroupId $ULBId $VServerConfig`

参数说明

* GroupId 伸缩组ID
* ULBId ULBId
* VServerConfig VServer信息(ID-端口)例如： vserver-sdfsd:80

例如：`./autoscaling add-vserver 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku ulb-ubc51v vserver-sdfsd:80`

## 从伸缩组删除一个VServer（该vserver资源也会被删除！）

`./autoscaling delete-vserver 'PublicKey' 'PrivateKey' 'ProjectId' $Region $GroupId $ULBId $VServerConfig`

参数说明

* GroupId 伸缩组ID
* ULBId ULBId
* VServerConfig VServer信息(ID-端口)例如： vserver-sdfsd:80

例如：`./autoscaling delete-vserver 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 uap-eg2dku ulb-ubc51v vserver-sdfsd:80`


## 创建一个 带宽包 启动配置

`./autoscaling create-bootup-config-bandwidth-package $PublicKey $PrivateKey $ProjectId $Region $Name $Bandwidth $TimeRange`

参数说明：

* Name 带宽包 启动配置 Name
* Bandwidth 带宽大小 单位：M 最小2M
* TimeRange 有效时长 单位：小时

例如：`./autoscaling create-bootup-config-bandwidth-package 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 sxy-btpcfgbwp-test 2 1`

## 修改一个 带宽包 启动配置

`./autoscaling modify-bootup-config-bandwidth-package $PublicKey $PrivateKey $ProjectId $Region $ID --name=$Name --bandwidth=$Bandwidth --time_range=$TimeRange`

参数说明：

* ID 带宽包 启动配置 ID
* Name 带宽包 启动配置 Name
* Bandwidth 带宽大小 单位：M 最小2M
* TimeRange 有效时长 单位：小时

例如：`./autoscaling modify-bootup-config-bandwidth-package 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 sxy-btpcfgbwp-test --bandwidth=4`


## 创建一个 timer policy

`./autoscaling create-timer-policy $PublicKey $PrivateKey $ProjectId $Region $Name $NotificationId $BootupConfig $EIPID`

参数说明：

* Name Policy Name
* NotificationId 通知组 ID
* BootupConfig 对应的启动配置 ID
* EIP_ID 要操作的EIP ID 

例如：`./autoscaling create-timer-policy 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 sxy-timer-policy-test 97526 uabc-bwpkg-dplzle eip-f24m2a`


## 获取所有 循环定时任务 列表

`./autoscaling list-timer $PublicKey $PrivateKey $ProjectId $Region`

例如：`./autoscaling list-timer 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2`

返回示例：
```
{
    "Action": "GetASTimerListResponse",
    "TotalCount": 2, //计数
    "RetCode": 0, //调用成功 
    "DataSet": [ //列表
        {
            "Status": "Normal", 
            "Name": "sxy-timer-test", 
            "TimerType": "BANDWIDTH_PACKAGE", 
            "Period": "2", 
            "StartTime": 1489054440, //开始时间 时间戳 秒
            "EndTime": 1489056600, //结束时间 时间戳 秒
            "TaskId": "utimer-klr5kb"
        }, 
        {
            "Status": "Disabled", 
            "Name": "instance-group-timer-test", 
            "TimerType": "INSTANCE_GROUP", 
            "Period": "1", 
            "StartTime": 1489054440, //开始时间 时间戳 秒
            "EndTime": 1489056600, //结束时间 时间戳 秒 
            "TaskId": "utimer-uijnuz"
        }
    ]
}

```

## 开启/关闭 循环定时任务

`./autoscaling update-timer-status $PublicKey $PrivateKey $ProjectId $Region $ID $Status`

参数说明：

* ID 循环定时任务ID
* Status 开关状态 开启：'ON' 、 关闭：'OFF'

例如：`./autoscaling update-timer-status 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 sxy-timer-test OFF`

## 通过配置文件 新建 带宽包循环定时任务

`./autoscaling create-bw-timer $PublicKey $PrivateKey $ProjectId $Region $Config`

参数说明：

* Config 配置文件

```
{
  "Name": "sxy-timer-test",//名称
  "Period": 1,//循环周期 单位 天
  "StartTime": 1489054440, //开始时间 时间戳 秒
  "EndTime": 1489056600, //结束时间 时间戳 秒
  "NotificationId": 97526,//通知组id
  "Bandwidth": 2, //带宽包带宽大小 单位：M 最小2M
  "TimeRange": 1, //带宽包有效时长 单位：小时
  "EIPID": "eip-f24m2a"//要绑定的EIPID
}
```

例如：`./autoscaling create-bw-timer 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 ./uas/config/timer.json`

## 修改 带宽包 循环定时任务
	 
`./autoscaling modify-bw-timer $PublicKey $PrivateKey $ProjectId $Region $ID --name=$Name --start_time=$StartTime --end_time=$EndTime --period=$Period --policy_id=$PolicyId --notification_id=$NotificationId`
	 
参数说明：

* ID 循环定时任务ID
* Name 循环定时任务 Name
* StartTime 开始时间 精确到秒 格式为"%Y-%m-%d %H:%M:%S"
* EndTime 结束时间 精确到秒 格式为"%Y-%m-%d %H:%M:%S"
* Period 循环周期 单位 天
* PolicyId 对应的Policy ID 
* NotificationId 通知组 ID
	 
例如：`./autoscaling modify-bw-timer 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 sxy-timer-test --period=2`

## 通过配置文件 新建 伸缩组循环定时任务

`./autoscaling create-ig-timer $PublicKey $PrivateKey $ProjectId $Region $Config`

提示：需要先在官网控制台新建一个伸缩组 拿到伸缩组id 填充到GroupId处

参数说明：

* Config 配置文件

```
{
  "Name": "instance-group-timer-test", //名称
  "Period": 1, //循环周期 单位 天
  "StartTime": 1489054440, //开始时间 时间戳 秒
  "EndTime": 1489056600, //结束时间 时间戳 秒
  "GroupId": "uap-ydzktf", // 伸缩组ID
  "ScaleMax": 3, //伸缩最大值
  "ScaleMin": 1, //伸缩最小值
  "NotificationId": 97526 //通知组id
}
```

例如：`./autoscaling create-ig-timer 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 ./uas/config/timer.json`


## 通过配置文件 修改 伸缩组循环定时任务

`./autoscaling modify-ig-timer $PublicKey $PrivateKey $ProjectId $Region $ID $Config`

参数说明：

* ID 循环定时任务ID
* Config 配置文件

```
{
  "Name": "instance-group-timer-test", //名称
  "Period": 1, //循环周期 单位 天
  "StartTime": 1489054440, //开始时间 时间戳 秒
  "EndTime": 1489056600, //结束时间 时间戳 秒
  "GroupId": "uap-ydzktf", // 伸缩组ID
  "ScaleMax": 3, //伸缩最大值
  "ScaleMin": 1, //伸缩最小值
  "NotificationId": 97526 //通知组id
}
```

例如：`./autoscaling modify-ig-timer 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 ./uas/config/timer.json`


## 查询循环定时任务详细信息

`./autoscaling get-timer $PublicKey $PrivateKey $ProjectId $Region $ID`

参数说明：

* ID 循环定时任务ID

提示：可使用 list-timer 先获取到所有列表，然后，根据 id 查询 某一个定时任务详细信息

带宽包返回结果示例：

```
{
  "Name": "sxy-timer-test",//名称
  "Status": "Normal",//任务状态 'Normal' | 'Deleted' | 'Expired' | 'Disabled' | 'Unknown'
  "TimerType": "BANDWIDTH_PACKAGE", // 类型为带宽包
  "Period": 1,//循环周期 单位 天
  "StartTime": 1489054440, //开始时间 时间戳 秒
  "EndTime": 1489056600, //结束时间 时间戳 秒
  "NotificationId": 97526,//通知组id
  "Bandwidth": 2, //带宽包带宽大小 单位：M 最小2M
  "TimeRange": 1, //带宽包有效时长 单位：小时
  "EIPID": "eip-f24m2a"//要绑定的EIPID
}
```
伸缩组返回结果示例：

```
{
    "Name": "instance-group-timer-test", //名称
    "Status": "Normal", //任务状态 'Normal' | 'Deleted' | 'Expired' | 'Disabled' | 'Unknown'
    "TimerType": "INSTANCE_GROUP", // 类型为伸缩组
    "Period": "1", //循环周期 单位 天
    "StartTime": 1489054440, //开始时间 时间戳 秒
    "EndTime": 1489056600, //结束时间 时间戳 秒
    "NotificationId": 97526, //通知组id
    "GroupId": "uap-ydzktf", // 伸缩组ID
    "ScaleMin": "1", //伸缩最大值
    "ScaleMax": "3" //伸缩最小值
}
```

例如：`./autoscaling get-timer 'PublicKey' 'PrivateKey' 'ProjectId' cn-bj2 utimer-msdf3h`
