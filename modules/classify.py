def match_word(keyword: str, pattern: str, match_type: str) -> bool:
    """
    部分一致/完全一致の判定関数
    """
    if match_type == "partial":
        return pattern in keyword
    elif match_type == "exact":
        return pattern == keyword
    return False

def check_rule(keyword: str, rule: dict) -> bool:
    """
    rule例:
      {
        "must": [("内科","partial"), ...],
        "any":  [("消化","partial"), ...],
        "not":  [("外科","partial"), ...]
      }
    - "must": 全部マッチする必要がある
    - "any":  いずれか1つマッチしていればOK（空ならスキップ）
    - "not":  1つでもマッチしたらNG
    """
    # must：全部マッチ必須
    for (pat, mtype) in rule.get("must", []):
        if not match_word(keyword, pat, mtype):
            return False

    # any：いずれかマッチ
    any_list = rule.get("any", [])
    if any_list:
        if not any(match_word(keyword, pat, mtype) for (pat, mtype) in any_list):
            return False

    # not：1つでもマッチしたらNG
    for (pat, mtype) in rule.get("not", []):
        if match_word(keyword, pat, mtype):
            return False

    return True


def classify_keywords(
    keywords, 
    classification_dict, 
    multiple=False,
    override_map=None,
    override_match_type="exact",
):
    """
    - keywords: 分類対象となる文字列のリスト
    - classification_dict: { "カテゴリ名": [rule1, rule2, ...], "分類不可": [] }
    - multiple: True の場合、複数カテゴリにマッチしても全て分類する
    - override_map: {"特定文字列": "分類先カテゴリ"} の辞書
    - override_match_type: "exact" or "partial"
        → override_map で「部分一致」させたいのか「完全一致」させたいのか指定
    """
    # 分類結果入れ物
    classified = {cat: [] for cat in classification_dict.keys()}

    for keyword in keywords:
        if not isinstance(keyword, str):
            # 文字列以外は強制的に「分類不可」
            classified["分類不可"].append(keyword)
            continue

        matched_categories = []

        # --------------------------
        # 1) override_map のチェック
        # --------------------------
        override_assigned = False
        if override_map:
            for ov_key, ov_categories in override_map.items():
                # ov_key が文字列か、タプル(リスト)かでハンドリングを変える
                if isinstance(ov_key, (tuple, list)):
                    # タプル/リスト内のいずれかに match_word()すればヒットとみなす
                    hit = any(match_word(keyword, single_key, override_match_type)
                              for single_key in ov_key)
                else:
                    # 文字列なら従来通り
                    hit = match_word(keyword, ov_key, override_match_type)

                if hit:
                    # ov_categories も1個か複数かもしれないので、ループでappend
                    if isinstance(ov_categories, str):
                        ov_categories = [ov_categories]
                    for cat in ov_categories:
                        classified[cat].append(keyword)
                        matched_categories.append(cat)
                    override_assigned = True

                    if not multiple:
                        break  # singleモードでは最初にヒットした時点で打ち切り

            # overrideでマッチして、かつ multiple=Falseなら次のkeywordへ
            if override_assigned and not multiple:
                continue

        # --------------------------
        # override でマッチしなかった or multiple=True の場合 → 通常ルール
        # --------------------------
        if not override_assigned or multiple:
            for category, rules in classification_dict.items():
                if category == "分類不可":
                    continue
                if any(check_rule(keyword, r) for r in rules):
                    classified[category].append(keyword)
                    matched_categories.append(category)
                    if not multiple:
                        break

        # --------------------------
        # いずれの手段でもマッチしなかったら「分類不可」
        # --------------------------
        if not matched_categories:
            classified["分類不可"].append(keyword)

    return classified

if __name__ == "__main__":
    # モジュールとしてインポートされた場合には実行されない
    pass