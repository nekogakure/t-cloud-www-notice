import os
import sys
import markdown

if len(sys.argv) < 2:
    print("Usage: python main.py <markdown_file>\n作業するディレクトリはnoticeディレクトリである必要があります。")
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