import os
import sys
import json
import markdown
import shutil

# マークダウンファイルが存在するディレクトリ
input_dir = '.'

# 出力ディレクトリの設定
output_dir = 'config'

# 出力ディレクトリを削除して再作成
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# index.jsonのパス
index_file_path = os.path.join(output_dir, 'index.json')
index_data = []

# ディレクトリ内のすべての .md ファイルをリストアップ
for file_name in os.listdir(input_dir):
    if file_name.endswith('.md'):
        file_path = os.path.join(input_dir, file_name)
        absolute_path = os.path.abspath(file_path)

        with open(absolute_path, 'r', encoding='utf-8') as f:
            target_file = f.read()

        md = markdown.Markdown(extensions=['tables'])
        html_content = md.convert(target_file)

        # 出力ファイル名の設定
        output_file_name = os.path.splitext(file_name)[0] + '.html'
        output_file_path = os.path.join(output_dir, output_file_name)

        # HTMLファイルに書き込み
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Converted HTML file saved to: {output_file_path}")

        # index.jsonにリストアップ
        index_data.append({
            'markdown_file': file_path,
            'html_file': output_file_path
        })

# index.jsonを更新
with open(index_file_path, 'w', encoding='utf-8') as f:
    json.dump(index_data, f, ensure_ascii=False, indent=4)

print(f"Updated index.json with {len(index_data)} entries.")