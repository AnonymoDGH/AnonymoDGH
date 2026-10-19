<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d14,50:16161e,100:7aa2f7&height=240&section=header&text=AnonymoDGH&fontColor=7aa2f7&fontSize=64&fontAlignY=38&desc=Security%20%C2%B7%20Reverse%20engineering%20%C2%B7%20Pure%20C%20%C2%B7%20Automation&descAlignY=62&descSize=18&animation=fadeIn" alt="header" width="100%" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=900&color=7AA2F7&center=true&vCenter=true&width=700&lines=I+dig+into+the+guts+of+things;Discord+webpack+%E2%80%A2+Minecraft+protocol+%E2%80%A2+Qwen+%26+Baidu+APIs;Pure+C+%E2%80%A2+JIT+to+x86-64+%E2%80%A2+genomes;If+it+has+an+endpoint%2C+I+will+find+it." alt="typing" />

<br/>

[![GitHub](https://img.shields.io/badge/github-AnonymoDGH-16161e?style=for-the-badge&logo=github&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://github.com/AnonymoDGH)
[![followers](https://img.shields.io/github/followers/AnonymoDGH?style=for-the-badge&logo=github&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://github.com/AnonymoDGH?tab=followers)
[![PyPI](https://img.shields.io/badge/pypi-7_packages-16161e?style=for-the-badge&logo=pypi&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-mineflayer--schem-16161e?style=for-the-badge&logo=npm&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://www.npmjs.com/~anonymodgh)

📍 Colombia 🇨🇴 · Security tooling · Reverse engineering · Bio in C

</div>

<br/>

<div align="center">

<img src="https://skillicons.dev/icons?i=python,js,ts,c,cpp,nodejs,react,nextjs,linux,docker,git,pytest,npm,wireshark&theme=dark&perline=14" alt="stack" />

</div>

<br/>

<div align="center">

## `$ whoami`

</div>

I build security tools, reverse-engineered clients, and bots — and now low-level bioinformatics in pure C. I dig into the guts of things — Discord's webpack, the Minecraft protocol, Qwen's and Baidu's internal APIs — and turn them into clean, tested code.

> Python, JavaScript and C are my stack. If it has an endpoint, an internal store, an NBT packet or a genome, I will find it.

<br/>

---

## 🐍 Toolkit — 7 packages on PyPI

`Pure Python (stdlib only)` `~74k lines` `3.4k tests`

<table>
<tr>
<td width="50%">

**[book-cipher-kit](https://github.com/AnonymoDGH/book-cipher-kit)**
Book cipher with Shamir secret sharing, audit trail, and TUI.

</td>
<td width="50%">

**[dns-tunnel-messenger](https://github.com/AnonymoDGH/dns-tunnel-messenger)**
Covert messaging over DNS: shaping, fragmentation, anti-replay.

</td>
</tr>
<tr>
<td width="50%">

**[metadata-stripper](https://github.com/AnonymoDGH/metadata-stripper)**
Strips metadata (EXIF/HEIF/PDF/Office), risk engine, GPS forensics.

</td>
<td width="50%">

**[honeypot-server](https://github.com/AnonymoDGH/honeypot-server)**
Deception platform: 8 protocols, tar pit, canary tokens, TTP classifier.

</td>
</tr>
<tr>
<td width="50%">

**[hash-auditor](https://github.com/AnonymoDGH/hash-auditor)**
Password auditing lab: rainbow tables, PCFG, masks, zxcvbn-lite.

</td>
<td width="50%">

**[cover-identity](https://github.com/AnonymoDGH/cover-identity)**
Consistent covert identities: full dossier, encrypted vault, drills.

</td>
</tr>
<tr>
<td width="50%">

**[deadman-switch](https://github.com/AnonymoDGH/deadman-switch)**
Dead man's switch: signed heartbeats, proof-of-life, quorum, legacy.

</td>
<td width="50%">

```bash
pip install book-cipher-kit dns-tunnel-messenger \
  metadata-stripper honeypot-server \
  hash-auditor cover-identity deadman-switch
```

</td>
</tr>
</table>

---

## 🔧 Reverse engineering

<table>
<tr>
<td width="50%">

**[Qwen-Reverse](https://github.com/AnonymoDGH/Qwen-Reverse)**
Async client for chat.qwen.ai — streaming, reasoning, tool calling, image/video.

</td>
<td width="50%">

**[baidu-reverse](https://github.com/AnonymoDGH/baidu-reverse)**
Async client for Baidu Wenxin — streaming, reasoning, proxy pool.

</td>
</tr>
<tr>
<td width="50%">

**[reverse-agent](https://github.com/AnonymoDGH/reverse-agent)**
Multi-provider terminal coding agent.

</td>
<td width="50%">

**[gguf2bin](https://github.com/AnonymoDGH/gguf2bin)**
C99 runtime: GGUF → G2BX → inference (Qwen3 / Qwen2 / Llama).

</td>
</tr>
</table>

---

## 🧬 Low-level C Lab — Bio, Memory & Self-modifying ML

`Pure C (stdlib only, no Python)` `JIT to x86-64` `~15k lines` `113+ tests`

<table>
<tr>
<td width="50%">

**[seqalign](https://github.com/AnonymoDGH/seqalign)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/seqalign?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
BLAST-lite en C11: Needleman-Wunsch + Smith-Waterman Gotoh affine, BLOSUM62, k-mer CSR — 125KB, 0 deps.

</td>
<td width="50%">

**[neuro-jit](https://github.com/AnonymoDGH/neuro-jit)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/neuro-jit?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Self-modifying ML in pure C — JIT-compiles forward pass to x86-64, weights baked as immediates.

</td>
</tr>
<tr>
<td width="50%">

**[memcore](https://github.com/AnonymoDGH/memcore)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/memcore?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Micro-modelo de texto en C puro que aprende continuo — memoria neuronal por sorpresa (Titans) + replay buffer.

</td>
<td width="50%">

**[neuro-snake](https://github.com/AnonymoDGH/neuro-snake)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/neuro-snake?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Snake trained by heuristic imitation, recompiled with neuro-jit — **×4.35 speedup**.

</td>
</tr>
<tr>
<td width="50%">

**[gguf2bin](https://github.com/AnonymoDGH/gguf2bin)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/gguf2bin?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
C99 runtime: GGUF → G2BX → inference (Qwen3/Qwen2/Llama).

</td>
<td width="50%"></td>
</tr>
</table>

---

## 📌 Featured projects

<table>
<tr>
<td width="50%">

**[mineflayer-schem](https://github.com/AnonymoDGH/mineflayer-schem)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/mineflayer-schem?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Builds structures from schematics with mineflayer · npm v1.5.2.

</td>
<td width="50%">

**[Discord-Quest-Auto-Completer](https://github.com/AnonymoDGH/Discord-Quest-Auto-Completer)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/Discord-Quest-Auto-Completer?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Completes Discord quests by injecting into the internal webpack.

</td>
</tr>
<tr>
<td width="50%">

**[Armonia](https://github.com/AnonymoDGH/Armonia)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/Armonia?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Generates music from natural language · 214K scores → WAV/MIDI/ABC.

</td>
<td width="50%">

**[vital-agent](https://github.com/AnonymoDGH/vital-agent)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/vital-agent?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Autonomous agent that must earn its own money... or die.

</td>
</tr>
<tr>
<td width="50%">

**[OurBook](https://github.com/AnonymoDGH/OurBook)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/OurBook?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
An MCP where the agent doesn't remember your data — it remembers your story.

</td>
<td width="50%">

**[ultimate-free-llm-resources](https://github.com/AnonymoDGH/ultimate-free-llm-resources)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/ultimate-free-llm-resources?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
The most complete collection of free LLM resources.

</td>
</tr>
<tr>
<td width="50%">

**[rdru-lm](https://github.com/AnonymoDGH/rdru-lm)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/rdru-lm?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Character-level LM with iterative transformer block + denoising.

</td>
<td width="50%">

**[nequi-clone](https://github.com/AnonymoDGH/nequi-clone)** ![stars](https://img.shields.io/github/stars/AnonymoDGH/nequi-clone?style=flat&labelColor=16161e&color=7aa2f7&logoColor=7aa2f7)
Nequi Clone fan-made (educativo) — WebView Android + backend mock: envíos, comprobantes, saldo contable.

</td>
</tr>
</table>

---

## 📊 Stats

<p align="center">
  <img height="292" src="./assets/stats.svg" alt="github stats" />
  <img height="292" src="./assets/langs.svg" alt="top languages" />
</p>

## 📈 Activity

<p align="center">
  <img src="./assets/activity.svg" alt="contribution activity" width="92%" />
</p>

## 🐍 Contributions

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/snake.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/snake-light.svg">
    <img alt="contribution snake" src="./assets/snake.svg" width="92%">
  </picture>
</p>

---

## 📬 Contact

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-AnonymoDGH-16161e?style=for-the-badge&logo=github&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://github.com/AnonymoDGH)
[![PyPI](https://img.shields.io/badge/PyPI-AnonymoDGH-16161e?style=for-the-badge&logo=pypi&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-anonymodgh-16161e?style=for-the-badge&logo=npm&logoColor=7aa2f7&labelColor=16161e&color=7aa2f7)](https://www.npmjs.com/~anonymodgh)

Got a weird idea, an interesting bug, or want to collaborate — reach out.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,50:16161e,100:0d0d14&height=120&section=footer" alt="footer" width="100%" />

</div>
