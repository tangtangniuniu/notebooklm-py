> Source: http://www.future-forum.org.cn/en/onews.asp?id=118

FuTURE Forum | Huawei Unveils ��Agentic-AI Core�� For 6G: A Self-Programming Network That Writes Its Own Procedures




* Tel:  +86 10 82800433\34\35
* Email:  future@future-forum.org

* [����](http://www.future-forum.org.cn/cn/)
* [![](img/facebook.jpg)](https://www.facebook.com/Future-Mobile-Communication-FORUM-105314108098037/)
* [![](img/youtube.jpg)](https://youtube.com/channel/UCvRaFmYYgQoX6d8rdhXWAdQ)

[Toggle navigation](#mmenu) 
 [![](skin/images/logo.png) ![](skin/images/logo-m.png)](http://www.future-forum.org.cn/cn)

* [Home](index.asp)
* [Events](#)
  + [Community Seminars](she.asp)
  + [International Exchange](hd.asp?classid=International)
  + [Technical Seminar](hd.asp?classid=Seminar)
  + [Research Working Group](hd.asp?classid=Research)
  + [Member Interaction](hd.asp?classid=Interaction)
  + [General Assembly](hd.asp?classid=Assembly)
  + [All Events](http://www.future-forum.org/en/list.asp)
* [Working Group](#)
  + [5G/6G SIG](group_list.asp?id=9)
  + [5G MMW](group_list.asp?id=6)
  + [Digital Low Altitude](#)
  + [Frequency](group_list.asp?id=3)
  + [IOV](group_list.asp?id=1)
  + [Broadcast](group_list.asp?id=4)
  + [Cell-Free Network](group_list.asp?id=5)
  + [New Mid-Band](#)
* [Industry Information](#)
  + [Industry News](http://www.future-forum.org.cn/en/otype.asp?classid=19)
  + [Literature and Reports](http://www.future-forum.org.cn/en/otype.asp?classid=1)
* [About Us](#)
  + [Forum Introduction](about.asp)
  + [Organization](Organization.asp)
  + [Members](member.asp)
  + [Join us](application.asp)

Industry Information

Location: [Home](javascript:;) > [Industry Information](javascript:;) >

### Huawei Unveils ��Agentic-AI Core�� For 6G: A Self-Programming Network That Writes Its Own Procedures

   2026/1/5 14:14:24

A research team from Huawei��s advanced wireless labs in Canada and China has published a blueprint for a 6G core network that can generate, update and execute its own control procedures without human intervention. Described in Engineering, the ��Agentic-AI Core�� (A-Core) treats every service��whether a simple connection request or a complex artificial intelligence (AI)-driven application��as a ��mission�� that is planned, instantiated and run by a team of specialized AI agents.

At the heart of the architecture is NetGPT, a large-scale network AI model fine-tuned on telecommunication knowledge. When an operator or third-party application function sends a natural-language intent such as ��establish a connection between an idle device and a data network,�� the mission-planning agent feeds the request to NetGPT. The model retrieves relevant network capabilities (NCs) from a continuously updated toolbox, chains them into a workflow, and validates the result in a sandbox before any packet is forwarded.

The toolbox itself is open to external contributors. An NC��essentially a mini-service that can be as granular as a paging procedure or as rich as a full AI-training pipeline��is registered through a six-step verification process that checks for semantic conflicts and redundancy. Once accepted, the NC becomes immediately available to all subsequent missions, eliminating the traditional wait for standards-body ratification.

During mission execution, the mission-execution agent orchestrates computing-block agents that configure the actual network functions (NFs) drawn from an NF pool. Resources are allocated on demand from a shared resource pool under the resource-management agent. If performance degrades��for example, if AI-inferencing latency rises above a threshold��the system can dynamically insert an additional NC (such as an integrated sensing and communication (ISAC) sensing capability) or swap in a new computing block with more central processing unit (CPU) or graphics processing unit (GPU) capacity, all without dropping the mission.

Two concrete use cases illustrate the approach. In the first, an operator��s intent to connect an idle device is decomposed into sub-intents: page the device, establish a radio bearer, create a protocol data unit (PDU) session, and optionally add session-level protection. Each sub-intent maps to a pre-registered NC, and the resulting mission is executed in seconds. In the second use case, an autonomous-driving service provider ships an untrained AI model to the network; A-Core trains it on historical vehicle and infrastructure data, then deploys the trained model for real-time map-segment inference to connected cars. When sensing data from roadside ISAC units improve accuracy, the corresponding NC is added mid-mission.

The article acknowledges the open challenges of A-Core research. Hallucinations from the underlying large foundation model could introduce non-existent NCs, so every workflow is validated against pre- and post-conditions. Latency variability of current large foundation models (LFMs) also complicates ultra-reliable low-latency services, a gap the team proposes to close with on-device model acceleration. Quantitative benchmarks remain to be defined, as existing core networks lack metrics for ��autonomous procedure generation.��

By replacing static, standards-defined workflows with on-the-fly composition of verified network capabilities, A-Core aims to reduce capital and operating expenditures while accelerating service innovation. The architecture is presented as a candidate direction for the International Telecommunication Union (ITU)��s IMT-2030 framework, where ��AI and communication�� has already been identified as a new usage scenario for 6G.

  
  

Source:eurasiareview

### Search

### Events

* [![](http://www.future-forum.org.cn/cn/leon/upload/2025122515155034113.jpg)](ac_list.asp?id=188 "Spectrum Working Group Meeting Focuses on Spectrum Issues Regarding Low-Altitude Economy, 26GHz Millimeter Wave, U6GHz, and WRC-27")

  [Spectrum Working Group Meeting Focuses on Spectrum Issues Regarding Low-Altitude Economy, 26GHz Millimeter Wave, U6GHz, and WRC-27](ac_list.asp?id=188 "Spectrum Working Group Meeting Focuses on Spectrum Issues Regarding Low-Altitude Economy, 26GHz Millimeter Wave, U6GHz, and WRC-27")

    2025/12/25
* [![](http://www.future-forum.org.cn/cn/leon/upload/2025082615155034113.jpg)](ac_list.asp?id=186 "FCN 2025 Successfully Held in Belgrade")

  [FCN 2025 Successfully Held in Belgrade](ac_list.asp?id=186 "FCN 2025 Successfully Held in Belgrade")

    2025/8/26
* [![](http://www.future-forum.org.cn/cn/leon/upload/2025042715155034113.jpg)](ac_list.asp?id=187 "Global 6G Conference 2025 Opens in Nanjing")

  [Global 6G Conference 2025 Opens in Nanjing](ac_list.asp?id=187 "Global 6G Conference 2025 Opens in Nanjing")

    2025/4/15
* [![](http://www.future-forum.org.cn/cn/leon/upload/2024122515155034113.jpg)](ac_list.asp?id=185 "Wireless Frontier New Technology and Test Technology Summit Successfully Held")

  [Wireless Frontier New Technology and Test Technology Summit Successfully Held](ac_list.asp?id=185 "Wireless Frontier New Technology and Test Technology Summit Successfully Held")

    2024/12/25

## About us

Supported by NDRC, MOST, MIIT, and NSFC, FuTURE Forum is a non-profitable international organization jointly initiated by famous mobile telecommunication operators, mobile communication device manufactures, research institutes and universities from both home and abroad in 2005. ��[more](http://www.future-forum.org/en/about.asp)��

## Tags

* [Global 6G Conference](http://en.g6gconference.com/)
* [World 5G Convention](http://www.w5gc.com/?lang=en_US)
* [Join us](application.asp)
* [FCN2026](http://www.future-forum.org.cn/en/fcn2026/index.html)
* [Organizational Structure](http://www.future-forum.org/cn/Organization.asp)

## Contact Us

Room 937, Building A, Zhongguancun e-Plaza Fortune Centre, Haidian District, Beijing, PRC.

Tel: +86 10 82800433\34\35

Fax: +86 10 82800449

Email: future@future-forum.org.cn

Webpage: www.future-forum.org.cn

## WeChat

![](skin/images/wechat.jpg)

Copyright © δ���ƶ�ͨ����̳ All Rights Reserved    [��ICP��05002969��-6](https://beian.miit.gov.cn)    ����������11010802013735��



[X](#mm-0)
[��Ա��¼](login.asp)

* [��վ��ҳ](index.asp)
* [��̳�](javascript:;)
  + [��Ⱥ��̳](http://www.future-forum.org/cn/she.asp)
  + [���ʽ���](hd.asp?classid=���ʽ���)
  + [��������](hd.asp?classid=��������)
  + [�������о�](hd.asp?classid=�������о�)
  + [��Ա����](hd.asp?classid=��Ա����)
  + [��ṫ��](hd.asp?classid=��ṫ��)
  + [��б�](http://www.future-forum.org/cn/list.asp)
* [������](javascript:;)
  + [5G/6G SIG������](group_list.asp?id=9)
  + [Ƶ�ʹ�����](group_list.asp?id=3)
  + [5G��Ϣ��ȫ������](group_list.asp?id=2)
  + [���������Ϲ�����](group_list.asp?id=1)
  + [�㲥��Ƶ������](group_list.asp?id=4)
  + [Open5G����������](group_list.asp?id=5)
  + [5G΢�����ײ�������](group_list.asp?id=6)
* [����](product_diy.html)
  + [��������](http://www.future-forum.org/cn/otype.asp?classid=10)
  + [���ֻ��ĸ�](d_list.asp?classid=���ֻ��ĵ�)
  + [�������ĸ�](d_list.asp?classid=�������ĵ�)
  + [�������Ƥ��](d_list.asp?classid=�������Ƥ��)
  + [��̳��־](zz.asp)
* [ҵ����Ѷ](news.html)
  + [��ҵ��̬](http://www.future-forum.org/cn/otype.asp?classid=19)
  + [���ױ���](http://www.future-forum.org/cn/otype.asp?classid=1)
* [Open5G����](http://www.open5g.org/forum.php)
* [��������](javascript:;)
  + [��̳���](about.asp)
  + [��֯�ܹ�](Organization.asp)
  + [��̳��Ա](member.asp)
  + [��Ա����](application.asp)