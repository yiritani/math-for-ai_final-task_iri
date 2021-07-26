# 人工知能のための数学最終レポート

*M21W0B09_入谷雄介*

1. [コンセプト](#concept)
1. [アプリ全体の流れ](#flow)
1. [アプリケーション使用方法](#ml_howto)
    1. [学習 & プロット表示](#ml_howto)
    1. [スクレイプ](#scrape_howto)


***
<a id="concept"></a>
## <u>コンセプト</u>
自宅の家賃が妥当なのかどうか調査するため、最寄り駅の賃貸物件の家賃から学習モデルを作成。<br>
散布図と線形回帰のプロットに自宅を被せて表示するプログラムを作成。<br>
基本的には「人工知能のための数学」の講義内で教授された記法を使う。<br>

To:赤石教授<br>
　　jupyterファイルの作成だけだとあまりにもすぐ終わってしまったので、アプリケーションとしてpythonでスクレイプからプロット表示までを行うapplicationsディレクトリを作成しました。<br> 
　　基本的に最終課題としての評価はjupyterファイルのみで充分かと思います。

***
## <u>ディレクトリ構成</u>
TOP ディレクトリ<br>
│<br>
├ applications   pythonファイル群<br>
│　├ ML_learning  学習〜プロット表示までするアプリ群<br>
│　├ scrape   suumoをスクレイプしてcsv作成までするアプリ群<br>
│<br>
├ jupyter <br>


***
<a id="flow"></a>
## <u>アプリ全体の大枠の流れ</u>

1.賃貸検索サイトをスクレイプ

2.スクレイプしたデータからインプット用csv生成<br>
[csvレイアウト]

|  FarFromStation<br>駅徒歩  |  Age<br>築年数    |  Price<br>家賃  |  ManagementPrice<br>管理費  | TotalPrice<br>家賃 + 管理費 |
| ---- | ---- | ---- | ---- | ---- |
|  int  |  int  |  float  |  float  | float  |

3.csvを読み込み自宅周辺の家賃状況を線形回帰直線と散布図で表示

4.3で表示したプロットに被せて自宅のデータを表示

5.4で作成したプロットをpngで保存

***
<a id="ml_howto"></a>
## <u>ML使用方法</u>
#### ※コマンドは全てgit clone したディレクトリ内で実行する。

1.コンテナ作成<br>
```
docker compose up -d --build
```

2.学習モデル作成 & プロットのpngをコンテナ内に出力
```
docker run math-for-ai_iritani_last-task python applications/ML_learning/controller.py
```

3.コンテナ内に出力されたpngのプロットをローカルにコピーし、表示する
```
docker run math-for-ai_iritani_last-task python applications/ML_learning/controller.py
```

***
<a id="scrape_howto"></a>
## <u>スクレイパー使用方法</u>
※デフォルトでインプット用のcsvを配置しているので、実施は必須ではない。
#### コマンドは全てコンテナ内で実行する想定

1.コンテナ作成<br>
```
docker compose up -d --build
```

2.コンテナに入る
```
docker exec -i -t iri-container_math-for-ai bash
```

3.suumoで部屋一覧を表示し、"2ページ目の"URLをコピー<br>
　「部屋ごとの表示」を選択すること
![Screen Shot 2021-07-26 at 18 29 19](https://user-images.githubusercontent.com/74131902/126967112-9b4a5212-be44-4950-a0e8-eb7528dadf62.png)
URL例：https://suumo.jp/jj/chintai/ichiran/FR301FC005/?shkr1=03&cb=0.0&shkr3=03&rn=0005&shkr2=03&mt=9999999&ar=030&bs=040&shkr4=03&ct=9999999&ra=013&ek=000525620&cn=9999999&mb=0&fw2=&et=9999999&page=
<br>※最後のページ番号は削除すること

4.config.yml1行目のURLを書き換える
```
vi applications/scrape/config/config.yml
```

5.scrape実行
```
python applications/scrape/controller.py
```

'END'がstdoutに表示されたら終了
