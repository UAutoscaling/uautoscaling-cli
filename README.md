# 依赖
* python 2.7 +

# 使用

通用参数说明:

* PublicKey 账户公钥 （请到UCloud控制台用户中心获取）
* PrivateKey 账户私钥 （请到UCloud控制台用户中心获取）
* Region 大区ID

## 获取Instance Group List

`./autoscaling list $PublicKey $PrivateKey $Region`

例如：
`
./autoscaling list 'PublicKey' 'PrivateKey' cn-bj2
` 

## 创建一个Instance Group

`./autoscaling create $PublicKey $PrivateKey $Region $Name $NotificationId $ScaleMax $ScaleMin $BootupConfig $RemovePolicy $DesiredAmount --eip $IsBindEIP -u $ULB_ID --vserver $VServerConfig $VServerConfig ...`

参数说明:

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

例如

`./autoscaling create 'PublicKey' 'PrivateKey' cn-bj2 test_multiple_vserver 60092 2 2 uabc-nylrb4 LAST 2 --eip 'YES' -u ulb-w0x3bn --vserver 'vserver-quklv4:9000' 'vserver-eraha3:8000'`

## 修改一个Instance Group

`./autoscaling modify $PublicKey $PrivateKey $Region $GroupId $Name $NotificationId $ScaleMax $ScaleMin $BootupConfig $RemovePolicy --eip $IsBindEIP`

参数说明:
* GroupId Instance Group ID
* Name Group的名称
* NotificationId 通知组ID
* ScaleMax 伸缩组的最大值
* ScaleMin 伸缩组最小值
* BootupConfig 启动配置ID（到启动配置那一页下参看)
* RemovePolicy 移出策略 （FIRST | LAST)
* IsBindEIP 实例是否绑定EIP (YES | NO). optional, default NO

例如

`./autoscaling modify 'PublicKey' 'PrivateKey' cn-bj2 uap-f0ogue test_multiple_vserver 60092 2 2 uabc-nylrb4 LAST --eip YES`


## 获取一个Instance Group

`./autoscaling get  $PublicKey $PrivateKey $Region $GroupId`

参数说明:

* GroupId 查找的GroupId

例如:

`./autoscaling get 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku`

## 增加伸缩策略

`./autoscaling add-rule $PublicKey $PrivateKey $Region $GroupId $Name $ScaleStep $ScaleDirection $ConditionType $ConsecutivePeriods $Thresholds`

参数说明:

* GroupId 查找的GroupId
* Name 策略名称
* ScaleStep 伸缩步长 例如1就是增加或者删除1台机器
* ScaleDirection 伸缩方向 (ADD|MINUS)
* ConditionType 条件类型 (LT 小于, GT 大于)
* ConsecutivePeriods 连续周期 (连续几个周期)
* Thresholds 阈值

说明:
监控都是1分钟为一个监控点，假如 ConsecutivePeriods 为 5， Thresholds 为 60， ConditionType 为 GT，表示 5个周期的监控指标超过60%

例如:
`./autoscaling add-rule 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku 'test rule' 1 ADD LT 1 20`

## 修改伸缩策略

`./autoscaling modify-rule $PublicKey $PrivateKey $Region $GroupId $RuleId $Name $ScaleStep $ScaleDirection $ConditionType $ConsecutivePeriods $Thresholds`

参数说明:

* RuleId 修改的Rule的ID

其它参数同 add-rule

说明:
监控都是1分钟为一个监控点，假如 ConsecutivePeriods 为 5， Thresholds 为 60， ConditionType 为 GT，表示 5个周期的监控指标超过60%

例如:
`./autoscaling modify-rule 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku uapr-355y11 'test rule' 1 ADD LT 1 20`


## 获取伸缩策略列表

`./autoscaling list-rule $PublicKey $PrivateKey $Region $GroupId`

参数说明:

* GroupId 对应的Instance Group ID

例如:
`./autoscaling list-rule 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku`

## 删除策略

`./autoscaling del-rule $PublicKey $PrivateKey $Region $GroupId $RuleId`

参数说明:

* GroupId 对应的Instance Group ID
* RuleId 对应的策略ID

`./autoscaling del-rule 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku uapr-355y11`


