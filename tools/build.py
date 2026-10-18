#!/usr/bin/env python3
# /// script
# dependencies = [
#     "pyyaml>=6.0",
#     "markdown>=3.6",
#     "jinja2>=3.1",
# ]
# ///
import argparse
from pathlib import Path
import re
import shutil
import sys
import yaml
import markdown
from jinja2 import Environment, FileSystemLoader

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
NOTES_DIR = ROOT_DIR / "notes"
TEMPLATES_DIR = ROOT_DIR / "templates"
ASSETS_DIR = ROOT_DIR / "assets"
PICS_DIR = ROOT_DIR / "pics"

# Configure Jinja2 environment
env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,
)

def clean_markdown_for_web(text: str) -> str:
    """Normalize image paths, links, mermaid diagrams, and mkdocs syntax"""
    # 1. Mermaid code blocks: ```mermaid ... ``` -> <pre class="mermaid">...</pre>
    def replace_mermaid(match):
        code = match.group(1).strip()
        return f'<pre class="mermaid">\n{code}\n</pre>\n'
    text = re.sub(r'```mermaid\s*\n([\s\S]*?)\n```', replace_mermaid, text)

    # 2. Strip MkDocs attribute annotations like {: loading=lazy }, { loading=lazy }, { #anchor }, { .md-button }, { width=750 }, { .lg .middle }
    text = re.sub(r'\{\s*[:.#][^}]+\}', '', text)
    text = re.sub(r'\{\s*(?:loading=lazy|width=\d+)\s*\}', '', text)

    # 3. Strip MkDocs icon shortcuts like :material-chip:, :octicons-arrow-right-24:
    text = re.sub(r':(?:material|octicons|fontawesome)-[a-z0-9-]+:', '', text)

    # 4. Remove MkDocs specific wrapper div containers
    text = re.sub(r'</?div(?:\s+class="[^"]*")?(?:\s+markdown)?>', '', text)

    # 5. Normalize relative image paths to pics/...
    text = re.sub(r'\((\.\./)+pics/', '(pics/', text)
    text = re.sub(r'\(\./pics/', '(pics/', text)

    # 6. Section index links
    text = re.sub(r'\]\((?:\.\./)?hardware/index\.md\)', r'](hardware.html)', text)
    text = re.sub(r'\]\((?:\.\./)?esphome/index\.md\)', r'](esphome.html)', text)
    text = re.sub(r'\]\((?:\.\./)?homeassistant/index\.md\)', r'](homeassistant.html)', text)
    text = re.sub(r'\]\((?:\.\./)?guides/index\.md\)', r'](guides.html)', text)
    text = re.sub(r'\]\((?:\.\./)?index\.md\)', r'](index.html)', text)

    # 7. Inter-page markdown links: ](hardware/sensor-12x6.md#anchor) -> ](sensor-12x6.html#anchor)
    text = re.sub(
        r'\]\((?:\.\./)?(?:hardware/|esphome/|homeassistant/|guides/)?([a-zA-Z0-9_.-]+)\.md(#[^)]+)?\)',
        r'](\1.html\2)',
        text
    )

    # 8. Convert MkDocs content tabs (=== "Title") to clean section subheadings
    lines = text.splitlines()
    processed_lines = []
    in_tab = False
    for line in lines:
        tab_match = re.match(r'^===\s+"(.*)"\s*$', line.strip())
        if tab_match:
            title = tab_match.group(1).replace(r'\"', '"')
            processed_lines.append(f'<h5 class="mt-4 mb-2 text-info">{title}</h5>')
            in_tab = True
        elif in_tab:
            if line.startswith("    "):
                processed_lines.append(line[4:])
            elif line.strip() == "":
                processed_lines.append("")
            else:
                in_tab = False
                processed_lines.append(line)
        else:
            processed_lines.append(line)
    text = "\n".join(processed_lines)

    # 9. Convert collapsible blocks (??? code "Title") and admonitions (!!! note "Title")
    text = re.sub(r'^\?\?\?\+?\s+(?:[a-zA-Z0-9_-]+)?(?:\s+"([^"]+)")?', r'> **\1**\n>', text, flags=re.MULTILINE)
    text = re.sub(r'^!!!\s+([a-zA-Z0-9_-]+)(?:\s+"([^"]+)")?', r'> **\2**\n>', text, flags=re.MULTILINE)

    return text.strip() + "\n"

