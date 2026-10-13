# Shulex Marketing & Knowledge Engineering (shulex-mkt)

[![Shulex](https://img.shields.io/badge/Brand-Shulex%20%7C%20Solvea-0284c7?style=flat-square)](https://www.shulex.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Skill: Atomic KB](https://img.shields.io/badge/Agent_Skill-shulex--atomic--kb-10b981?style=flat-square)](skills/shulex-atomic-kb/SKILL.md)

> **让 AI 客服告别“胡说八道”的终极解决方案** —— 电商与企业客服知识库「四层原子化拆解方法论」实操模板与 AI Agent Skill。

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

## 📥 获取与使用现成模板

### 1. 完整 Excel 标准模板（拿走直接填）
* 📂 **下载地址**：[`templates/客服知识库原子化拆解标准模板_Shulex出品.xlsx`](templates/客服知识库原子化拆解标准模板_Shulex出品.xlsx)
* 内含完整的使用说明、维护飞轮机制、以及 4 张已填入标准实操范例的 Sheet，直接复制或覆盖即可使用。

### 2. 在线 Markdown 预览
无需下载 Excel，在 GitHub 即可直接查看 4 张标准表的排版范例：
1. [表 1：全店基础政策与红线规矩表](templates/markdown/01_basic_policies.md)
2. [表 2：产品与参数原子结构表](templates/markdown/02_product_specs.md)
3. [表 3：买家大白话与口语同义句扩展表](templates/markdown/03_colloquial_synonyms.md)
4. [表 4：决策与行动指令表](templates/markdown/04_action_triggers.md)

---

## 🤖 使用 Agent Skill（给你的 AI 助手安装本能力）

如果你在使用 **Claude Code**、**Google Antigravity**、**Cursor** 或其他支持 Agent Skills 的 AI 编码助手，可以直接将本 Skill 引入你的环境：

* 🔗 **Skill 规范文件**：[`skills/shulex-atomic-kb/SKILL.md`](skills/shulex-atomic-kb/SKILL.md)

### 使用场景：
只需将未整理的乱七八糟的 Word、FAQ 或产品说明书发给 AI，并提示：
> *“参考 `skills/shulex-atomic-kb/SKILL.md`，帮我把这份产品手册清洗并重构为四层原子化知识库表格。”*

AI 将自动完成**冲突消除 ➔ 参数结构化 ➔ 买家大白话扩充 ➔ 动作闭环绑定**的全流程。

---

## 🏢 关于 Shulex & Solvea

* **Shulex (数里行间)**：专注于跨境电商与国内品牌的下一代全体验 AI 客服与 VOC 洞察平台。
* **Solvea**：面向海外与日本 DX 市场的全渠道 AI 接线员与智能服务系统。
* 🌐 官方网站：[https://www.shulex.com](https://www.shulex.com) | [https://solvea.cx](https://solvea.cx)

---

## 📄 License

本项目遵循 [MIT License](LICENSE)。欢迎自由使用、复用与二次分发！
