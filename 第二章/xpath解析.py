# xpath 是XML文档搜索内容的一门语言
# html是xml的一个子集

from lxml import etree

xml = """
<catalog>
    <book id="bk101">
        <author>Gambardella, Matthew</author>
        <title>XML Developer's Guide</title>
        <genre>Computer</genre>
        <price>44.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An in-depth look at creating applications with XML.</description>
    </book>
    <book id="bk102">
        <author>Ralls, Kim</author>
        <title>Midnight Rain</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2000-12-16</publish_date>
        <description>A former architect battles an evil sorceress.</description>
    </book>
    <book id="bk103">
        <author>Corets, Eva</author>
        <title>Maeve Ascendant</title>
        <genre>Fantasy</genre>
        <price>8.99</price>
        <publish_date>2000-11-17</publish_date>
        <description>After the death of her mother, Maeve sets out on a journey to find herself.</description>
    </book>
    <book id="bk104">
        <author>Corets, Eva</author>
        <title>Oberon's Legacy</title>
        <genre>Fantasy</genre>
        <price>12.99</price>
        <publish_date>2001-03-10</publish_date>
        <description>A story of love and power in the magical world of Oberon.</description>
    </book>
</catalog>

"""

tree = etree.XML(xml)
# result = tree.xpath("/catalog/book") # /表示层级关系，从根节点开始，查找所有book节点
# for book in result:
#     print(etree.tostring(book, pretty_print=True).decode())

result = tree.xpath("/catalog/book/title/text()") # 查找所有book节点下的title节点
print(result)