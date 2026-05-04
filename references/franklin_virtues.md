# Franklin 13 条道德准则

> 来源：本杰明·富兰克林自传
> 使用方式：`(ISO周数 - 1) % 13` 取索引

| 编号 | 英文 | 中文 | 原文 |
|------|------|------|------|
| 1 | TEMPERANCE | 节制 | Eat not to dullness; drink not to elevation. |
| 2 | SILENCE | 缄默 | Speak not but what may benefit others or yourself; avoid trifling conversation. |
| 3 | ORDER | 秩序 | Let all your things have their places; let each part of your business have its time. |
| 4 | RESOLUTION | 决心 | Resolve to perform what you ought; perform without fail what you resolve. |
| 5 | FRUGALITY | 节俭 | Make no expense but to do good to others or yourself; i.e., waste nothing. |
| 6 | INDUSTRY | 勤奋 | Lose no time; be always employ'd in something useful; cut off all unnecessary actions. |
| 7 | SINCERITY | 真诚 | Use no hurtful deceit; think innocently and justly, and, if you speak, speak accordingly. |
| 8 | JUSTICE | 正义 | Wrong none by doing injuries, or omitting the benefits that are your duty. |
| 9 | MODERATION | 中庸/适度 | Avoid extremes; forbear resenting injuries so much as you think they deserve. |
| 10 | CLEANLINESS | 清洁 | Tolerate no uncleanliness in body, clothes, or habitation. |
| 11 | TRANQUILITY | 宁静 | Be not disturbed at trifles, or at accidents common or unavoidable. |
| 12 | CHASTITY | 节欲 | Rarely use venery but for health or offspring, never to dullness, weakness, or the injury of your own or another's peace or reputation. |
| 13 | HUMILITY | 谦逊 | Imitate Jesus and Socrates. |

## 输出格式

三段式，300字以内：

1. **准则原文**：中英文对照，含英文原文 quote
2. **名将通鉴**：一位历史人物与该准则相关的故事/典故，100字
3. **今日行动**：一条具体、可执行的今日行动建议，50字

## 计算方式

```python
from datetime import datetime
iso_week = datetime.now().isocalendar().week
index = (iso_week - 1) % 13  # 0-based index
```

- 每年 52 周 ≈ 4 轮完整循环
- 周一早晨 ISO 周数翻转，准则同步更新
