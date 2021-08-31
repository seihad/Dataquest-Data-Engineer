#### 1
# data = "QUEST"
# for letter in data:
#     decimal_letter = ord(letter)
#     binary_letter = bin(decimal_letter)
#     print(binary_letter)

#### 2
# text = "The Swedish word for quest is sökande"
# encoded = text.encode(encoding= 'ascii', errors='replace')
# print(encoded)
# print(type(encoded))

#### 3
# bytes1 = bytes.fromhex("02")
# print(bytes1)

# bytes2= bytes.fromhex("5a")
# print(bytes2)

# bytes3 = bytes.fromhex("ff")
# print(bytes3)

#### 4
# string_1 = "lowercase"
# string_2 = "UPPERCASE"
# def check_uppercase(word):
#     for letter in word:
#         if not 65 <= ord(letter) <= 90:
#             return False
#     return True

# print(check_uppercase(string_1))
# print(check_uppercase(string_2))

#### 5
# trad_chinese = "你好嗎?"
# encoded = trad_chinese.encode(encoding="BIG5")
# print(len(encoded))

#### 7
# sentence = "ASCII cannot represent these: 你好嗎"
# encoded_utf8 = sentence.encode(encoding="utf-8", errors="replace")
# print(encoded_utf8)
# encoded_big5 = sentence.encode(encoding="BIG5", errors="replace")
# print(encoded_big5)
# encoded_ascii = sentence.encode(encoding="ASCII", errors="replace")
# print(encoded_ascii)

#### 8
encoded = b'The movie \xe2\x80\x94 Data Quest \xe2\x80\x94 costs 10\xc2\xa3'

decoded_cp1252 = encoded.decode(encoding="cp1252")

print(decoded_cp1252)

import chardet

encoding = chardet.detect(encoded)["encoding"]

decoded = encoded.decode(encoding=encoding)
print(decoded)
