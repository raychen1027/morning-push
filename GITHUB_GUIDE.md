# Morning Push Skill — GitHub 仓库推送指南

## 1. 在 GitHub 上创建空仓库

打开 https://github.com/new，创建新仓库：

- **Repository name**: `morning-push`
- **Description**: `OpenClaw skill — 每日晨间推送（前日复盘 + Franklin 晨间美德）`
- **Public**
- ✅ 不要勾选 "Initialize this repository with a README"

## 2. 本地推送到 GitHub

```bash
# 进入准备好的目录
cd ~/.openclaw/workspace/morning-push-repo

# 初始化 git
git init
git add .
git commit -m "v0.0.1 — Morning Push Skill for OpenClaw"

# 关联远程仓库（把 YOUR_USERNAME 换成你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/morning-push.git

# 推送
git branch -M main
git push -u origin main
```

## 3. 在其他机器安装

```bash
# 克隆到 OpenClaw skills 目录
mkdir -p ~/.openclaw/skills
git clone https://github.com/YOUR_USERNAME/morning-push.git ~/.openclaw/skills/morning-push

# 验证
openclaw skills list | grep morning-push
```

## 4. 最终仓库地址

```
https://github.com/YOUR_USERNAME/morning-push
```

---

## 快捷复制版（改完用户名直接跑）

```bash
cd ~/.openclaw/workspace/morning-push-repo

git init
git add .
git commit -m "v0.0.1"
git remote add origin https://github.com/YOUR_USERNAME/morning-push.git
git branch -M main
git push -u origin main
```

## 从 GitHub 安装（其他龙虾端）

```bash
openclaw skills install https://github.com/YOUR_USERNAME/morning-push
```

或者手动：
```bash
cd ~/.openclaw/skills
git clone https://github.com/YOUR_USERNAME/morning-push.git
```
