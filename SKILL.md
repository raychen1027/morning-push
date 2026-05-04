---
name: morning-push
description: 每日晨间推送内容生成技能。触发场景：(1)生成前日复盘晨报（柳比歇夫日志+KSS+通鉴），(2)根据当天日期计算富兰克林13条道德准则，(3)合并生成双推送。触发词：晨间推送、每日战报、前日复盘、富兰克林晨课、morning push。
---

# Morning Push — 每日晨间推送

生成前日复盘 + 富兰克林晨间美德双推送。

## 核心规则

| 模块 | 日期基准 |
|------|---------|
| **富兰克林** | **今天**（`datetime.now()` 算 ISO 周数 → `(周-1)%13`） |
| **前日复盘** | **昨天**（`{yesterday}` 路径读取笔记文件） |

> 周一 Franklin 翻周，复盘仍回顾周日。顺序：先复盘，后 Franklin。

## 工作流程

### Step 1: 富兰克林准则

```bash
python3 ~/.openclaw/workspace/skills/morning-push/scripts/franklin_virtue.py
```

输出 JSON 含 `iso_week`, `virtue_id`, `virtue_en`, `virtue_cn`, `quote`。

### Step 2: 读取数据源（按优先级）

1. `/root/.openclaw/workspace/memory/daily-note-analysis/{yesterday}-raw.md`
2. `/root/.openclaw/workspace/memory/daily-note-analysis/{yesterday}.md`
3. Fallback：轻量拉取昨天 Get 笔记

### Step 3: 生成推送

按 `references/morning_push_format.md` 格式输出。

**前日复盘**（≤500字）：A类字符柱状图（█=1h，小数▊▌▏）+ B类时间轴表格 + 核心脉络200字 + KSS各3条 + 通鉴一隅100字。

**富兰克林**（≤300字）：准则原文（含英文quote）+ 名将通鉴 + 今日行动。

## 资源

- `scripts/franklin_virtue.py` — ISO 周数计算
- `references/franklin_virtues.md` — 13条准则完整列表
- `references/morning_push_format.md` — 输出格式规范

## 版本

v0.0.1
