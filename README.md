# レベルトラッカー プロッター

このスクリプトは、CSVファイルからデシベルレベルデータを読み込み、PNG画像として保存されるプロットを生成します。

## セットアップ

1.  **リポジトリをクローンする:**

    ```bash
    git clone https://github.com/noricha-vr/level-tracker.git
    cd level-tracker
    ```

2.  **仮想環境を作成して有効化する:**

    プロジェクトごとに仮想環境を作成することを推奨します。

    ```bash
    # 仮想環境を作成 (例: .venv)
    uv venv
    # 仮想環境を有効化 (macOS/Linux)
    source .venv/bin/activate
    # Windows (Command Prompt): .venv\Scripts\activate.bat
    # Windows (PowerShell): .venv\Scripts\Activate.ps1
    ```
    ターミナルのプロンプトの先頭に `(.venv)` のような表示が付けば、仮想環境が有効化されています。

3.  **依存関係をインストールする:**

    `pyproject.toml` ファイルに基づいて依存関係をインストールします。

    **方法 A: `uv` を使用する場合** (推奨)

    *uv* がインストールされていない場合は、[公式ドキュメント](https://github.com/astral-sh/uv#installation)に従ってインストールしてください。
    ```bash
    # uv を使って依存関係をインストール
    uv pip sync
    ```
    または、プロジェクト自体を編集可能モードでインストールする場合:
    ```bash
    # uv pip install -e .
    ```

    **方法 B: `pip` を使用する場合**

    ```bash
    # pip を使って依存関係をインストール
    pip install .
    ```
    *Note:* `pip install .` は `pyproject.toml` を参照して依存関係をインストールします。

## 使い方

ターミナルからスクリプトを実行します。オプションでCSVファイルへのパスをコマンドライン引数として指定できます。パスが指定されない場合は、デフォルトで `test.csv` が使用されます。

```bash
python plot_decibel.py [データCSVファイルへのパス]
```

例:

```bash
python plot_decibel.py my_measurement.csv
```

または、デフォルトファイルを使用する場合:

```bash
python plot_decibel.py
```

## 出力

生成されたプロット画像 (例: `test.png` や `my_measurement.png`) は `output` ディレクトリに保存されます。

## スクリプト詳細 (`plot_decibel.py`)

- CSVファイルを読み込みます (デフォルトエンコーディング: Shift_JIS / `cp932`)。
- デフォルトで最初の4行をスキップします。
- 列名の前後の空白を削除します。
- 'ｱﾄﾞﾚｽ' 列が存在する場合は削除します。
- すべての数値列を時間に対してプロットします (1秒あたり10サンプルと仮定して計算)。
- プロットを `output` ディレクトリに保存します。