## 为伸缩组增加一个实例

`./autoscaling add-instance $PublicKey $PrivateKey $Region $GroupId $InstanceId`

参数说明:

* GroupId 对应的Instance Group ID
* InstanceId 要增加的uhost ID

`./autoscaling add-instance 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku uhost-ubc51v`


## 从伸缩组删除一个实例

`./autoscaling remove-instance $PublicKey $PrivateKey $Region $GroupId $InstanceId`

参数说明:

* GroupId 对应的Instance Group ID
* InstanceId 要删除的uhost ID

`./autoscaling remove-instance 'PublicKey' 'PrivateKey' cn-bj2 uap-eg2dku uhost-ubc51v`


## 创建一个 带宽包 启动配置

`./autoscaling create-bootup-config-bandwidth-package $PublicKey $PrivateKey $Region $Name $Bandwidth $TimeRange`

参数说明:

* Name 带宽包 启动配置 Name
* Bandwidth 带宽大小 单位：M 最小2M
* TimeRange 有效时长 单位：小时

`./autoscaling create-bootup-config-bandwidth-package 'PublicKey' 'PrivateKey' cn-bj2 sxy-btpcfgbwp-test 2 1`


## 创建一个 timer policy

`./autoscaling create-timer-policy $PublicKey $PrivateKey $Region $Name $NotificationId $BootupConfig $EIPID`

参数说明:

* Name Policy Name
* NotificationId 通知组 ID
* BootupConfig 对应的启动配置 ID
* EIP_ID 要操作的EIP ID 

`./autoscaling create-timer-policy 'PublicKey' 'PrivateKey' cn-bj2 sxy-timer-policy-test 97526 uabc-bwpkg-dplzle eip-f24m2a`


## 创建一个 循环定时任务

`./autoscaling create-timer $PublicKey $PrivateKey $Region $Name $StartTime $EndTime $Period $PolicyId $NotificationI`

参数说明:

* Name 循环定时任务 Name
* StartTime 开始时间 精确到秒 时间戳
* EndTime 结束时间 精确到秒 时间戳
* Period 循环周期 单位 天
* PolicyId 对应的Policy ID 
* NotificationId 通知组 ID

`./autoscaling create-timer 'PublicKey' 'PrivateKey' cn-bj2 sxy-timer-test 1478156400 1479020400 1 uap-3afyvs 97526`

## 修改一个 循环定时任务

`./autoscaling modify-timer $PublicKey $PrivateKey $Region $TaskId $Name $StartTime $EndTime $Period $PolicyId $NotificationId`

参数说明:

* ID 循环定时任务ID
* Name 循环定时任务 Name
* StartTime 开始时间 精确到秒 时间戳
* EndTime 结束时间 精确到秒 时间戳
* Period 循环周期 单位 天
* PolicyId 对应的Policy ID 
* NotificationId 通知组 ID

`./autoscaling modify-timer 'PublicKey' 'PrivateKey' cn-bj2 sxy-timer-test 1478156400 1479020400 utimer-dumwyp 1 uap-3afyvs 97526`

## 修改一个 循环定时任务状态 开关

`./autoscaling update-timer-status $PublicKey $PrivateKey $Region $ID $Status`

参数说明:

* ID 循环定时任务ID
* Status 开关状态 开：'ON' 、 关：'OFF

`./autoscaling update-timer-status 'PublicKey' 'PrivateKey' cn-bj2 sxy-timer-test OFF`


## 一键新建带宽包定时任务

`./autoscaling new-timer $PublicKey $PrivateKey $Region $Config`

参数说明:

* Config 配置文件

```
{
  "Name": "sxy-timer-test",//名称
  "Period": 1,//循环周期 单位 天
  "StartTime": 1478167200,//开始时间  时间戳 精确到秒
  "EndTime": 1478599200,//结束时间  时间戳 精确到秒
  "NotificationId": 97526,//通知组id
  "Bandwidth": 2, //带宽大小 单位：M 最小2M
  "TimeRange": 1, //有效时长 单位：小时
  "EIPID": "eip-f24m2a"//要绑定的EIPID
}
```

`./autoscaling new-timer 'PublicKey' 'PrivateKey' cn-bj2 ./uas/config/timer.json`
