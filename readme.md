# テスト用JSONデータ作成ツール
## 概要
* データプロバイダに[mimesis](https://lk-geimfari.github.io/mimesis/)を利用して、テスト用JSONデータを作成します。
* python実行環境にmimesisが必要です。
    ```
    (virtualenv) C:\work\cygwin64\home\tetsuo.hino\git\test_data_generator>pip list
    Package    Version
    ---------- -------
    mimesis    4.0.0
    pip        19.0.3
    setuptools 40.8.0  
    ```
         
## vehicle_json.py
* 車両データモドキを作成します。
    
    ```
    (virtualenv) C:\work\cygwin64\home\tetsuo.hino\git\test_data_generator>python vehicle_json.py --help
    usage: vehicle_json [--lines] [--log]
    
    optional arguments:
      -h, --help            show this help message and exit
      --lines LINES         number of lines
      --log {DEBUG,INFO,WARN,ERROR,CRITICAL}
                            log level
    ```

* 作成されたjsonは以下のようになります。

    ```
    {"id": 1, "name": "Volvo 200 Series", "code": "USA", "owner": {"id": 4177, "first_name": "Kirstie", "last_name": "Ware", "address": "674 Bayview Promenade"}, "vehicle_date": "1994-03-13", "temparature": -16}
    {"id": 2, "name": "Packard Eight", "code": "USA", "owner": {"id": 3968, "first_name": "Santiago", "last_name": "Dejesus", "address": "293 Forest View Trail"}, "vehicle_date": "1925-08-15", "temparature": 42}
    {"id": 3, "name": "Rambler Classic", "code": "USA", "owner": {"id": 4712, "first_name": "Katelynn", "last_name": "Frederick", "address": "461 Lundeen Heights"}, "vehicle_date": "1946-08-29", "temparature": 49}
    {"id": 4, "name": "Bmw 3 Series", "code": "USA", "owner": {"id": 6961, "first_name": "Filiberto", "last_name": "Ramsey", "address": "105 Hicks Stravenue"}, "vehicle_date": "1988-08-14", "temparature": -6}
    {"id": 5, "name": "Continental Mark Ii", "code": "USA", "owner": {"id": 5463, "first_name": "Chance", "last_name": "Boyle", "address": "952 Ecker Spur"}, "vehicle_date": "1929-06-27", "temparature": 2}
    {"id": 6, "name": "Mercury Grand Marquis", "code": "USA", "owner": {"id": 1854, "first_name": "Tayna", "last_name": "Vargas", "address": "1017 Athens Spur"}, "vehicle_date": "1916-11-11", "temparature": 35}
    ```