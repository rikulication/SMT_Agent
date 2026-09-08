from langchain_text_splitters import MarkdownHeaderTextSplitter

def split_markdown(markdown):
    headers = [
        ("#", "scene"),
        ("##", "state"),
        ("###", "detail"),
        # ("####", "detail2"),
    ]

    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers)

    docs = splitter.split_text(markdown)

    for i, doc in enumerate(docs):
        doc.metadata["rule_id"] = i
        scene = doc.metadata.get("scene", "")
        state = doc.metadata.get("state", "")
        detail = doc.metadata.get("detail", "")
        doc.page_content = f"""
状态：{state}
详情：{detail}

客服回复：
{doc.page_content}
""".strip()
    return docs