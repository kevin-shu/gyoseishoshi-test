"""Extract article text from e-Gov law XML files into structured JSON.

Parses the three administrative law XML files and outputs JSON with
chapter and article structure, including article numbers, captions,
and full paragraph text.

Usage:
    python3 scripts/extract_articles.py
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


REFS_DIR = Path(__file__).parent.parent / "references"
OUTPUT_DIR = Path(__file__).parent

LAWS = {
    "litigation": "行政事件訴訟法.xml",
    "procedure": "行政手続法.xml",
    "appeal": "行政不服審査法.xml",
}


def extract_sentence_text(elem: ET.Element) -> str:
    """Extract all text from Sentence elements, handling nested elements."""
    texts = []
    for sentence in elem.iter("Sentence"):
        text = sentence.text or ""
        for child in sentence:
            text += child.text or ""
            text += child.tail or ""
        texts.append(text.strip())
    return "".join(texts)


def extract_column_text(item_sentence: ET.Element) -> str:
    """Extract text from ItemSentence with Column elements (definition lists)."""
    columns = item_sentence.findall("Column")
    if columns:
        parts = []
        for col in columns:
            col_text = extract_sentence_text(col)
            parts.append(col_text)
        return "　".join(parts)
    return extract_sentence_text(item_sentence)


def extract_subitem(subitem: ET.Element, prefix: str = "") -> dict[str, Any]:
    """Extract a sub-item (Subitem1, Subitem2, etc.)."""
    title_elem = subitem.find(f"{subitem.tag}Title")
    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
    sentence_elem = subitem.find(f"{subitem.tag}Sentence")
    text = ""
    if sentence_elem is not None:
        text = extract_column_text(sentence_elem)
    else:
        text = extract_sentence_text(subitem)

    result: dict[str, Any] = {"title": title, "text": text}

    # Look for deeper sub-items
    deeper_tags = [
        "Subitem1", "Subitem2", "Subitem3", "Subitem4", "Subitem5"
    ]
    for tag in deeper_tags:
        children = subitem.findall(tag)
        if children:
            result["subitems"] = [extract_subitem(c) for c in children]
            break

    return result


def extract_item(item: ET.Element) -> dict[str, Any]:
    """Extract an Item element (号)."""
    title_elem = item.find("ItemTitle")
    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
    sentence_elem = item.find("ItemSentence")
    text = ""
    if sentence_elem is not None:
        text = extract_column_text(sentence_elem)

    result: dict[str, Any] = {"title": title, "text": text}

    # Sub-items
    for tag in ["Subitem1", "Subitem2"]:
        children = item.findall(tag)
        if children:
            result["subitems"] = [extract_subitem(c) for c in children]
            break

    return result


def extract_paragraph(para: ET.Element) -> dict[str, Any]:
    """Extract a Paragraph element (項)."""
    num_elem = para.find("ParagraphNum")
    num = ""
    if num_elem is not None and num_elem.text:
        num = num_elem.text.strip()

    sentence_elem = para.find("ParagraphSentence")
    text = extract_sentence_text(sentence_elem) if sentence_elem is not None else ""

    items = [extract_item(item) for item in para.findall("Item")]

    result: dict[str, Any] = {"num": num, "text": text}
    if items:
        result["items"] = items

    return result


def extract_article(article: ET.Element) -> dict[str, Any]:
    """Extract an Article element (条)."""
    num = article.get("Num", "")
    caption_elem = article.find("ArticleCaption")
    caption = ""
    if caption_elem is not None and caption_elem.text:
        caption = caption_elem.text.strip().strip("（）()")

    title_elem = article.find("ArticleTitle")
    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""

    paragraphs = [extract_paragraph(p) for p in article.findall("Paragraph")]

    return {
        "num": num,
        "caption": caption,
        "title": title,
        "paragraphs": paragraphs,
    }


def extract_section(section: ET.Element) -> dict[str, Any]:
    """Extract a Section element (節)."""
    title_elem = section.find("SectionTitle")
    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""

    articles = [extract_article(a) for a in section.findall("Article")]

    result: dict[str, Any] = {"title": title, "articles": articles}

    # Subsections (款)
    subsections = section.findall("Subsection")
    if subsections:
        result["subsections"] = []
        for ss in subsections:
            ss_title_elem = ss.find("SubsectionTitle")
            ss_title = ss_title_elem.text.strip() if ss_title_elem is not None and ss_title_elem.text else ""
            ss_articles = [extract_article(a) for a in ss.findall("Article")]
            result["subsections"].append({
                "title": ss_title,
                "articles": ss_articles,
            })

    return result


def extract_chapter(chapter: ET.Element) -> dict[str, Any]:
    """Extract a Chapter element (章)."""
    num = chapter.get("Num", "")
    title_elem = chapter.find("ChapterTitle")
    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""

    # Direct articles (no section)
    direct_articles = [extract_article(a) for a in chapter.findall("Article")]

    # Sections
    sections = [extract_section(s) for s in chapter.findall("Section")]

    result: dict[str, Any] = {
        "num": num,
        "title": title,
    }

    if sections:
        result["sections"] = sections
    if direct_articles:
        result["articles"] = direct_articles

    return result


def extract_law(xml_path: Path) -> dict[str, Any]:
    """Extract full law structure from XML."""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    law_num_elem = root.find("LawNum")
    law_num = law_num_elem.text.strip() if law_num_elem is not None and law_num_elem.text else ""

    body = root.find("LawBody")
    title_elem = body.find("LawTitle") if body is not None else None
    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""

    main = body.find("MainProvision") if body is not None else None
    chapters = [extract_chapter(ch) for ch in main.findall("Chapter")] if main is not None else []

    return {
        "law_num": law_num,
        "title": title,
        "chapters": chapters,
    }


def main() -> None:
    """Extract all three laws and write JSON output."""
    for key, filename in LAWS.items():
        xml_path = REFS_DIR / filename
        if not xml_path.exists():
            print(f"WARNING: {xml_path} not found, skipping")
            continue

        print(f"Extracting {filename}...")
        law = extract_law(xml_path)

        total_articles = 0
        for ch in law["chapters"]:
            total_articles += len(ch.get("articles", []))
            for sec in ch.get("sections", []):
                total_articles += len(sec.get("articles", []))
                for ss in sec.get("subsections", []):
                    total_articles += len(ss.get("articles", []))

        print(f"  {law['title']}: {len(law['chapters'])} chapters, {total_articles} articles")

        output_path = OUTPUT_DIR / f"articles_{key}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(law, f, ensure_ascii=False, indent=2)
        print(f"  Written to {output_path}")


if __name__ == "__main__":
    main()