def md_to_html(md_text: str) -> str:
    """Convert cleaned markdown to semantic HTML"""
    return markdown.markdown(
        md_text,
        extensions=['extra', 'tables', 'fenced_code', 'toc', 'sane_lists']
    )

def read_note(filename: str) -> str:
    """Read a markdown file directly from the notes/ directory and render to HTML"""
    file_path = NOTES_DIR / filename
    if not file_path.exists():
        print(f"Warning: Note file not found: {file_path}", file=sys.stderr)
        return ""
    raw_md = file_path.read_text(encoding="utf-8")
    cleaned_md = clean_markdown_for_web(raw_md)
    return md_to_html(cleaned_md)

def build_site(outdir: Path):
    """Build the complete static website into outdir"""
    outdir.mkdir(parents=True, exist_ok=True)

    # 1. Copy static assets and pictures
    out_assets = outdir / "assets"
    if out_assets.exists():
        shutil.rmtree(out_assets)
    shutil.copytree(ASSETS_DIR, out_assets)

    out_pics = outdir / "pics"
    if out_pics.exists():
        shutil.rmtree(out_pics)
    shutil.copytree(PICS_DIR, out_pics)

    # Create .nojekyll for GitHub Pages
    (outdir / ".nojekyll").touch(exist_ok=True)

    # 2. Load YAML data files
    site_data = yaml.safe_load((DATA_DIR / "site.yml").read_text(encoding="utf-8"))
    hardware_data = yaml.safe_load((DATA_DIR / "hardware.yml").read_text(encoding="utf-8"))
    esphome_data = yaml.safe_load((DATA_DIR / "esphome.yml").read_text(encoding="utf-8"))
    homeassistant_data = yaml.safe_load((DATA_DIR / "homeassistant.yml").read_text(encoding="utf-8"))
    guides_data = yaml.safe_load((DATA_DIR / "guides.yml").read_text(encoding="utf-8"))
    specs_data = yaml.safe_load((DATA_DIR / "specs.yml").read_text(encoding="utf-8"))
    about_data = yaml.safe_load((DATA_DIR / "about.yml").read_text(encoding="utf-8"))

    # Set globals so all templates (including partials like header.html) have direct access to item arrays
    env.globals["hardware_items"] = hardware_data["items"]
    env.globals["esphome_items"] = esphome_data["items"]
    env.globals["homeassistant_items"] = homeassistant_data["items"]
    env.globals["guides_items"] = guides_data["items"]

    # 3. Render Landing Page
    index_tpl = env.get_template("index.html")
    index_html = index_tpl.render(
        title="Open IoT & Smart Home Ecosystem",
        description="Modular LEGO-mounted environmental sensor carriers, low-power E-Paper smart clocks, ESPHome fleet firmware, and coordinated Home Assistant automations.",
        active_page="home",
        active_group="home",
        site=site_data,
        about=about_data,
        hardware=hardware_data,
        esphome=esphome_data,
        homeassistant=homeassistant_data,
        guides=guides_data,
        specs=specs_data,
    )
    (outdir / "index.html").write_text(index_html, encoding="utf-8")

    # 4. Render About Page (sourced directly from notes/about.md)
    about_file = about_data.get("file", "about.md")
    about_tpl = env.get_template("about.html")
    about_html = about_tpl.render(
        title="About Project & Ecosystem Architecture",
        description="Open-source modular IoT ecosystem, ESPHome fleet, and Home Assistant automation",
        active_page="about",
        active_group="about",
        site=site_data,
        about=about_data,
        html_content=read_note(about_file),
    )
    (outdir / "about.html").write_text(about_html, encoding="utf-8")

    # 5. Render Specs Page
    specs_tpl = env.get_template("specs.html")
    specs_html = specs_tpl.render(
        title="Hardware Comparison Lineup",
        description="Comprehensive specifications for custom carrier boards and deployed IoT fleet nodes",
        active_page="specs",
        active_group="specs",
        site=site_data,
        specs=specs_data,
    )
    (outdir / "specs.html").write_text(specs_html, encoding="utf-8")

    # 6. Render Catalog Pages
    catalog_tpl = env.get_template("catalog.html")
    catalog_configs = [
        ("hardware", "Hardware", "Custom KiCad sensor carrier boards sized for standard LEGO plate footprints", hardware_data["items"], "#6cb670"),
        ("esphome", "ESPHome", "Production catalog of 41 nodes across rooms, e-paper display drivers, and YAML configurations", esphome_data["items"], "#fbbf24"),
        ("homeassistant", "Home Assistant Hub", "Central coordination server, encrypted API stream, and 10 production automation blueprints", homeassistant_data["items"], "#38bdf8"),
        ("guides", "Hardware & Build Guides", "Assembly guides, component placement, pinout matrices, and OTA deployment workflows", guides_data["items"], "#f472b6"),
    ]

    for cat_id, cat_title, cat_subtitle, cat_items, cat_accent in catalog_configs:
        cat_html = catalog_tpl.render(
            title=cat_title,
            subtitle=cat_subtitle,
            description=cat_subtitle,
            active_page=cat_id,
            active_group=cat_id,
            site=site_data,
            items=cat_items,
            accent_color=cat_accent,
        )
        (outdir / f"{cat_id}.html").write_text(cat_html, encoding="utf-8")

    # 7. Render Detail Pages (content sourced directly from notes/<item.file>)
    detail_tpl = env.get_template("detail.html")
    detail_configs = [
        (hardware_data["items"], "Hardware", "hardware.html", "hardware", "#6cb670"),
        (esphome_data["items"], "ESPHome", "esphome.html", "esphome", "#fbbf24"),
        (homeassistant_data["items"], "Home Assistant Hub", "homeassistant.html", "homeassistant", "#38bdf8"),
        (guides_data["items"], "Build Guides", "guides.html", "guides", "#f472b6"),
    ]

    count = 0
    for items, parent_title, parent_url, group_id, accent_color in detail_configs:
        num_items = len(items)
        for idx, item in enumerate(items):
            prev_item = items[idx - 1] if idx > 0 else None
            next_item = items[idx + 1] if idx < num_items - 1 else None
            note_filename = item.get("file", f"{item['id']}.md")
            rendered_content = read_note(note_filename)
            det_html = detail_tpl.render(
                title=item["title"],
                description=item.get("summary", ""),
                active_page=item["id"],
                active_group=group_id,
                accent_color=accent_color,
                site=site_data,
                item=item,
                parent_title=parent_title,
                parent_url=parent_url,
                siblings=items,
                prev_item=prev_item,
                next_item=next_item,
                html_content=rendered_content,
            )
            (outdir / f"{item['id']}.html").write_text(det_html, encoding="utf-8")
            count += 1

    total_pages = count + 7
    print(f"Successfully built {total_pages} pages into '{outdir}'!")

def main():
    parser = argparse.ArgumentParser(description="Build IoT static website from markdown notes and templates")
    parser.add_argument("--outdir", default="_site", help="Destination directory for built static site (default: _site)")
    args = parser.parse_args()

    out_path = Path(args.outdir)
    if not out_path.is_absolute():
        out_path = ROOT_DIR / out_path

    build_site(out_path)

if __name__ == "__main__":
    main()
