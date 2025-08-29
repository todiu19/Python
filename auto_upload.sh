
# Đi vào đúng thư mục repo Git
cd "/Users/tonguyen/Documents/III-1/Python" || exit
#!/bin/bash

git add .

# Commit với thời gian hiện tại làm message
git commit -m "Auto commit $(date '+%Y-%m-%d %H:%M:%S')"

# Pull trước để tránh conflict
git pull --rebase origin main

# Push lên GitHub
git push origin main

