from langsplit import split_by_lang
from tests.data.generate_test_json import texts_de_fr_en, texts_zh_jp_ko_en
from langsplit.split.utils import DEFAULT_THRESHOLD


new_lang_map = {
    "zh": "zh",
    "zh-cn": "zh",
    "zh-tw": "x",
    "ko": "ko",
    "ja": "ja",
}


def test_split_to_substring():
    for text in texts_zh_jp_ko_en:
        substr = split_by_lang(
            text=text,
            verbose=False,
            lang_map=new_lang_map,
            threshold=DEFAULT_THRESHOLD,
            default_lang="en",
        )
        for index, item in enumerate(substr):
            print(item)
            # print(f"{index}|{item.lang}:{item.text}")
        print("----------------------")

    for text in texts_de_fr_en:
        substr = split_by_lang(
            text=text,
            verbose=False,
            # lang_map=new_lang_map,
            threshold=DEFAULT_THRESHOLD,
            default_lang="en",
        )
        for index, item in enumerate(substr):
            print(item)
            # print(f"{index}|{item.lang}:{item.text}")
        print("----------------------")


def main():
    test_split_to_substring()


if __name__ == "__main__":
    main()
