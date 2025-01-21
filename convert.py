import os
import sys
import markdown
import json

if len(sys.argv) < 2:
    print("Usage: python convert.py <markdown_file>")
    sys.exit(1)

file_path = sys.argv[1]
absolute_path = os.path.abspath(file_path)

with open(absolute_path, 'r', encoding='utf-8') as f:
    target_file = f.read()

md = markdown.Markdown(extensions=['tables'])
html_content = md.convert(target_file)

# 出力ディレクトリとファイル名の設定
output_dir = 'html'
os.makedirs(output_dir, exist_ok=True)
output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.html'
output_file_path = os.path.join(output_dir, output_file_name)

# HTMLファイルに書き込み
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Converted HTML file saved to: {output_file_path}")

# index.jsonにリストアップ
index_file_path = os.path.join(output_dir, 'index.json')
if os.path.exists(index_file_path):
    with open(index_file_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
else:
    index_data = []

index_data.append({
    'markdown_file': file_path,
    'html_file': output_file_path
})

with open(index_file_path, 'w', encoding='utf-8') as f:
    json.dump(index_data, f, ensure_ascii=False, indent=4)

print(f"Updated index.json with: {output_file_path}")