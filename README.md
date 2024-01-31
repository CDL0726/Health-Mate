**整体实训营项目时间线**

作品提交时间：2024 年 2 月 4 日  
优秀作品公布：2024 年 2 月 6 日  

[大作业提交表](https://aicarrier.feishu.cn/sheets/EYF4s03B0hm3p1t2WMFcqcUHnwc)  

**需要提交的资料**    
项目介绍文档（GitHub Repo 或者部署的网页）  
5 分钟以上的介绍视频（上传 B站）   
模型需要上传一份到 OpenXLab   
OpenXLab 演示体验 Demo （非必须其他方式的演示 Demo 也可以）   

备注：  
优秀的项目将会被推荐到更高 Level 的书生·浦语大模型挑战赛，提交简单的书生·浦语相关项目申请后，可获得 2 月 7 日——2 月 27 日 至少单卡 A100 的比赛项目算力支持。

![](https://github.com/CDL0726/Health-Mate/blob/img/Repo.jpg)  

# **整体实训营项目大作业**  

# AI健康伴侣 Health-Mate
#####  Jan. 28 2024
#####  Team Members:  陈德林、方烁、房宇亮 

### AI健康伴侣 Health-Mate
   以GenAI赋能，为家庭用户提供健康管理抓手，让人们治末病，身体与心理共同健康，第一阶段以心理健康切入点，第二阶段加入身体与心理的共同健康。
   以书生·浦语2.0 为底坐大模型， 结合家庭健康管理的具体应用场景，如心理健康 慢病管理为切入点，将书生·浦语2.0进行落地应用，实现科技向善，惠泽百姓！

### 计划安排：
      - LLM模型下载
      - 数据集收集 如：心理数据
      - 基于InternLM2和Langchain 搭建健康知识库
      - XTurner 心理数据微调
      - LMDeploy 模型部署
      - Opencompass 模型评测
      
#### 模型下载 Huggingface
      import os

    # 设置环境变量
      os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

    # 下载模型
       os.system('huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir /home/zhanghui/models/sentence-transformer')

#### 数据收集
     https://openxlab.org.cn/datasets/Scchy/LLM-Data 
     这个数据集下载方案：
     import os
     from openxlab.dataset import download

     load_d = '/home/xlab-app-center/data'
     out_f =  f'{load_d}/Scchy___LLM-Data/cookingBook.json'
     if not os.path.exists(out_f):
     download(dataset_repo='Scchy/LLM-Data', source_path='cookingBook.json', target_path=load_d)
     

#### Lagent 大模型智能体搭建
[Lagent](https://github.com/InternLM/InternLM/blob/main/agent/lagent_zh-CN.md) 

