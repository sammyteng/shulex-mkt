# Shulex Marketing & Knowledge Engineering (shulex-mkt)

[![Shulex](https://img.shields.io/badge/Brand-Shulex%20%7C%20Solvea-0284c7?style=flat-square)](https://www.shulex.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Excel Edition](https://img.shields.io/badge/Edition-Excel%20%E5%AE%9E%E6%93%8D%E7%89%88-16a34a?style=flat-square)](excel-edition/)
[![AI Skill Edition](https://img.shields.io/badge/Edition-AI%20Agent%20Skill%20%E7%89%88-6366f1?style=flat-square)](ai-skill-edition/)

> **让 AI 客服彻底告别“胡说八道”的终极解决方案** —— 电商与企业客服知识库「四层原子化拆解方法论」官方开源仓库。

---

## 🌟 本项目提供两个版本（根据你的角色二选一）：

```
shulex-mkt/
├── 📁 excel-edition/    👉 【版本 A：人工实操 Excel 版】适合运营、客服主管、店长，下载即填
└── 📁 ai-skill-edition/ 👉 【版本 B：AI 智能体 Skill 版】适合开发者与 AI 助手，一键导入使用
```

| 版本对比 | 👨‍💼 [人工实操 Excel 版](excel-edition/) | 🤖 [AI 智能体 Skill 版](ai-skill-edition/) |
| :--- | :--- | :--- |
| **适合对象** | 店长、客服主管、传统运营、培训师 | AI 工程师、大模型开发者、Claude/Cursor 用户 |
| **使用方式** | 下载现成的 `.xlsx` 表格，直接在电脑里填 | 将 `SKILL.md` 或 Prompt 导入 AI 智能体 |
| **核心交付** | 包含 5 个 Sheet、带真实示范的工业级 Excel | 包含工作流规范、Python 转换脚本与 System Prompt |
| **直达链接** | 👉 [进入 Excel 版目录](excel-edition/) | 👉 [进入 AI Skill 版目录](ai-skill-edition/) |

---

## 📖 为什么需要“原子化知识库”？

90% 的企业在接入智能客服或大模型时，都会踩同一个坑：**把几十页没整理过的产品说明书、Word、老制度直接喂给 AI**。

其结果往往是灾难性的：
* ❌ **文档版本冲突**：新旧退换货政策混杂，AI 检索上下文产生冲突，张嘴瞎编；
* ❌ **非结构化长段落**：一段话里塞了 5 个产品的安装条件，AI 出现严重幻觉；
* ❌ **缺乏大白话桥接**：说明书写的是“设备无法开机”，买家提问全都是“灯不亮/按了没反应”，AI 答非所问；
* ❌ **没有动作闭环**：只回答“可以退货”，不告诉买家怎么退、谁付运费，充其量只是个“复读机”。

**解法**：通过**四层原子化金字塔**，将复杂业务拆解为 4 张最小颗粒度、绝对无歧义的标准化表格。

---

## 📐 核心框架：四层原子化金字塔

| 层级 | 表格名称 | 核心解决问题 | 格式与特点 |
| :--- | :--- | :--- | :--- |
| **Layer 1** | [表1-基础政策规矩表](templates/markdown/01_basic_policies.md) | 质保多久？运费谁出？退换规则是什么？ | 全店绝对统一，唯一权威版本，杜绝冲突 |
| **Layer 2** | [表2-产品参数原子表](templates/markdown/02_product_specs.md) | 尺寸、电压、接口、兼容性与故障代码 | 纯结构化表格，一查即准，从物理层面消灭参数幻觉 |
| **Layer 3** | [表3-买家大白话扩展表](templates/markdown/03_colloquial_synonyms.md) | 解决“官方术语”与“买家大白话”之间的断层 | 每个标准问题补充 3~5 句真实口语同义句 |
| **Layer 4** | [表4-决策与行动指令表](templates/markdown/04_action_triggers.md) | 告别复读机，连带实际后台动作（Action） | 带前置判定、索要凭据、自动拉起 ERP/工单 |

---

## 🚀 极速获取与使用

### 1. 获取 Excel 模板
* 直接下载：[`excel-edition/客服知识库原子化拆解标准模板_Shulex出品.xlsx`](https://github.com/sammyteng/shulex-mkt/raw/main/excel-edition/%E5%AE%A2%E6%9C%8D%E7%9F%A5%E8%AF%86%E5%BA%93%E5%8E%9F%E5%AD%90%E5%8C%96%E6%8B%86%E8%A7%A3%E6%A0%87%E5%87%86%E6%A8%A1%E6%9D%BF_Shulex%E5%87%BA%E5%93%81.xlsx)
* 在线预览：[网页端 Markdown 预览](templates/markdown/01_basic_policies.md)

### 2. 获取 AI Agent Skill
* Skill 规范文件：[`ai-skill-edition/SKILL.md`](ai-skill-edition/SKILL.md)
* 大模型 Prompt 模板：[`ai-skill-edition/prompt-templates/system_prompt_for_llm.md`](ai-skill-edition/prompt-templates/system_prompt_for_llm.md)
* 转换脚本：[`ai-skill-edition/scripts/atomize_kb.py`](ai-skill-edition/scripts/atomize_kb.py)

---

## 🏢 关于 Shulex & Solvea

* **Shulex (数里行间)**：专注于跨境电商与国内品牌的下一代全体验 AI 客服与 VOC 洞察平台。
* **Solvea**：面向海外与日本 DX 市场的全渠道 AI 接线员与智能服务系统。
* 🌐 官方网站：[https://www.shulex.com](https://www.shulex.com) | [https://solvea.cx](https://solvea.cx)

---

## 📄 License

本项目遵循 [MIT License](LICENSE)。欢迎自由使用、复用与二次分发！
