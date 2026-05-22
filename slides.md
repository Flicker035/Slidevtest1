---
bash: /Slidevtest1/
theme: seriph
title: Python 虚拟环境与 MCP 配置技术演示
background: https://source.unsplash.com/random/1920x1080?tech
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Python 环境搭建与 MCP 服务配置实践
  基于 VSCode 的技术演示指南
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Python 虚拟环境与 MCP 配置技术演示
简洁、专业的技术演示 PPT

---

# 目录
- 基础配置：虚拟环境搭建与依赖安装
- MCP 配置详解
- 实操演示：工具调用与状态确认
- 使用 MCP 获取小红书笔记的步骤
- 异常排查与安全规范

---

# 一、基础配置：虚拟环境搭建

## Python 虚拟环境搭建结果
- **成功创建虚拟环境**：使用 `python -m venv .venv` 命令
- **激活环境**：在 PowerShell 中执行激活脚本
- **环境隔离**：确保项目依赖不冲突系统 Python

### 关键步骤效果
```
(.venv) PS D:\Redbook-Search-Comment-MCP2.0-main>
```
*虚拟环境激活成功提示*

---

# 一、基础配置：依赖安装

## requirements.txt 文件作用与执行效果
- **文件作用**：列出项目所需 Python 包及其版本
- **执行命令**：`pip install -r requirements.txt`
- **安装结果**：自动下载并安装所有依赖包

### 执行效果展示
```bash
pip install -r requirements.txt
# 输出：Successfully installed playwright-1.40.0 ...
```
*依赖安装完成，无错误提示*

---

# 一、基础配置：Playwright 安装

## playwright install 命令执行结果及意义
- **命令意义**：安装浏览器内核，支持自动化测试
- **执行结果**：下载 Chromium、Firefox 等浏览器
- **重要性**：确保小红书网页能正常加载和操作

### 安装输出示例
```bash
playwright install
# 输出：Downloading Chromium 120.0.6099.0...
```
*浏览器内核安装成功*

---

# 二、MCP 配置详解

## .vscode/mcp.json 配置文件展示
- **配置文件位置**：`.vscode/mcp.json`
- **核心字段**：type、command、args

### 配置文件内容
```json
{
  "mcpServers": {
    "xiaohongshu-mcp": {
      "type": "stdio",
      "command": ".venv\\Scripts\\python.exe",
      "args": ["xiaohongshu_mcp.py"]
    }
  }
}
```

---

# 二、MCP 配置详解：字段解析

## type 字段
- **含义**：指定 MCP 服务器的通信类型
- **取值规范**："stdio" 表示标准输入输出通信
- **配置目的**：定义服务器如何与 VS Code 交互

## command 字段
- **含义**：指定执行 MCP 服务器的命令
- **取值规范**：指向 Python 可执行文件路径
- **配置目的**：告诉 VS Code 如何启动服务器

## args 字段
- **含义**：传递给命令的参数列表
- **取值规范**：数组形式，如 `["script.py"]`
- **配置目的**：指定运行的 Python 脚本

---

# 二、command 字段深度解析

## 为何必须指向虚拟环境内部的 python.exe
- **必要性**：确保使用项目特定的 Python 环境和依赖
- **错误配置影响**：使用系统 Python 可能导致依赖缺失或版本冲突
- **实际场景**：如果指向系统 python.exe，playwright 等包可能未安装

### 正确配置示例
```json
"command": ".venv\\Scripts\\python.exe"
```
*指向虚拟环境 Python*

### 错误配置示例
```json
"command": "python"
```
*可能导致 ImportError*

---

# 三、实操演示：MCP Server 状态确认

## 在 VS Code 中查看 MCP Server 状态
1. 打开 VS Code
2. 按 `Ctrl+Shift+P` 打开命令面板
3. 输入 "MCP" 并选择 "MCP: Show Servers"
4. 查看服务器状态

### 状态展示
- **Running** 状态：绿色图标，表示服务器正常运行
- **确认位置**：MCP 服务器列表中显示 "Running"

*标注：Running 状态表示配置正确，服务器已启动*

---

# 三、实操演示：工具调用过程

## mcp0_search_notes 工具调用演示
1. 在 VS Code 中打开聊天面板
2. 输入查询，如 "搜索小红书笔记 美食"
3. 观察工具调用过程
4. 查看返回结果

### 调用步骤
- **输入**：用户查询
- **处理**：MCP 服务器接收并执行搜索
- **输出**：返回笔记数据

