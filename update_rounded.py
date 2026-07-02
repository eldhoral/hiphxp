import re

with open("index-achromatic.html", "r") as f:
    html = f.read()

# Nav submit button
html = html.replace('class="magnetic-el inline-flex items-center justify-center px-6 py-2 border-2', 'class="magnetic-el inline-flex items-center justify-center px-6 py-2 rounded-full border-2')

# Mobile menu submit button
html = html.replace('class="mobile-menu-link w-full text-center px-6 py-4 border-2 border-accent', 'class="mobile-menu-link w-full text-center px-6 py-4 rounded-full border-2 border-accent')

# Hero tag
html = html.replace('class="gsap-hero-el text-accent font-mono text-sm md:text-base tracking-widest uppercase mb-4 font-bold inline-block border border-accent/30 px-3 py-1 bg-accent/10"', 'class="gsap-hero-el text-accent font-mono text-sm md:text-base tracking-widest uppercase mb-4 font-bold inline-block border border-accent/30 rounded-full px-3 py-1 bg-accent/10"')

# Hero explore button
html = html.replace('class="magnetic-el hover-target inline-flex items-center justify-center px-8 py-4 border-2 border-border', 'class="magnetic-el hover-target inline-flex items-center justify-center px-8 py-4 rounded-full border-2 border-border')

# Track cards
html = html.replace('class="gsap-grid-item hover-target group relative bg-muted/30 border border-border/50 hover:border-accent transition-colors duration-300 p-4"', 'class="gsap-grid-item hover-target group relative bg-muted/30 border border-border/50 rounded-2xl hover:border-accent transition-colors duration-300 p-4"')

# Track images
html = html.replace('class="aspect-square bg-zinc-800 mb-4 relative overflow-hidden', 'class="aspect-square bg-zinc-800 rounded-xl mb-4 relative overflow-hidden')

# View All button
html = html.replace('class="px-8 py-4 border-2 border-border text-foreground', 'class="px-8 py-4 rounded-full border-2 border-border text-foreground')

# Design switcher btn
html = html.replace('class="px-6 py-3 bg-zinc-100 text-zinc-900 border-2 border-zinc-900', 'class="px-6 py-3 bg-zinc-100 text-zinc-900 border-2 border-zinc-900 rounded-full')

# Design switcher menu
html = html.replace('hidden flex-col shadow-2xl overflow-hidden rounded-md', 'hidden flex-col shadow-2xl overflow-hidden rounded-2xl')

with open("index-achromatic.html", "w") as f:
    f.write(html)
print("Updated to rounded design")
