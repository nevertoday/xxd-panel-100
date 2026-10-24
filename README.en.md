<div align="center">

# XXD Panel 100｜Folk-Craft Narrative Painting

**Turns a photo into a small, naive folk story with crayon grain and an everyday feel.**

<a href="README.md">简体中文</a> · <strong>English</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 100"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 100"></td>
  </tr>
</table>

<p align="center"><sub>Top: the original photo. Bottom: the same photo in this style.</sub></p>

## What it is

A Skill for AI agents such as Claude Code and Codex. Give it a photo and it paints a finished PNG following the original Panel 100 prompt.

- **What it looks like:** The subject is pressed into simple silhouettes and big primitive shapes with exaggerated features; space is flat, told through height, overlap and size, and small supporting objects are scattered around like symbols. Dark areas are filled in crayon, oil pastel or soft pencil, rubbed, layered and broken so the paper shows through, with slightly clumsy edges. The ground is warm white paper, and only a few of the photo's liveliest colours are used, in small touches on clothes, plants, food or the focal point. Text is sparse, in a plain folk-editorial typeface with slight hand-printed errors and occasional handwriting, appearing like a sign, menu or note inside the picture.
- **Keywords:** Primitive forms · Simplified silhouettes · Flattened perspective · Crayon and oil-pastel grain · Warm white paper · Limited bright colours
- **What you can make:** A top–bottom comparison (photo above, design below), a left–right comparison, the design alone, or a wallpaper set for phone, tablet, desktop and watch. Pick several at once, at any ratio or exact pixel size.
- **What it is not:** Not a filter and not a template: every image is redrawn from your photo, and each photo is its own job.

## Get started in three steps

**1. Install.** Works with Claude Code, Codex and other agents that support Skills:

```bash
npx skills add https://github.com/nevertoday/xxd-panel-100 --skill xxd-panel-100
```

Then restart your agent session. You can also `git clone` this repository and link the folder to `~/.claude/skills/xxd-panel-100` or `~/.codex/skills/xxd-panel-100`.

**2. Make sure your agent can generate images.** This Skill has no image model of its own; it uses your agent's image generation, preferably GPT Image 2.

