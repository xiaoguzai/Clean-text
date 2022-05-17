def clean_weibo_title(title: str):
    """
    对微博数据中的标题内容（待生成）进行清洗
    Args:
        title: 标题
    Returns:
    """
    # 去除##符号（一般为微博数据的话题标记）
    title = re.sub(r"#", "", title)
    # 去除[]中间的文字（一般为微博数据中的表情）
    title = re.sub(r"(\[{1,2})(.*?)(\]{1,2})", "", title)
    # 合并标题中过多的空格
    title = re.sub(r"\s+", " ", title)
    return title


def clean_weibo_content(content: str):
    """
    对微博数据中的文本内容进行清洗
    Args:
        content: 文本
    Returns:
    """
    # 去除网址
    content = re.sub(r"(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b", "", content)
    # 合并正文中过多的空格
    content = re.sub(r"\s+", " ", content)
    # 去除\u200b字符
    content = content.replace("\u200b", "")
    return content


  
