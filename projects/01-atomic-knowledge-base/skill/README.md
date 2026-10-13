# 🤖 客服知识库原子化拆解 · AI Agent Skill 版

> **适用人群**：AI 工程师、大模型应用开发者、智能客服实施人员、Claude Code / Antigravity / Cursor 用户  
> **核心作用**：给你的 AI 智能体加载【原子化知识库拆解】技能包，自动把长篇大论的文档清洗为高可用、防幻觉的 4 层表格。

---

## ⚡ 核心能力文件

* 📄 **Agent Skill 规范主文件**：[`SKILL.md`](SKILL.md)（直接作为 Agent Skill 引入，包含 YAML 元数据与工作流 SOP）
* 💬 **大模型即用 Prompt**：[`prompt-templates/system_prompt_for_llm.md`](prompt-templates/system_prompt_for_llm.md)（一键复制给 ChatGPT、Claude 或 Dify）
* 🐍 **自动化脚本**：[`scripts/atomize_kb.py`](scripts/atomize_kb.py)（用于脚手架生成与自动化清洗）

---

## 🚀 三种调用方式

### 方式 1：在 Claude Code / Antigravity 中直接使用
将本目录软链接或复制到你的 Agent skills 目录：
```bash
# 复制到全局 skills 目录
cp -r ai-skill-edition ~/.claude/skills/shulex-atomic-kb
```
在会话中直接对 AI 说：
> *“使用 `shulex-atomic-kb` 技能，帮我把附件里的产品手册拆解为原子化知识库。”*

---

### 方式 2：在 ChatGPT / Claude Web / Cursor 中使用
1. 打开 [`prompt-templates/system_prompt_for_llm.md`](prompt-templates/system_prompt_for_llm.md)；
2. 将内容作为 System Prompt 粘贴给模型；
3. 将未整理的文档（Word/PDF/文本）发给模型，它将自动输出标准 4 张表格。

---

### 方式 3：集成到 Dify / FastGPT 知识库清洗流水线
在知识库入库前的 Pre-processing 节点中，使用上述 System Prompt 将用户上传的文件做结构化提取后再切分 Embedding，**RAG 检索准确率提升 40% 以上**。

---

## 💬 官方技术顾问支持

如需定制复杂业务系统的知识库清洗流水线、或对接 Shulex API：

<div align="center">
  <img src="../assets/shulex-contact-qr.png" width="180" alt="Shulex 客服二维码" />
  <p><b>▲ 微信扫码添加技术顾问</b></p>
</div>
