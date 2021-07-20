import random

template = [
    "{}は{}です．",
    "{}の{}だろう．",
    "この{}は{}でしょう．",
    "{}の{}.",
    "{}過ぎて{}できない．",
    "限りなく{}に近い{}.",
]

single = [
    "{}でしょう．．",
    "{}かもしれませんね．．",
    "{}だったらいいですね．．",
    "{}", ]


def sentence(results):
    if len(results) == 1:
        t = random.choice(single)
        ans = t.format(results[0])
    else:
        t = random.choice(template)
        ans = t.format(results[0], results[1])
    return ans
