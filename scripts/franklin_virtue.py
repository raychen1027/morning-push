import json
from datetime import datetime

VIRTUES = [
    {"id": 1, "en": "TEMPERANCE", "cn": "节制", "quote": "Eat not to dullness; drink not to elevation."},
    {"id": 2, "en": "SILENCE", "cn": "缄默", "quote": "Speak not but what may benefit others or yourself; avoid trifling conversation."},
    {"id": 3, "en": "ORDER", "cn": "秩序", "quote": "Let all your things have their places; let each part of your business have its time."},
    {"id": 4, "en": "RESOLUTION", "cn": "决心", "quote": "Resolve to perform what you ought; perform without fail what you resolve."},
    {"id": 5, "en": "FRUGALITY", "cn": "节俭", "quote": "Make no expense but to do good to others or yourself; i.e., waste nothing."},
    {"id": 6, "en": "INDUSTRY", "cn": "勤奋", "quote": "Lose no time; be always employ'd in something useful; cut off all unnecessary actions."},
    {"id": 7, "en": "SINCERITY", "cn": "真诚", "quote": "Use no hurtful deceit; think innocently and justly, and, if you speak, speak accordingly."},
    {"id": 8, "en": "JUSTICE", "cn": "正义", "quote": "Wrong none by doing injuries, or omitting the benefits that are your duty."},
    {"id": 9, "en": "MODERATION", "cn": "中庸/适度", "quote": "Avoid extremes; forbear resenting injuries so much as you think they deserve."},
    {"id": 10, "en": "CLEANLINESS", "cn": "清洁", "quote": "Tolerate no uncleanliness in body, clothes, or habitation."},
    {"id": 11, "en": "TRANQUILITY", "cn": "宁静", "quote": "Be not disturbed at trifles, or at accidents common or unavoidable."},
    {"id": 12, "en": "CHASTITY", "cn": "节欲", "quote": "Rarely use venery but for health or offspring, never to dullness, weakness, or the injury of your own or another's peace or reputation."},
    {"id": 13, "en": "HUMILITY", "cn": "谦逊", "quote": "Imitate Jesus and Socrates."},
]


def main():
    now = datetime.now()
    iso_week = now.isocalendar().week
    virtue_index = (iso_week - 1) % 13
    virtue = VIRTUES[virtue_index]

    result = {
        "iso_week": iso_week,
        "virtue_id": virtue["id"],
        "virtue_en": virtue["en"],
        "virtue_cn": virtue["cn"],
        "quote": virtue["quote"],
        "date": now.strftime("%Y-%m-%d"),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
