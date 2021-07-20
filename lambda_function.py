import collections
from termextract import japanese_plaintext
from termextract import core
import sentence
import synonym


def lambda_handler(event, context):

    text = event['subject']

    # 複合語を抽出し、重要度を算出
    frequency = japanese_plaintext.cmp_noun_dict(text)
    LR = core.score_lr(frequency,
                       ignore_words=japanese_plaintext.IGNORE_WORDS,
                       lr_mode=1, average_rate=1
                       )
    term_imp = core.term_importance(frequency, LR)

    results = []
    # 重要度が高い順に並べ替えて出力
    data_collection = collections.Counter(term_imp)
    for cmp_noun, value in data_collection.most_common():
        # print(core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
        results.append([core.modify_agglutinative_lang(cmp_noun), value])

    print(results)
    results = synonym.synonym(results)
    ans = sentence.sentence(results)
    print(ans)

    return {
        'statusCode': 200,
        'body': ans
    }
