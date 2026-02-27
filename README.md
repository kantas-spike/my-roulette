# my-roulette

`my-roulette`は、指定された範囲の数値または文字列をランダムに表示するツールです。
(Pytestの学習用に作成したプロジェクトです。)

## インストール

作業フォルダに移動後に、リポジトリからプロジェクトをクローンします。

```shell
git clone リポジトリのURL .
```

pyproject.tomlに定義されたパッケージを仮想環境(.venv)にインストールします。

```shell
uv sync
```

## 使い方

`my-roulette`のコマンドをオプションなしで実行すると、1〜6の整数からランダムに1つ選択して表示します。

```shell
uv run my-roulette
3
```

利用可能なオプションは以下により確認できます。

```shell
uv run my-roulette --help
usage: my-roulette [-h] [-s START_NUM] [-e END_NUM] [-d SPIN_DURATION]

指定された範囲の数値または文字列をランダムに表示する。

options:
  -h, --help            show this help message and exit
  -s, --start START_NUM
                        ランダムに表示する数値範囲の開始番号. (デフォルト値: 1)
  -e, --end END_NUM     ランダムに表示する数値範囲の終了番号. (デフォルト値: 6)
  -d, --spin-duration SPIN_DURATION
                        ルーレットが回る秒数. (デフォルト値: 1.5)
```
