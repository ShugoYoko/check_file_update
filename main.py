import glob
import os
import datetime


def main() -> None:
    # 日付取得
    date_from: str = input("From:更新日を入力してください。例.2023-5-1 :")
    date_to: str = input("To:更新日を入力してください。例.2023-5-31 :")
    # 調査対象
    path: str = input("調査対象パス :")
    check_path: str = path + "/**"
    for file_path in glob.glob(check_path, recursive=True):
        if os.path.isfile(file_path):
            file_stamp: float = os.path.getmtime(file_path)
            # datetimeに変換
            file_datetime: datetime = datetime.datetime.fromtimestamp(file_stamp)
            from_list: list = date_from.split('-')
            from_date: datetime = datetime.datetime(int(from_list[0]), int(from_list[1]), int(from_list[2]))
            to_list: list = date_to.split('-')
            to_date: datetime = datetime.datetime(int(to_list[0]), int(to_list[1]), int(to_list[2]))
            # 日時の範囲内のものを表示
            if from_date <= file_datetime <= to_date:
                print(file_path)


if __name__ == "__main__":
    main()
