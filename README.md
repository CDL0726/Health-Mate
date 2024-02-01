# Agent HealthMate 全寿命周期健康管理 大模型智能体  

![](https://github.com/CDL0726/Health-Mate/blob/main/Lagent2%20T-Eval.png)  

### 项目介绍  
   GenAI赋能，解读用户的健康密码，根据个性化的数据，生成易懂化的解读，为家庭健康决策人提供全寿命周期的健康管理大语言模型智能体，成为陪伴用户一生的健康伴侣。
   
### 大模型智能体主要功能：  
  - 慢病管理
  - 健康管理  

### 模型工具
[InternLM2](https://github.com/InternLM/InternLM)    [Lagent](https://github.com/InternLM/lagent)  
[开源代码](https://open-compass.github.io/T-Eval/)  
[项目主页](open-compass.github.io/T-Eval)  
[论文](arxiv.org/abs/2312.14033)  
      
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




