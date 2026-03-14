<div align="center">

<!-- ANIMATED BANNER SVG -->
<svg width="860" height="160" viewBox="0 0 860 160" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0d0d"/>
      <stop offset="100%" style="stop-color:#0a0a1a"/>
    </linearGradient>
    <linearGradient id="line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00ff9d;stop-opacity:0"/>
      <stop offset="50%" style="stop-color:#00ff9d;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#00ff9d;stop-opacity:0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow2">
      <feGaussianBlur stdDeviation="6" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .title { font-family: 'Courier New', monospace; fill: #00ff9d; filter: url(#glow); }
      .subtitle { font-family: 'Courier New', monospace; fill: #888; }
      .cursor { animation: blink 1s infinite; }
      .scan { animation: scan 4s linear infinite; }
      .fade-in { animation: fadeIn 2s ease forwards; }
      @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
      @keyframes scan { 0%{transform:translateY(-160px)} 100%{transform:translateY(320px)} }
      @keyframes fadeIn { from{opacity:0} to{opacity:1} }
    </style>
  </defs>

  <rect width="860" height="160" fill="url(#bg)" rx="12"/>

  <!-- Grid lines -->
  <g opacity="0.07" stroke="#00ff9d" stroke-width="0.5">
    <line x1="0" y1="20" x2="860" y2="20"/>
    <line x1="0" y1="40" x2="860" y2="40"/>
    <line x1="0" y1="60" x2="860" y2="60"/>
    <line x1="0" y1="80" x2="860" y2="80"/>
    <line x1="0" y1="100" x2="860" y2="100"/>
    <line x1="0" y1="120" x2="860" y2="120"/>
    <line x1="0" y1="140" x2="860" y2="140"/>
    <line x1="86" y1="0" x2="86" y2="160"/>
    <line x1="172" y1="0" x2="172" y2="160"/>
    <line x1="258" y1="0" x2="258" y2="160"/>
    <line x1="344" y1="0" x2="344" y2="160"/>
    <line x1="430" y1="0" x2="430" y2="160"/>
    <line x1="516" y1="0" x2="516" y2="160"/>
    <line x1="602" y1="0" x2="602" y2="160"/>
    <line x1="688" y1="0" x2="688" y2="160"/>
    <line x1="774" y1="0" x2="774" y2="160"/>
  </g>

  <!-- Scan line -->
  <rect class="scan" x="0" y="0" width="860" height="3" fill="url(#line)" opacity="0.3"/>

  <!-- Corner brackets -->
  <g stroke="#00ff9d" stroke-width="2" fill="none" opacity="0.8" filter="url(#glow)">
    <path d="M20,12 L12,12 L12,28"/>
    <path d="M840,12 L848,12 L848,28"/>
    <path d="M20,148 L12,148 L12,132"/>
    <path d="M840,148 L848,148 L848,132"/>
  </g>

  <!-- Main title -->
  <text x="430" y="72" text-anchor="middle" class="title" font-size="38" font-weight="bold" letter-spacing="6" filter="url(#glow2)">AnonymoDGH</text>

  <!-- Subtitle -->
  <text x="430" y="100" text-anchor="middle" class="subtitle" font-size="13" letter-spacing="3">
    <tspan fill="#00ff9d" opacity="0.7">&gt; </tspan>
    <tspan fill="#ccc">developer</tspan>
    <tspan fill="#555"> // </tspan>
    <tspan fill="#ccc">builder</tspan>
    <tspan fill="#555"> // </tspan>
    <tspan fill="#ccc">hacker</tspan>
    <tspan class="cursor" fill="#00ff9d">_</tspan>
  </text>

  <!-- Bottom line -->
  <rect x="80" y="130" width="700" height="1" fill="url(#line)" opacity="0.5"/>
  <text x="430" y="148" text-anchor="middle" class="subtitle" font-size="10" letter-spacing="4" fill="#00ff9d" opacity="0.4">SYSTEM ONLINE</text>
</svg>

<!-- TYPING SVG -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=800&color=00FF9D&center=true&vCenter=true&multiline=false&width=600&lines=Building+things+that+matter.;Breaking+things+to+understand+them.;chmod+%2Bx+everything.;%24+git+push+origin+main+--force)](https://git.io/typing-svg)

<br/>

<!-- STATUS BADGES -->
![](https://komarev.com/ghpvc/?username=AnonymoDGH&style=for-the-badge&color=00ff9d&labelColor=0d0d0d&label=VISITS)
&nbsp;
[![GitHub followers](https://img.shields.io/github/followers/AnonymoDGH?style=for-the-badge&color=00ff9d&labelColor=0d0d0d&label=FOLLOWERS)](https://github.com/AnonymoDGH)

</div>

---

## `> whoami`

```bash
$ cat /etc/profile.d/anonymodgh.sh

NAME="AnonymoDGH"
ROLE="Full Stack Developer & Security Enthusiast"
LOCATION="Colombia 🇨🇴"
STATUS="Always building something"
COFFEE_DEPENDENCY=true
```

---

## `> ls -la ./stack`

<div align="center">

<!-- LANGUAGES -->
**Languages**

![Python](https://img.shields.io/badge/Python-0d0d0d?style=for-the-badge&logo=python&logoColor=00ff9d)
![JavaScript](https://img.shields.io/badge/JavaScript-0d0d0d?style=for-the-badge&logo=javascript&logoColor=00ff9d)
![TypeScript](https://img.shields.io/badge/TypeScript-0d0d0d?style=for-the-badge&logo=typescript&logoColor=00ff9d)
![Go](https://img.shields.io/badge/Go-0d0d0d?style=for-the-badge&logo=go&logoColor=00ff9d)
![Bash](https://img.shields.io/badge/Bash-0d0d0d?style=for-the-badge&logo=gnubash&logoColor=00ff9d)
![Rust](https://img.shields.io/badge/Rust-0d0d0d?style=for-the-badge&logo=rust&logoColor=00ff9d)

**Frontend**

![React](https://img.shields.io/badge/React-0d0d0d?style=for-the-badge&logo=react&logoColor=00ff9d)
![Next.js](https://img.shields.io/badge/Next.js-0d0d0d?style=for-the-badge&logo=next.js&logoColor=00ff9d)
![TailwindCSS](https://img.shields.io/badge/Tailwind-0d0d0d?style=for-the-badge&logo=tailwindcss&logoColor=00ff9d)

**Backend & Infra**

![Node.js](https://img.shields.io/badge/Node.js-0d0d0d?style=for-the-badge&logo=node.js&logoColor=00ff9d)
![Docker](https://img.shields.io/badge/Docker-0d0d0d?style=for-the-badge&logo=docker&logoColor=00ff9d)
![Linux](https://img.shields.io/badge/Linux-0d0d0d?style=for-the-badge&logo=linux&logoColor=00ff9d)
![Nginx](https://img.shields.io/badge/Nginx-0d0d0d?style=for-the-badge&logo=nginx&logoColor=00ff9d)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0d0d0d?style=for-the-badge&logo=postgresql&logoColor=00ff9d)
![Redis](https://img.shields.io/badge/Redis-0d0d0d?style=for-the-badge&logo=redis&logoColor=00ff9d)

</div>

---

## `> cat ./stats.json`

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=AnonymoDGH&show_icons=true&theme=chartreuse-dark&bg_color=0d0d0d&border_color=00ff9d&title_color=00ff9d&icon_color=00ff9d&text_color=aaaaaa&ring_color=00ff9d&hide_border=false&count_private=true" />
&nbsp;
<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AnonymoDGH&layout=compact&theme=chartreuse-dark&bg_color=0d0d0d&border_color=00ff9d&title_color=00ff9d&text_color=aaaaaa&hide_border=false" />

<img src="https://github-readme-streak-stats.herokuapp.com?user=AnonymoDGH&theme=dark&background=0d0d0d&border=00ff9d&stroke=00ff9d&ring=00ff9d&fire=ff6b35&currStreakNum=ffffff&sideNums=ffffff&currStreakLabel=00ff9d&sideLabels=888888&dates=555555" />

</div>

---

## `> tail -f ./activity.log`

<div align="center">

[![AnonymoDGH's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=AnonymoDGH&bg_color=0d0d0d&color=00ff9d&line=00ff9d&point=ffffff&area=true&area_color=00ff9d&hide_border=false&border_color=00ff9d&theme=react-dark)](https://github.com/ashutosh00710/github-readme-activity-graph)

</div>

---

## `> ping ./contact`

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-0d0d0d?style=for-the-badge&logo=github&logoColor=00ff9d)](https://github.com/AnonymoDGH)
[![Twitter](https://img.shields.io/badge/Twitter-0d0d0d?style=for-the-badge&logo=x&logoColor=00ff9d)](https://twitter.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0d0d0d?style=for-the-badge&logo=linkedin&logoColor=00ff9d)](https://linkedin.com/)
[![Email](https://img.shields.io/badge/Email-0d0d0d?style=for-the-badge&logo=gmail&logoColor=00ff9d)](mailto:)

</div>

---

<!-- SNAKE CONTRIBUTION GRAPH -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnonymoDGH/AnonymoDGH/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AnonymoDGH/AnonymoDGH/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/AnonymoDGH/AnonymoDGH/output/github-contribution-grid-snake-dark.svg">
</picture>

</div>

<!-- FOOTER SVG -->
<div align="center">
<svg width="860" height="40" viewBox="0 0 860 40" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00ff9d;stop-opacity:0"/>
      <stop offset="30%" style="stop-color:#00ff9d;stop-opacity:0.6"/>
      <stop offset="70%" style="stop-color:#00ff9d;stop-opacity:0.6"/>
      <stop offset="100%" style="stop-color:#00ff9d;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="860" height="40" fill="#0d0d0d" rx="0"/>
  <rect x="0" y="0" width="860" height="1" fill="url(#fg)"/>
  <text x="430" y="26" text-anchor="middle" font-family="'Courier New', monospace" font-size="11" fill="#00ff9d" opacity="0.4" letter-spacing="4">// EOF — thanks for reading</text>
</svg>
</div>
