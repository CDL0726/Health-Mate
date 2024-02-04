# Agent HealthMate 全寿命周期健康管理 大模型智能体  

![](https://github.com/CDL0726/Health-Mate/blob/main/Lagent2%20T-Eval.png)  

### 1. 项目介绍  
   GenAI赋能，解读用户的健康密码，根据个性化的数据，生成易懂化的解读，为家庭健康决策人提供全寿命周期的健康管理大语言模型智能体，成为陪伴用户一生的健康伴侣。
   
### 2. 大模型智能体主要功能：  
  - 慢病管理
  - 健康管理  

### 3. 模型工具
[InternLM2](https://github.com/InternLM/InternLM)    [Lagent](https://github.com/InternLM/lagent)  
[开源代码](https://open-compass.github.io/T-Eval/)  
[项目主页](open-compass.github.io/T-Eval)  
[论文](arxiv.org/abs/2312.14033)  

      
### 4. Lagent2 智能体工具调用  
#### 4.1 环境准备 
选择和第一个 `InternLM` 一样的镜像环境，运行以下命令安装依赖，如果上一个 `InternLM2-Chat-20B` 已经配置好环境不需要重复安装.

       # 升级pip
         python -m pip install --upgrade pip

         pip install modelscope==1.9.5
         pip install transformers==4.35.2
         pip install streamlit==1.24.0
         pip install sentencepiece==0.1.99
         pip install accelerate==0.24.1
        
#### 4.2 模型下载  
InternStudio 平台的 `share` 目录下已经为我们准备了全系列的 `InternLM` 模型，所以我们可以直接复制即可。使用如下命令复制： 
         
         mkdir -p /root/model/Shanghai_AI_Laboratory
         cp -r /root/share/model_repos/internlm2-chat-20b /root/model/Shanghai_AI_Laboratory   
  
#### 4.3 Lagent2 安装  
首先切换路径到 `/root/code` 克隆 `lagent` 仓库，并通过 `pip install -e .` 源码安装 `Lagent2`  

        cd /root/code  
        pip install lagent streamlit  -U 
               
#### 4.4 修改代码  
由于代码修改的地方比较多，大家直接将 `/root/code/lagent/examples/react_web_demo.py` 内容替换为以下代码  

[lagent/examples/internlm2_agent_web_demo.py](https://github.com/InternLM/lagent/blob/main/examples/internlm2_agent_web_demo.py)    

##### 4.4.1 进一步修改  
 `/root/code/lagent/examples/react_web_demo.py`用上面的代码替换后的代码修改如下：  
 
 4.4.1.1 120行model_name前面增加一行模型存放地址的参数  
 `/root/data/model/Shanghai_AI_Laboratory/internlm2-chat-20b',` 如下图：  
 ![](https://github.com/CDL0726/Health-Mate/blob/main/revise1.png)  
 

 4.4.1.2 然后运行 `'/root/.conda/envs/internlm/lib/python3.10/site-packages/lagent/llms/base_llm.py'`    
 注：这个地方envs后面的internlm是conda环境名称，找一下自己的conda环境名字叫什么，替换一下
 
 4.4.1.3 激活自己的 `conda env` 环境   
 然后改一下BaseModel类里面的这一段，加上红框里面这两行  
 ![](https://github.com/CDL0726/Health-Mate/blob/main/revise2.png)  

 
#### 4.5 运行一个智能体的网页样例  
你可能需要先安装 Streamlit 包

```bash
# pip install streamlit
streamlit run examples/internlm2_agent_web_demo.py
```
```
streamlit run /root/code/lagent/examples/react_web_demo.py --server.address 127.0.0.1 --server.port 6006
```
#### 4.6 配置本地端口  
```
ssh-keygen -t rsa
cat ~\.ssh\id_rsa.pub
ssh -CNg -L 6006:127.0.0.1:6006 root@ssh.intern-ai.org.cn -p 33090
```
在本地终端输入以下指令 `.6006` 是在服务器中打开的端口，而 `33090` 是根据开发机的端口进行更改。

```
lmdeploy serve api_server /root/internlm-demo/internlm2-chat-20b/workspace_w4a16_kvcache \
	--server-name 0.0.0.0 \
	--server-port 23333 \
	--tp 1
```
#### 4.6 智能体的网页样例图  
![](https://github.com/CDL0726/Health-Mate/blob/main/agent1.png)   

### 5. Agent实际应用  
[慢病管理 - CVD]()  
[健康管理 - 心理咨询]()

### 6. 智能体同类产品
[智谱清言](https://github.com/CDL0726/Health-Mate/blob/main/agent2.png)  
[GPTs]()  


### 7. Lagent大模型智能体 进一步研究
[Lagent](https://github.com/InternLM/InternLM/blob/main/agent/lagent_zh-CN.md) 
- 插件如何建立与调用
- 上传的文件格式拓展：图片 视频
---
### 8. 特别鸣谢  
- 上海人工智能实验室 A100算力支持
- 书生·浦语大模型实战营
- 浦语小助手
- 银佳助教




