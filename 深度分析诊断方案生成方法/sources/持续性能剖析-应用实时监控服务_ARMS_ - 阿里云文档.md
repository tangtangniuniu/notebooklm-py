> Source: https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling/

持续性能剖析-应用实时监控服务(ARMS)-阿里云帮助中心




[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[![](https://img.alicdn.com/imgextra/i2/O1CN01bYc1m81RrcSAyOjMu_!!6000000002165-54-tps-60-60.apng)

AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](/)

输入文档关键字查找

* [产品概述](/zh/arms/application-monitoring/product-overview/)
* [快速入门](/zh/arms/application-monitoring/getting-started/)
* [操作指南](/zh/arms/application-monitoring/user-guide/)
* [实践教程](/zh/arms/application-monitoring/use-cases/)
* [安全合规](/zh/arms/application-monitoring/security-and-compliance/)
* [开发参考](/zh/arms/application-monitoring/developer-reference/)
* [服务支持](/zh/arms/application-monitoring/support/)
* [视频专区](/zh/arms/application-monitoring/videos/)

[首页](/)

# 持续性能剖析

更新时间：

复制为 MD 格式

[产品详情](https://www.aliyun.com/product/arms)

[我的收藏](/my_favorites.html)

持续性能剖析可以有效发现Java程序中因为CPU、内存和IO导致的瓶颈问题，并且按照方法名称、类名称和行号进行细分统计，最终协助开发者优化程序、降低延迟、增加吞吐、节约成本。本文介绍如何开通ARMS持续性能剖析功能以及如何查看持续性能剖析数据。

持续性能剖析功能经性能测试，在一般的Spring Web应用所有功能效果全部开启的情况下， CPU增加开销5%左右，堆外增加内存开销50 M左右，GC以及请求延迟增加不明显。

## 前提条件

**重要** 

* 仅[专家版](https://help.aliyun.com/zh/arms/application-monitoring/product-overview/pro-edition-1#task-2121328)和[按写入可观测数据量计费](https://help.aliyun.com/zh/arms/application-monitoring/product-overview/billing-description#24aa417b937em)模式支持持续性能剖析功能。
* 持续性能剖析数据仅支持存储7天，存储在用户名下的SLS中（SLS Project：proj-xtrace-<encode>-<region-id>，SLS Logstore：logstore-profiling）。

* 请先[接入ARMS应用监控](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/overview#concept-2198561)，并且[升级ARMS探针](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/update-the-arms-agent-for-java-applications)至v2.7.3.5或以上版本。
* 持续性能剖析功能当前仅支持OpenJDK和Oracle JDK，不支持IBM OpenJ9和Oracle GraalVM JDK。

## 使用限制

### **操作系统内核**

Linux 2.6.32-431.23.3.el6.x86\_64及以上。

**说明** 

通过`uname -r`命令可以查询当前内核版本。

### **JDK版本**

ARMS的持续性能剖析功能使用Java虚拟机工具接口（Java Virtual Machine Tool Interface，简称[JVM TI](https://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html)）获取应用的方法栈，从而获得应用运行期间的CPU以及内存使用详情。JVM TI存在已知的[Crash问题](https://bugs.openjdk.org/browse/JDK-8283849)，可能导致应用崩溃，这个问题在OpenJDK 8u352/11.0.17/17.0.5，Oracle JDK 11.0.21/17.0.9版本中已经得到了修复。对于问题修复之前的JDK版本，ARMS团队进行了多次测试，发现问题的触发依赖特殊的场景，发生概率极低。因此，在JDK版本不能满足要求的情况下，ARMS不会强制关闭持续性能剖析能力，您可以根据需要，临时打开持续性能剖析功能，并通过应用IP限制生效范围。但为了应用运行稳定，我们强烈建议您按照要求升级JDK版本，在低版本的JDK上使用持续性能剖析功能，存在应用崩溃的风险。

持续性能剖析功能主要依赖于JDK中存在调试符号（debug symbols），Alpine基础镜像为了控制体积而去除了JDK调试符号导致功能使用受影响，如需使用相关功能建议优先考虑使用非Alpine基础镜像。

**持续性能剖析建议JDK版本：**

|  |  |
| --- | --- |
| **JDK类型** | **版本** |
| OpenJDK | * OpenJDK 8u352+ * OpenJDK 11.0.17+ * OpenJDK 17.0.5+ |
| Oracle JDK | * Oracle JDK 11.0.21+ * Oracle JDK 17.0.9+ |

## 开启持续性能剖析功能

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**应用监控** > **应用列表**。
2. 在**应用列表**页面顶部选择目标地域，然后单击目标应用名称。

   **说明** 

   **语言**列的图标含义如下：

   ![Java图标](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343019661/p522528.png)：接入应用监控的Java应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0525839171/p813051.png)：接入应用监控的Golang应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6972247271/p847175.png)：接入应用监控的Python应用。

   **-**：接入可观测链路 OpenTelemetry 版的应用。
3. 在上方导航栏选择**应用配置** > **自定义配置**。
4. 在**持续性能剖析设置**区域，打开总开关，并设置**实时生效IP**或**实时生效网段**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4011386571/p978242.png)
5. 单击**保存**。

## 查看持续性能剖析数据

* 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**应用监控** > **持续性能剖析**。
* 在[ARMS控制台](https://arms.console.aliyun.com/#/home)的**应用监控** > **应用列表**页面进入目标应用，然后在上方导航栏选择**应用诊断** > **持续性能剖析**。

## 数据查询

![2025-06-24_15-17-10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7273001571/p977175.png)

* 筛选元数据（图示①）

  Profile元数据包含应用名和[Profile类型](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling-data-description#f6e06119e1r0k)两个部分，可以通过这两个部分确定一组Profile。

  选择一组元数据后，系统将根据您所选择的元数据自动更新趋势图和火焰图。

  **说明** 

  更换选择的元数据，系统将清除**快捷筛选**区域内已有的标签筛选条件。

  ![image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)
* 设置元数据的时间范围（图示②）

  该时间范围用于指定元数据和快捷筛选数据的获取范围。为保证响应速度，默认为最近15分钟。通常情况下无需更改。在数据变动较频繁或间隔较大时，可以进行对应调整。

  该时间仅影响趋势图和火焰图的时间范围，不会影响元数据的时间范围，支持自动刷新。
* 快捷筛选（图示③）

  快捷标签数据依赖于元数据的时间范围，标签键来源于性能监控数据中的`labels`字段（JSON格式）。不同标签之间为“与”的逻辑关系。选择标签后，系统将根据您所选择的标签自动更新趋势图和火焰图。

  + 主机地址：开始性能剖析的实例IP。
  + 线程名称：应用的全部线程，可以根据CPU耗时、内存占用等发现异常线程。
  + 线程组名称：展示线程组，是一组规则相同的线程合集，可以根据CPU耗时、内存占用等发现一类异常线程。
* 趋势图（图示④）

  对应Profile元数据在指定时间范围内的趋势。
* 火焰图（图示⑤）。

  选择元数据、标签、时间后，系统将自动生成一组Profile的[火焰图](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling-flame-chart-description)。

  + 单击![image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)图标，可以查看Copilot对当前火焰图分析出的问题和处理建议。您也可以自定义问题，进一步了解CPU、内存、火焰图相关数据。

    ![2025-06-25_15-15-29](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)
  + 选择**显示模式**，可以设置**仅火焰图**、**仅表格**或**表格+火焰图**。
  + 单击**查看SQL**，可以查看构建该火焰图的SQL语句，您可以根据SQL语句前往阿里云日志服务SLS的对应Project和Logstore进行数据分析。

    ![2025-06-24_16-13-06](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

## 数据对比

通过数据对比可以查看目标Profile在当前一段时间和过去一段时间内的数值对比。

![2025-06-24_16-31-01](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

* 筛选元数据（图示①）

  Profile元数据包含应用名和[Profile类型](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling-data-description#f6e06119e1r0k)两个部分，可以通过这两个部分确定一组Profile。

  选择一组元数据后，系统将根据您所选择的元数据自动更新趋势图和火焰图。

  **说明** 

  更换元数据的选择，系统将清除**快捷筛选**区域内已有的标签筛选条件。

  ![image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)
* 设置元数据的时间范围（图示②）

  该时间范围用于指定元数据和快捷筛选数据的获取范围。为保证响应速度，默认为最近15分钟。通常情况下无需更改。在数据变动较频繁或间隔较大时，可以进行对应调整。

  该时间仅影响趋势图和火焰图的时间范围，不会影响元数据的时间范围，支持自动刷新。
* 快捷筛选（图示③）

  快捷标签数据依赖于元数据的时间范围，标签键来源于性能监控数据中的`labels`字段（JSON格式）。不同标签之间为“与”的逻辑关系。选择标签后，系统将根据您所选择的标签自动更新趋势图和火焰图。

  + 主机地址：开始性能剖析的实例IP。
  + 线程名称：应用的全部线程，可以根据CPU耗时、内存占用等发现异常线程。
  + 线程组名称：展示线程组，是一组规则相同的线程合集，可以根据CPU耗时、内存占用等发现一类异常线程。
* 趋势图（图示④）

  趋势图用于展示当前一段时间和过去一段时间内数据波动情况和总体趋势。趋势图是基于元数据和标签的筛选结果，以时间进行聚合，其聚合策略来源于元数据区域。

  在**当前值**区域，时间范围固定与主时间范围（图示②）相同，您可以在**过去值**区域，单击**过去N小时**指定要对比的时间段。
* 火焰图（图示⑤）。

  选择元数据、标签、时间后，系统将自动生成Profile的[火焰图](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling-flame-chart-description)。单击![2025-06-24_17-21-47](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)图标，可以切换查看简单对比视图和融合对比视图。

  #### **简单对比视图**

  ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

  #### **融合对比视图**

  红色代表相对过去占比增加，蓝色代表相对过去占比减少。

  ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

  + 单击![image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)图标，可以查看Copilot对当前火焰图分析出的问题和处理建议。您也可以自定义问题，进一步了解CPU、内存、火焰图相关数据。

    ![2025-06-25_16-07-31](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

    在融合对比视图中，Copilot会对两段时间内的性能剖析数据进行对比分析，给出对比火焰图的前后性能变化，影响性能的因素等。单击**火焰图详情分析**，Copilot可以进一步分析具体的性能问题，并给出修复建议。

    ![2025-06-25_16-11-23](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)
  + 选择**显示模式**，可以设置**仅火焰图**、**仅表格**或**表格+火焰图**。
  + 单击**查看SQL**，可以查看构建该火焰图的SQL语句，您可以根据SQL语句前往阿里云日志服务SLS的对应Project和Logstore进行数据分析。

    ![2025-06-24_16-13-06](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

## **相关文档**

* [【产品变更】ARMS应用监控持续剖析功能升级公告](https://help.aliyun.com/zh/arms/product-overview/arms-application-monitoring-continuous-profiling-function-upgrade-announcement)
* [火焰图说明](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling-flame-chart-description)
* [持续性能剖析数据说明](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/continuous-profiling-data-description)
* [常见问题](https://help.aliyun.com/zh/arms/application-monitoring/user-guide/new-continuous-profiling-faq)

[上一篇：Python应用持续剖析](/zh/arms/application-monitoring/user-guide/continuous-profiling-for-python-applications)[下一篇：火焰图说明](/zh/arms/application-monitoring/user-guide/continuous-profiling-flame-chart-description)

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

![阿里云APP](https://img.alicdn.com/imgextra/i4/O1CN01XLesV31fkf7pYNATb_!!6000000004045-2-tps-400-400.png)

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证： [浙B2-20080101](http://beian.miit.gov.cn/) 域名注册服务机构许可： [浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[![](//gw.alicdn.com/tfs/TB1GxwdSXXXXXa.aXXXXXXXXXXX-65-70.gif)](https://zzlz.gsxt.gov.cn/businessCheck/verifKey.do?showType=p&serial=91330106673959654P-SAIC_SHOW_10000091330106673959654P1710919400712&signData=MEUCIQDEkCd8cK7%2Fyqe6BNMWvoMPtAnsgKa7FZetfPkjZMsvhAIgOX1G9YC6FKyndE7o7hL0KaBVn4f%20V%2Fiof3iAgpsV09o%3D)[![浙公网安备 33010602009975号](//img.alicdn.com/tfs/TB1..50QpXXXXX7XpXXXXXXXXXX-40-40.png)](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)