> Source: https://help.aliyun.com/zh/sls/configure-ram-permissions-for-the-smart-operations-assistant

因Copilot功能变更配置智能运维助手RAM权限-日志服务-阿里云




[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[![](https://img.alicdn.com/imgextra/i2/O1CN01bYc1m81RrcSAyOjMu_!!6000000002165-54-tps-60-60.apng)

AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](/)

输入文档关键字查找

* [开始使用](/zh/sls/start-using-sls/)
* [资源管理](/zh/sls/resource-management/)
* [数据采集](/zh/sls/data-collection-1/)
* [数据处理](/zh/sls/data-processing-sls/)
* [数据存储](/zh/sls/data-storage/)
* [查询与分析](/zh/sls/index-and-query/)
* [数据监控](/zh/sls/data-monitoring/)
* [数据输出与集成](/zh/sls/sls-log-output-and-integration/)
* [技术解决方案](/zh/sls/sls-technical-solutions/)
* [开发参考](/zh/sls/developer-reference/)
* [安全合规](/zh/sls/security-compliance/)
* [常见问题](/zh/sls/faq-15)

[首页](/)

# 为智能运维助手配置RAM权限

更新时间：

复制为 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](/my_favorites.html)

日志服务（SLS）智能运维助手基于云监控 2.0 的数字员工能力构建，支持通过自然语言生成 SQL 语句，解释日志内容或 SQL 逻辑，并提供 SQL 语句优化建议以提升查询效率。本文介绍如何通过 RAM访问控制为子账号或角色配置智能运维助手的使用权限。

## **权限变更说明**

日志服务原 **Copilot 功能**已切换至**云监控 2.0 数字员工**。由于底层能力的切换，使用日志服务 SQL 诊断、日志查询辅助等功能时的鉴权逻辑发生变化。

* **原鉴权策略（已废弃）：**依赖`log:GetMLServiceResults` 接口权限。

  ```
  {
    "Version": "1",
    "Statement": [
      {
        "Action": "log:GetMLServiceResults",
        "Resource": "acs:log:*",
        "Effect": "Allow"
      }
    ]
  }
  ```
* **新版鉴权逻辑：**需要授予云监控2.0数字员工相关的 `cms:*`权限。请根据实际需求选择以下两种策略之一进行配置。

  + **最小权限策略：**云监控 2.0 数字员工的最小权限策略可以保证日志服务原 Copilot 的基础使用：

    ```
    {
        "Effect": "Allow",
        "Action": [
            "cms:CreateChat",
            "cms:CreateThread"
        ],
        "Resource": "acs:cms:*:*:digitalemployee/apsara-*"
    }
    ```
  + **完整管理权限：**如果 RAM 用户需要对数字员工进行完整的生命周期管理（包括创建、修改、删除数字员工配置等），请授予所有相关权限。

    ```
    [
      {
        "Effect": "Allow",
        "Action": [
          "cms:CreateChat",
          "cms:GetDigitalEmployee",
          "cms:CreateDigitalEmployee",
          "cms:ListDigitalEmployees",
          "cms:UpdateDigitalEmployee",
          "cms:DeleteDigitalEmployee"
        ],
        "Resource": [
          "acs:cms:*:*:digitalemployee/*"
        ]
      },
      {
        "Effect": "Allow",
        "Action": [
          "cms:GetThread",
          "cms:CreateThread",
          "cms:ListThreads",
          "cms:UpdateThread",
          "cms:DeleteThread",
          "cms:GetThreadData"
        ],
        "Resource": [
          "acs:cms:*:*:digitalemployee/*"
        ]
      }
    ]
    ```

[上一篇：MetricStore Prometheus接口免密读写](/zh/sls/metricstore-prometheus-interface-unauthenticated-read-write)[下一篇：日志服务监控审计](/zh/sls/log-auditing-and-monitoring)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

![阿里云APP](https://img.alicdn.com/imgextra/i4/O1CN01XLesV31fkf7pYNATb_!!6000000004045-2-tps-400-400.png)![阿里云微信](https://img.alicdn.com/tfs/TB1AOdINW6qK1RjSZFmXXX0PFXa-258-258.jpg)

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证： [浙B2-20080101](http://beian.miit.gov.cn/) 域名注册服务机构许可： [浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[![](//gw.alicdn.com/tfs/TB1GxwdSXXXXXa.aXXXXXXXXXXX-65-70.gif)](https://zzlz.gsxt.gov.cn/businessCheck/verifKey.do?showType=p&serial=91330106673959654P-SAIC_SHOW_10000091330106673959654P1710919400712&signData=MEUCIQDEkCd8cK7%2Fyqe6BNMWvoMPtAnsgKa7FZetfPkjZMsvhAIgOX1G9YC6FKyndE7o7hL0KaBVn4f%20V%2Fiof3iAgpsV09o%3D)[![浙公网安备 33010602009975号](//img.alicdn.com/tfs/TB1..50QpXXXXX7XpXXXXXXXXXX-40-40.png)浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)