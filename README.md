### Security tooling · Reverse engineering · Automation

I build security tools, reverse-engineered API clients and bots, and more recently low-level bioinformatics in pure C. I like taking internals apart (Discord's webpack, the Minecraft protocol, the internal APIs of Qwen and Baidu) and turning them into clean, tested code. If it has an endpoint, an internal store, an NBT packet or a genome, I will find it.

I work mostly in Python, JavaScript and C. Based in Colombia.

[![GitHub](https://img.shields.io/badge/GitHub-AnonymoDGH-313131?style=flat&labelColor=545454&logo=github&logoColor=white)](https://github.com/AnonymoDGH)
[![PyPI](https://img.shields.io/badge/PyPI-7%20packages-313131?style=flat&labelColor=545454&logo=pypi&logoColor=white)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-mineflayer--schem-313131?style=flat&labelColor=545454&logo=npm&logoColor=white)](https://www.npmjs.com/~anonymodgh)

## Security toolkit

Seven packages on PyPI. Pure Python, standard library only, about 74k lines of code and 3.4k tests.

```sh
pip install book-cipher-kit dns-tunnel-messenger metadata-stripper honeypot-server hash-auditor cover-identity deadman-switch
```

| Package | Description |
|:--|:--|
| [book-cipher-kit](https://github.com/AnonymoDGH/book-cipher-kit) | Book cipher with Shamir secret sharing, an audit trail and a TUI |
| [dns-tunnel-messenger](https://github.com/AnonymoDGH/dns-tunnel-messenger) | Covert messaging over DNS: traffic shaping, fragmentation, anti-replay |
| [metadata-stripper](https://github.com/AnonymoDGH/metadata-stripper) | Metadata removal for EXIF, HEIF, PDF and Office files, with a risk engine and GPS forensics |
| [honeypot-server](https://github.com/AnonymoDGH/honeypot-server) | Deception platform: 8 protocols, tar pit, canary tokens, TTP classifier |
| [hash-auditor](https://github.com/AnonymoDGH/hash-auditor) | Password auditing lab: rainbow tables, PCFG, masks, zxcvbn-lite |
| [cover-identity](https://github.com/AnonymoDGH/cover-identity) | Consistent cover identities: full dossier, encrypted vault, drills |
| [deadman-switch](https://github.com/AnonymoDGH/deadman-switch) | Dead man's switch: signed heartbeats, proof of life, quorum, legacy |

## Reverse engineering

| Project | Description |
|:--|:--|
| [Qwen-Reverse](https://github.com/AnonymoDGH/Qwen-Reverse) | Async client for chat.qwen.ai: streaming, reasoning, tool calling, image and video |
| [baidu-reverse](https://github.com/AnonymoDGH/baidu-reverse) | Async client for Baidu Wenxin: streaming, reasoning, proxy pool |
| [reverse-agent](https://github.com/AnonymoDGH/reverse-agent) | Multi-provider terminal coding agent |
| [gguf2bin](https://github.com/AnonymoDGH/gguf2bin) | C99 runtime: GGUF → G2BX → inference (Qwen3, Qwen2, Llama) |

## Low-level C lab

Bioinformatics, memory and self-modifying ML. Pure C, standard library only, no Python, JIT to x86-64. About 15k lines of code and 113+ tests.

| Project | Description |
|:--|:--|
| [seqalign](https://github.com/AnonymoDGH/seqalign) | BLAST-lite in C11: Needleman-Wunsch and Smith-Waterman with Gotoh affine gaps, BLOSUM62, k-mer CSR. 125 KB, zero dependencies, 113 tests |
| [neuro-jit](https://github.com/AnonymoDGH/neuro-jit) | Self-modifying ML in pure C: JIT-compiles the forward pass to x86-64, with weights embedded as immediates |
| [memcore](https://github.com/AnonymoDGH/memcore) | Pure C text micro-model that learns continually: surprise-driven neural memory (Titans) plus a replay buffer |
| [neuro-snake](https://github.com/AnonymoDGH/neuro-snake) | Snake trained by heuristic imitation and recompiled with neuro-jit, for a 4.35x speedup |
| [gguf2bin](https://github.com/AnonymoDGH/gguf2bin) | C99 inference runtime for GGUF models, listed above |

## Other projects

| Project | Description |
|:--|:--|
| [mineflayer-schem](https://github.com/AnonymoDGH/mineflayer-schem) | Builds structures from schematics with mineflayer. Published on npm, v1.5.2 |
| [Discord-Quest-Auto-Completer](https://github.com/AnonymoDGH/Discord-Quest-Auto-Completer) | Completes Discord quests by injecting into the client's internal webpack |
| [Armonia](https://github.com/AnonymoDGH/Armonia) | Music generation from natural language: 214K scores to WAV, MIDI and ABC |
| [vital-agent](https://github.com/AnonymoDGH/vital-agent) | An autonomous agent that has to earn its own money, or die |
| [OurBook](https://github.com/AnonymoDGH/OurBook) | An MCP where the agent does not remember your data; it remembers your story |
| [ultimate-free-llm-resources](https://github.com/AnonymoDGH/ultimate-free-llm-resources) | The most complete collection of free LLM resources |
| [rdru-lm](https://github.com/AnonymoDGH/rdru-lm) | Character-level LM with an iterative transformer block and denoising |
| [nequi-clone](https://github.com/AnonymoDGH/nequi-clone) | Fan-made Nequi clone for educational use: Android WebView and a mock backend with transfers, receipts and ledger balance |

## Stack

| | |
|:--|:--|
| **Languages** | Python, JavaScript, TypeScript, C (C11), C++ |
| **Runtime and tooling** | Node.js, Linux, Docker, Git, Wireshark |
| **Testing and distribution** | pytest, PyPI, npm |
| **Web** | React, Next.js, Webpack internals |
| **Minecraft** | Prismarine / mineflayer |

## Activity

<p>
  <img src="./assets/stats.svg" alt="GitHub stats" width="49%" />
  <img src="./assets/langs.svg" alt="Top languages" width="49%" />
</p>

<img src="./assets/activity.svg" alt="Recent activity" width="100%" />

<details>
<summary>Contribution graph</summary>
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/snake.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/snake-light.svg" />
  <img src="./assets/snake.svg" alt="Contribution graph" width="100%" />
</picture>
</details>

## Contact

Have an unusual idea, an interesting bug, or want to collaborate? Get in touch through [GitHub](https://github.com/AnonymoDGH), [PyPI](https://pypi.org/user/AnonymoDGH/) or [npm](https://www.npmjs.com/~anonymodgh).
