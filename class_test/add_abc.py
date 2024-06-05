import base64
import zlib

# 原始数据
original_data = '10224804417'.encode('utf-8')

# zlib压缩
compressed_data = zlib.compress(original_data)

# Base64编码
encoded_str = base64.b64encode(compressed_data).decode('utf-8')

print(encoded_str)
