import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


async def Gen_Smile():
    lst=(" ".join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]))
    return lst