### 示例结果
```
找到 5 条相关笔记：
1. 标题：夏日清凉饮品推荐
   内容：分享几款...
```
*工具调用成功，返回结构化数据*

---

# 三、实操演示：关键步骤效果图

## 虚拟环境创建成功界面
![虚拟环境激活](https://via.placeholder.com/800x400?text=Virtual+Env+Activated)
*PowerShell 中显示 (.venv) 前缀*

## 依赖安装完成提示
![依赖安装](https://via.placeholder.com/800x400?text=Dependencies+Installed)
*pip install 输出成功信息*

## 配置文件保存界面
![MCP 配置](https://via.placeholder.com/800x400?text=MCP+Config+Saved)
*VS Code 中 .vscode/mcp.json 文件*

---

# 四、使用 MCP 获取小红书笔记的步骤

## 步骤 1：准备工作
- **确保 MCP 服务器运行**：检查 VS Code 中服务器状态为 "Running"
- **激活虚拟环境**：在终端中激活 .venv 环境
- **验证依赖**：确认 playwright 等包已安装

### 检查命令
```bash
# 激活环境
.venv\Scripts\activate

# 验证安装
pip list | grep playwright
```

---

# 四、使用 MCP 获取小红书笔记的步骤

## 步骤 2：启动查询
1. 在 VS Code 中打开聊天面板 (`Ctrl+Alt+I`)
2. 输入自然语言查询，如 "帮我搜索小红书上的美食笔记"
3. 系统自动识别并调用 MCP 工具

### 查询示例
```
搜索小红书笔记：热门咖啡店推荐
```

---

# 四、使用 MCP 获取小红书笔记的步骤

## 步骤 3：执行搜索
- **工具调用**：MCP 服务器接收查询，执行 xiaohongshu_mcp.py 中的搜索逻辑
- **网页自动化**：使用 Playwright 打开小红书搜索页面
- **数据提取**：解析搜索结果，提取笔记标题、内容、作者等信息

### 后台执行过程
```python
# 模拟执行逻辑
search_query = "美食"
notes = search_xiaohongshu_notes(search_query)
return format_notes(notes)
```

---

# 四、使用 MCP 获取小红书笔记的步骤

## 步骤 4：查看结果
- **结果展示**：聊天面板显示搜索到的笔记列表
- **数据格式**：结构化显示，包括标题、摘要、点赞数等
- **可操作性**：支持进一步查询或保存数据

### 示例输出
```
📝 找到 10 条相关笔记：

1. **标题**：夏日必备清凉饮品
   **作者**：美食小达人
   **点赞**：1250
   **摘要**：分享 5 款解暑饮品做法...

2. **标题**：网红咖啡店打卡攻略
   **作者**：咖啡爱好者
   **点赞**：890
   **摘要**：推荐 3 家必去咖啡店...
```

---

# 四、使用 MCP 获取小红书笔记的步骤

## 步骤 5：数据处理
- **保存结果**：将笔记数据导出为 JSON 或 Markdown 格式
- **进一步分析**：使用 Python 脚本处理数据
- **合规使用**：确保数据仅用于学习和研究目的

### 数据导出示例
```json
{
  "notes": [
    {
      "title": "夏日必备清凉饮品",
      "author": "美食小达人",
      "likes": 1250,
      "content": "分享 5 款解暑饮品做法..."
    }
  ]
}
```

---

# 五、异常排查：模拟场景

## 路径错误异常场景
- **异常现象**：MCP 服务器启动失败，显示 "python.exe not found"
- **排查思路**：检查 command 字段路径是否正确
- **解决步骤**：
  1. 确认虚拟环境存在
  2. 验证 python.exe 路径
  3. 更新配置文件
- **恢复效果**：服务器状态变为 Running

### 错误提示示例
```
Error: spawn python.exe ENOENT
```
*路径错误导致的启动失败*

---

# 五、安全与规范说明

## 安全要点
- **评论内容合规**：确保获取的内容符合平台使用条款
- **账号操作边界**：仅获取公开笔记，避免登录或私密操作
- **自动化工具风险**：避免高频请求，防止账号被封

### 风险提示
- 遵守法律法规
- 尊重平台规则
- 合理使用数据

---

# 六、总结
- 掌握 Python 虚拟环境搭建
- 理解 MCP 配置关键字段
- 熟练 VS Code 中服务器状态确认
- 实践工具调用与异常排查
- 遵循安全规范，确保合规操作

*技术演示结束，感谢观看*