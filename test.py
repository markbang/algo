import bcrypt

# --- 第 1 部分: 哈希一个新的密码 (例如 "bangbang") ---

# 准备要哈希的密码，需要编码为字节串
password_to_hash = b"bangbang"

# 生成一个盐 (salt)
# bcrypt.gensalt() 会创建一个随机的盐，并包含默认的 cost factor (通常是 12)
salt = bcrypt.gensalt()

# 使用生成的盐哈希密码
hashed_password = bcrypt.hashpw(password_to_hash, salt)

print("--- 哈希新密码示例 ---")
print(f"原始密码: {password_to_hash.decode()}")
print(f"生成的盐: {salt.decode()}")
print(f"生成的新哈希值: {hashed_password.decode()}")
print("-" * 25)


# --- 第 2 部分: 验证 "bangbang" 是否与给定的哈希匹配 ---

# 用户输入的密码，同样需要编码为字节串
user_input_password = b"bangbang"

# 从问题中得到的已知哈希值
known_hash = b"$2b$12$vIAs2L9LLkYj2ZgfM0LSV.qxc84Sd5HbA..jk9s1aq3ipJ7Cu6zPC"

print("\n--- 验证已知哈希示例 ---")
print(f"待验证的密码: {user_input_password.decode()}")
print(f"已知的哈希: {known_hash.decode()}")

# 使用 bcrypt.checkpw() 函数进行验证
# 这个函数会从 known_hash 中自动提取盐和 cost factor，然后用它们来哈希 user_input_password，
# 最后比较结果是否与 known_hash 中的哈希部分一致。
if bcrypt.checkpw(user_input_password, known_hash):
    print("结果: 密码匹配！")
else:
    print("结果: 密码不匹配。")
print("-" * 25)
