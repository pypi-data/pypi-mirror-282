from enum import Enum


class ModeEnum(Enum):
    """
    種別を表すEnumクラス
    """

    PAYMENT = 1
    INCOME = 2
    TRANSFER = 3

    @classmethod
    def from_str(cls, mode_str: str):
        """
        文字列からEnumへの変換を行うクラスメソッド
        """
        mapping = {
            "payment": cls.PAYMENT,
            "income": cls.INCOME,
            "transfer": cls.TRANSFER,
        }
        return mapping.get(mode_str, None)


def get_mode_id(mode: str) -> int:
    """
    種別の文字列をEnumの値に変換する関数
    """
    mode_enum = ModeEnum.from_str(mode)
    return mode_enum.value if mode_enum else None


def get_unique_places(data) -> list:
    """
    データからユニークな店舗のリストを取得する
    """
    unique_places = set()
    unique_places_result = []

    for entry in data:
        place_name = entry.get("place")

        # 店舗名が存在し、まだユニークな店舗のセットに含まれていない場合
        if place_name and place_name not in unique_places:
            unique_places_result.append(
                {key: entry[key] for key in ["place", "place_uid"] if key in entry}
            )
            unique_places.add(place_name)
    return unique_places_result
