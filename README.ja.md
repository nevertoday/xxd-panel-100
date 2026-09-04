<div align="center">

# 🦁 XXD Panel 100｜民芸物語絵

### 写真を粒子と生活感のある稚拙な民藝物語へ

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-000000?style=flat-square)](./SKILL.md)
[![Modes](https://img.shields.io/badge/Modes-4-EF805E?style=flat-square)](#)
[![Output](https://img.shields.io/badge/Output-PNG-4AA1AE?style=flat-square)](#)

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <strong>日本語</strong> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## 作例展示

**16:9 横長・左右構成の作例**

| sample-05 | sample-06 |
|---|---|
| ![sample-05](assets/examples/sample-05.png) | ![sample-06](assets/examples/sample-06.png) |
| ![sample-07](assets/examples/sample-07.png) | ![sample-08](assets/examples/sample-08.png) |

**3:4 縦長・上下構成の作例**

| sample-09 | sample-10 |
|---|---|
| ![sample-09](assets/examples/sample-09.png) | ![sample-10](assets/examples/sample-10.png) |
| ![sample-11](assets/examples/sample-11.png) | ![sample-12](assets/examples/sample-12.png) |

`sample-01`–`sample-04` は、検証可能なオリジナル公開作例のために確保しています。上の8点は、16:9の横長・左右構成4点と、3:4の縦長・上下構成4点です。すべて Panel 100 が自身の原文プロンプトに基づいて個別に生成したもので、別番号の作品は流用していません。作例のコピーは英語で自動生成しています。

<!-- xxd-human-intro:start -->
## このスタイルが解決すること

**Panel 100** は写真の主体、動作、関係を稚拙なシルエット、primitive forms、少数の民藝記号へ凝縮します。クレヨン、オイルパステル、粗い鉛筆の粒子を残し、写真の最も生命的な色を明快な限定色へ再編します。

### 向いている用途

- 写真の主体、動作、関係を少数の形にしても物語を保ちたい場合
- primitive なシルエット、平面的遠近、クレヨンやオイルパステルの粒子を求める場合
- 元写真由来の明るい限定色、民藝記号、暖かな紙白を生かしたい場合
- 上下・左右・デザインのみ・複数比率・壁紙・フォルダ一括処理

### すぐ試す

> この画像を XXD Panel 100 で処理し、最適な構図とサイズを先に提案してください。

<!-- xxd-human-intro:end -->

## 原文プロンプト · 5言語

[简体中文](references/original-prompt/zh-CN.md) · [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

中国語ファイルが逐語の原文であり、実行時の唯一の創作権威です。他4言語は忠実な読解訳で、生画像プロンプトを書き換えません。

**特徴：** 稚拙な民藝物語 · primitive forms · flattened perspective · クレヨン粒子 · 限定色 · 民藝編集文字

<!-- xxd-panel-benefit:start -->
## すぐ分かる適性

| 確認したいこと | このスタイルの答え |
|---|---|
| **得られるもの** | 粗いシルエット、手作業の粒子、日常物語が一体になった民藝編集ポスター |
| **識別しやすい特徴** | primitive forms、平面空間、クレヨン粒子、暖白紙、少量の差し色、民藝文字 |
| **入力の尊重** | 同一性、姿勢、物語を保ち、不要部分を省き、輪郭フィルターにはしない |
| **用途** | アートポスター、表紙、SNS、デザイン単体、複数比率、四端末壁紙 |
<!-- xxd-panel-benefit:end -->

## 変換ロジック

```text
主体と関係を読む → 複雑な背景を削除 → 稚拙なシルエットと primitive forms に圧縮 → flattened perspective で物語を再構成 → 元写真の鮮やかな少数色を抽出 → 乾性画材の粒子と民藝文字で完成
```

## 完成作の特徴

- 簡略シルエットと大きな primitive forms が主体の同一性と物語を保ちます。
- 暗部は均一に塗らず、擦れ、重ね、断裂、紙の透けを残します。
- 暖白紙と暗いシルエットに、元写真由来の少数の鮮やかな差し色を組み合わせます。
- 文字は看板、メニュー、メモ、出版注記のように物語へ入ります。
- 児童カートゥーン、可愛いステッカー、写実、滑らかなベクター、複雑遠近、3D、テンプレートを避けます。

美的制約は[原文プロンプト](references/original-prompt/zh-CN.md)だけにあります。Skill と実行アダプターは納品変数のみを扱います。 [Skill](SKILL.md) · [英語実行アダプター](references/xxd-panel-100-prompt.en.md)

<details>
<summary><strong>全機能と引数（必要なときに開く）</strong></summary>

## 原文プロンプトを唯一の美的基準にする

`references/original-prompt/zh-CN.md` が、このプロジェクト唯一の創作・美的基準です。Skill は原文を要約・拡張せず、共通の配色計画、美的動機、タイトル、マイクロコピーを追加しません。色、素材、構図、余白、言葉、タイポグラフィは、GPT Image 2 が原文プロンプトの規則どおりに実行します。

モードとサイズは、原文の変換美学を変えずに、旧来の 3:4 上下出力コンテナを完全に置き換えます。各成果物では選択された一つのモード契約だけを GPT Image 2 に送り、四つの候補を一つの汎用テンプレート内で解釈させません。

## 組み合わせ可能な4つの出力

`top-bottom`、`left-right`、`design-only`、`wallpaper-pack` は単独でも複数でも選べます。複数選択時も、各モードを独立したプロンプトで別々に生成します。

- `top-bottom`：現実画像を上、デザイン変換を下に置く一枚の完成キャンバス。
- `left-right`：上端から下端まで左右構造を保ち、元画像を左、デザインを右に配置します。文字もその構造内に統合し、幅は非対称でも構いません。
- `design-only`：元画像は不可視の参照に限定し、見える要素はすべて当該 Panel のデザイン変換言語に従います。
- `wallpaper-pack`：各端末用にデザイン変換のみの壁紙を独立再構成します。

境界線、中央比率、ピクセル座標は測定しません。決定論的な合成は、ユーザーが正確な分割または元写真のピクセル保持を明示した場合だけ使います。

通常サイズも複数選択できます：自動適応、元画像比率、1:1、3:4、4:3、4:5、5:4、2:3、3:2、9:16、16:9、21:9、5:7、7:5、カスタム比率／正確なピクセル。暗黙の既定サイズはありません。異なる比率は、同じ原文プロンプトから個別に再構成します。

壁紙セットは連動型または独立型。連動型は最初の一枚を基準画像とし、残りを元写真＋基準画像から各端末向けに再構成します。一枚を四サイズへ機械的に切り抜くことはありません。

各呼び出しではタスクディレクトリを一つだけ作り、最終 PNG をすべてその直下へ保存します。元画像、モード、サイズ、端末ごとのサブフォルダーは作らず、元画像の順序と安全化した名前を含む `source-001-street-left-right-3x2-2160x1440.png` や `source-001-street-wallpaper-linked-phone-1440x3200.png` のようなファイル名で識別します。

画像フォルダーを直接渡すと、この兵士 Skill が同じ Panel 100 の原文美学で一括処理します。一般的なラスター形式を既定で再帰検索し、件数を報告してから、モード・サイズ・文字・言語を一度だけ確認します。各画像は内容や文言を混ぜず独立生成し、バッチ全体は一つのフラットなタスクフォルダーへ保存します。個別の失敗は記録し、後続画像を黙って省略しません。

## 文字モード

生成前に次の一つを選びます。

1. **原文プロンプトに従ってモデルが文字を生成**：ユーザーは言語・地域だけを指定し、内容、量、調子、組版は GPT Image 2 が原文どおりに生成します。表示される言葉は現在の画像の内容、空気感、または暗示から生まれ、事実・資料として見える情報には、ユーザー提供・画像内で確認可能・検証済みの根拠が必要です。
2. **自分の正確な文言を使う**：一字一句そのまま渡し、書き換え・翻訳・タイトル追加をしません。組版は原文に従います。
3. **文字なし**：文字と疑似文字を厳格に禁止します。

外側の Skill はタイトルやマイクロコピーを先に書きません。出力言語は操作言語と別に確認し、人物、風景、ファイル名から推測しません。

## 完成キャンバス優先とラスター境界

画像モデルが完成画面全体の美的再構成を担当し、二連レイアウトも完成キャンバス一枚の直接生成を既定とします。`scripts/compose_panel.py` は条件付きの復旧、無劣化ピクセル調整、読み取り専用監査にだけ残し、毎回の事前計画や美的評価には使いません。

納品物はすべてPNGラスターで、呼び出しごとに `~/Desktop/xxd/` に新規タスクを作ります。設定済み画像経路は匿名化された状態だけを返し、提供元、接続先、認証情報、ヘッダー、プロンプト、応答、アカウント情報を公開しません。SVG、HTML、Canvas、図解、プログラム描画は最終作品の代替になりません。

## 宿主能力に適応する質問とインライン引数

同じ Skill が、宿主に実在する対話機能へ適応します。装飾記号をクリック可能な UI のようには見せません。

- **Claude Code に `AskUserQuestion + multiSelect: true` がある場合**：モードとサイズは本物のチェックボックス、文字方式と壁紙関係は単一選択。一般サイズは正方形・縦・横のグループに分け、選択を累積し、カスタム値は自由入力します。
- **Codex に `request_user_input` しかない場合**：文字方式や壁紙関係など、相互排他的な項目だけに使います。モードやサイズを単一選択に見せかけず、組み合わせ入力で受け取ります。
- **対話ツールがない場合**：1回目にモード、2回目にサイズ＋文字方式を入力します。偽の `- [ ]` は表示せず、フォームのためだけに Plan mode への切り替えも求めません。

2回目は最初に「自動推薦／元画像比率／一般比率／カスタム」だけを表示します。一般比率を選んだときだけ、正方形 `1:1`、縦 `3:4、4:5、2:3、9:16、5:7`、横 `4:3、5:4、3:2、16:9、21:9、7:5` を展開します。複数比率と正確なピクセルを指定できます。

すべての設定はインラインでも指定できます。

```text
/xxd-panel-100 photo.jpg --mode top-bottom,design-only --size auto,3:4,9:16 --text prompt --locale ja-JP
```

`--mode`、複数指定可能な `--size`、`--text prompt|exact|none`、`--locale`、`--copy`、`--wallpaper linked|independent`、`--wallpaper-size`、`--out`、`--prefs` に対応します。必要な値が揃っていれば質問を省略し、不足分だけを尋ねます。

### 前回の設定を引き継ぐ、または新しく設定する

有効な履歴があり、今回の納品設定が未解決の場合、前回のモード、サイズ、文字と言語、壁紙関係、出力先を要約し、**そのまま引き継ぐ**、**引き継いで変更する**、**新しく設定する**の3択を提示します。今回明示された要件が常に優先され、必要なパラメータが揃っている場合は余分な質問をしません。

`--prefs last|edit|new|off|clear` で動作を直接指定できます。

```text
/xxd-panel-100 photo.jpg --prefs last
/xxd-panel-100 photo.jpg --prefs edit
/xxd-panel-100 photo.jpg --prefs new
```

保存するのは納品設定だけです。元画像、正確な文案、生成結果、Panel 選択、モデル経路、API 認証情報などの機密情報は保存しません。

`photo.jpg` を画像フォルダーのパスへ置き換えると自動で一括処理に入り、別の `--batch` 指定は不要です。

### パラメータ早見表

| パラメータ | 用途 | 主な値・形式 |
|---|---|---|
| `--mode` | 一つ以上の完成形式を選ぶ | `top-bottom`、`left-right`、`design-only`、`wallpaper-pack` |
| `--size` | 通常モードの比率・正確なピクセルを複数指定 | `auto`、`source`、`3:4`、`9:16`、`2160x3840` |
| `--text` | 表示文字の生成方法 | `prompt`、`exact`、`none` |
| `--locale` | 表示文字の言語・地域 | `zh-CN`、`en-GB`、`ja-JP`、`ko-KR`、`ar-SA` |
| `--copy` | 文言をそのまま渡し、`--text exact` を有効化 | `--copy "正確な文言"` |
| `--wallpaper` | 4端末壁紙の関係 | `linked`、`independent` |
| `--wallpaper-size` | 端末別に壁紙ピクセルを上書き | `phone=...`、`ipad=...`、`desktop=...`、`watch=...` |
| `--out` | 出力ルートを指定し、新規タスクフォルダーを作る | フォルダーパス |
| `--prefs` | 前回設定の継承・編集・新規設定・無効化・消去 | `last`、`edit`、`new`、`off`、`clear` |

`photo.jpg` はローカルパス、アップロード画像、画像フォルダー、またはユーザーが明示した別の入力へ置き換えられます。フォルダーは自動で一括処理になります。

### 用途別コピー用コマンド

```text
# 上下比較：キャンバスは自動推薦、文字は日本語
/xxd-panel-100 photo.jpg --mode top-bottom --size auto --text prompt --locale ja-JP

# 左右比較：3:2 横長、文字なし
/xxd-panel-100 photo.jpg --mode left-right --size 3:2 --text none

# デザインのみ：9:16 スマートフォン縦長、日本語文字
/xxd-panel-100 photo.jpg --mode design-only --size 9:16 --text prompt --locale ja-JP

# 連続性のある4端末壁紙：基準画像から各端末へ再構成
/xxd-panel-100 photo.jpg --mode wallpaper-pack --wallpaper linked --text none

# 独立壁紙：端末ごとの正確な解像度を指定
/xxd-panel-100 photo.jpg --mode wallpaper-pack --wallpaper independent --wallpaper-size phone=1440x3200,ipad=2048x2732,desktop=3840x2160,watch=1024x1024 --text none

# 元画像の比率に合わせる
/xxd-panel-100 photo.jpg --mode design-only --size source --text none

# 正方形・縦・横を個別生成
/xxd-panel-100 photo.jpg --mode design-only --size 1:1,3:4,16:9 --text none

# カスタム比率と正確なピクセルを同時指定
/xxd-panel-100 photo.jpg --mode design-only --size 11:14,2160x3840,3840x2160 --text none

# 原文プロンプトに文言を生成させ、言語だけを指定
/xxd-panel-100 photo.jpg --mode design-only --size 3:4 --text prompt --locale ja-JP

# 正確な文言を、書き換え・翻訳・タイトル追加なしで使用
/xxd-panel-100 photo.jpg --mode design-only --size 3:4 --copy "光をここに残す" --locale ja-JP

# 2モード × 3サイズで独立した完成構図を6枚生成
/xxd-panel-100 photo.jpg --mode top-bottom,design-only --size 1:1,3:4,9:16 --text prompt --locale ja-JP

# フォルダー全体へ Panel 100 を適用し、共通設定は一度だけ解決
/xxd-panel-100 "/path/to/photos" --mode design-only --size auto,9:16 --text prompt --locale ja-JP

# 繰り返しパラメータも累積し、指定ルート下へ出力
/xxd-panel-100 photo.jpg --mode top-bottom --mode left-right --size 3:4 --size 16:9 --text none --out ./deliveries
```

## 画像モデルの優先順位

GPT Image 2 を既定の第一候補とします。高忠実度の参照画像、生成前の完成キャンバス確認、二連モードの完成画面一括生成、条件を満たした場合だけのスクリプト合成という既存の流れは変わりません。

現在のツールまたは設定済み経路から実際に利用でき、元画像の忠実度、完成画角、対象言語の文字、連動壁紙の複数参照を満たせる場合は、Seedance 5.0 Pro、Nano Banana Pro（Gemini Image Pro）、Nano Banana 2（Gemini Image Flash）、その他の互換ビットマップモデルも利用できます。代替モデルが変更できるのは生成経路だけで、モード、画角、文案、言語、壁紙関係、完成キャンバス優先の方針は変更できません。

適切な経路がない場合は、画像生成ツールを有効にするか API Key を提供するようユーザーに案内します。ユーザーが提供した認証情報は現在のタスクで利用できますが、返信やログに再表示・記録・開示しません。明示的な依頼がない限り、長期保存やプロバイダー、アカウント、課金、グローバル経路の設定変更も行いません。

</details>

## 使い始める

```bash
git clone https://github.com/nevertoday/xxd-panel-100.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-100" ~/.codex/skills/xxd-panel-100
```

`npx skills` でも直接インストールできます：

```bash
npx skills add https://github.com/nevertoday/xxd-panel-100 --skill xxd-panel-100
```

このコマンドは GitHub からリポジトリを取得し、同名の Skill を現在の Agent にインストールします。ユーザー単位の Codex Skills ディレクトリへ入れる場合は、末尾に `--global --agent codex --yes` を追加してください。

Claude Code では同じフォルダを次へリンクできます： `~/.claude/skills/xxd-panel-100`. インストール後に Agent セッションを再起動してください。

```text
$xxd-panel-100
Use this photograph, ask me for the modes and copy setting, then generate fresh raster outputs.
```

完全仕様: [Skill ワークフロー](SKILL.md) · [原始スタイル資料](references/original-prompt/zh-CN.md) · [英語ランタイムアダプター](references/xxd-panel-100-prompt.en.md) · [中国語ランタイムアダプター](references/xxd-panel-100-prompt.zh-CN.md)

<!-- xxd-panel-catalog:start -->
## XXD Panel 全プロジェクト一覧

100 個の Panel は、それぞれ独立した原文プロンプトと美的ロジックを保持しています。表には 001 から 100 までを欠番なく掲載し、現在のプロジェクトを太字で示します。

| プロジェクト | スタイル特性 |
|---|---|
| [xxd-panel-001](https://github.com/nevertoday/xxd-panel-001) | 素朴な線 · レトロな紙肌 · 混合画材 · 気の利いた比喩 · 温かな余白 |
| [xxd-panel-002](https://github.com/nevertoday/xxd-panel-002) | 物語る輪郭 · ためらう線 · 類似色 · 部分拡大 · 版ずれ文字 |
| [xxd-panel-003](https://github.com/nevertoday/xxd-panel-003) | 連続する黒線 · 公共的主題 · 力点 · 沈黙の余白 · 解放 |
| [xxd-panel-004](https://github.com/nevertoday/xxd-panel-004) | 土地の現実 · 精密な単線 · 幾何学的遠近 · 主題色 · 都市ブランド文字 |
| [xxd-panel-005](https://github.com/nevertoday/xxd-panel-005) | 鈍い大形 · 暗い構造場 · 部分的な露出 · 三層の色秩序 · シルクスクリーン × パステル |
| [xxd-panel-006](https://github.com/nevertoday/xxd-panel-006) | 主体 10〜20% · 紙の余白 80〜90% · 細い手描き線 · 4色以内 · アクリル平塗り |
| [xxd-panel-007](https://github.com/nevertoday/xxd-panel-007) | 実物小図 · 接写／断面／反復 · ずれた余白 · 細い黒手書き · スキャン紙感 |
| [xxd-panel-008](https://github.com/nevertoday/xxd-panel-008) | 正投影アイソメトリック · 足場／階段／門 · 空間パラドックス · 動的パステル · マット 3D |
| [xxd-panel-009](https://github.com/nevertoday/xxd-panel-009) | 小さな主役 · 大きな余白 · 一つの空間関係 · 特色印刷 · ハーフトーン・シルクスクリーン |
| [xxd-panel-010](https://github.com/nevertoday/xxd-panel-010) | 粗い黒シルエット · 内側の白い特徴 · 乾式画材と紙目 · 最小限の環境記号 · 絵本の小文字 |
| [xxd-panel-011](https://github.com/nevertoday/xxd-panel-011) | 一つの核となる像 · 一組の関係 · 連続する黒線 · 能動的な余白 · 一点の記憶色 |
| [xxd-panel-012](https://github.com/nevertoday/xxd-panel-012) | 高密度の集積 · 外周への希薄化 · 幾何学的な制御 · 一つの生命色 · 黒灰のマイクロタイプ |
| [xxd-panel-013](https://github.com/nevertoday/xxd-panel-013) | 横長チケット一枚 · 74/26 分割 · 癒やし系水彩 · 象牙色の余白 · 現地語の情報スタブ |
| [xxd-panel-014](https://github.com/nevertoday/xxd-panel-014) | 折りと切面 · 重層と入れ子 · 元写真の重心 · 本物の紙繊維 · 読める紙文字 |
| [xxd-panel-015](https://github.com/nevertoday/xxd-panel-015) | 分解—選択—凝縮—再構成 · 少数の形 · 厳密な色役割 · 象牙色の余白 · アートブックの小文字 |
| [xxd-panel-016](https://github.com/nevertoday/xxd-panel-016) | ONE SUBJECT · ONE MOTION · A LARGE FIELD OF AIR |
| [xxd-panel-017](https://github.com/nevertoday/xxd-panel-017) | 丸い形 · 粗く途切れる線 · 純色の平塗り · 明るい色面 · 軽快な非対称 |
| [xxd-panel-018](https://github.com/nevertoday/xxd-panel-018) | 一つの視覚アンカー · 少数の前中後層 · 象牙色の余白 · マット紙 · 完全なマイクロタイプ |
| [xxd-panel-019](https://github.com/nevertoday/xxd-panel-019) | RECOGNISE FIRST · REDUCE WITH INTENT · COMPOSE WITH TYPE |
| [xxd-panel-020](https://github.com/nevertoday/xxd-panel-020) | 厚塗りの島 · 立体ミニチュア · 本物のナイフ跡 · 大きな紙面余白 · 抑制された編集文字 |
| [xxd-panel-021](https://github.com/nevertoday/xxd-panel-021) | 純黒矩形 · 主体の大半は内部 · 一つだけ越境 · 揺れるコピー線 · 白いネガ形と微小な灰色面 |
| [xxd-panel-022](https://github.com/nevertoday/xxd-panel-022) | 純黒矩形 · 主体の大半は内部 · 一つだけ越境 · 滑らかで安定した線 · 一点だけの色 |
| [xxd-panel-023](https://github.com/nevertoday/xxd-panel-023) | 元写真が選ぶ窓 · 淡く呼吸する背景 · 柔らかな色光 · スプレー粒子 · 虚実の投影と小文字 |
| [xxd-panel-024](https://github.com/nevertoday/xxd-panel-024) | 写真的な主体 · 細長い淡色窓 · 横／縦／斜めを元写真から選択 · 東洋の余白 · 高級編集 |
| [xxd-panel-025](https://github.com/nevertoday/xxd-panel-025) | 一目で主体 · 二目で隠れた像 · 図地反転 · 2〜4色のモランディ · 物理的なシルクスクリーン |
| [xxd-panel-026](https://github.com/nevertoday/xxd-panel-026) | RECOGNISE QUIETLY · REDUCE GENTLY · LET THE PAPER BREATHE |
| [xxd-panel-027](https://github.com/nevertoday/xxd-panel-027) | 厚い乳白紙 · 浅い凸凹 · 細い線刻 · 艶消し金の焦点 · 博物館の秩序 |
| [xxd-panel-028](https://github.com/nevertoday/xxd-panel-028) | 正投影アイソメトリック · 小さな紙の基台 · 元写真由来の色 · 細い墨線 · 編集的模型 |
| [xxd-panel-029](https://github.com/nevertoday/xxd-panel-029) | 横長の色面 · 淡いワックスパステル · 粗い手漉き紙 · リソグラフの粒子 · 力の抜けた手書き文字 |
| [xxd-panel-030](https://github.com/nevertoday/xxd-panel-030) | 本物の自然素材 · 矩形色面 · 自然な越境 · 最小限の黒線 · エディトリアルな余白 |
| [xxd-panel-031](https://github.com/nevertoday/xxd-panel-031) | 一つの核心モチーフ · 元写真由来の幾何母体 · 民俗図録 · 内部の粗い印痕 · 外部の精密な秩序 |
| [xxd-panel-032](https://github.com/nevertoday/xxd-panel-032) | 図文一体 · 文字体系に忠実な字形 · 元写真の特徴を埋め込む · 光学的字間 · 上質な余白 |
| [xxd-panel-033](https://github.com/nevertoday/xxd-panel-033) | 識別できるモチーフ · 平面コラージュ · 尺度対比 · 元写真由来の鮮色 · カバー組版 |
| [xxd-panel-034](https://github.com/nevertoday/xxd-panel-034) | 小さな印影 · 2〜4色の特色 · 手彫り線 · 温かな紙 · フィールド注記 |
| [xxd-panel-035](https://github.com/nevertoday/xxd-panel-035) | 一つのブロック主体 · 元写真由来の鮮色 · マットABS · 静かな背景 · モジュラー文字 |
| [xxd-panel-036](https://github.com/nevertoday/xxd-panel-036) | 一つの関係 · 細い連続線 · 2〜4色域 · 水彩の縁 · 呼吸する余白 |
| [xxd-panel-037](https://github.com/nevertoday/xxd-panel-037) | 一枚の徽章 · 元写真のエナメル色 · 白金属縁 · 流金の細部 · 実在する短い影 |
| [xxd-panel-038](https://github.com/nevertoday/xxd-panel-038) | 元写真の布色 · ほつれた縁 · 手縫い · 能動的余白 · 隠れた感情 |
| [xxd-panel-039](https://github.com/nevertoday/xxd-panel-039) | 一図一核 · 中国の絹糸 · 針方向の層 · 清潔な地 · 東洋の余白 |
| [xxd-panel-040](https://github.com/nevertoday/xxd-panel-040) | 実在する主役 · 黒い線画の小人 · ミクロな物語 · 大きな余白 |
| [xxd-panel-041](https://github.com/nevertoday/xxd-panel-041) | テーマ比喩 · 等距秩序 · 淡い手稿 · 和色の透明感 · 東洋の余白 |
| [xxd-panel-042](https://github.com/nevertoday/xxd-panel-042) | 元の視点 · 2〜5の真の層 · 安定した基点 · 透明水彩 · 編集注記 |
| [xxd-panel-043](https://github.com/nevertoday/xxd-panel-043) | 本物の泡 · 正面フラットレイ · 元写真由来の暗色地 · 微細気泡の縁 · 静かな空間 |
| [xxd-panel-044](https://github.com/nevertoday/xxd-panel-044) | 薄層の純金 · 正面平面 · 元写真由来の暗色地 · 鎚目 · 静かな秩序 |
| [xxd-panel-045](https://github.com/nevertoday/xxd-panel-045) | 丸いモジュール · 元写真の色 · 等距奥行 · マットな触感 · 編集ミクロ組版 |
| [xxd-panel-046](https://github.com/nevertoday/xxd-panel-046) | 明るい白地 · 鮮やかな厚塗り · 微縮の実体感 · 斜めの色面 · 温かな光 |
| [xxd-panel-047](https://github.com/nevertoday/xxd-panel-047) | 等距ミニチュア · 主題的厚塗り · 実在接触 · 暖白紙 · 明るい色 |
| [xxd-panel-048](https://github.com/nevertoday/xxd-panel-048) | 透明構造 · 科学図解 · 明澄な単色 · 精密注釈 · 編集的余白 |
| [xxd-panel-049](https://github.com/nevertoday/xxd-panel-049) | 限定色木版 · 手彫りの跡 · マットな重ね刷り · 暖かな紙 · 不完全な縁 |
| [xxd-panel-050](https://github.com/nevertoday/xxd-panel-050) | 専用トラベルシーン · エアリーブルー · ミニマルなフラットベクター · 編集的余白 · 一枚ごとの固有性 |
| [xxd-panel-051](https://github.com/nevertoday/xxd-panel-051) | ミニチュア紙工芸 · 横長の浮遊景観帯 · 手仕事の証拠 · エアリーブルー · 大きな余白 |
| [xxd-panel-052](https://github.com/nevertoday/xxd-panel-052) | ペーパークラフト · 横長の浮島 · 本物の手仕事 · 空気感のある寒色ブルー · 広い余白 |
| [xxd-panel-053](https://github.com/nevertoday/xxd-panel-053) | 観察ペン線 · 透明な淡彩 · 音楽的リズム · ほぼ白い紙 · 能動的な余白 |
| [xxd-panel-054](https://github.com/nevertoday/xxd-panel-054) | 選択的記憶 · 主役 · 六枚のステッカー · マット印刷 · 空気感のある青 |
| [xxd-panel-055](https://github.com/nevertoday/xxd-panel-055) | 主体の物語 · 癒やしのパステル · 淡い油彩筆触 · 空気感のある青 · 編集的余白 |
| [xxd-panel-056](https://github.com/nevertoday/xxd-panel-056) | 核心イメージ · 巨大な余白 · 暖冷の跳色 · 稚拙な手描き · 視覚的比喩 |
| [xxd-panel-057](https://github.com/nevertoday/xxd-panel-057) | 幾何構成 · インテリジェント・モザイク · 建築図解 · アートマップ · 暖冷の色面 |
| [xxd-panel-058](https://github.com/nevertoday/xxd-panel-058) | 潜台詞の読解 · 幾何学的ミニマリズム · コンセプト風景 · 柔らかな手仕事感 · 淡い余白 |
| [xxd-panel-059](https://github.com/nevertoday/xxd-panel-059) | 手描きの物語 · 童心の比喩 · 温かな紙感 · ほのかなユーモア · 詩的な傍白 |
| [xxd-panel-060](https://github.com/nevertoday/xxd-panel-060) | 黒い主形 · 巨大な余白 · 網点消散 · 禅的思考 · 思索の断片 |
| [xxd-panel-061](https://github.com/nevertoday/xxd-panel-061) | 選択的記憶 · 3–6断片 · 切り紙色面 · Risograph · 即興編集レイアウト |
| [xxd-panel-062](https://github.com/nevertoday/xxd-panel-062) | 極細黒線 · 単一強調色 · 賢い不器用さ · 淡い紙 · 専門的余白 |
| [xxd-panel-063](https://github.com/nevertoday/xxd-panel-063) | 中心Mask · ピクセル形体 · 負形の入れ子 · 軽いglitch · 限定色 |
| [xxd-panel-064](https://github.com/nevertoday/xxd-panel-064) | 手ちぎり紙 · 古紙コラージュ · 鉛筆と墨 · タイプライター小字 · 詩的アーカイブ |
| [xxd-panel-065](https://github.com/nevertoday/xxd-panel-065) | 黒い構造線 · 元画像由来の二色線 · 版ずれ · 旧印刷リズム · 微細組版 |
| [xxd-panel-066](https://github.com/nevertoday/xxd-panel-066) | 童真的物語 · 不器用な黒線 · 3–6色平塗り · 癒やし色 · 手書き観察 |
| [xxd-panel-067](https://github.com/nevertoday/xxd-panel-067) | 固定赤青 · 手描き二色墨 · 童真ユーモア · 日常観察 · 淡い紙 |
| [xxd-panel-068](https://github.com/nevertoday/xxd-panel-068) | 経営位置 · 計白当黒 · 墨線淡彩 · 東方題跋 · 現代編集 · 清雅な余白 |
| [xxd-panel-069](https://github.com/nevertoday/xxd-panel-069) | 粗筆ウィンドウ · 鮮活な元画像色 · 繊細な輪郭 · 越境関係 · 暖白の余白 |
| [xxd-panel-070](https://github.com/nevertoday/xxd-panel-070) | 手描き輪郭 · 明るい厚塗り／半透明色面 · ミニチュア主体 · 暖白の余白 · タイプライター風編集書体 |
| [xxd-panel-071](https://github.com/nevertoday/xxd-panel-071) | 柔らかなパステル · パステルクレヨン · 水溶性色鉛筆 · 白に近い紙面 · 浮遊する記憶 · 詩的な手書き文字 |
| [xxd-panel-072](https://github.com/nevertoday/xxd-panel-072) | 半透明すりガラス窓 · 領域差ソフトフォーカス · ミニマル幾何学 · 識別輪郭 · 現代編集文字 |
| [xxd-panel-073](https://github.com/nevertoday/xxd-panel-073) | 等角投影微縮建築 · 切断立方体 · 大陸棚断面 · 合理的足場 · 白いテクスチャ紙 |
| [xxd-panel-074](https://github.com/nevertoday/xxd-panel-074) | 標準角丸正方形 · 正面擬似3D／2.5D · 元写真の魂 · 連続遮蔽 · マット彫刻 · ブランドアイコン |
| [xxd-panel-075](https://github.com/nevertoday/xxd-panel-075) | 濃色クレヨン · アイボリー手工紙 · 柔らかな不定形色面 · リソグラフ粒子 · 大きな余白 · 私的注記 |
| [xxd-panel-076](https://github.com/nevertoday/xxd-panel-076) | 粗い濃色クレヨン · 木炭 · 明るいマカロン色面 · 45%連続余白 · 天然紙 · 観察注記 |
| [xxd-panel-077](https://github.com/nevertoday/xxd-panel-077) | ミニマル紙彫刻 · 明瞭な切り紙輪郭 · 前後レイヤー · 柔らかな影 · 人間的マカロン · 旅行誌組版 |
| [xxd-panel-078](https://github.com/nevertoday/xxd-panel-078) | アイボリーコットン紙 · 深い凹圧 · 凹溝シャンパン金箔 · 繊細線形標章 · 無インク空押し · 控えめな高級感 |
| [xxd-panel-079](https://github.com/nevertoday/xxd-panel-079) | 強い幾何直線 · 自由な有機曲線 · ペン淡彩 · 未完成感 · 広い紙白 · 編集的な図文構成 |
| [xxd-panel-080](https://github.com/nevertoday/xxd-panel-080) | 柔らかな有機幾何 · デジタルガッシュ · クレヨン粒子 · 植物系配色 · 自然な比喩 · 感情の余白 |
| [xxd-panel-081](https://github.com/nevertoday/xxd-panel-081) | 均一彩色モノライン · 開いた輪郭 · 密度階層 · 2–4色特色 · リソグラフ粒子 · 私的記念叙事 |
| [xxd-panel-082](https://github.com/nevertoday/xxd-panel-082) | 不規則水彩色域 · Naïve + Wonky · Isometric／2.5D · 素朴な輪郭 · 鮮やかな色 · 立体主役 |
| [xxd-panel-083](https://github.com/nevertoday/xxd-panel-083) | Ugly-cute 落書き · Wonky 輪郭 · 制御された不正確さ · 一人のユーモア主役 · 粗いクレヨン · 少・変・不器用・正確 |
| [xxd-panel-084](https://github.com/nevertoday/xxd-panel-084) | ミニマル都市線描 · 幾何学骨格 · 密度点描 · 透視リーディングライン · 限定色 · 詩的余白 |
| [xxd-panel-085](https://github.com/nevertoday/xxd-panel-085) | 手工微縮舞台 · コレクション向け立体表紙 · 粘土とフェルト · 切り紙と糸 · マットな触感 · 芸術的余白 |
| [xxd-panel-086](https://github.com/nevertoday/xxd-panel-086) | ミッドセンチュリー・モダニズム限定色シルクスクリーン · シルエット幾何 · 2–4色特色 · ドライブラシ · 一つの焦点 · 大きな余白 |
| [xxd-panel-087](https://github.com/nevertoday/xxd-panel-087) | 実体糸の関係システム地図 · ピンの節点 · 朱色の糸 · 関係写像 · 創発幾何 · 研究壁の余白 |
| [xxd-panel-088](https://github.com/nevertoday/xxd-panel-088) | 実験的文字画像構成 · 文字即画像 · 解体組版 · ドット輪郭 · 文字密度勾配 · 視覚詩 |
| [xxd-panel-089](https://github.com/nevertoday/xxd-panel-089) | 私的生活手帳スケッチ · 一人の主役 · 少数の日常断片 · 緩い手描き線 · 水彩と色鉛筆 · 成熟した余白 |
| [xxd-panel-090](https://github.com/nevertoday/xxd-panel-090) | 図式的ビジュアル思考マップ · 概念中心 · 文字ノード · 幾何骨格 · 軌跡矢印 · 視覚記譜 · 大きな余白 |
| [xxd-panel-091](https://github.com/nevertoday/xxd-panel-091) | 単色青ペン物語スケッチ · コバルト／ペンブルー／群青／藍 · 方向ハッチング · 探索線 · 自然な紙白 |
| [xxd-panel-092](https://github.com/nevertoday/xxd-panel-092) | Expressive pen · loose contours · geometric and scribble hatching · negative-space composition |
| [xxd-panel-093](https://github.com/nevertoday/xxd-panel-093) | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| [xxd-panel-094](https://github.com/nevertoday/xxd-panel-094) | Fine pen-and-ink · selective solid black · source-derived spot colour · vast negative space · vintage book illustration |
| [xxd-panel-095](https://github.com/nevertoday/xxd-panel-095) | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| [xxd-panel-096](https://github.com/nevertoday/xxd-panel-096) | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| [xxd-panel-097](https://github.com/nevertoday/xxd-panel-097) | Mid-century vernacular commercial graphic · schematic line drawing · two-colour spot printing · functional humour |
| [xxd-panel-098](https://github.com/nevertoday/xxd-panel-098) | 擬素朴水彩絵本挿絵 · 緩い墨線 · 平面水彩／ガッシュ · 記号的造形 · 天真な遠近 · 成熟した物語構図 |
| [xxd-panel-099](https://github.com/nevertoday/xxd-panel-099) | ブランドマスコット平面ベクター · 太い黒輪郭 · 丸い幾何 · 誇張比率 · 2–4色ブランド配色 · 超大文字背景 |
| **[xxd-panel-100](https://github.com/nevertoday/xxd-panel-100)** | 稚拙な民藝感の平面物語 · primitive forms · 簡略シルエット · flattened perspective · クレヨン／オイルパステル粒子 · 暖白紙 · 鮮やかな限定色 |
<!-- xxd-panel-catalog:end -->

## XXD について

XXD は Xiaoxiaodong のブランド名略称です。作成・管理： [@xiaoxiaodong01](https://x.com/xiaoxiaodong01).

## サポートとメンバーシップ

### Xiaoxiaodong 総控 · 将軍総指揮 Skill · CNY 100

CNY 100 の一回払いで、このシリーズの将軍総指揮 Skill（`xxd-panel-all`）を利用できます。全兵士 Skills の統括、推薦、指名派遣、一括調整に対応します。WeChat では「将軍総指揮 Skill」と記載してください。

<!-- xxd-panel-command-system:start -->
**購入後に利用可能：全隊を指揮する「将軍 Skill」**

| 階級 | Skill | 担当 |
|---|---|---|
| **将軍級** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 利用可能な番号付き Skills の検出、画像・テーマ・用途からの推薦、番号指定の派遣、同一素材の複数スタイル試作、フォルダー画像の一括割り当てと個別派遣。 |
| **兵士級** | `xxd-panel-NNN`（現在 001–100） | 各番号が固有の原文プロンプトと美学だけを実行し、将軍から渡された一つの仕事を完成させます。 |

将軍 Skill は、番号付き Skills 全隊の司令塔です。購入後すぐに利用でき、インストール、更新、編成、派遣方法についてサポートを受けられます。将軍は整理と派遣だけを担当し、兵士の原文美学を改変・混合・上書きしません。各完成作品は、選ばれた兵士 Skill が独立して制作します。
<!-- xxd-panel-command-system:end -->

### 知識星球＋会員プロンプトライブラリ＋全将軍 Skills 会員 · 年額 CNY 699

[知識星球](https://wx.zsxq.com/group/15554814142882)、[XXD 会員プロンプトライブラリ](https://vip.xiaoxiaodong.ai/)、全将軍 Skills 会員は同じ会員権です。**一度の年額決済で3つの特典をすべて利用でき、二重の購入は不要です。**

[Knowledge Planet](https://wx.zsxq.com/group/15554814142882) · [Member Prompt Library](https://vip.xiaoxiaodong.ai/)

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="XXD WeChat" width="280"></a></p>

<div align="center"><strong>筆触を少し止め、色を少しずらし、感情を残す。</strong></div>

---

<div align="center">

## ☕ オープンソースを支援

> **広告表示：** このセクションのQRコードおよび有料会員・サービスのリンクはXXDのプロモーション情報です。スキャンや購入は任意であり、オープンソースの利用には影響しません。

このプロジェクトが役に立ったら、Buy Me a Coffee から任意で応援していただけます。


<p align="center"><a href="https://github.com/nevertoday/zhongguo-traditional-colors/blob/main/docs/images/buy-me-a-coffee-qr.png?raw=true"><img src="https://github.com/nevertoday/zhongguo-traditional-colors/blob/main/docs/images/buy-me-a-coffee-qr.png?raw=true" alt="Buy Me a Coffee" width="180"></a></p>

</div>

## ライセンス

本プロジェクト（Skill、プロンプト、スクリプト、ドキュメント、付属サンプルを含む）は **PolyForm Noncommercial License 1.0.0** で提供されます。完全な法的条文は [LICENSE](LICENSE) に、公式ページは <https://polyformproject.org/licenses/noncommercial/1.0.0> にあります。

かんたんに言うと：

- 個人の学習・研究・実験・テスト・趣味・私的な娯楽に利用できます。慈善団体、教育機関、公的な研究／安全／保健機関、環境保護団体、政府機関も利用できます。
- **非営利目的**であれば、使用、複製、改変、派生物の作成、共有ができます。共有時は、このライセンス（または上記 URL）と、作者が示したすべての `Required Notice:` 行を添えてください。
- 商用製品・サービス、対価を受ける納品、アクセス権やライセンスの販売、商用利用を予定した用途は禁止です。商用利用には著作権者から別途書面で許可を得てください。
- 明記された著作権と限定的な特許権だけが許諾されます。商標・ブランド名など、明記されていない権利は与えられず、ライセンスの再許諾・譲渡もできません。
- 違反の書面通知を受けた場合、32 日以内に完全な遵守と実際の是正を行わなければライセンスは終了します。特許侵害を主張する書面を提出した場合も特許ライセンスは終了します。
- 本プロジェクトは**現状有姿**で提供され、法律の許す範囲で保証はありません。利用と結果のリスクは利用者が負います。
