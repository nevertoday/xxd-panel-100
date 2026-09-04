<div align="center">

# 🦁 XXD Panel 100｜民艺叙事画

### 把照片提炼成有颗粒、有生活感的稚拙民艺叙事


<strong>简体中文</strong> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## 样张展示

**16:9 横版左右样张**

| sample-05 | sample-06 |
|---|---|
| ![sample-05](assets/examples/sample-05.png) | ![sample-06](assets/examples/sample-06.png) |
| ![sample-07](assets/examples/sample-07.png) | ![sample-08](assets/examples/sample-08.png) |

**3:4 竖版上下样张**

| sample-09 | sample-10 |
|---|---|
| ![sample-09](assets/examples/sample-09.png) | ![sample-10](assets/examples/sample-10.png) |
| ![sample-11](assets/examples/sample-11.png) | ![sample-12](assets/examples/sample-12.png) |

以上八张包括四张 16:9 横版左右样张和四张 3:4 竖版上下样张，均由 Panel 100 依据自己的原始提示词独立生成，不借用其他编号作品。样张使用英文智能配字。

<!-- xxd-human-intro:start -->
## 适用场景与解决的问题

**Panel 100** 把照片中最值得记住的主体、动作和关系，提炼成稚拙剪影、primitive forms 与少量民艺符号。蜡笔、油画棒和粗铅笔留下真实颗粒，照片中最鲜活的颜色则被重新组织成明快而克制的限制性色彩。

### 适合这些情况

- **想保留故事而不是描摹照片：** 删除复杂背景，只留下一个核心动作、关系或场景。
- **需要真实手工触感：** 黑色剪影保留擦拭、叠涂、断裂和纸张透底，不做光滑数字矢量。
- **想要鲜活但不廉价的颜色：** 从原图挑选最有生命力的少量色彩，以暖白纸面和深色剪影稳定画面。
- **需要灵活交付：** 支持上下、左右、纯设计、多比例和四端壁纸，也能批量处理图片目录。

### 快速开始

发送一张图片给 Agent，并说明：

> 用 XXD Panel 100 帮我处理这张图，先推荐最合适的构图和尺寸。

<!-- xxd-human-intro:end -->

## 原始提示词 · 五种语言

