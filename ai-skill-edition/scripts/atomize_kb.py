#!/usr/bin/env python3
"""
Shulex Atomic Knowledge Base Generator
Usage:
    python atomize_kb.py input_manual.txt [output_dir]
"""

import sys
import os
import json

def generate_markdown_templates(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    files = {
        "01_basic_policies.md": """# 表 1：基础政策与红线规矩表
| 业务场景 | 触发条件 | 运费承担方 | 标准执行口径 | 例外说明 | 建议话术闭环动作 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 7天无理由退货 | 签收7天内且不影响二次销售 | 买家承担 | 支持7天无理由，包装完好原件退回 | 拆封贴身件不退 | 发送退货地址与注意事项 |
""",
        "02_product_specs.md": """# 表 2：产品与参数原子结构表
| 商品名称/型号 | 核心参数 (尺寸/电压/功率) | 官方适配清单 | 明确不兼容清单 | 常见故障代码 | 排除方法与标准答复 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 示例商品A | 重量150g; 5V/2A; 蓝牙5.3 | iOS 12+, Android 8+ | 蓝牙4.0及以下 | 闪烁红灯 | 长按电源键10秒重置 |
""",
        "03_colloquial_synonyms.md": """# 表 3：买家大白话同义句扩展表
| 标准业务问题 | 买家口语1 | 买家口语2 | 买家口语3 | AI 标准理解与答复重点 |
| :--- | :--- | :--- | :--- | :--- |
| 设备无法开机 | 按了没反应 | 灯怎么都不亮 | 怎么死机了 | 引导长按5秒解锁或充电排查 |
""",
        "04_action_triggers.md": """# 表 4：决策与行动指令表
| 用户意图 | 触发前置条件 | 判定等级 | 索要信息 | 联动后台动作 (Action) | 闭环完成话术 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 破损补发 | 收到48h内提供破损照片 | L1 自动 | 运单号+损坏部位图 | 自动生成补发工单 | 已为您登记补发，单号稍后短信同步 |
"""
    }
    
    for filename, content in files.items():
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {filepath}")

def main():
    if len(sys.argv) < 2:
        print("Shulex Atomic KB Generator")
        print("Usage: python atomize_kb.py <output_folder_path>")
        sys.exit(1)
        
    out_dir = sys.argv[1]
    print(f"Scaffolding Atomic KB tables in {out_dir}...")
    generate_markdown_templates(out_dir)
    print("Done! You can now import these structured tables into your RAG / Agent pipeline.")

if __name__ == "__main__":
    main()
