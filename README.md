<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050510,100:0f0f2e&height=200&section=header&text=AnonymoDGH&fontSize=70&fontColor=00ff9d&fontAlignY=35&animation=fadeIn&desc=python%20%7C%20reverse%20engineering%20%7C%20automation%20%7C%20colombia&descAlignY=55&descSize=18&descColor=7a7a9a" />

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=19&duration=2800&pause=900&color=00FF9D&center=true&vCenter=true&width=800&lines=7+paquetes+Python+publicados+en+PyPI+%F0%9F%90%8D;Reverse-engineering+Qwen%2C+Baidu+y+Discord+%F0%9F%94%A7;Construyo+bots+de+Minecraft+con+mineflayer;Si+tiene+un+endpoint%2C+lo+voy+a+encontrar;Open-source+%C2%B7+Made+in+Colombia+%F0%9F%87%A8%F0%9F%87%B4)](https://git.io/typing-svg)

![Profile Views](https://komarev.com/ghpvc/?username=AnonymoDGH&style=for-the-badge&color=00ff9d&labelColor=050510&label=PROFILE+VIEWS)
&nbsp;
[![GitHub followers](https://img.shields.io/github/followers/AnonymoDGH?style=for-the-badge&color=00ff9d&labelColor=050510)](https://github.com/AnonymoDGH?tab=followers)
&nbsp;
[![GitHub stars](https://img.shields.io/github/stars/AnonymoDGH?style=for-the-badge&color=00ff9d&labelColor=050510)](https://github.com/AnonymoDGH)

</div>

---

## `$ whoami`

```
┌─────────────────────────────────────────────────────────────────┐
│  handle    :: AnonymoDGH (P1bub)                                │
│  location  :: Colombia 🇨🇴                                       │
│  focus     :: security tooling · reverse engineering · bots     │
│  stack     :: Python · JavaScript/Node.js · TypeScript · C      │
│  publish   :: 7 paquetes en PyPI · mineflayer-schem en npm      │
│  status    :: perpetuamente construyendo algo maldito (y cool)  │
└─────────────────────────────────────────────────────────────────┘
```

Automato lo aburrido... y también lo que no debería automatizarse. Me meto en las tripas de las cosas: los <b>módulos de Webpack de Discord</b>, la <b>capa de protocolo de Minecraft</b>, las APIs internas de <b>Qwen y Baidu</b>, y cualquier sistema que parezca opaco. Si tiene un endpoint, un store interno o un paquete NBT, lo encuentro.

Últimamente: construí un <b>toolkit completo de seguridad en Python puro</b> — 7 paquetes publicados en PyPI, ~74.000 líneas de código y más de 3.400 tests.

---

## 🐍 `$ pip install` — The Toolkit

> Siete herramientas de seguridad con temática de espionaje, escritas en **Python puro (stdlib only)**, con tests deterministas y publicadas en PyPI. Todas nacieron como props de investigación para ficción y terminaron siendo implementaciones reales y completas.

| Paquete | Qué hace | Instalar |
|---|---|---|
| 📖 **[book-cipher-kit](https://github.com/AnonymoDGH/book-cipher-kit)** | Cifrado de libro con Shamir secret sharing, audit trail, word map de voz y TUI | `pip install book-cipher-kit` |
| 📡 **[dns-tunnel-messenger](https://github.com/AnonymoDGH/dns-tunnel-messenger)** | Mensajería encubierta sobre DNS: traffic shaping, fragmentación, anti-replay, fuzz suite | `pip install dns-tunnel-messenger` |
| 🖼️ **[metadata-stripper](https://github.com/AnonymoDGH/metadata-stripper)** | Limpia metadatos (EXIF/HEIF/PDF/Office/audio/vídeo), motor de riesgo, forense GPS, servicio HTTP | `pip install metadata-stripper` |
| 🍯 **[honeypot-server](https://github.com/AnonymoDGH/honeypot-server)** | Plataforma de decepción: 8 protocolos falsos, tar pit, canary tokens, clasificador TTP (MITRE), deception score | `pip install honeypot-server` |
| 🔓 **[hash-auditor](https://github.com/AnonymoDGH/hash-auditor)** | Laboratorio de auditoría de contraseñas: rainbow tables, PCFG, máscaras hashcat, zxcvbn-lite, políticas | `pip install hash-auditor` |
| 🎭 **[cover-identity](https://github.com/AnonymoDGH/cover-identity)** | Generador de identidades encubiertas consistentes: dossier completo, bóveda cifrada, simulacros de interrogatorio | `pip install cover-identity` |
| 🪤 **[deadman-switch](https://github.com/AnonymoDGH/deadman-switch)** | Interruptor del hombre muerto: heartbeats firmados, proof-of-life con duress, quórum de cancelación, legado digital | `pip install deadman-switch` |

<div align="center">

![toolkit](https://img.shields.io/badge/74k-líneas_de_código-00ff9d?style=for-the-badge&labelColor=050510)
![tests](https://img.shields.io/badge/3.4k_tests-pasando-00ff9d?style=for-the-badge&labelColor=050510)
![stdlib](https://img.shields.io/badge/100%25-stdlib-00ff9d?style=for-the-badge&labelColor=050510)
![pypi](https://img.shields.io/badge/PyPI-v0.2.0-00ff9d?style=for-the-badge&logo=pypi&labelColor=050510)

</div>

---

## 🔧 `$ reverse-engineering`

Clientes async construidos desde cero a partir de las APIs internas, sin SDK oficial:

- **[Qwen-Reverse](https://github.com/AnonymoDGH/Qwen-Reverse)** — cliente async de chat.qwen.ai: streaming con razonamiento en tiempo real, tool calling, imagen y vídeo
- **[baidu-reverse](https://github.com/AnonymoDGH/baidu-reverse)** — cliente async de Baidu Wenxin (chat.baidu.com): streaming, razonamiento, pool de proxies
- **[reverse-agent](https://github.com/AnonymoDGH/reverse-agent)** — agente de coding multi-proveedor para terminal (Qwen-reverse + OpenRouter, Groq, DeepSeek...)
- **[gguf2bin](https://github.com/AnonymoDGH/gguf2bin)** — runtime C99 propio: GGUF → G2BX → inferencia (Qwen3 / Qwen2 / Llama)

---

## 📌 `$ ls ./projects --destacados`

<div align="center">
<table>
<tr>
<td width="50%">

[![mineflayer-schem](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=mineflayer-schem&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/mineflayer-schem)

</td>
<td width="50%">

[![Discord-Quest-Auto-Completer](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=Discord-Quest-Auto-Completer&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/Discord-Quest-Auto-Completer)

</td>
</tr>
<tr>
<td width="50%">

[![Armonia](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=Armonia&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/Armonia)

</td>
<td width="50%">

[![Qwen-Reverse](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=Qwen-Reverse&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/Qwen-Reverse)

</td>
</tr>
<tr>
<td width="50%">

[![vital-agent](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=vital-agent&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/vital-agent)

</td>
<td width="50%">

[![OurBook](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=OurBook&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/OurBook)

</td>
</tr>
<tr>
<td width="50%">

[![ultimate-free-llm-resources](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=ultimate-free-llm-resources&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/ultimate-free-llm-resources)

</td>
<td width="50%">

[![gguf2bin](https://github-readme-stats.vercel.app/api/pin/?username=AnonymoDGH&repo=gguf2bin&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&icon_color=00ff9d)](https://github.com/AnonymoDGH/gguf2bin)

</td>
</tr>
</table>
</div>

**Menciones rápidas:**

- 🎵 **[Armonia](https://github.com/AnonymoDGH/Armonia)** — genera música desde lenguaje natural, entrenado en 214K partituras reales → WAV, MIDI y ABC
- 💗 **[vital-agent](https://github.com/AnonymoDGH/vital-agent)** — agente autónomo de "life-credit" que debe ganar su propio dinero... o muere (TUI estilo Cursor con Textual)
- 📖 **[OurBook](https://github.com/AnonymoDGH/OurBook)** — el primer MCP donde el agente no recuerda tus datos, recuerda tu *historia*
- 🤖 **[mineflayer-schem](https://github.com/AnonymoDGH/mineflayer-schem)** — plugin de mineflayer para construir estructuras desde schematics (`npm i mineflayer-schem`, v1.5.2, +50 commits de fixes sobre el original)
- 🎮 **[Discord-Quest-Auto-Completer](https://github.com/AnonymoDGH/Discord-Quest-Auto-Completer)** — completa quests de Discord inyectándose en el webpack interno, cero dependencias
- 🧠 **[rdru-lm](https://github.com/AnonymoDGH/rdru-lm)** — language model character-level que aplica el mismo bloque transformer iterativamente + objetivo de denoising
- 📚 **[ultimate-free-llm-resources](https://github.com/AnonymoDGH/ultimate-free-llm-resources)** — la colección más completa de recursos LLM gratuitos: APIs, modelos, herramientas

---

## 🛠️ `$ cat ./stack.json`

**Lenguajes**

![Python](https://img.shields.io/badge/Python-050510?style=for-the-badge&logo=python&logoColor=00ff9d)
![JavaScript](https://img.shields.io/badge/JavaScript-050510?style=for-the-badge&logo=javascript&logoColor=00ff9d)
![TypeScript](https://img.shields.io/badge/TypeScript-050510?style=for-the-badge&logo=typescript&logoColor=00ff9d)
![Node.js](https://img.shields.io/badge/Node.js-050510?style=for-the-badge&logo=node.js&logoColor=00ff9d)
![C](https://img.shields.io/badge/C-050510?style=for-the-badge&logo=c&logoColor=00ff9d)
![C++](https://img.shields.io/badge/C++-050510?style=for-the-badge&logo=cplusplus&logoColor=00ff9d)

**Seguridad & Testing**

![pytest](https://img.shields.io/badge/pytest-050510?style=for-the-badge&logo=pytest&logoColor=00ff9d)
![PyPI](https://img.shields.io/badge/PyPI-publishing-050510?style=for-the-badge&logo=pypi&logoColor=00ff9d)
![Wireshark](https://img.shields.io/badge/Wireshark-050510?style=for-the-badge&logo=wireshark&logoColor=00ff9d)
![Linux](https://img.shields.io/badge/Linux-050510?style=for-the-badge&logo=linux&logoColor=00ff9d)

**Web & Tooling**

![React](https://img.shields.io/badge/React-050510?style=for-the-badge&logo=react&logoColor=00ff9d)
![Next.js](https://img.shields.io/badge/Next.js-050510?style=for-the-badge&logo=next.js&logoColor=00ff9d)
![Docker](https://img.shields.io/badge/Docker-050510?style=for-the-badge&logo=docker&logoColor=00ff9d)
![Git](https://img.shields.io/badge/Git-050510?style=for-the-badge&logo=git&logoColor=00ff9d)
![Webpack](https://img.shields.io/badge/Webpack-internals-050510?style=for-the-badge&logo=webpack&logoColor=00ff9d)

**Ecosistema Minecraft**

![Prismarine](https://img.shields.io/badge/Prismarine-mineflayer-050510?style=for-the-badge&logo=minecraft&logoColor=00ff9d)
![npm](https://img.shields.io/badge/npm-mineflayer--schem-050510?style=for-the-badge&logo=npm&logoColor=00ff9d)

---

## 📊 `$ cat ./stats.log`

<div align="center">

<img height="185" src="https://github-readme-stats.vercel.app/api?username=AnonymoDGH&show_icons=true&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&icon_color=00ff9d&text_color=c9c9dd&count_private=true&include_all_commits=true&ring_color=00ff9d" />
<img height="185" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AnonymoDGH&layout=compact&bg_color=05051000&border_color=00ff9d80&title_color=00ff9d&text_color=c9c9dd&langs_count=8" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com?user=AnonymoDGH&theme=dark&background=05051000&border=00ff9d80&stroke=00ff9d&ring=00ff9d&fire=7fff00&currStreakNum=ffffff&sideNums=c9c9dd&currStreakLabel=00ff9d&sideLabels=7a7a9a&dates=5a5a75" width="90%"/>

</div>

---

## 📈 `$ tail -f ./activity.log`

<div align="center">

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=AnonymoDGH&bg_color=05051000&color=00ff9d&line=00ff9d&point=7fff00&area=true&border_color=00ff9d80&title_color=00ff9d)](https://github.com/ashutosh00710/github-readme-activity-graph)

</div>

---

## 🐍 `$ ./contrib-snake --run`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnonymoDGH/AnonymoDGH/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AnonymoDGH/AnonymoDGH/output/github-contribution-grid-snake.svg">
  <img alt="contribution snake" src="https://raw.githubusercontent.com/AnonymoDGH/AnonymoDGH/output/github-contribution-grid-snake-dark.svg" width="95%">
</picture>

</div>

---

## 📬 `$ ping ./contact`

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-AnonymoDGH-050510?style=for-the-badge&logo=github&logoColor=00ff9d)](https://github.com/AnonymoDGH)
[![PyPI](https://img.shields.io/badge/PyPI-AnonymoDGH-050510?style=for-the-badge&logo=pypi&logoColor=00ff9d)](https://pypi.org/user/AnonymoDGH/)
[![npm](https://img.shields.io/badge/npm-anonymodgh-050510?style=for-the-badge&logo=npm&logoColor=00ff9d)](https://www.npmjs.com/~anonymodgh)

Si tienes una idea rara, un bug interesante o quieres colaborar — dime.

</div>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0f2e,100:050510&height=120&section=footer&text=EOF%20%E2%80%A2%20AnonymoDGH%20%E2%80%A2%20Colombia&fontSize=16&fontColor=00ff9d&fontAlignY=70&animation=fadeIn" />

</div>