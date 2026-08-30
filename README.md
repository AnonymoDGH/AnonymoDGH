<div align="center">

# AnonymoDGH

Security tooling · Reverse engineering · Automation · Colombia 🇨🇴

[![GitHub](https://img.shields.io/badge/github-AnonymoDGH-16161e?style=flat&logo=github&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://github.com/AnonymoDGH)
[![followers](https://img.shields.io/github/followers/AnonymoDGH?style=flat&logo=github&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://github.com/AnonymoDGH?tab=followers)
[![PyPI](https://img.shields.io/badge/pypi-7_packages-16161e?style=flat&logo=pypi&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-mineflayer--schem-16161e?style=flat&logo=npm&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://www.npmjs.com/~anonymodgh)

</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">$ whoami</h2>

I build security tools, reverse-engineered clients, and bots — and now low-level bioinformatics in pure C. I dig into the guts of things — Discord's webpack, the Minecraft protocol, Qwen's and Baidu's internal APIs — and turn them into clean, tested code.

Python, JavaScript and C are my stack. If it has an endpoint, an internal store, an NBT packet or a genome, I will find it.

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">🐍 Toolkit — 7 packages on PyPI</h2>

Pure Python (stdlib only) · ~74k lines · 3.4k tests

| Package | What it does |
| :-- | :-- |
| **[book-cipher-kit](https://github.com/AnonymoDGH/book-cipher-kit)** | Book cipher with Shamir secret sharing, audit trail, and TUI |
| **[dns-tunnel-messenger](https://github.com/AnonymoDGH/dns-tunnel-messenger)** | Covert messaging over DNS: shaping, fragmentation, anti-replay |
| **[metadata-stripper](https://github.com/AnonymoDGH/metadata-stripper)** | Strips metadata (EXIF/HEIF/PDF/Office), risk engine, GPS forensics |
| **[honeypot-server](https://github.com/AnonymoDGH/honeypot-server)** | Deception platform: 8 protocols, tar pit, canary tokens, TTP classifier |
| **[hash-auditor](https://github.com/AnonymoDGH/hash-auditor)** | Password auditing lab: rainbow tables, PCFG, masks, zxcvbn-lite |
| **[cover-identity](https://github.com/AnonymoDGH/cover-identity)** | Consistent covert identities: full dossier, encrypted vault, drills |
| **[deadman-switch](https://github.com/AnonymoDGH/deadman-switch)** | Dead man's switch: signed heartbeats, proof-of-life, quorum, legacy |

```bash
pip install book-cipher-kit dns-tunnel-messenger metadata-stripper \
            honeypot-server hash-auditor cover-identity deadman-switch
```

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">🔧 Reverse engineering</h2>

| Project | What it is |
| :-- | :-- |
| **[Qwen-Reverse](https://github.com/AnonymoDGH/Qwen-Reverse)** | Async client for chat.qwen.ai — streaming, reasoning, tool calling, image/video |
| **[baidu-reverse](https://github.com/AnonymoDGH/baidu-reverse)** | Async client for Baidu Wenxin — streaming, reasoning, proxy pool |
| **[reverse-agent](https://github.com/AnonymoDGH/reverse-agent)** | Multi-provider terminal coding agent |
| **[gguf2bin](https://github.com/AnonymoDGH/gguf2bin)** | C99 runtime: GGUF → G2BX → inference (Qwen3 / Qwen2 / Llama) |

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">📌 Featured projects</h2>

| Project | Description | ★ |
| :-- | :-- | :--: |
| **[seqalign](https://github.com/AnonymoDGH/seqalign)** | BLAST-lite en C11 — Needleman-Wunsch, Smith-Waterman, BLOSUM62, k-mer CSR · 125KB, 0 deps, 113 tests | ![stars](https://img.shields.io/github/stars/AnonymoDGH/seqalign?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[mineflayer-schem](https://github.com/AnonymoDGH/mineflayer-schem)** | Builds structures from schematics with mineflayer · npm v1.5.2 | ![stars](https://img.shields.io/github/stars/AnonymoDGH/mineflayer-schem?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[Discord-Quest-Auto-Completer](https://github.com/AnonymoDGH/Discord-Quest-Auto-Completer)** | Completes Discord quests by injecting into the internal webpack | ![stars](https://img.shields.io/github/stars/AnonymoDGH/Discord-Quest-Auto-Completer?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[Armonia](https://github.com/AnonymoDGH/Armonia)** | Generates music from natural language · 214K scores → WAV/MIDI/ABC | ![stars](https://img.shields.io/github/stars/AnonymoDGH/Armonia?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[vital-agent](https://github.com/AnonymoDGH/vital-agent)** | Autonomous agent that must earn its own money... or die | ![stars](https://img.shields.io/github/stars/AnonymoDGH/vital-agent?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[OurBook](https://github.com/AnonymoDGH/OurBook)** | An MCP where the agent doesn't remember your data — it remembers your story | ![stars](https://img.shields.io/github/stars/AnonymoDGH/OurBook?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[ultimate-free-llm-resources](https://github.com/AnonymoDGH/ultimate-free-llm-resources)** | The most complete collection of free LLM resources | ![stars](https://img.shields.io/github/stars/AnonymoDGH/ultimate-free-llm-resources?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[rdru-lm](https://github.com/AnonymoDGH/rdru-lm)** | Character-level LM with iterative transformer block + denoising | ![stars](https://img.shields.io/github/stars/AnonymoDGH/rdru-lm?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">🛠️ Stack</h2>

`Python`  `JavaScript`  `TypeScript`  `Node.js`  `C`  `C11`  `C++`
`pytest`  `PyPI`  `npm`  `Wireshark`  `Linux`  `Docker`  `Git`
`React`  `Next.js`  `Webpack internals`  `Prismarine / mineflayer`

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">📊 Stats</h2>

<img height="292" src="./assets/stats.svg" alt="github stats" />
<img height="292" src="./assets/langs.svg" alt="top languages" />

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">📈 Activity</h2>

<img src="./assets/activity.svg" alt="contribution activity" width="92%"/>

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">🐍 Contributions</h2>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/snake.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/snake-light.svg">
  <img alt="contribution snake" src="./assets/snake.svg" width="92%">
</picture>

</div>
</div>

---

<div align="center">
<div style="max-width: 920px; margin: 1.2rem auto; padding: 1.8rem 2rem; background: rgba(22, 22, 30, 0.55); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-radius: 16px; border: 1px solid rgba(122, 162, 247, 0.14); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);">

<h2 style="font-family: 'JetBrains Mono', monospace; color: #7aa2f7; font-size: 20px; letter-spacing: 1px; margin: 0 0 1rem 0;">📬 Contact</h2>

[![GitHub](https://img.shields.io/badge/GitHub-AnonymoDGH-16161e?style=flat&logo=github&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://github.com/AnonymoDGH)
[![PyPI](https://img.shields.io/badge/PyPI-AnonymoDGH-16161e?style=flat&logo=pypi&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-anonymodgh-16161e?style=flat&logo=npm&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://www.npmjs.com/~anonymodgh)

Got a weird idea, an interesting bug, or want to collaborate — reach out.

</div>
</div>