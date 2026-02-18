# 設計仕様書

> **注意**: 本ドキュメントは設計仕様書です。変更履歴や実装の詳細な変更点については、`ChangeLog`を参照してください。本ドキュメントでは、現在のシステムの設計と仕様を記述します。

## 1. プロジェクト概要

### 1.1 プロジェクト名
gls (GPU List)

### 1.2 目的
GPUの仕様情報を一覧表示するコマンドラインツール。複数のGPUモデルの性能指標（TFLOP/s、VRAM、TDPなど）を比較表示する。

### 1.3 バージョン
1.0.38

## 2. アーキテクチャ

### 2.1 全体構成

```
gls/
├── gls.py              # メインコマンド（GPUリスト表示）
├── database.py         # GPUデータベース（辞書リスト）
├── setDevice.py        # デバイス設定ツール（curses UI）
├── __init__.py         # パッケージ初期化（バージョン情報）
└── [GPU名]_*.py        # GPUデバイスシミュレーターファイル
    ├── *_smi.py        # nvidia-smi シミュレーター
    ├── *_deviceQuery.py # deviceQuery シミュレーター
    └── *_rocminfo.py   # rocminfo シミュレーター（AMD用）
```

### 2.2 主要モジュール

#### 2.2.1 gls.py
- **役割**: メインコマンドラインインターフェース
- **機能**:
  - GPUデータベースから情報を読み込み
  - pandas DataFrameに変換
  - カラー表示とテーブルフォーマット
  - CSV/HTMLエクスポート（`--csv`オプション）
  - アップグレード機能（`--upgrade`）
  - アンインストール機能（`--remove`）
  - バージョン表示（`--version`）

#### 2.2.2 database.py
- **役割**: GPU仕様データの定義
- **データ構造**: 辞書のリスト（`gpu_data`）
- **データ項目**:
  - `vendor`: ベンダー名（NVIDIA, AMD, INTEL）
  - `product`: 製品名
  - `tdp`: 熱設計電力（Watt）
  - `vram_size`: VRAM容量（GB）
  - `vram_bw`: VRAM帯域幅（GB/s）
  - `vram_ecc`: ECCサポート（True/False）
  - `n_sp_core`: SPコア数
  - `n_mp`: マルチプロセッサ数（SM/CU/EU）
  - `gpu_clock`: GPUクロック（MHz）
  - `mem_clock`: メモリクロック（MHz）
  - `mem_bus_width`: メモリバス幅（bits）
  - `n_tensor_core`: テンソルコア数
  - `gen_tensor_core`: テンソルコア世代
  - `tflops_fp32`: FP32性能（TFLOP/s）
  - `tflops_fp16`: FP16性能（TFLOP/s）
  - `tflops_fp8_tensor`: FP8テンソル性能（TFLOP/s）
  - `tflops_fp8_tensor_sparse`: FP8スパース性能（TFLOP/s）
  - `system_interface`: システムインターフェース（PCIe等）
  - `gpu_chip`: GPUチップ名
  - `gpu_variant`: GPUバリアント
  - `gpu_arch`: GPUアーキテクチャ
  - `date_market`: 市場投入日
  - `url`: 参考URL

#### 2.2.3 setDevice.py
- **役割**: デバイス設定ツール
- **機能**:
  - cursesベースのインタラクティブメニュー
  - GPUデバイスの選択
  - 設定ファイル（`~/.glsconfig`）への保存

#### 2.2.4 GPUデバイスシミュレーターファイル
- **役割**: 各種GPUデバイスのコマンドシミュレーション
- **種類**:
  - `*_smi.py`: nvidia-smiコマンドのシミュレーション
  - `*_deviceQuery.py`: CUDA deviceQueryコマンドのシミュレーション
  - `*_rocminfo.py`: AMD rocminfoコマンドのシミュレーション（MI300Xのみ）
- **実装**: 固定出力文字列を返すシンプルな実装

## 3. データフロー

### 3.1 GPUリスト表示フロー

```
1. ユーザーが `gls` コマンドを実行
   ↓
2. gls.py の main() 関数が呼び出される
   ↓
3. database.py から gpu_data をインポート
   ↓
4. pandas DataFrame に変換
   ↓
5. change_df() でデータ整形
   - 不要な列の削除（url, vram_ecc, hints）
   - 列の並び替え
   - FP32でソート
   - 数値フォーマット適用
   ↓
6. set_title_colored() でタイトル行に色付け
   ↓
7. set_title_underline() でタイトル行に下線追加
   ↓
8. apply_row_colors() で行に交互に色付け
   ↓
9. 標準出力に表示
```

### 3.2 CSV/HTMLエクスポートフロー

```
1. ユーザーが `gls --csv` コマンドを実行
   ↓
2. /tmp/gls.cache/ ディレクトリを作成
   ↓
3. DataFrame を CSV 形式で保存（/tmp/gls.cache/output.csv）
   ↓
4. DataFrame を HTML 形式で保存（/tmp/gls.cache/output.html）
```

