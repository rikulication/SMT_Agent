# 一、API配置
在根目录下面创建.env文件  
LLM_API_KEY="sk-6******************************************a"  
LLM_MODEL_ID="deepseek-v4-flash"  
LLM_BASE_URL="https://api.deepseek.com"  
填写好对应的模型和apiKey
# 二、环境配置
1、win+r 然后输入cmd打开命令行  
2、运行 `python -m venv venv` 创建虚拟环境  
3、输入 `venv\Scripts\activate` 激活虚拟环境  
4、运行 `pip install -r requirements.txt`  安装依赖的python库
# 三、运行
所有库安装成功之后，使用  
`uvicorn main:app --host 0.0.0.0 --port 8000 --reload`  
来启动程序,直到出现  
`INFO:     Application startup complete.`  
就代表程序启动成功，运行对应的影刀程序就可以实现自动回复