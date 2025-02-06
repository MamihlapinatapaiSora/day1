def read_file(filename):
    """读取文本文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # 打开文件并读取内容
            return f.read()  # 返回文件内容
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")  # 打印错误信息
        return ""  # 返回空字符串

def clean_text(text):
    """清洗文本：转小写、去标点"""
    import string
    text = text.lower()  # 将文本转换为小写
    return text.translate(str.maketrans('', '', string.punctuation))  # 去除标点符号

def word_frequency(text):
    """统计词频"""
    words = text.split()  # 将文本拆分为单词列表
    freq = {}  # 创建一个空字典来存储词频
    for word in words:
        freq[word] = freq.get(word, 0) + 1  # 统计每个单词出现的次数
    return freq

def show_top_words(freq, n=5):
    """显示最高频的n个词"""
    sorted_words = sorted(freq.items(), key=lambda x: -x[1])  # 按词频降序排序
    print(f"\nTop {n} 高频词：")
    for word, count in sorted_words[:n]:
        print(f"{word}: {count}次")  # 打印前 n 个高频词及其出现次数

# 主程序流程
text = read_file("news.txt")  # 读取文件内容
if text:
    cleaned = clean_text(text)  # 清洗文本
    freq = word_frequency(cleaned)  # 统计词频
    show_top_words(freq)  # 显示最高频的词