## 4. サポートGPU

### 4.1 NVIDIA GPU

#### データセンター向け
- **H200 SXM**: 141GB HBM3e, Hopperアーキテクチャ
- **H100 SXM x8**: 80GB HBM3, Hopperアーキテクチャ
- **H100 NVL x2**: 94GB HBM3, Hopperアーキテクチャ
- **GH200**: 480GB HBM3, Hopperアーキテクチャ
- **A100 SXM x4**: 40GB HBM2e, Ampereアーキテクチャ
- **A40 x10**: 48GB GDDR6, Ampereアーキテクチャ
- **A10**: Ampereアーキテクチャ
- **V100 x8**: Voltaアーキテクチャ
- **L40S**: 48GB GDDR6, Ada Lovelaceアーキテクチャ
- **L4**: 24GB GDDR6, Ada Lovelaceアーキテクチャ

#### プロフェッショナル向け
- **RTX 6000 Ada x8**: 48GB GDDR6, Ada Lovelaceアーキテクチャ
- **RTX A6000 x9**: 48GB GDDR6, Ampereアーキテクチャ
- **RTX 4000 Ada**: 20GB GDDR6, Ada Lovelaceアーキテクチャ
- **RTX 2000 Ada**: 16GB GDDR6, Ada Lovelaceアーキテクチャ

#### コンシューマー向け
- **RTX 5090**: Ada Lovelaceアーキテクチャ
- **RTX 4090**: 24GB GDDR6X, Ada Lovelaceアーキテクチャ
- **RTX 4060 Ti**: 16GB GDDR6, Ada Lovelaceアーキテクチャ
- **RTX 3090**: 24GB GDDR6X, Ampereアーキテクチャ
- **RTX 3080**: 10GB GDDR6X, Ampereアーキテクチャ
- **RTX 3070**: 8GB GDDR6, Ampereアーキテクチャ
- **GTX 1050 Ti**: 4GB GDDR5, Pascalアーキテクチャ
- **GTX 680**: 2GB GDDR5, Keplerアーキテクチャ

### 4.2 AMD GPU

#### データセンター向け
- **MI300X x4**: 192GB HBM3, CDNA 3.0アーキテクチャ
- **MI250X**: 128GB HBM2e, CDNA 2.0アーキテクチャ（カタログ情報のみ）

#### プロフェッショナル向け
- **PRO W7900**: 48GB GDDR6, RDNA 3.0アーキテクチャ（カタログ情報のみ）
- **PRO W7800**: 32GB GDDR6, RDNA 3.0アーキテクチャ（カタログ情報のみ）

#### コンシューマー向け
- **RX9070XT**: 16GB GDDR6, RDNA 4.0アーキテクチャ
- **RX7900GRE**: 16GB GDDR6, RDNA 3.0アーキテクチャ
- **RX7900XTX**: 24GB GDDR6, RDNA 3.0アーキテクチャ
- **HD 5870**: 1GB GDDR5, TeraScale 2アーキテクチャ

### 4.3 INTEL GPU

#### コンシューマー向け
- **Arc A770**: 16GB GDDR6, Xe-HPGアーキテクチャ（カタログ情報のみ）
- **Arc A380**: 6GB GDDR6, Xe-HPGアーキテクチャ（カタログ情報のみ）

## 5. コマンドラインインターフェース

### 5.1 glsコマンド

#### 基本コマンド
```bash
gls                    # GPUリストを表示
gls --csv              # CSV/HTMLファイルを生成（/tmp/gls.cache/）
gls --upgrade          # 最新版にアップグレード
gls --remove           # アンインストール
gls --version          # バージョン表示
gls --help             # ヘルプ表示
```

### 5.2 nvidia-smiシミュレーター

各GPUモデルに対応するnvidia-smiコマンドが利用可能：

```bash
nvidia-smi                    # デフォルト（GH200）
nvidia-smi -a                 # 詳細情報表示
nvidia-smi.rtx4090            # RTX 4090用
nvidia-smi.h100               # H100 SXM用
nvidia-smi.a100               # A100 SXM用
# ... その他多数
```

### 5.3 deviceQueryシミュレーター

各GPUモデルに対応するdeviceQueryコマンドが利用可能：

```bash
deviceQuery                   # デフォルト（GH200）
deviceQuery.rtx4090          # RTX 4090用
deviceQuery.h100              # H100 SXM用
deviceQuery.mi300x            # MI300X用
# ... その他多数
```

### 5.4 AMD ROCmコマンド

```bash
rocm-smi                      # ROCm SMI（MI300X x4）
rocm-smi -a                   # 詳細情報表示
rocminfo                      # ROCm情報（MI300X x4）
```

### 5.5 setDeviceコマンド

```bash
setDevice                     # インタラクティブメニューでGPUデバイスを選択
```

## 6. データ表示仕様

### 6.1 表示列

表示される列は以下の順序：

