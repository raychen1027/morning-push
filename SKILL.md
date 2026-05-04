---
name: morning-push
description: 每日晨间推送内容生成技能。当用户需要生成"前日复盘"晨报、富兰克林晨间美德推送、或完整的每日晨间双推送时触发。适用场景：(1) 每天早上生成昨日复盘（柳比歇夫日志+KSS+通鉴），(2) 根据当天日期计算并输出富兰克林13条道德准则，(3) 合并生成双推送内容。用户说"晨间推送""每日战报""前日复盘""富兰克林晨课""早上5点推送"时激活。
---

# Morning Push — 每日晨间推送

生成每日晨间双推送内容：前日复盘 + 富兰克林晨间美德。

## 触发条件

- "生成晨间推送"
- "前日复盘"
- "富兰克林晨课"
- "早上5点推送"
- "每日战报"
- "morning push"

## 核心规则

### 日期边界（不可混淆）

| 模块 | 日期基准 |
|------|---------|
| **富兰克林** | **今天**（运行当天 `datetime.now()`） |
| **前日复盘** | **昨天**（数据源 `{yesterday}`） |

> 周一早晨 Franklin 准则随新周翻转，复盘仍回顾周日。

### 推送顺序（不可调换）

1. **【一】前日复盘 · 柳比歇夫日志**
2. **【二】富兰克林晨间美德**

---

## 工作流程

### Step 1: 富兰克林准则计算

运行脚本获取今天对应的准则：

```bash
python3 ~/.openclaw/workspace/skills/morning-push/scripts/franklin_virtue.py
```

输出 JSON：
```json
{
  "iso_week": 19,
  "virtue_id": 6,
  "virtue_en": "INDUSTRY",
  "virtue_cn": "勤奋",
  "quote": "Lose no time...",
  "date": "2026-05-04"
}
```

### Step 2: 读取前日复盘数据源

按优先级读取：
1. `/root/.openclaw/workspace/memory/daily-note-analysis/{yesterday}-raw.md`
2. `/root/.openclaw/workspace/memory/daily-note-analysis/{yesterday}.md`
3. Fallback：轻量拉取昨天 Get 笔记

### Step 3: 生成推送内容

按 `references/morning_push_format.md` 格式规范输出。

#### 前日复盘板块

- **A类**：字符柱状图（█=1h，小数用▊▌▏）
- **B类**：Markdown 表格时间轴（时间段|类别|时长）
- **核心脉络**：昨日发生了什么，200字战报
- **KSS**：Keep/Stop/Start 各最多3条
- **通鉴一隅**：历史关联，100字

约束：≤500 字

#### 富兰克林板块

- 三段式：准则原文（中英文）+ 名将通鉴 + 今日行动
- 约束：≤300 字

---

## 资源文件

### scripts/franklin_virtue.py
计算当前日期的 ISO 周数，输出对应的 Franklin 准则 JSON。

### references/franklin_virtues.md
Franklin 13条道德准则完整列表、输出格式规范、计算方式。

### references/morning_push_format.md
晨间推送完整格式规范：A/B类统计方式、数据源优先级、语言风格、版本信息。

---

## 版本

v0.0.1 — 初始版本，含 Franklin + 前日复盘双推送