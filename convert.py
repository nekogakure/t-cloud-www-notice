import os
import sys
import json

if len(sys.argv) < 2:
    print("Usage: python convert.py <markdown_file>")
    sys.exit(1)

file_path = sys.argv[1]
absolute_path = os.path.abspath(file_path)

# 出力ディレクトリの設定
output_dir = 'html'
os.makedirs(output_dir, exist_ok=True)

# index.jsonにリストアップ
index_file_path = os.path.join(output_dir, 'index.json')
if os.path.exists(index_file_path):
    with open(index_file_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
else:
    index_data = []

index_data.append({
    'markdown_file': file_path,
})

with open(index_file_path, 'w', encoding='utf-8') as f:
    json.dump(index_data, f, ensure_ascii=False, indent=4)

print(f"Updated index.json with markdown file: {file_path}")
