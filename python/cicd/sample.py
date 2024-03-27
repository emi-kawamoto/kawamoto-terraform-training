import os

userName = os.environ.get('USER_NAME')
password  = os.environ.get('PASSWORD')

print(f"入力されたユーザー名は {userName} です")
print(f"入力されたパスワードは {password} です")