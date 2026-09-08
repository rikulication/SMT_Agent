from loader import load_md
from splitter import split_markdown
from vectorstore import Vectorstore

path = "knowledge/documents/客服规则.md"


if __name__ == "__main__":
    # md = load_md(path)
    # chunk = split_markdown(md)
    collection_name = "customer_service"
    
    vs = Vectorstore(collection_name)
    datebase = vs.load_vectorstore()
    test_questions = [
        "你好，我的订单追踪信息在哪里？",
        # "客户还没有下单，只是在咨询",
        # "我不明白客户说的是什么意思",
        # "客户自己取消订单后多久能收到退款",
        # "客户收到商品发现损坏怎么办",
        # "海关申报价格可以修改吗",
    ]
    for query in test_questions:
        results = datebase.similarity_search_with_score(
            query,
            k=3
        )
        print(f'问题:{query}')
        for doc,score in results:
            print("得分:",score)
            print(doc.page_content)
            print("-" * 250)
        print("=" *500)