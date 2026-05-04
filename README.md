# Morning Push Skill for OpenClaw

> 每日晨间推送技能 — 前日复盘 + Franklin 晨间美德，v0.0.1

## 简介

`morning-push` 是一个 OpenClaw Skill，用于生成每日晨间双推送内容：

1. **前日复盘** — 基于柳比歇夫日志框架的昨日回顾（A类柱状图 + B类时间轴 + KSS + 通鉴）
2. **Franklin 晨间美德** — 根据当天 ISO 周数自动计算对应的 Franklin 13 条道德准则

## 安装

### 方式一：OpenClaw 原生安装（推荐）

```bash
# 克隆到本地 skill 目录
mkdir -p ~/.openclaw/skills

cd ~/.openclaw/skills
git clone https://github.com/raychen1027/morning-push.git

# 验证安装
openclaw skills list | grep morning-push
```

### 方式二：手动复制

```bash
# 下载 ZIP 解压
curl -L https://github.com/raychen1027/morning-push/archive/refs/heads/main.zip -o morning-push.zip
unzip morning-push.zip -d ~/.openclaw/skills/
```

## 触发条件

安装后，你的龙虾会自动识别以下触发词：

- "生成晨间推送"
- "前日复盘"
- "富兰克林晨课"
- "每日战报"
- "morning push"

## 核心规则

| 模块 | 日期基准 |
|------|---------|
| **Franklin 晨课** | **今天**（运行当天 `datetime.now()`） |
| **前日复盘** | **昨天**（数据源 `{yesterday}`） |

> 周一早晨 Franklin 准则随新周翻转，复盘仍回顾周日——日期不混用。

## 目录结构

```
morning-push/
├── SKILL.md                        # 技能主文件（触发条件 + 工作流程）
├── INSTALL.md                      # 安装指南
├── scripts/
│   └── franklin_virtue.py          # ISO周数计算脚本
└── references/
    ├── franklin_virtues.md         # Franklin 13条准则完整列表
    └── morning_push_format.md      # 晨间推送格式规范
```

## 快速上手

安装后，在对话中说：

```
生成今天的晨间推送
```

龙虾会自动：
1. 读取昨天的笔记数据源
2. 计算今天的 Franklin 准则
3. 按格式输出双推送内容

## 更新日志

### v0.0.1 (2026-05-04)
- 初始版本
- 支持 Franklin + 前日复盘双推送
- 日期边界规则：Franklin 看"今天"，复盘看"昨天"
- 柳比歇夫日志 A类字符柱状图 + B类 Markdown 时间轴表格

## License

MIT

## 作者

Ray (@raychen1027)

---

**提示**：如果你从其他来源导入此 skill，请确保 `SKILL.md` 位于正确的路径：

```
~/.openclaw/skills/morning-push/SKILL.md
```

高优先级来源会覆盖低优先级的同名 skill。
