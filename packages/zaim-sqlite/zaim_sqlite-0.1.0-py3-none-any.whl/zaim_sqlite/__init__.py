import os
from pyzaim import ZaimAPI
from tqdm import tqdm
from zaim_sqlite.lib import (
    ModeEnum,
    create_tables,
    get_engine,
    get_mode_id,
    get_session,
    get_unique_places,
    init_logger,
    upsert,
)
from zaim_sqlite.model import Account, Category, Genre, Mode, Money, Place


def main():
    # 環境変数から各種キーを取得
    consumer_id = os.environ.get("ZAIM_CONSUMER_ID")
    consumer_secret = os.environ.get("ZAIM_CONSUMER_SECRET")
    access_token = os.environ.get("ZAIM_ACCESS_TOKEN")
    access_token_secret = os.environ.get("ZAIM_ACCESS_SECRET")
    oauth_verifier = os.environ.get("ZAIM_ACCESS_VERIFIER")
    database = os.environ.get("DB")

    # Zaim2Sqlite クラスのインスタンスを作成
    app = ZaimSqlite(
        consumer_id,
        consumer_secret,
        access_token,
        access_token_secret,
        oauth_verifier,
        database,
    )

    # 口座一覧を挿入する
    app.upsert_accounts()

    # カテゴリ一覧を挿入する
    app.upsert_categories()

    # ジャンル一覧を挿入する
    app.upsert_genres()

    # 入出金履歴を挿入する
    app.upsert_money()


class ZaimSqlite:
    def __init__(
        self,
        consumer_id: str,
        consumer_secret: str,
        access_token: str,
        access_token_secret: str,
        oauth_verifier: str,
        database: str,
    ):
        """
        ZaimSqlite クラスの初期化。
        """
        # ロガーの初期化
        self.logger = init_logger()
        self.logger.info("[開始] Zaim2Sqlite クラスの初期化")

        # ZaimAPI の初期化
        self.api = ZaimAPI(
            consumer_id,
            consumer_secret,
            access_token,
            access_token_secret,
            oauth_verifier,
        )

        # Engine の作成
        engine = get_engine(database)

        # Sessionの作成
        self.session = get_session(engine)

        # テーブルを作成する
        create_tables(engine)

        # 種別一覧を挿入する
        self._upsert_modes()

        self.logger.info("[完了] Zaim2Sqlite クラスの初期化")

    def upsert_accounts(self):
        """
        口座一覧を挿入する
        """
        # 口座一覧を取得
        accounts = self.api.account_itos

        for key, value in tqdm(accounts.items(), desc="口座一覧"):
            value = value if value != "-" else None
            upsert(self.session, Account, id=key, name=value)

    def upsert_categories(self):
        """
        カテゴリ一覧を挿入する
        """
        # カテゴリ一覧を取得
        categories = self.api._get_category()["categories"]

        for category in tqdm(categories, desc="カテゴリ一覧"):
            upsert(
                self.session,
                Category,
                id=category["id"],
                name=category["name"],
                mode_id=get_mode_id(category["mode"]),
                active=(category["active"] == 1),
                parent_category_id=category["parent_category_id"],
                sort=category["sort"],
            )

    def upsert_genres(self):
        """
        ジャンル一覧を挿入
        """
        # ジャンル一覧を取得
        genres = self.api._get_genre()["genres"]

        for genre in tqdm(genres, desc="ジャンル一覧"):
            upsert(
                self.session,
                Genre,
                id=genre["id"],
                name=genre["name"],
                category_id=genre["category_id"],
                active=(genre["active"] == 1),
                parent_genre_id=genre["parent_genre_id"],
                sort=genre["sort"],
            )

    def upsert_money(self):
        """
        入出金履歴を挿入する
        """
        # 入出金履歴を取得
        data = self.api.get_data()

        # 店舗情報を挿入する
        self._upsert_places(data)

        for money in tqdm(data, desc="入出金履歴"):
            mode_id = get_mode_id(money["mode"])
            active = money["active"] == 1
            place_id = self._get_place_id_by_name(money["place"])

            upsert(
                self.session,
                Money,
                id=money["id"],
                name=money["name"] or None,
                date=money["date"],
                mode_id=mode_id,
                category_id=money["category_id"] or None,
                genre_id=money["genre_id"] or None,
                from_account_id=money["from_account_id"] or None,
                to_account_id=money["to_account_id"] or None,
                amount=money["amount"],
                comment=money["comment"] or None,
                active=active,
                receipt_id=money["receipt_id"] or None,
                place_id=place_id,
            )

    def _upsert_modes(self):
        """
        種別一覧を挿入する
        """
        for mode in tqdm(ModeEnum, desc="種別一覧"):
            upsert(self.session, Mode, id=mode.value, name=mode.name.lower())

    def _upsert_places(self, data):
        """
        店舗情報の挿入
        """
        places = get_unique_places(data)

        for place in tqdm(places, desc="店舗情報"):
            upsert(
                self.session,
                Place,
                id=None,
                name=place["place"],
                place_uid=place["place_uid"],
            )

    def _get_place_id_by_name(self, place_name: str) -> int:
        """
        店舗名から店舗IDを取得
        """
        place = self.session.query(Place).filter(Place.name == place_name).first()
        return place.id if place else None
