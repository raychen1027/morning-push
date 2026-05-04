---
name: morning-push
description: 每日晨间推送技能。触发：晨间推送/每日战报/前日复盘/富兰克林晨课/morning push。生成前日复盘（柳比歇夫日志+KSS+通鉴）+ Franklin准则（ISO周数→(周-1)%13取13条之一）。
---

# Morning Push

## 日期边界
| 模块 | 基准 |
| Franklin | 今天 `datetime.now().isocalendar().week` |
| 前日复盘 | 昨天 `{yesterday}` |
> 周一Franklin翻周，复盘仍回顾周日。顺序：先复盘，后Franklin。

## 流程
1. 运行 `scripts/franklin_virtue.py` 获取今天准则JSON
2. 读数据源：{yesterday}-raw.md → {yesterday}.md → Get笔记fallback
3. 生成双推送

## 格式
### 前日复盘（≤500字）
- A类柱状图：█=1h，小数▊▌▏，无图例
- B类时间轴：表格（时间段|类别|时长），最小粒度15min
- 核心脉络：昨日发生了什么，200字战报
- KSS：Keep/Stop/Start各≤3条，每条≤30字
- 通鉴一隅：历史关联，100字

### Franklin（≤300字）
- 三段式：准则原文（含英文quote）+ 名将通鉴 + 今日行动
