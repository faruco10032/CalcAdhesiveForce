# CalcAdhesiveForce
粘着力計測データの解析コード

## 環境
OS:windows

Pyhton 3.7

## 内容
* CSVファイルを読み込んでオフセット値との差分を表示する
* 入力するデータは16列，1行ごとのデータ
* ファイルパス指定
* 同一階層内に画像保存用ディレクトリを作成し，各フレームの画像を生成，保存する

## 今後の実装内容
* GUIの作成
  * 計測データの選択を簡単に
  * 粘着力のピーク値を表示
  * 複数の計測データを一度に参照
* ~~出力画像のフォルダを作成~~

## オプショナル
* 縦軸の単位を指定する
  * キャリブレーション結果から1ポイントあたりの力（mN）を計算
  * mN/計測値をかける

## 参考サイト
* CSV読み込み：https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869
* データプロット：http://python-remrin.hatenadiary.jp/entry/2017/05/27/114816
* matplotlib.pyplot.savefig：https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.savefig.html
* ディレクトリの作成：https://www.gesource.jp/programming/python/code/0009.html
* GUI：https://qiita.com/chanmaru/items/1b64aa91dcd45ad91540
* GUI：https://qiita.com/chanmaru/items/8e5ebf7d8b0b21c8fd3a
* ファイルダイアログの表示：https://pg-chain.com/python-filedialog
* ファイルパスの取得：https://note.nkmk.me/python-os-basename-dirname-split-splitext/
* ファイルパスの取得：https://kaworu.jpn.org/python/Python%E3%81%A7%E3%83%91%E3%82%B9%E3%81%8B%E3%82%89%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%90%8D%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B