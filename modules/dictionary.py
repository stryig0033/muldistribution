classification_dict = {
    # ------ 内科系 ------
    "内科": [
        {
            "any": [("内科", "partial")]
        }
    ],
    "一般内科": [
        {
            "any": [('総合', 'partial'), ("一般内科", "partial"), ("人間ドック", "partial"), ("予防接種", "partial"), ("総合内科", 'partial'), ('健康診断', 'partial'), ('健診', 'partial'), ('漢方', 'partial'), ('漢内', 'partial'), ('在宅', 'partial')],
            "not": [('外科', 'partial')],
        }
    ],
    "呼吸器内科": [
        {
            "must": [("内", "partial")],
            "any": [("呼吸", "partial"), ("呼", "partial")],
            "not": [('外科', 'partial')],
        }
    ],
    "消化器内科": [
        {
            "must": [('内', 'partial')],
            "any":  [("消化", "partial"), ("胃", "partial"), ("腸", "partial"), ('消', 'partial'), ('視', 'partial')],# 視 for 内視鏡
            "not": [('外科', 'partial')],
        }
    ],
    "循環器内科": [
        {
            "must": [("内", "partial")],
            "any": [("循環器", "partial"), ("循", "partial")],
            "not": [('外科', 'partial')],
        }
    ],
    "腎臓・内分泌内科":[
        {
            "must": [("内", "partial")],
            "any": [("透析", "partial"), ("腎臓", 'partial'), ('甲状腺', 'partial'), ("甲内", "partial"), ('腎', 'partial'), ('透', 'partial')],
            "not": [('外科', 'partial')],
        }
    ],
    "糖尿病・代謝内科":[
        {
            "any": [("糖尿", "partial"), ("代謝", "partial"), ('糖代', 'partial'), ('糖', 'partial'), ('代', 'partial')],
            "not": [('外科', 'partial')],
        }
    ],
    "血液・腫瘍内科":[
        {
            "must": [("内", "partial")],
            "any": [("血", "partial"), ("腫瘍", "partial")],
            "not": [('外科', 'partial')],
        }
    ],
    "アレルギー科": [
        {
            "any": [("ア", "partial"), ('ｱ', 'partial'), ('ア疾内', 'partial')]
        }
    ],
    "リウマチ科": [
        {
            "any": [("リウ", "partial"), ('ﾘｳ', 'partial'),  ("リュウ", "partial"), ("膠", "partial"), ("リマウチ", 'partial')]
        }
    ],
    "感染症内科": [
        {
            "any": [("感", "partial"), ("性", "partial"), ('エイズ', 'partial')],
            "not": [('外科', 'partial')],
        }
    ],
    "老年科": [
        {
            "any": [("老年", "partial"), ('老人', 'partial'), ('高齢者', 'partial'), ('加齢', 'partial'), ('老精', 'partial'), ('老内', 'partial')]
        }
    ],
    "心療内科": [
        {
            "must": [("内", "partial")],
            "any": [("心", "partial"), ('心身', 'partial')],
            "not": [('外科', 'partial')],
        }
    ],
    "肝・胆・膵内科": [
        {
            "must": [('内', 'partial')],
            "any": [("肝", "partial"), ("胆", "partial"), ("膵", "partial")],
            "not": [('外', 'partial')],
        }
    ],

    # ------ 外科系 ------
    "外科": [
        {
            "any": [("外", "partial")]
        }
    ],
    "一般外科": [
        {
            "any": [('総合', 'partial'), ("一般外科", "partial"), ("総合外科", 'partial')]
        }
    ],
    "呼吸器外科": [
        {
            "must": [("外", "partial")],
            "any": [("呼吸", "partial"), ("呼", "partial")],
            "not": [('内科', 'partial')],
        }
    ],
    "消化器外科": [
        {
            "must": [('外', 'partial')],
            "any":  [("消化", "partial"), ("胃", "partial"), ("腸", "partial"), ('消', 'partial')],
            "not": [('内科', 'partial')],
        }
    ],
    "循環器外科": [
        {
            "must": [("外", "partial")],
            "any": [("循環器", "partial"), ("循", "partial"), ('心', 'partial')],
            "not": [('内科', 'partial')],
        }
    ],
    "大腸・肛門外科": [
        {
            "any": [('大腸', 'partial'), ('肛', 'partial'), ('こう', "partial")],
            "not": [('内科', 'partial')],
        }
    ],
    "肝・胆・膵外科": [
        {
            "must": [('外', 'partial')],
            "any": [("肝", "partial"), ("胆", "partial"), ("膵", "partial")],
            "not": [('内科', 'partial')],
        }
    ],
    "血管外科": [
        {
            "must": [('外', 'partial')],
            'any': [('血', 'partial')],
            "not": [('内科', 'partial')],
        }
    ],
    "乳腺・内分泌外科": [
        {
            "any": [('乳', 'partial'), ('内分泌外', 'partial')],
            "not": [('内科', 'partial')],
        }
    ],
    "人工臓器・移植外科": [
        {
            # "must": [('外', "partial")],
            "any": [('人工臓器', 'partial'), ('移', 'partial')]
        }
    ],
    # "心臓外科": [
    #     {
    #         "must": [("外", "partial"), ("心臓","partial")],　　循環器外科と統合
    #         "not": [('内科', 'partial')],
    #     }
    # ],
    "呼吸器外科": [
        {
            "must": [("外", "partial")],
            "any": [("呼吸", "partial")],
            "not": [('内科', 'partial')],
        }
    ],
    "脳神経外科": [
        {
            "any": [('脳', 'partial'), ('神経', 'partial'), ('脳神', 'partial')]
        }
    ],
    "腎臓・内分泌外科":[
        {
            "must": [("外", "partial")],
            "any": [("透析", "partial"), ("腎臓", 'partial'), ('甲状腺', 'partial'), ('内分内', 'partial'), ('人工透内', 'partial')],
            "not": [('内科', 'partial')],
        }
    ],

    # ------ その他系 ------
    "麻酔科": [
        {
            "any": [("麻", "partial"), ('ペ', 'partial'), ('ﾍﾟ', 'partial'),]
        }
    ],
    "泌尿器科": [
        {
            "any": [('泌尿', 'partial'),('泌', 'partial'), ('頻尿', 'partial'), ('ひ尿', 'partial')]
        }
    ],
    "皮膚科": [
        {
            "any": [("皮", "partial")]
        }
    ],
    "眼科": [
        {
            "any": [('眼', 'partial'), ('コンタクト', 'partial'), ('ｺﾝﾀｸﾄ', 'partial')]
        }
    ],
    "整形外科": [
        {
            "any": [("整", "partial"), ('レントゲン', 'partial'), ('ﾚﾝﾄｹﾞﾝ', 'partial'), ('ペ', 'partial'), ('ぺ', 'partial'),  ('ﾍﾟ', 'partial'), ('膝関節', 'partial'), ("物理療法", 'partial')]
        }
    ],
    "耳鼻咽喉科・頭頸部外科": [
        {
            "any": [("耳", "partial"), ("鼻", "partial"), ("じび", "partial"), ('咽', 'partial'), ('喉', 'partial'), ("いんこう", "partial"), ('頭', 'partial'), ("頸", "partial")]
        }
    ],
    "リハビリテーション科": [
        {
            "any": [('リハ', 'partial'), ('ﾘﾊ', 'partial'), ('ﾘハ', 'partial')]
        }
    ],
    "形成外科・美容外科": [
        {
            "any": [('形', 'partial'), ('美', 'partial'),('ボトックス', 'partial'), ('プラセンタ', 'partial'), ('ﾎﾞﾄｯｸｽ', 'partial'), ('ﾌﾟﾗｾﾝﾀ', 'partial')]
        }
    ],
    "歯科・口腔顎顔面外科": [
        {
            "any": [('歯', 'partial'), ('口腔', 'partial'), ('顎', 'partial'), ('インプラント', 'partial'), ('ｲﾝﾌﾟﾗﾝﾄ', 'partial'), ('矯正', 'partial'), ('ホワイトニング', 'partial'), ('ﾎﾜｲﾄﾆﾝｸﾞ', 'partial')], 
        }
    ],
    "小児科": [
        {
            "any": [("児", "partial"), ('新生児', 'partial'), ("児童", 'partial'), ('子', 'partial')],
            "not": [('外', 'partial')],
        }
    ],
    "小児外科": [
        {
            "must": [("小児", "partial"), ('外', 'partial')]
        }
    ],
    "産婦人科": [
        {
            "any": [("産", "partial"), ("婦", "partial"), ('不妊', 'partial')]
        }
    ],
    "精神神経科": [
        {
            "any": [('精', 'partial'), ('神', 'partial')]
        }
    ],
    "放射線科": [
        {
            "any": [('放', 'partial'), ('核', 'partial')]
        }
    ],
    "救急・集中治療科": [
        {
            "any": [('救', 'partial'), ('集中', 'partial')]
        }
    ],
    "臨床腫瘍科": [
        {
            "any": [('臨床', 'partial'), ('腫', 'partial'), ('化学療法', 'partial'), ('がん', 'partial'), ('癌', 'partial')]
        }
    ],
    "病理診断科": [
        {
            "any": [('病理', 'partial'), ('病理', 'partial'), ('理学', 'partial'), ('病診', 'partial')]
        }
    ],

    # ------ 追加 ------
    "緩和ケア科": [
        {
            "any": [('緩', 'partial')]
        }
    ],
    "鍼灸院": [
        {
            "any": [('はり', "partial"), ('指圧', 'partial')]
        }
    ],
    
    # どこにも該当しなかった場合
    "分類不可": []
}