import re
import json
from datetime import datetime
from lyylog import log
import xml.etree.ElementTree as ET
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
import time
import lyyre
import Levenshtein
import xpinyin
user_defined_pinyin = {"长虹": "changhong"}


def convert_to_pinyin(text, user_define_pinyin=None):
    """
    取汉字拼音，如果输入参数是纯英文，则保留原名称。如果“长虹”始终解析为“zhjanghong"，则直接传入字典，用”常虹“代替”长虹“去取拼音，从而完美解决多音字问题。
    """
    pinyin = xpinyin.Pinyin()   # 创建 Pinyin 实例

    # 如果提供了用户定义的拼音映射，则替换文本中的相应汉字
    if user_define_pinyin is not None:
        for key, value in user_define_pinyin.items():
            text = text.replace(key, value)
    
    # 使用 xpinyin 获取不带声调的拼音，将所有汉字转换为拼音，非汉字字符保持不变
    pinyin_list = []
    for char in text:
        if char.isascii():  # 如果字符是 ASCII 字符，直接添加到拼音列表
            pinyin_list.append(char)
        else:
            # 获取汉字的拼音，取第一个拼音（不带声调）
            pinyin_str = pinyin.get_pinyin(char) if pinyin.get_pinyin(char) else char
            pinyin_list.append(pinyin_str)
    
    # 将拼音列表转换为字符串，并去除拼音中的声调
    print("pinyin_list=",pinyin_list)
    pinyin_str = ''.join(pinyin_list)
    no_tone_pinyin = ''.join([p for p in pinyin_str if p not in 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüń'])
    return no_tone_pinyin
    
    # 如果文本只包含 ASCII 字符，则保留原名称
    if text.isascii():
        print(f"({text})是纯英文")
        pinyin = text
    
    return pinyin

class TeacherMessageThrottler:
    def __init__(self):
        # 使用defaultdict来存储每个老师的消息队列
        from collections import defaultdict, deque
        self.messages = defaultdict(deque)

    def _cleanup(self, teacher):
        # 移除指定老师1分钟前的消息
        current_time = time.time()
        while self.messages[teacher] and current_time - self.messages[teacher][0][1] > 60:
            self.messages[teacher].popleft()

    def should_send_message(self, teacher, message):
        self._cleanup(teacher)
        # 检查指定老师的消息是否在最近1分钟内发送过
        for msg, _ in self.messages[teacher]:
            if are_sentences_similar(msg, message):
                # if msg == message:
                return False  # 如果发送过，不再发送
        # 如果没有发送过，记录消息和当前时间戳
        self.messages[teacher].append((message, time.time()))
        return True  # 允许发送消息

def format_url_in_ocr_text_include_markdown_img(msg_json, text, debug=False):
    """
    对OCR识别出的文字重新判断一次，
        如果是图片链接，则去除空格重新当图片处理一遍。
        否则，如果是普通的，则替换原来的图片链接为识别后的内容，并当成普通文本处理。
    """
    old_text = msg_json["markdown"]["text"] 
    if debug: print("enter format_ocr_text_include_markdown_img")
    url_pattern = r'!\s?\[\s?(?:screenshot)?\s?\]\s?\((http:?//.*\.(bmp)|(png)|(jpg))'

    # 在文本中查找所有匹配的网址
    matches = re.findall(url_pattern, text)
    if len(matches)>0:
        for match in matches:
            if debug: print(match)
            
            cleaned_url = re.sub(r'\s+', '', match[0])
            if debug: print(cleaned_url)
            msg_json["markdown"]["text"]  = cleaned_url
            msg_json["img"] = cleaned_url
            print("in foramt_url of lyytext, url ormat finished")
            return msg_json
    else:
        print("in ocr format text=",text)
        msg_json["markdown"]["text"] = text
        msg_json["markdown"]["title"] = text[:30]
        del msg_json["img"]
        print("in format_url_after_ocr of lyytext, 没找到图片包或者 图片链接json= ",msg_json)
        return msg_json

def extract_token(string,debug=False):
    pattern = r"access_token=(.*?)&"
    match = re.search(pattern, string)
    if match:
        access_token = match.group(1)
        if debug: print("extract_token result:",access_token)
        return access_token




def are_sentences_similar(sentence1, sentence2, threshold=0.92):
    # 定义一个正则表达式，用于匹配英文、中文和数字
    pattern = re.compile(r'[\u4e00-\u9fa5a-zA-Z0-9]')
    
    # 使用正则表达式过滤字符串，只保留英文、中文和数字
    filtered_sentence1 = ''.join(pattern.findall(sentence1))
    filtered_sentence2 = ''.join(pattern.findall(sentence2))
    
    # 计算两个字符串的相似度
    similarity = Levenshtein.ratio(filtered_sentence1, filtered_sentence2)
    
    # 判断相似度是否达到阈值
    return similarity >= threshold

def dingding_extract_packet_size(message,deub=False):
    # 使用正则表达式定义两个捕获组，提取图片包和尺寸2部分
    pattern = r'http.*\/(.*)_(\d{2,4}_\d{2,4})'
    
    # 使用正则表达式匹配并提取两个分组
    match = re.search(pattern, message)
    if match:
        group1 = match.group(1)
        group2 = match.group(2)
        print("group1=",group1,"group2=",group2)
        return group1, group2
    else:
        return None,None
    
def encode_number(number,debug=False):
    """
    钉钉图片，把尺寸数字转换成字符作为图片包的一部分
    """
    # 计算1024的倍数
    thousands = number // 1024
    # 获取剩余的数值
    remainder = number % 1024
    if debug:print("remainder:",remainder)
    # 计算16的倍数
    sixteens = remainder // 16
    # 获取个位数值（每增加4代表字符集中的下一个字符）
    units = remainder % 16
    if debug: print("units:",units)
    # 将数值转换为对应的字符
    encoded = characters[thousands] + characters[sixteens] + characters[units * 4+1]
    return encoded

# 解码函数
def decode_number(encoded,debug=False):
    """
        钉钉图片，从图片包字符提取尺寸数字
    """
    # 将字符转换为对应的数值
    thousands = characters.index(encoded[0])
    sixteens = characters.index(encoded[1])
    units = int(characters.index(encoded[2])/4)
    
    # 根据编码规则重建原始的数字
    number = (thousands * 1024) + (sixteens * 16) + units
    if debug:print(" in decode_number, number=",number)
    return number

def txt_to_jd_jsontext(msgtype, chinesename, msg_time, txt, return_json=False):
    """
    生成适合在jd控件中显示的json格式文本
    """
    msg_json = {}
    msg_json["msgtype"] = msgtype
    msg_json["chinesename"] = chinesename
    msg_json["time"] = msg_time
    msg_json["message"] = txt
    if return_json:
        return msg_json
    else:
        return json.dumps(msg_json)

def extract_token(string,debug=False):
    pattern = r"access_token=(.*?)&"
    match = re.search(pattern, string)
    if match:
        access_token = match.group(1)
        if debug: print("extract_token result:",access_token)
        return access_token


def read_xml_branch_value(xml_file=r"D:\Soft\_Stock\KTPro\User\BlockInfo\UserBlockInfo6633458850865152.data", branch_name="BC", attribute_name="ToTDX.", option="Stock"):
    """
    # 解析XML文件,交易师的xml文件是UTF-16编码的，分支名是BC

    """

    with open(xml_file, "r", encoding="utf-16-le") as f:
        tree = ET.parse(f)
    root = tree.getroot()

    # 查找指定分支的元素
    for elem in root.iter(branch_name):
        if elem.attrib.get("Name") == attribute_name:
            return elem.attrib.get(option)

    return None


def write_xml_branch_value(xml_file=r"D:\Soft\_Stock\KTPro\User\BlockInfo\UserBlockInfo6633458850865152.data", branch_name="BC", attribute_name="ToTDX.", option="Stock", new_value="", debug=False):
    # 解析XML文件,交易师的xml文件是UTF-16编码的，分支名是BC
    with open(xml_file, "r", encoding="utf-16-le") as f:
        tree = ET.parse(f)
    root = tree.getroot()

    # 查找指定分支的元素
    for elem in root.iter(branch_name):
        if elem.attrib.get("Name") == attribute_name:
            elem.attrib[option] = new_value
            break
    # 保存修改后的XML文件
    tree.write(xml_file, encoding="utf-16-le", xml_declaration=False)
    if debug:
        result = read_xml_branch_value(xml_file, branch_name, attribute_name, option)
        print(f"write_xml_branch_value: {xml_file} {branch_name} {attribute_name} {option} {new_value}, result={result}")


def is_ad(text, keywords, threshold):
    count = 0
    for keyword in keywords:
        if keyword in text:
            count += 1
    if count >= threshold:
        return True
    else:
        return False


def ocr_text_not_useful(ocr_result_text, blacklist_latterns):

    if ocr_result_text is None or len(ocr_result_text) == 0:
        print("结果空值，OCR没识别出来")
        return True

    elif deny_ocr_text_patterns(blacklist_latterns, ocr_result_text, debug=False):
        log("包含禁止OCR关键字" + ocr_result_text)
        return True
    

    elif "http" not in ocr_result_text:
        # 获取当前日期和时间
        now = datetime.now()
        clean_text = lyyre.exclude_userfull_number_before_calc(ocr_result_text)
        if count_digits(clean_text) > 20:
            log("数字太多,占比超20%，怕是表格哦。不识别,clean_text" + clean_text)
            return True
    else:
        return False


def get_all_values_in_dict(data):
    """
    获取字典中所有值，包含子字典
    返回包含所有值的列表
    """
    values = []
    for key, value in data.items():
        if isinstance(value, dict):
            values.extend(get_all_values_in_dict(value))
        else:
            values.append(str(value))
    return values


def list_include_dict_to_str(words_list):
    """
    a=[{"words":"今日首板：15只"},{"words":"板：5只"},{"words":"三板：1只"}]

    """
    print("words_list=", words_list, type(words_list))
    text = ""
    for item in words_list:
        text += item["words"]

    return text


def count_digits(s):
    """计算字符串中数字占比"""
    # 将字符串中的所有字符转换为数字类型
    digits = sum(c.isdigit() for c in s)
    # 统计数字数量
    total_length = len(s)
    # 计算数字占比并返回结果
    return (digits / total_length) * 100


def batch_replace_text_by_dict(text, to_replace_dict: dict, debug=False):
    # 输入原文本和替换对字典，替换对为字典格式，key替换为value
    for key, value in to_replace_dict.items():
        text = text.replace(key, value)
    return text


def batch_format_remove_subtext(text: str, to_remove_list: list, debug=False):
    for item in to_remove_list:
        text = text.replace(item, "")
        if debug and item in text:
            print(text, "in batch_format_remove_subtext, 包含:", item)
    return text


def deny_ocr_text_patterns(regex_pattern_list, text, debug=False):
    for regex in regex_pattern_list:
        pattern = re.compile(regex)
        match = pattern.findall(text)
        if len(match) > 0:
            if debug:
                print("in deny_ocr_text_patterns, match=", match)
            return True
        else:
            if debug:
                print("没有匹配,regex=", regex)

    return False


def replace_regex_to_strings(original_text: str, regex_pattern: str, to_replace_text: str = "", debug=False):
    # 根据正则表达式替换匹配的子文本。当to_replace为空时，等于删除匹配文本。
    pattern = re.compile(regex_pattern)
    new_str = re.sub(pattern, to_replace_text, original_text)
    if debug:
        matches = re.findall(pattern, original_text)
        if matches:
            print("in replace_regex_to_strings, 匹配的部分：", matches, "子文本替换为: ", to_replace_text)
    return new_str


def batch_remove_regex_strings_by_list(regex_pattern_list, text, debug=False):
    # 删除符合 模式列表 中的任意模式的字符
    for regex in regex_pattern_list:
        text = replace_regex_to_strings(text, regex, "", debug=debug)
    return text


def batch_replace_by_regex_dict(regex_new_dict: dict, text: str, debug=False):
    # 批量替换指定正则表达式为指定字符，通过使用字典中的值替换键
    for key_regex_str, value_to_replace in regex_new_dict.items():
        text = replace_regex_to_strings(text, key_regex_str, value_to_replace, debug=debug)
    return text


def batch_strip_text(text: str, to_remove_words_list: list, debug: bool = False):
    # 批量删除首尾不要的字符
    for words in to_remove_words_list:
        text = text.strip(words)
        if debug:
            if text.startswith(words) or text.endswith(words):
                print("in batch_strip_text, text startwith=" + words)
    # 删除文本两端的空格
    return text.strip()


def replace_digits_with_chinese(text):
    mapping = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
    replaced_text = ""
    for char in text:
        if char.isdigit():
            replaced_text += mapping[char]
        else:
            replaced_text += char
    return replaced_text


def extract_regex_strings(regex, text):
    #  正则表达式模式
    pattern = re.compile(regex)

    #  查找所有匹配项并将其添加到列表中
    regex_strings = pattern.findall(text)

    return regex_strings


def clean_text(text):

    # 定义正则表达式模式
    pattern = r"(\d{1,2}:\d{1,2}:\d{1,2}[]) ([\u4e00-\u9fa50-9]+) (.*)"

    # 匹配并删除符合格式的文本
    clean_text = re.sub(pattern, "", text)

    # 查找并替换时间格式
    clean_text = re.sub(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}", "", clean_text)

    print(clean_text)
    return clean_text


def remove_date_time(texting):
    patterns = [r"\d{2}:\d{2}:\d{2}[ ]?", r"\d{4}-\d{2}-\d{2}[ ]?", r"\d{1,2}:\d{2}:\d{2}"]

    for pattern in patterns:
        texting = re.sub(pattern, "", str(texting))
    return texting


def get_name_from_code(code):
    import lyystkcode

    stock_code_name_dict = lyystkcode.get_code_name_dict()
    code = str(code).zfill(6)
    if code in stock_code_name_dict.keys():
        return f"[{(code)}:{stock_code_name_dict[code]}]"


def add_stockname_for_stkcode(txt):

    def replace(match):
        num = match.group(0)
        start_digit = num[0]
        if start_digit in ["3", "6", "0"]:
            new_num = str(get_name_from_code(int(num)))
            return num.replace(num, new_num)
        else:
            return num

    replaced_text = re.sub(r"\b(?:3|6|0)\d{5}\b", replace, txt)
    # print("toadd_stkname_txt=", txt, "replaced_text=", replaced_text)
    return replaced_text


def num_to_chinese(match):
    num_map = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
    return "".join(num_map[digit] for digit in match.group())


def format_to_speak_text(txt):
    """
    文本朗读时候，数字会被读成阿拉伯数字，这里把数字转换成中文，单个读。
    """

    txt = re.sub(r"\d{6}", num_to_chinese, txt)

    txt = remove_date_time(txt)
    txt = clean_text(txt)
    return txt


if __name__ == "__main__":
    # 测试
    txt = "2021-09-30 15:00:00 今日首板：15只板：5只三板：1只"
    result= convert_to_pinyin("长虹")
    print(result)