"""Wrap locally generated Platane/snk SVGs in a self-contained profile header."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    'dark': ('#0d1117', '#29313b', '#e6edf3', '#8b949e', '#3fb950', '#bf77e8'),
    'light': ('#ffffff', '#d8dee4', '#1f2328', '#656d76', '#1a7f37', '#8954c7'),
}

for theme, (bg, border, ink, muted, green, purple) in THEMES.items():
    snake = (ROOT / f'assets/snake-{theme}.svg').read_text()
    # Nest vector contents, not an external image: animations work in README <img>.
    snake = re.sub(r'<svg\b[^>]*>', '<svg x="24" y="125" width="952" height="208" viewBox="-16 -32 880 192">', snake, count=1)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="378" viewBox="0 0 1000 378" role="img" aria-labelledby="title desc">
<title id="title">麋鹿 MILU — GitHub contribution snake</title>
<desc id="desc">xiehang0616 的真实 GitHub 贡献记录。紫色贪吃蛇沿绿色贡献格子移动，动画循环播放。</desc>
<style>
 .label{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}}
 .copy{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif}}
 @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect x=".5" y=".5" width="999" height="377" rx="18" fill="{bg}" stroke="{border}"/>
<g transform="translate(38 37)" fill="none" stroke="{green}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
 <path d="M14 19 7 10 7 0 M7 8 0 5 M7 4 12 0 M22 19 29 10 29 0 M29 8 36 5 M29 4 24 0"/>
 <path d="M10 17 18 21 26 17 24 32 18 38 12 32Z"/>
 <path d="M14 27h.1 M22 27h.1 M17 33h2"/>
</g>
<text class="label" x="96" y="65" fill="{ink}" font-size="32" font-weight="700" letter-spacing="2">MILU<tspan class="copy" fill="{muted}" font-size="22" font-weight="400" letter-spacing="0"> / 麋鹿</tspan></text>
<text class="label" x="958" y="51" fill="{muted}" font-size="12" text-anchor="end">@xiehang0616</text>
<circle cx="830" cy="73" r="3" fill="{green}"/>
<text class="label" x="958" y="77" fill="{muted}" font-size="10" text-anchor="end" letter-spacing="1.4">ALWAYS EXPLORING</text>
<text class="copy" x="39" y="111" fill="{muted}" font-size="16">把 AI 想法，做成可以体验的作品。</text>
<path d="M39 134H961" stroke="{border}"/>
{snake}
<text class="label" x="39" y="356" fill="{muted}" font-size="10" letter-spacing="1.5">A LITTLE PROGRESS, EVERY DAY.</text>
<rect x="821" y="348" width="7" height="7" rx="2" fill="{purple}"/>
<text class="label" x="958" y="356" fill="{muted}" font-size="10" text-anchor="end">CONTRIBUTION SNAKE</text>
</svg>'''
    ET.fromstring(svg)
    path = ROOT / f'assets/milu-header-{theme}.svg'
    path.write_text(svg)
    print(f'Generated {path.name}: {len(svg.encode()):,} bytes')