[简体中文](references/original-prompt/zh-CN.md) · [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

简体中文文件逐字保存用户提供的原文，并且是运行时唯一创作与审美权威；其他四个版本是忠实阅读译文，不会反过来改写生图提示词。

**关键词：** Naïve folk narrative · primitive forms · flattened perspective · crayon grain · limited colour · folk editorial type

<!-- xxd-panel-benefit:start -->
## 快速判断：XXD Panel 100 适合你吗？

| 你关心的问题 | 这套风格给你的回答 |
|---|---|
| **你会得到什么** | 一张以朴拙剪影、手工颗粒和生活叙事共同成立的民艺编辑海报 |
| **一眼可辨的特点** | primitive forms、平面空间、蜡笔颗粒、暖白纸面、少量跳色与民艺文字 |
| **它如何尊重你的输入** | 保留主体、姿态与故事关系，只删除冗余细节，不擅自改写原图的核心叙事 |
| **可以用在哪里** | 艺术海报、封面、社交内容、纯设计图、多比例成品和四端壁纸 |
<!-- xxd-panel-benefit:end -->

## 它如何把你的输入变成独特成品

```text
辨认主体与叙事关系 → 删除复杂背景 → 压缩成稚拙剪影与 primitive forms → 用 flattened perspective 重组故事 → 从原图提炼少量鲜活颜色 → 以蜡笔颗粒和民艺文字完成编辑叙事
```

## 成品中最容易识别的风格特点

- 简化剪影与大块 primitive forms 保留身份，允许适度压缩比例和夸张特征。
- 黑色和深色不均匀填满，保留擦拭、摩擦、断裂、叠涂与纸张透底。
- 暖白纸面与深色剪影稳定结构，少量照片来源的鲜活跳色承担叙事焦点。
- 文字像招牌、菜单、便笺或出版注释一样进入画面，不形成规整商业标题栏。
- 拒绝儿童卡通、可爱贴纸、写实插画、光滑矢量、复杂透视、3D 和模板化效果。

原始审美约束与拒绝项只存在于[原始提示词](references/original-prompt/zh-CN.md)；Skill 与运行适配器只处理本次交付变量。 [Skill 工作流](SKILL.md) · [英文运行适配器](references/xxd-panel-100-prompt.en.md)

<details>
<summary><strong>完整能力与参数（需要时再展开）</strong></summary>

## 原始提示词优先，而不是二次导演

`references/original-prompt/zh-CN.md` 是本项目唯一的创作与审美权威。Skill 不再额外总结或扩写它，也不会统一规划颜色、色板、美学动机、标题或微文案。原始提示词要求怎样处理颜色、材料、构图、留白与文字，GPT Image 2 就按那套逻辑执行。

模式与尺寸会完整替换原始提示词旧有的 3:4 上下交付容器，但不改写它的转译美学。每张成品只向 GPT Image 2 发送一个已选模式的最终契约，不再把四种模式放进同一个通用模板让模型自行猜测。

## 四种可组合输出模式

模式可以单选或多选：`top-bottom`、`left-right`、`design-only`、`wallpaper-pack`；多选时，每个模式分别生成、分别拥有自己的提示词。

- `top-bottom`：整张画面由上方现实画面与下方设计转译两个主要部分组成。
- `left-right`：整张画面从顶部到底部保持完整左右结构，原图在左、设计在右；文字融入这两个区域，不再生成横跨全宽的第三块底栏。左右宽度可以不对称，由模型自主构图。
- `design-only`：原图只作为不可见的身份、结构、颜色与事实依据；整张成品的每个可见元素都必须属于该 Skill 自己的设计转译语言。
- `wallpaper-pack`：每台设备分别生成完整画布的设计转译壁纸，原图不作为照片区域出现。

上下或左右都不做分界线、中线百分比或像素坐标检测。只有用户明确要求像素级分区或原片逐像素不变时，才使用确定性拼合。

普通成品尺寸同样可以多选：自动适配、跟随原图、1:1、3:4、4:3、4:5、5:4、2:3、3:2、9:16、16:9、21:9、5:7、7:5，或自定义比例／准确像素。没有静默默认尺寸；每个不同比例都会基于同一份原始提示词独立重构。

壁纸套装可选“连贯”或“四张独立”。连贯模式先生成一张定调图，其余设备同时参考原图与定调图重新构图；不会把一张图机械裁成四种尺寸。

每次调用只建立一个任务目录，所有最终 PNG 直接放在该目录中，不再按来源、模式、尺寸或设备创建子文件夹。文件名使用 `source-序号-原文件名-模式-比例-像素.png`；壁纸额外包含连贯关系与设备，例如 `source-001-street-left-right-3x2-2160x1440.png`、`source-001-street-wallpaper-linked-phone-1440x3200.png`。

直接传入一个图片目录时，这个士兵 Skill 会自动批量处理目录中的图片，并让每张图片都使用 Panel 100 的同一套原始审美。默认递归扫描常见位图，先报告数量，再统一确认一次模式、尺寸、文字和语言；每张图片独立生成，互不借用内容或文案。整批仍然只创建一个扁平任务目录，单张失败会被记录，但不会静默跳过后续图片。

## 文字方式

正式生图前只确认三种选择：

1. **模型根据原始提示词生成文字**：用户只指定语言或地区，文字内容、数量、气质与排版由 GPT Image 2 按原始提示词生成；所有文字都从当前图片的内容、气质或隐喻中自然生长，任何事实或资料式信息都必须有用户输入、图片可见内容或已核实信息作为依据。
2. **使用我的准确文字**：逐字传给图像模型，不改写、不翻译、不补标题；排版仍遵循原始提示词。
3. **不要文字**：严格禁止文字与伪文字。

外层 Skill 不再预编标题、微文案或文案包。文字语言与操作语言分开确认，不根据人物、场景或文件名猜测国家与受众。

## 完整画布优先与位图边界

图像模型负责整张成品的审美重构，双联也默认一次直出完整画布。`scripts/compose_panel.py` 只保留为条件明确的兜底、无创尺寸校准和只读审计工具，不再预先规划每次任务，也不评价审美是否成功。

全部交付为 PNG 位图。每次调用都在 `~/Desktop/xxd/` 下创建新任务；已配置图像通道只返回脱敏状态，不公开供应商、端点、凭据、请求头、提示词、响应或账户信息。SVG、HTML、Canvas、图表和程序绘图不能替代最终作品。

## 能力自适应问询与快捷参数

同一个 Skill 会根据宿主真正提供的交互能力选择界面，不会把文本符号伪装成可点击控件：

- **Claude Code 提供 `AskUserQuestion + multiSelect: true` 时**：模式和尺寸使用真正的 checkbox；文字方式与壁纸关系使用单选。常用尺寸会按方形、竖版、横版分组展示，并累计多组选项；自定义尺寸进入自由输入。
- **Codex 只提供 `request_user_input` 时**：它只用于文字方式、壁纸关系等互斥单选，不拿来伪装模式或尺寸多选。模式与尺寸改用清楚的组合输入。
- **没有交互工具时**：使用两轮文字问询。第一轮选择一个或多个模式；第二轮填写尺寸与文字方式。Skill 不显示假的 `- [ ]`，也不会为了获得表单要求用户切换 Plan mode。

默认第二轮只展示“智能推荐／跟随原图／常用比例／自定义”四个入口；只有选择常用比例时，才展开完整比例库：方形 `1:1`，竖版 `3:4、4:5、2:3、9:16、5:7`，横版 `4:3、5:4、3:2、16:9、21:9、7:5`。所有比例都可组合，也可直接输入准确像素。

全部设置都可以直接作为参数传入：

```text
/xxd-panel-100 photo.jpg --mode top-bottom,design-only --size auto,3:4,9:16 --text prompt --locale ja-JP
```

支持 `--mode`、可重复或逗号分隔的 `--size`、`--text prompt|exact|none`、`--locale`、`--copy`、`--wallpaper linked|independent`、`--wallpaper-size`、`--out` 和 `--prefs`。参数齐全时跳过全部问询；参数不完整时只询问缺失项。

### 继承上次偏好，或全新配置

检测到历史偏好时，Skill 会先展示上次的模式、尺寸、文字与语言、壁纸关系和输出位置，再提供三个互斥选项：**直接沿用**、**沿用并修改**、**全新配置**。本次明确说出的要求始终优先；完整参数仍然直接执行。

可使用 `--prefs last|edit|new|off|clear` 直接指定行为：

```text
/xxd-panel-100 photo.jpg --prefs last
/xxd-panel-100 photo.jpg --prefs edit
/xxd-panel-100 photo.jpg --prefs new
```

偏好只保存交付设置，不保存原图、准确文案、生成结果、Panel 选择、模型通道、API 凭据或其他敏感信息。

`photo.jpg` 也可以直接替换为图片目录路径；目录输入会自动进入批量，不需要额外的 `--batch` 开关。

### 参数速查

| 参数 | 用途 | 常用值或格式 |
|---|---|---|
| `--mode` | 选择一种或多种成品用途 | `top-bottom`、`left-right`、`design-only`、`wallpaper-pack` |
| `--size` | 普通模式的比例或准确像素，可多选 | `auto`、`source`、`3:4`、`9:16`、`2160x3840` |
| `--text` | 文字来源 | `prompt`、`exact`、`none` |
| `--locale` | 画面中文字的语言或地区 | `zh-CN`、`en-GB`、`ja-JP`、`ko-KR`、`ar-SA` |
| `--copy` | 逐字使用用户文案，并启用 `--text exact` | `--copy "准确文案"` |
| `--wallpaper` | 四端壁纸之间的关系 | `linked`、`independent` |
| `--wallpaper-size` | 按设备覆盖壁纸分辨率 | `phone=...`、`ipad=...`、`desktop=...`、`watch=...` |
| `--out` | 指定输出根目录，仍会新建本次任务目录 | 文件夹路径 |
| `--prefs` | 处理上次偏好或关闭本次记忆 | `last`、`edit`、`new`、`off`、`clear` |

`photo.jpg` 可以替换为本地图片路径、已上传图片、图片目录或用户明确给出的其他来源。目录会自动进入批量处理。

### 按用途复制命令

```text
# 上下对照：智能推荐画幅，模型按原始提示词生成简体中文文字
/xxd-panel-100 photo.jpg --mode top-bottom --size auto --text prompt --locale zh-CN

# 左右对照：3:2 横版，无文字
/xxd-panel-100 photo.jpg --mode left-right --size 3:2 --text none

# 只要设计图：9:16 手机竖版，日语文字
/xxd-panel-100 photo.jpg --mode design-only --size 9:16 --text prompt --locale ja-JP

# 四端连贯壁纸：先建立一张定调图，再按设备分别重构
/xxd-panel-100 photo.jpg --mode wallpaper-pack --wallpaper linked --text none

# 四张独立壁纸：同时指定四台设备的准确分辨率
/xxd-panel-100 photo.jpg --mode wallpaper-pack --wallpaper independent --wallpaper-size phone=1440x3200,ipad=2048x2732,desktop=3840x2160,watch=1024x1024 --text none

# 跟随原图比例
/xxd-panel-100 photo.jpg --mode design-only --size source --text none

# 同一用途生成方形、竖版和横版三种完整构图
/xxd-panel-100 photo.jpg --mode design-only --size 1:1,3:4,16:9 --text none

# 自定义比例与准确像素可以一起多选
/xxd-panel-100 photo.jpg --mode design-only --size 11:14,2160x3840,3840x2160 --text none

# 模型依照原始提示词决定文字，只限定语言
/xxd-panel-100 photo.jpg --mode design-only --size 3:4 --text prompt --locale en-GB

# 使用准确文案，不改写、不翻译、不补标题
/xxd-panel-100 photo.jpg --mode design-only --size 3:4 --copy "让风经过这里" --locale zh-CN

# 两种模式 × 三种尺寸，共生成六张独立完整构图
/xxd-panel-100 photo.jpg --mode top-bottom,design-only --size 1:1,3:4,9:16 --text prompt --locale zh-CN

# 整个目录统一使用 Panel 100；公共设置只解析一次
/xxd-panel-100 "/path/to/photos" --mode design-only --size auto,9:16 --text prompt --locale zh-CN

# 重复参数也会累积，并把本次任务放到指定根目录
/xxd-panel-100 photo.jpg --mode top-bottom --mode left-right --size 3:4 --size 16:9 --text none --out ./deliveries
```

## 生图模型优先级

GPT Image 2 是默认首选，并继续执行本项目现有的高保真垫图、生成前确认整张画幅、双联一次生成完整画布、脚本仅作条件式兜底等逻辑。

当当前工具或已配置兼容通道确实可用，并能满足原图保真、整张成品比例、目标语言文字和连贯壁纸多图参考等要求时，也支持 Seedance 5.0 Pro、Nano Banana Pro（Gemini Image Pro）、Nano Banana 2（Gemini Image Flash）或其他兼容位图模型。备用模型只替换生成通道，不得改变模式、画幅、文案、语言、壁纸关系和完整画布优先策略。

如果没有合适的生图通道，Skill 会请用户启用生图工具或提供 API Key。用户主动提供的凭据可以用于当前任务，但不得在回复或日志中回显、展示或泄露；未经用户明确要求，不会长期保存凭据或修改供应商、账户、计费及全局路由配置。

</details>

## 开始使用

```bash
git clone https://github.com/nevertoday/xxd-panel-100.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-100" ~/.codex/skills/xxd-panel-100
```

也可以直接使用 `npx skills` 安装：

```bash
npx skills add https://github.com/nevertoday/xxd-panel-100 --skill xxd-panel-100
```

该命令会从 GitHub 获取仓库，并把同名 Skill 安装到当前 Agent。若要安装到用户级 Codex Skills 目录，可在命令末尾加上 `--global --agent codex --yes`。

Claude Code 用户可把同一文件夹链接到 `~/.claude/skills/xxd-panel-100`. 安装后请重启 Agent 会话。

```text
$xxd-panel-100
Use this photograph, ask me for the modes and copy setting, then generate fresh raster outputs.
```

完整规格: [Skill 工作流](SKILL.md) · [原始风格档案](references/original-prompt/zh-CN.md) · [英文运行适配器](references/xxd-panel-100-prompt.en.md) · [中文运行适配器](references/xxd-panel-100-prompt.zh-CN.md)

<!-- xxd-panel-catalog:start -->
## XXD Panel 全系列项目

XXD Panel 当前系列已更新至 001–112；每个 Panel 仍保留独立的原始提示词与审美逻辑。下表是本项目发布时的历史目录，连续列出 001–100；当前项目以粗体标出。

| 项目地址 | 风格特点 |
|---|---|
| [xxd-panel-001](https://github.com/nevertoday/xxd-panel-001) | 稚拙线条 · 复古纸感 · 混合媒材 · 轻巧隐喻 · 暖色留白 |
| [xxd-panel-002](https://github.com/nevertoday/xxd-panel-002) | 叙事轮廓 · 迟疑手线 · 近似色调 · 局部夸张 · 套印文字 |
| [xxd-panel-003](https://github.com/nevertoday/xxd-panel-003) | 连续黑线 · 公共议题 · 受力结点 · 留白沉默 · 向外释放 |
| [xxd-panel-004](https://github.com/nevertoday/xxd-panel-004) | 在地现实 · 精准单线 · 几何透视 · 主题配色 · 城市品牌文字 |
| [xxd-panel-005](https://github.com/nevertoday/xxd-panel-005) | 钝拙体块 · 暗色结构场 · 局部显形 · 三层色阶 · 丝网印刷 × 粉蜡笔 |
| [xxd-panel-006](https://github.com/nevertoday/xxd-panel-006) | 小主体 · 80%–90% 纸面留白 · 纤细手线 · 四色以内 · 丙烯平涂 |
| [xxd-panel-007](https://github.com/nevertoday/xxd-panel-007) | 实物小图 · 局部／剖面／重复 · 错位留白 · 细黑手写 · 扫描纸感 |
| [xxd-panel-008](https://github.com/nevertoday/xxd-panel-008) | 正交等距 · 平台／台阶／门洞 · 空间悖论 · 动态粉彩 · 极净哑光 3D |
| [xxd-panel-009](https://github.com/nevertoday/xxd-panel-009) | 极小主体 · 巨大留白 · 单一空间关系 · 专色体系 · Halftone 丝网印刷 |
| [xxd-panel-010](https://github.com/nevertoday/xxd-panel-010) | 粗黑剪影 · 内部白色特征区 · 干媒介纸感 · 极少环境记号 · 童书编辑小字 |
| [xxd-panel-011](https://github.com/nevertoday/xxd-panel-011) | 一个核心意象 · 一组关系 · 连续黑线 · 主动留白 · 一抹记忆点色 |
| [xxd-panel-012](https://github.com/nevertoday/xxd-panel-012) | 高密聚合 · 外围稀释 · 几何约束 · 一种生命主线色 · 黑灰微排版 |
| [xxd-panel-013](https://github.com/nevertoday/xxd-panel-013) | 一张横向票体 · 74/26 分区 · 治愈水彩 · 象牙白留白 · 本地化信息票根 |
| [xxd-panel-014](https://github.com/nevertoday/xxd-panel-014) | 折叠与切面 · 层叠与嵌套 · 源图重心构图 · 真实纸纤维 · 可读纸艺文字 |
| [xxd-panel-015](https://github.com/nevertoday/xxd-panel-015) | 解构—筛选—提炼—重构 · 少量形体 · 严格色彩角色 · 象牙色留白 · 艺术书微排版 |
| [xxd-panel-016](https://github.com/nevertoday/xxd-panel-016) | ONE SUBJECT · ONE MOTION · A LARGE FIELD OF AIR |
| [xxd-panel-017](https://github.com/nevertoday/xxd-panel-017) | 圆润形体 · 粗糙断线 · 纯色平涂 · 明亮色场 · 轻快不对称 |
| [xxd-panel-018](https://github.com/nevertoday/xxd-panel-018) | 一个视觉锚点 · 前中后少量纸层 · 暖象牙留白 · 哑光纸触感 · 完整微排版 |
| [xxd-panel-019](https://github.com/nevertoday/xxd-panel-019) | RECOGNISE FIRST · REDUCE WITH INTENT · COMPOSE WITH TYPE |
| [xxd-panel-020](https://github.com/nevertoday/xxd-panel-020) | 厚涂颜料岛 · 立体微缩场景 · 真实刀痕 · 大面积纸面留白 · 克制编辑排版 |
| [xxd-panel-021](https://github.com/nevertoday/xxd-panel-021) | 纯黑矩形 · 主体大部入场 · 一个特征越界 · 抖动复印线 · 白色负形与微灰面 |
| [xxd-panel-022](https://github.com/nevertoday/xxd-panel-022) | 纯黑矩形 · 主体大部入场 · 一个特征越界 · 流畅稳定线 · 唯一单点彩色 |
| [xxd-panel-023](https://github.com/nevertoday/xxd-panel-023) | 源图择窗 · 浅色呼吸背景 · 柔和有色光影 · 喷绘颗粒 · 虚实投影与微排版 |
| [xxd-panel-024](https://github.com/nevertoday/xxd-panel-024) | 真实摄影主体 · 窄长浅色窗口 · 横／竖／斜向自适应 · 东方留白 · 高级商业编辑 |
| [xxd-panel-025](https://github.com/nevertoday/xxd-panel-025) | 一眼主体 · 第二眼隐藏意象 · 正负形反转 · 2–4 色莫兰迪 · 真实丝网触感 |
| [xxd-panel-026](https://github.com/nevertoday/xxd-panel-026) | RECOGNISE QUIETLY · REDUCE GENTLY · LET THE PAPER BREATHE |
| [xxd-panel-027](https://github.com/nevertoday/xxd-panel-027) | 乳白厚纸 · 浅凸浅凹 · 极简线刻 · 哑金焦点 · 博物馆展陈 |
| [xxd-panel-028](https://github.com/nevertoday/xxd-panel-028) | 正交等距 · 微缩基座 · 源图限定色盘 · 精细墨线 · 纸上编辑插画 |
| [xxd-panel-029](https://github.com/nevertoday/xxd-panel-029) | 横向色域 · 浅色蜡粉笔 · 粗纤维手工纸 · Risograph 颗粒 · 松弛手写 |
| [xxd-panel-030](https://github.com/nevertoday/xxd-panel-030) | 真实自然材料 · 矩形色域 · 自然越界 · 极少黑线 · 编辑留白 |
| [xxd-panel-031](https://github.com/nevertoday/xxd-panel-031) | 一个核心母题 · 源图几何母体 · 民俗图录 · 内部粗粝印痕 · 外部精确秩序 |
| [xxd-panel-032](https://github.com/nevertoday/xxd-panel-032) | 图文一体 · 原生文字结构 · 源图特征嵌入 · 视觉字距 · 高级留白 |
| [xxd-panel-033](https://github.com/nevertoday/xxd-panel-033) | 可识别母题 · 平面拼贴 · 尺度对比 · 源图鲜明配色 · 封面排版 |
| [xxd-panel-034](https://github.com/nevertoday/xxd-panel-034) | 小尺度章印 · 2–4 种专色 · 手刻线 · 暖色纸张 · 田野注释 |
| [xxd-panel-035](https://github.com/nevertoday/xxd-panel-035) | 单一积木主体 · 明艳源图色 · 哑光 ABS · 安静背景 · 模块文字 |
| [xxd-panel-036](https://github.com/nevertoday/xxd-panel-036) | 一个关系 · 纤细连续线 · 二至四色域 · 水彩渗化 · 柔软留白 |
| [xxd-panel-037](https://github.com/nevertoday/xxd-panel-037) | 一枚徽章 · 源图珐琅色 · 白金属外框 · 流金细节 · 实体短影 |
| [xxd-panel-038](https://github.com/nevertoday/xxd-panel-038) | 源图布色 · 真实毛边 · 手缝针脚 · 主动留白 · 隐藏情绪 |
| [xxd-panel-039](https://github.com/nevertoday/xxd-panel-039) | 一图一核 · 中国丝线 · 针向层次 · 洁净底色 · 东方留白 |
| [xxd-panel-040](https://github.com/nevertoday/xxd-panel-040) | 真实主体 · 黑线小人 · 微型叙事 · 大量留白 |
| [xxd-panel-041](https://github.com/nevertoday/xxd-panel-041) | 主题隐喻 · 等距秩序 · 淡手稿 · 日系清透色 · 东方留白 |
| [xxd-panel-042](https://github.com/nevertoday/xxd-panel-042) | 原始视角 · 二至五层 · 稳定锚点 · 透明水彩 · 编辑注释 |
| [xxd-panel-043](https://github.com/nevertoday/xxd-panel-043) | 真实皂沫 · 正面平视 · 源图深底 · 细密泡缘 · 安静空间 |
| [xxd-panel-044](https://github.com/nevertoday/xxd-panel-044) | 薄层纯金 · 正面平面 · 源图深底 · 锤纹压痕 · 安静秩序 |
| [xxd-panel-045](https://github.com/nevertoday/xxd-panel-045) | 圆润模块 · 源图色彩 · 等距纵深 · 哑光触感 · 编辑微排版 |
| [xxd-panel-046](https://github.com/nevertoday/xxd-panel-046) | 明亮白底 · 鲜活厚涂 · 微缩实体 · 斜向色带 · 温暖光感 |
| [xxd-panel-047](https://github.com/nevertoday/xxd-panel-047) | 等距微缩 · 主题厚涂 · 真实接触 · 暖白纸面 · 明亮色彩 |
| [xxd-panel-048](https://github.com/nevertoday/xxd-panel-048) | 透明结构 · 科学图解 · 清透单色 · 精确注释 · 编辑留白 |
| [xxd-panel-049](https://github.com/nevertoday/xxd-panel-049) | 限色木刻 · 手工刀痕 · 哑光套印 · 温暖纸面 · 不完整边缘 |
| [xxd-panel-050](https://github.com/nevertoday/xxd-panel-050) | 定制旅行场景 · 空气蓝 · 极简平涂矢量 · 编辑留白 · 一图一身份 |
| [xxd-panel-051](https://github.com/nevertoday/xxd-panel-051) | 微缩纸艺 · 横向悬浮景观带 · 真实手工材质 · 空气蓝 · 大量留白 |
| [xxd-panel-052](https://github.com/nevertoday/xxd-panel-052) | 纸艺微缩 · 横向浮岛 · 真实手作 · 空气感冷蓝 · 大量留白 |
| [xxd-panel-053](https://github.com/nevertoday/xxd-panel-053) | 观察线稿 · 透明淡彩 · 音乐性节奏 · 近白纸面 · 大胆留白 |
| [xxd-panel-054](https://github.com/nevertoday/xxd-panel-054) | 选择性记忆 · 主视觉 · 六枚贴纸 · 哑光印刷 · 空气感蓝 |
| [xxd-panel-055](https://github.com/nevertoday/xxd-panel-055) | 主体叙事 · 治愈粉彩 · 浅油画笔触 · 空气感蓝 · 编辑留白 |
| [xxd-panel-056](https://github.com/nevertoday/xxd-panel-056) | 核心意象 · 巨大留白 · 暖冷跳色 · 稚拙手绘 · 视觉隐喻 |
| [xxd-panel-057](https://github.com/nevertoday/xxd-panel-057) | 几何构成 · 智能马赛克 · 建筑图解 · 艺术地图 · 暖冷色块 |
| [xxd-panel-058](https://github.com/nevertoday/xxd-panel-058) | 潜台词解读 · 几何极简 · 观念景观 · 柔和手工质感 · 淡色留白 |
| [xxd-panel-059](https://github.com/nevertoday/xxd-panel-059) | 手绘叙事 · 童真隐喻 · 温暖纸感 · 轻微诙谐 · 诗性旁白 |
| [xxd-panel-060](https://github.com/nevertoday/xxd-panel-060) | 黑色主形 · 极大留白 · 网点消散 · 禅意思考 · 哲思碎片 |
| [xxd-panel-061](https://github.com/nevertoday/xxd-panel-061) | 选择性记忆 · 3–6 个片段 · 剪纸色块 · Risograph · 即兴编辑排版 · 治愈色盘 |
| [xxd-panel-062](https://github.com/nevertoday/xxd-panel-062) | 极简黑线 · 单一强调色 · 聪明笨拙 · 浅色纸底 · 专业留白 |
| [xxd-panel-063](https://github.com/nevertoday/xxd-panel-063) | 核心 Mask · 像素形体 · 负形嵌套 · 轻微 glitch · 有限色盘 · 大留白 |
| [xxd-panel-064](https://github.com/nevertoday/xxd-panel-064) | 手撕纸边 · 旧纸拼贴 · 铅笔墨线 · 打字机小字 · 档案感 · 诗性留白 |
| [xxd-panel-065](https://github.com/nevertoday/xxd-panel-065) | 黑色结构线 · 两种源图彩线 · 错位叠压 · 旧印刷节奏 · 微型排版 |
| [xxd-panel-066](https://github.com/nevertoday/xxd-panel-066) | 童真叙事 · 笨拙黑线 · 3–6 色平涂 · 治愈色彩 · 手写观察 · 大留白 |
| [xxd-panel-067](https://github.com/nevertoday/xxd-panel-067) | 固定红蓝 · 手绘双墨 · 童真幽默 · 生活观察 · 极浅纸底 · 手写短句 |
| [xxd-panel-068](https://github.com/nevertoday/xxd-panel-068) | 经营位置 · 计白当黑 · 墨线淡彩 · 东方题跋 · 现代编辑 · 清雅留白 |
| [xxd-panel-069](https://github.com/nevertoday/xxd-panel-069) | 粗笔绘画视窗 · 鲜活取色 · 纤细描边 · 越界关系 · 暖白留白 · 自由图文混排 |
| [xxd-panel-070](https://github.com/nevertoday/xxd-panel-070) | 手绘描边 · 明亮厚涂／半透明色块 · 微缩主体 · 暖白留白 · 打字机式编辑字体 |
| [xxd-panel-071](https://github.com/nevertoday/xxd-panel-071) | 柔和粉彩 · 粉蜡笔 · 水溶性色铅笔 · 近白纸面 · 漂浮记忆片段 · 诗性手写 |
| [xxd-panel-072](https://github.com/nevertoday/xxd-panel-072) | 半透明磨砂视窗 · 区域差异化柔焦 · 极简几何 · 清晰识别轮廓 · 明艳治愈色 · 现代编辑排版 |
| [xxd-panel-073](https://github.com/nevertoday/xxd-panel-073) | 等距微缩建筑 · 剖切立方体 · 大陆架空间 · 理性脚手架 · 手绘建筑图解 · 白色纹理纸 |
| [xxd-panel-074](https://github.com/nevertoday/xxd-panel-074) | 标准圆角方形 · 正面伪 3D／2.5D · 原图灵魂提炼 · 连续空间遮挡 · 哑光雕塑感 · 品牌图标提案 |
| [xxd-panel-075](https://github.com/nevertoday/xxd-panel-075) | 深色蜡笔速写 · 米白手工纸 · 柔和不规则色域 · Risograph 颗粒 · 大面积留白 · 打字机私人注记 |
| [xxd-panel-076](https://github.com/nevertoday/xxd-panel-076) | 粗粝深色蜡笔 · 炭笔彩铅 · 明亮马卡龙色块 · 45% 连续留白 · 天然纸面 · 打字机观察注记 |
| [xxd-panel-077](https://github.com/nevertoday/xxd-panel-077) | 极简纸雕拼贴 · 清晰剪纸轮廓 · 前后层叠 · 柔和投影 · 人文马卡龙 · 旅行杂志排版 |
| [xxd-panel-078](https://github.com/nevertoday/xxd-panel-078) | 暖米白棉纸 · 深压凹印 · 凹槽香槟金箔 · 纤细线性标识 · 无墨压痕 · 低调奢华 |
| [xxd-panel-079](https://github.com/nevertoday/xxd-panel-079) | 强几何直线 · 自由有机曲线 · 钢笔淡彩 · 未完成感 · 大面积纸白 · 编辑式图文混排 |
| [xxd-panel-080](https://github.com/nevertoday/xxd-panel-080) | 柔性有机几何 · 数字水粉蜡笔 · 颗粒肌理 · 植物系配色 · 自然隐喻 · 情绪留白 |
| [xxd-panel-081](https://github.com/nevertoday/xxd-panel-081) | 等粗彩色单线 · 开放轮廓 · 线密度层级 · 2–4 色专印 · Risograph 颗粒 · 私人纪念叙事 |
| [xxd-panel-082](https://github.com/nevertoday/xxd-panel-082) | 不规则水彩色域 · Naïve + Wonky · Isometric／2.5D · 稚拙轮廓 · 鲜活配色 · 立体主角 |
| [xxd-panel-083](https://github.com/nevertoday/xxd-panel-083) | Ugly-cute 丑萌涂鸦 · Wonky 发抖轮廓 · 故意失准 · 单一幽默主角 · 粗糙蜡笔 · 少怪笨准 |
| [xxd-panel-084](https://github.com/nevertoday/xxd-panel-084) | 极简城市线描 · 几何线性骨架 · 点描密度层次 · 透视引导线 · 限制性色彩 · 诗意留白 |
| [xxd-panel-085](https://github.com/nevertoday/xxd-panel-085) | 手工微缩舞台 · 收藏级立体封面 · 黏土毛毡纸板 · 手剪线绳 · 哑光触感 · 艺术留白 |
| [xxd-panel-086](https://github.com/nevertoday/xxd-panel-086) | 中世纪现代主义限色丝网版画 · 剪影几何 · 2–4 色专印 · 干刷拖墨 · 一个焦点 · 大面积留白 |
| [xxd-panel-087](https://github.com/nevertoday/xxd-panel-087) | 实体线绳关系系统地图 · 图钉节点 · 朱红线绳 · 关系映射 · 涌现几何 · 研究墙式留白 |
| [xxd-panel-088](https://github.com/nevertoday/xxd-panel-088) | 实验字体图像构成 · 文字即图像 · 解构排版 · 点阵轮廓 · 文字密度梯度 · 视觉诗 |
| [xxd-panel-089](https://github.com/nevertoday/xxd-panel-089) | 私人生活手账小品 · 一个主角 · 少量生活碎片 · 松散手绘线 · 水彩彩铅与粉蜡笔 · 成熟留白 |
| [xxd-panel-090](https://github.com/nevertoday/xxd-panel-090) | 图式化视觉思维地图 · 概念中心 · 文字节点 · 几何骨架 · 轨迹箭头 · 视觉记谱 · 大面积留白 |
| [xxd-panel-091](https://github.com/nevertoday/xxd-panel-091) | 单色蓝笔叙事速写 · 钴蓝／钢笔蓝／群青／靛蓝 · 方向排线 · 寻找线 · 选择性细化 · 自然纸白 |
| [xxd-panel-092](https://github.com/nevertoday/xxd-panel-092) | Expressive pen · loose contours · geometric and scribble hatching · negative-space composition |
| [xxd-panel-093](https://github.com/nevertoday/xxd-panel-093) | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| [xxd-panel-094](https://github.com/nevertoday/xxd-panel-094) | Fine pen-and-ink · selective solid black · source-derived spot colour · vast negative space · vintage book illustration |
| [xxd-panel-095](https://github.com/nevertoday/xxd-panel-095) | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| [xxd-panel-096](https://github.com/nevertoday/xxd-panel-096) | Independent original aesthetic · photo-grounded transformation · flexible multi-format delivery |
| [xxd-panel-097](https://github.com/nevertoday/xxd-panel-097) | Mid-century vernacular commercial graphic · schematic line drawing · two-colour spot printing · functional humour |
| [xxd-panel-098](https://github.com/nevertoday/xxd-panel-098) | 拟朴素水彩绘本插画 · 松散墨线 · 平面水彩／类水粉 · 符号化造型 · 天真透视 · 明快照片取色 · 成熟叙事构图 |
| [xxd-panel-099](https://github.com/nevertoday/xxd-panel-099) | 品牌吉祥物平面矢量插画 · 粗黑轮廓 · 圆润几何 · 夸张比例 · 2–4 色品牌化取色 · 超大文字背景 |
| **[xxd-panel-100](https://github.com/nevertoday/xxd-panel-100)** | 稚拙民艺感平面叙事 · primitive forms · 简化剪影 · flattened perspective · 蜡笔／油画棒颗粒 · 暖白纸面 · 鲜活限制色 |
<!-- xxd-panel-catalog:end -->

## 关于 XXD

XXD 是小小东品牌名的缩写，本项目由小小东创建并维护： [@xiaoxiaodong01](https://x.com/xiaoxiaodong01).

## 广告信息｜XXD 付费服务与会员

> **广告与商业信息声明：** 以下二维码、会员与付费服务链接属于小小东的广告信息。是否扫码或购买完全自愿，不影响本开源项目的访问与使用。



### 小小东总控 · 将军总指挥 Skill · 100 元

一次支付 100 元获得本套将军总指挥 Skill（`xxd-panel-all`），用于主控、推荐、点将和批量调度全部士兵 Skills。扫码后请备注“将军总指挥 Skill”。

<!-- xxd-panel-command-system:start -->
**购买后可使用：主控全队的将军 Skill**

| 层级 | Skill | 负责什么 |
|---|---|---|
| **将军级** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 识别当前可用的编号 Skills；按图片、主题和用途推荐；按编号点将；组织同图多风格试稿；为图片文件夹批量分配并逐项派发。 |
| **士兵级** | `xxd-panel-NNN`（当前 001–112） | 每个编号只执行自己独立的原始提示词与审美，把将军派发的单个任务完成为成品。 |

将军 Skill 是整个编号 Skills 队伍的总控入口。购买后即可使用，并获得安装、版本更新、队伍配置和调度方式的答疑。将军只负责组织与派发，不会改写、混合或覆盖士兵的原始美学；每张成品仍由被选中的士兵 Skill 独立完成。
<!-- xxd-panel-command-system:end -->

### 知识星球＋成员提示词库＋Skills 所有将军会员 · 699 元/年

[知识星球](https://wx.zsxq.com/group/15554814142882)、[小小东成员提示词库](https://vip.xiaoxiaodong.ai/)与 Skills 所有将军会员是同一份会员权益：**一次年费同时开通三项权益，无需重复付费。**

[Knowledge Planet](https://wx.zsxq.com/group/15554814142882) · [Member Prompt Library](https://vip.xiaoxiaodong.ai/)

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="XXD WeChat" width="280"></a></p>

<div align="center"><strong>先保留身份，再把它变成一眼记住的角色。</strong></div>

---

<div align="center">

## ☕ 支持这个开源项目

如果项目对你有帮助，愿意的话，可以用小小东本人的微信或支付宝赞赏码支持算力。


<table><tr>
<td align="center"><a href="https://colors.xiaoxiaodong.ai/docs/images/wechat-reward-qr.png"><img src="https://colors.xiaoxiaodong.ai/docs/images/wechat-reward-qr.png" alt="XXD WeChat reward" width="180"></a><br><strong>WeChat</strong></td>
<td align="center"><a href="https://colors.xiaoxiaodong.ai/docs/images/alipay-reward-qr.png"><img src="https://colors.xiaoxiaodong.ai/docs/images/alipay-reward-qr.png" alt="XXD Alipay reward" width="180"></a><br><strong>Alipay</strong></td>
</tr></table>

</div>

## 许可证

本项目（包括 Skill、提示词、脚本、文档及随附样张）采用 **PolyForm Noncommercial License 1.0.0**。完整法律条文请见 [LICENSE](LICENSE)，官方页面见 <https://polyformproject.org/licenses/noncommercial/1.0.0>。

用人话说：

- 个人可以用于学习、研究、实验、测试、兴趣项目和私人娱乐；慈善机构、教育机构、公共研究/安全/卫生机构、环保组织及政府机构也可以使用。
- 在**非商业目的**下，你可以使用、复制、修改、制作衍生作品并分享；分享时必须同时提供本许可证（或上面的链接）以及作者提供的所有 `Required Notice:` 声明。
- 不允许用于商业产品或服务、收费交付、出售访问权或许可，或任何预期会带来商业应用的用途。需要商业使用时，请先向版权方另行取得书面许可。
- 本协议只授予其中明确写出的著作权许可和有限的专利许可，不授予商标、品牌名称或其他未明确授予的权利，也不能把你的许可再转授给他人。
- 如果收到书面违约通知，须在 32 天内纠正并采取实际补救措施，否则许可会立即终止；就专利侵权提出书面主张也会终止专利许可。
- 内容按“现状”提供，在法律允许的范围内不作任何担保，使用风险和可能的损失由使用者自行承担。
