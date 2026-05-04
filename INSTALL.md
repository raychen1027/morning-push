# Morning Push Skill — 安装指南

## 方式一：复制 skill 目录（推荐）

直接把整个 `morning-push/` 文件夹复制到目标机器的 skill 目录：

```bash
# 从本机复制到其他机器
scp -r ~/.openclaw/skills/morning-push user@other-host:~/.openclaw/skills/

# 或者手动复制文件夹
# 目标路径：~/.openclaw/skills/morning-push/SKILL.md
```

## 方式二：解压 .skill 包

```bash
# .skill 文件本质是 zip
unzip morning-push.skill -d ~/.openclaw/skills/

# 确认路径正确
ls ~/.openclaw/skills/morning-push/SKILL.md
```

## 方式三：通过 OpenClaw 安装（需发布到 ClawHub）

```bash
# 如果已发布到 clawhub
openclaw skills install morning-push
```

## 安装后验证

```bash
# 查看是否加载
openclaw skills list | grep morning-push

# 或直接问龙虾：
# "你有什么技能？" / "What skills do you have?"
```

## 目录结构

```
~/.openclaw/skills/morning-push/
├── SKILL.md                    ← 技能主文件
├── scripts/
│   └── franklin_virtue.py      ← ISO周数计算脚本
└── references/
    ├── franklin_virtues.md     ← Franklin 13条准则
    └── morning_push_format.md  ← 格式规范
```

## 版本

v0.0.1