- Codex works as is when its built-in image generation is on.
- Claude Code and other agents without built-in image generation need an OpenAI-compatible image API. It takes about five minutes: see [Setting up image generation](#setting-up-image-generation).

Not sure? Just try it. If images can't be generated, the Skill stops and tells you before doing any work.

**3. Send a photo and say one sentence:**

> Use xxd-panel-100 to turn this photo into a 3:4 top–bottom poster with an English title.

If your request is complete, it starts right away; anything you left out (layout, ratio, text) it asks about, usually in one or two questions. Results are PNGs in a new folder under `~/Desktop/xxd/xxd-panel-100/`.

## Which photos work best

**Works well**

- Everyday photos with one central action or relationship: someone cooking, a street food stall, two people walking hand in hand
- Scenes with a lived-in feel: a corner of a market, quilts airing in a courtyard, a small shopfront
- People, animals and objects with a clear silhouette: a cyclist, a chicken, a teapot

**Not a good fit**

- Portraits that need fine features or an exact likeness
- Photos that rely on complex perspective or heavy detail: city skylines, machinery, full interiors
- Requests for children's cartoons, cute stickers, glossy vectors or realistic illustration

## Samples

Each image below is a finished result this Skill made from one photo. The top–bottom and left–right sets use different photos.

### Top–bottom: photo above, design below

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 100"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 100"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-11.png" alt="XXD Panel 100"></td>
    <td width="50%"><img src="./assets/examples/sample-12.png" alt="XXD Panel 100"></td>
  </tr>
</table>

### Left–right: photo left, design right

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-05.png" alt="XXD Panel 100"></td>
    <td width="50%"><img src="./assets/examples/sample-06.png" alt="XXD Panel 100"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-07.png" alt="XXD Panel 100"></td>
    <td width="50%"><img src="./assets/examples/sample-08.png" alt="XXD Panel 100"></td>
  </tr>
</table>

## Just say it

No parameters to memorise. Say what you want:

| You want | Say |
|---|---|
| Top–bottom comparison | Make a 3:4 top–bottom comparison |
| Left–right comparison | Make a 16:9 left–right comparison, photo on the left |
| Design only | Just the design, no photo, 9:16 portrait |
| A wallpaper set | Make matching wallpapers for phone, tablet, desktop and watch |
| Several ratios | Make this one at 1:1, 3:4 and 16:9 |
| Your own text | Use the title “Let the wind pass through” exactly as written |
| No text | No text at all |
| Text language | Write the text in Japanese |
| A whole folder | Turn every photo in this folder into a top–bottom comparison |
| Same as last time | Use my settings from last time |

Prefer the command line? The flags map one to one:

```text
/xxd-panel-100 photo.jpg --mode top-bottom --size 3:4 --text prompt --locale en-US
/xxd-panel-100 photo.jpg --mode design-only --size 9:16 --text none
/xxd-panel-100 ./photos --mode left-right --size 16:9 --text prompt --locale ja-JP
```

All flags are listed under [Parameters](#parameters).

## FAQ

**Does the original photo have to appear?** No. Ask for “design only” or a wallpaper set and the whole canvas is design.

**Who writes the text?** By default the image model writes it from your photo; you only choose the language. Give your own words and they are used exactly; or ask for no text. Anything that looks factual (places, dates, numbers) comes only from you or from what is visible in the photo, never invented.

**What if I don't like the result?** Say “one more”. It redraws from the original photo instead of editing the last result, so every attempt is different.

**Do photos in a batch mix together?** No. Each photo is generated on its own and never borrows another photo's colours, text or layout. Settings are asked once for the whole batch.

**Where do my photos go?** Only to the image model your agent uses. The Skill uploads nothing elsewhere and never prints endpoints or keys.

**How does this relate to other Panels?** XXD Panels are a family of styles, one per number, fully independent; install only the ones you like. To have AI recommend a style for a photo, or compare several at once, use the catalog [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all).

## Original prompt

This style is defined entirely by Xiaoxiaodong's [original prompt](references/original-prompt/zh-CN.md) (in Chinese). The Skill only appends the layout, size and text settings you choose; it never summarises, translates or rewrites the prompt.

Reading translations (for reading only; never sent to the image model): [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

## Setting up image generation

You need an OpenAI-compatible API that serves `gpt-image-2` (or a compatible model) and its API key. This creates a separate config and leaves your Codex settings alone:

```bash
mkdir -p ~/.xxd-imagegen
cat > ~/.xxd-imagegen/config.toml <<'EOF'
model_provider = "image"

[model_providers.image]
base_url = "https://api.openai.com/v1"   # or your compatible endpoint
env_key = "XXD_IMAGE_API_KEY"
EOF

# add to ~/.zshrc or ~/.bashrc so your agent can read them
echo 'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen' >> ~/.zshrc
echo 'export XXD_IMAGE_API_KEY=your-key' >> ~/.zshrc
```

Reopen your terminal and agent, then check once from this Skill's folder:

```bash
python3 scripts/configured_imagegen.py probe
```

`"ok":true` means it works. The check only reports readiness; it never prints the endpoint or key. If your Codex already generates images through a compatible API, skip this step.

## Parameters

| Flag | Values |
|---|---|
| `--mode` | `top-bottom` · `left-right` · `design-only` · `wallpaper-pack` (phone, tablet, desktop, watch); combine freely |
| `--size` | `auto` recommended · `source` match the photo · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · exact pixels such as `2160x3840`; combine freely |
| `--text` | `prompt` written from the photo · `exact` your words (with `--copy "…"`) · `none` no text |
| `--locale` | text language, e.g. `zh-CN` `en-US` `ja-JP` `ko-KR` `ar` |
| `--wallpaper` | `linked` a matching set · `independent` four separate designs |
| `--wallpaper-size` | device pixels, e.g. `phone=1440x3200,desktop=3840x2160` |
| `--out` | another output root (default `~/Desktop/xxd/xxd-panel-100/`) |
| `--prefs` | `last` reuse · `edit` start from last time · `new` choose again · `off` don't remember this time · `clear` forget |

- With every value given, nothing is asked; otherwise only the missing values are. Pass a folder instead of `photo.jpg` to batch.
- Combinations are generated one by one: 2 modes × 3 sizes = 6 images, each composed for its own canvas rather than cropped.
- Comparisons are exactly 50:50. Usually the model paints only the design half and a script places the untouched photo beside it, so the split is centred and the photo is unchanged.
- Files are named like `source-001-street-top-bottom-3x4-1152x1536.png`, all in one flat task folder.
- Only layout, size, text mode and language are remembered, never photos, copy or keys.

<!-- xxd-readme-ads:start -->
## About XXD

XXD is Xiaoxiaodong's abbreviated brand name. This project is created and maintained by [@xiaoxiaodong01](https://x.com/xiaoxiaodong01).

## Xiaoxiaodong multi-platform membership · CNY 699/year

> **Advertising disclosure:** The QR code, membership, and paid-service links below are XXD promotional information. Scanning or purchasing is entirely optional and does not affect access to this open-source project.

One annual membership unlocks three benefits together: **Knowledge Planet + the XXD Member Prompt Library + membership for all General Skills**. They are included in one membership; no separate purchase is required.

<!-- xxd-panel-command-system:start -->

### How the Skills work together

| Level | Included | What it does |
|---|---|---|
| **General** | [`xxd-panel-all`](https://github.com/xiaoxiaodong-ai/xxd-panel-all) | Detects available numbered Skills, recommends them by image, theme, or use, and organizes multi-style and batch tasks. |
| **Soldier** | `xxd-panel-NNN` | Each numbered Skill follows its own original brief and aesthetic to complete the specific task assigned by the General. |

<!-- xxd-panel-command-system:end -->

### What you receive

1. **One-to-one WeChat AI learning and project support**
   Add Xiaoxiaodong on WeChat via the QR code below to discuss AI learning, tools, and real projects one to one, with practical guidance and answers. Representative questions may be organized into member resources.
2. **A growing member prompt library**
   The [XXD Member Prompt Library](https://vip.xiaoxiaodong.ai/) currently contains about 32,000 prompts and will keep expanding, with a goal of exceeding 100,000.
3. **All General Skills and usage support**
   One membership covers every General Skill, with usage guidance and Q&A when you need help.
4. **Priority for high-need requests**
   Frequently requested, high-need prompts and Skills are reviewed and developed first where appropriate.

### How to join

- [Activate membership on the member website](https://vip.xiaoxiaodong.ai/).
- Or scan the QR code below to add Xiaoxiaodong on WeChat for one-to-one activation support.

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="Contact Xiaoxiaodong" width="280"></a></p>
<!-- xxd-readme-ads:end -->

## License

This project—including its Skill, prompts, scripts, documentation, and accompanying samples—is released under the **PolyForm Noncommercial License 1.0.0**. The complete legal text is in [LICENSE](LICENSE); the official page is <https://polyformproject.org/licenses/noncommercial/1.0.0>.

In plain language:

- You may use it for personal study, research, experiments, testing, hobbies, and private entertainment. Charities, educational institutions, public research/safety/health organisations, environmental-protection organisations, and government institutions may also use it.
- For **noncommercial purposes**, you may use, copy, modify, create derivative works, and share the project. When sharing, include this license (or the link above) and every `Required Notice:` line supplied by the author.
- Commercial products or services, paid delivery, selling access or licenses, and uses with an anticipated commercial application are not allowed. Obtain separate written permission from the copyright holder for commercial use.
- The license grants only the stated copyright and limited patent rights. It grants no trademark, brand, or other unstated rights, and you may not sublicense or transfer your license.
- If you receive written notice of a violation, you have 32 days to come into full compliance and take practical corrective steps; otherwise the licenses end. A written patent-infringement claim also ends the patent license.
- The project is provided **as is**, without warranties, and you accept the risks and any resulting liability to the extent permitted by law.