1. `product`: 製品名（左寄せ）
2. `FP32`: FP32性能（TFLOP/s）
3. `FP16`: FP16性能（TFLOP/s）
4. `GB/s`: VRAM帯域幅（GB/s）
5. `TDP`: 熱設計電力（Watt）
6. `GB`: VRAM容量（GB）
7. `SPs`: SPコア数
8. `MPs`: マルチプロセッサ数
9. `GHz`: GPUクロック（GHz）
10. `interface`: システムインターフェース
11. `TCs`: テンソルコア数
12. `FP8_TC`: FP8テンソル性能（TFLOP/s）
13. `ASIC`: GPUチップ名（最大7文字）
14. `arch`: GPUアーキテクチャ
15. `release`: 市場投入日

### 6.2 表示フォーマット

- **数値フォーマット**:
  - FP32/FP16/FP8_TC: 小数点以下1桁（例: `82.6`）
  - GB/s: 小数点以下1桁（例: `1008.1`）
  - GB: 小数点以下1桁（例: `24.0`）
  - GHz: 小数点以下2桁（例: `2.52`）

- **ソート**: FP32性能の降順

- **カラー表示**:
  - タイトル行: マゼンタ（太字）
  - タイトル行の下に下線
  - 偶数行: ライトグリーン
  - 奇数行: ライトシアン

## 7. 依存関係

### 7.1 Pythonパッケージ

- **wheel** (>=0.45.0): パッケージング
- **pandas** (>=2.0.0): データ処理とDataFrame操作
- **tabulate** (>=0.9.0): テーブル表示
- **colorama** (>=0.4.6): カラー出力（Windows対応）

### 7.2 Pythonバージョン

- Python 3.x（推奨: Python 3.8以上）

### 7.3 システム要件

- Ubuntu >= 20.04（setup.pyのコメントより）

## 8. インストールと配布

### 8.1 インストール方法

```bash
pip install git+https://github.com/thamada/gls.git
```

### 8.2 アップグレード方法

```bash
gls --upgrade
# または
gls --update
```

### 8.3 アンインストール方法

```bash
gls --remove
# または
gls --uninstall
```

### 8.4 パッケージ構成

- **setup.py**: setuptoolsを使用したパッケージ設定
- **entry_points**: コンソールスクリプトの定義
  - `gls`: メインコマンド
  - `nvidia-smi.*`: 各GPUモデル用nvidia-smi
  - `deviceQuery.*`: 各GPUモデル用deviceQuery
  - `rocm-smi`: AMD ROCm SMI
  - `rocminfo`: AMD ROCm情報
  - `setDevice`: デバイス設定ツール

## 9. 設定ファイル

### 9.1 ~/.glsconfig

`setDevice`コマンドで生成される設定ファイル：

```
[選択されたGPUのインデックス]
[選択されたGPUの名前]
```

## 10. 出力ファイル

### 10.1 CSV/HTMLエクスポート

`gls --csv`コマンドで以下のファイルが生成される：

- `/tmp/gls.cache/output.csv`: CSV形式のGPUデータ
- `/tmp/gls.cache/output.html`: HTML形式のGPUデータ

## 11. 技術的詳細

### 11.1 データ処理

- **pandas DataFrame**: GPUデータの操作と変換に使用
- **データ整形**: `change_df()`関数で列の並び替え、フォーマット、ソートを実行
- **表示整形**: `set_title_colored()`, `set_title_underline()`, `apply_row_colors()`で視覚的な整形

### 11.2 カラー出力

- **colorama**: クロスプラットフォーム対応のカラー出力ライブラリ
- **ANSIエスケープシーケンス**: カラーコードの処理と除去

### 11.3 バージョン管理

- **__init__.py**: `__version__`変数でバージョン情報を保持
- **setup.py**: 正規表現でバージョン情報を取得（exec()は使用しない）

## 12. 拡張性

### 12.1 新しいGPUの追加

1. `database.py`の`gpu_data`リストに新しいGPUエントリを追加
2. 必要に応じて、対応する`*_smi.py`と`*_deviceQuery.py`ファイルを作成
3. `setup.py`の`entry_points`に新しいコマンドを追加

### 12.2 新しいコマンドの追加

1. 新しいモジュールファイルを作成
2. `main()`関数を実装
3. `setup.py`の`entry_points`に追加

## 13. 制限事項と注意点

### 13.1 データの正確性

- 一部のGPUデータは「カタログ情報のみ」とマークされており、実機検証が必要
- `hints`フィールドに「Only from catalog brochure. Get real hardware!」と記載されているものがある

### 13.2 シミュレーターの制限

- GPUデバイスシミュレーターファイルは固定出力を返すのみ
- 実際のハードウェア状態を反映しない

### 13.3 プラットフォーム対応

- 主にLinux環境を想定（Ubuntu >= 20.04）
- Windowsでも動作するが、一部機能が制限される可能性がある

## 14. 今後の拡張予定

- より多くのGPUモデルの追加
- 実機検証データの追加
- パフォーマンス比較機能の強化
- グラフ表示機能の追加
- API化によるプログラムからの利用
