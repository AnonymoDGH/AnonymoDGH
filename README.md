<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&duration=3000&pause=800&color=7AA2F7&center=true&vCenter=true&width=600&lines=AnonymoDGH;Security+%C2%B7+Reverse+engineering;Pure+C+%C2%B7+Bio+%C2%B7+Automation" alt="typing banner" />

**Security tooling · Reverse engineering · Automation · Colombia 🇨🇴**

[![GitHub](https://img.shields.io/badge/github-AnonymoDGH-16161e?style=flat&logo=github&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://github.com/AnonymoDGH)
[![followers](https://img.shields.io/github/followers/AnonymoDGH?style=flat&logo=github&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://github.com/AnonymoDGH?tab=followers)
[![PyPI](https://img.shields.io/badge/pypi-7_packages-16161e?style=flat&logo=pypi&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-mineflayer--schem-16161e?style=flat&logo=npm&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://www.npmjs.com/~anonymodgh)

</div>

---

### `$ whoami`

I build security tools, reverse-engineered clients, and bots — and now low-level bioinformatics in pure C. I dig into the guts of things — Discord's webpack, the Minecraft protocol, Qwen's and Baidu's internal APIs — and turn them into clean, tested code.

Python, JavaScript and C are my stack. If it has an endpoint, an internal store, an NBT packet or a genome, I will find it.

---

### 🐍 Toolkit — 7 packages on PyPI

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

---

### 🔧 Reverse engineering

| Project | What it is |
| :-- | :-- |
| **[Qwen-Reverse](https://github.com/AnonymoDGH/Qwen-Reverse)** | Async client for chat.qwen.ai — streaming, reasoning, tool calling, image/video |
| **[baidu-reverse](https://github.com/AnonymoDGH/baidu-reverse)** | Async client for Baidu Wenxin — streaming, reasoning, proxy pool |
| **[reverse-agent](https://github.com/AnonymoDGH/reverse-agent)** | Multi-provider terminal coding agent |
| **[gguf2bin](https://github.com/AnonymoDGH/gguf2bin)** | C99 runtime: GGUF → G2BX → inference (Qwen3 / Qwen2 / Llama) |

---

### 🧬 Low-level C Lab — Bio, Memory & Self-modifying ML

Pure C (stdlib only, no Python) · JIT to x86-64 · ~15k lines · 113+ tests

| Project | What it does | ★ |
| :-- | :-- | :--: |
| **[seqalign](https://github.com/AnonymoDGH/seqalign)** | BLAST-lite en C11: Needleman-Wunsch + Smith-Waterman Gotoh affine, BLOSUM62, k-mer CSR — 125KB, 0 deps | ![stars](https://img.shields.io/github/stars/AnonymoDGH/seqalign?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[neuro-jit](https://github.com/AnonymoDGH/neuro-jit)** | Self-modifying ML in pure C — JIT-compiles forward pass to x86-64, weights baked as immediates | ![stars](https://img.shields.io/github/stars/AnonymoDGH/neuro-jit?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[memcore](https://github.com/AnonymoDGH/memcore)** | Micro-modelo de texto en C puro que aprende continuo — memoria neuronal por sorpresa (Titans) + replay buffer | ![stars](https://img.shields.io/github/stars/AnonymoDGH/memcore?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[neuro-snake](https://github.com/AnonymoDGH/neuro-snake)** | Snake trained by heuristic imitation, recompiled with neuro-jit — **×4.35 speedup** | ![stars](https://img.shields.io/github/stars/AnonymoDGH/neuro-snake?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[gguf2bin](https://github.com/AnonymoDGH/gguf2bin)** | C99 runtime: GGUF → G2BX → inference (Qwen3/Qwen2/Llama) | ![stars](https://img.shields.io/github/stars/AnonymoDGH/gguf2bin?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |

---

### 📌 Featured projects

| Project | Description | ★ |
| :-- | :-- | :--: |
| **[mineflayer-schem](https://github.com/AnonymoDGH/mineflayer-schem)** | Builds structures from schematics with mineflayer · npm v1.5.2 | ![stars](https://img.shields.io/github/stars/AnonymoDGH/mineflayer-schem?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[Discord-Quest-Auto-Completer](https://github.com/AnonymoDGH/Discord-Quest-Auto-Completer)** | Completes Discord quests by injecting into the internal webpack | ![stars](https://img.shields.io/github/stars/AnonymoDGH/Discord-Quest-Auto-Completer?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[Armonia](https://github.com/AnonymoDGH/Armonia)** | Generates music from natural language · 214K scores → WAV/MIDI/ABC | ![stars](https://img.shields.io/github/stars/AnonymoDGH/Armonia?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[vital-agent](https://github.com/AnonymoDGH/vital-agent)** | Autonomous agent that must earn its own money... or die | ![stars](https://img.shields.io/github/stars/AnonymoDGH/vital-agent?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[OurBook](https://github.com/AnonymoDGH/OurBook)** | An MCP where the agent doesn't remember your data — it remembers your story | ![stars](https://img.shields.io/github/stars/AnonymoDGH/OurBook?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[ultimate-free-llm-resources](https://github.com/AnonymoDGH/ultimate-free-llm-resources)** | The most complete collection of free LLM resources | ![stars](https://img.shields.io/github/stars/AnonymoDGH/ultimate-free-llm-resources?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[rdru-lm](https://github.com/AnonymoDGH/rdru-lm)** | Character-level LM with iterative transformer block + denoising | ![stars](https://img.shields.io/github/stars/AnonymoDGH/rdru-lm?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |
| **[nequi-clone](https://github.com/AnonymoDGH/nequi-clone)** | Nequi Clone fan-made (educativo) — WebView Android + backend mock: envíos, comprobantes, saldo contable | ![stars](https://img.shields.io/github/stars/AnonymoDGH/nequi-clone?style=flat&labelColor=16161e&color=16161e&logoColor=7aa2f7) |

---

### 🛠️ Stack

`Python` `JavaScript` `TypeScript` `Node.js` `C` `C11` `C++`
`pytest` `PyPI` `npm` `Wireshark` `Linux` `Docker` `Git`
`React` `Next.js` `Webpack internals` `Prismarine / mineflayer`

---

### 📊 Stats

<p align="center">
  <img height="292" src="./assets/stats.svg" alt="github stats" />
  <img height="292" src="./assets/langs.svg" alt="top languages" />
</p>

### 📈 Activity

<p align="center">
  <img src="./assets/activity.svg" alt="contribution activity" width="92%" />
</p>

### 🐍 Contributions

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/snake.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/snake-light.svg">
    <img alt="contribution snake" src="./assets/snake.svg" width="92%">
  </picture>
</p>

---

### 📬 Contact

[![GitHub](https://img.shields.io/badge/GitHub-AnonymoDGH-16161e?style=flat&logo=github&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://github.com/AnonymoDGH)
[![PyPI](https://img.shields.io/badge/PyPI-AnonymoDGH-16161e?style=flat&logo=pypi&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-anonymodgh-16161e?style=flat&logo=npm&logoColor=7aa2f7&labelColor=16161e&color=16161e)](https://www.npmjs.com/~anonymodgh)

Got a weird idea, an interesting bug, or want to collaborate — reach out.
