import os

# 书名目录
project_root = '软件定义网络项目实战'

# 章节文件列表，格式：(filename, chapter_title)
chapters = [
    ('01-project-prep-and-basics.tex', '第一部分：项目准备与基础知识'),
    ('02-sdn-basic-project.tex', '项目一：构建基础SDN网络'),
    ('03-env-setup.tex', '实验环境搭建与准备'),
    ('04-sdn-basic-project.tex', '项目一：构建基础SDN网络'),
    ('05-dynamic-flow.tex', '项目二：动态流量调度系统'),
    ('06-security-acl.tex', '项目三：网络安全与隔离机制'),
    ('07-dc-optimization.tex', '项目四：数据中心网络优化'),
    ('08-p4-programming.tex', '项目五：P4编程与可编程数据平面'),
    ('09-neutron-integration.tex', '项目六：OpenStack Neutron与SDN集成'),
    ('10-future-summary.tex', '未来展望与总结')
]

def make_dirs():
    # 创建项目根目录
    if not os.path.exists(project_root):
        os.mkdir(project_root)
    # 创建 chapters 目录
    chapters_dir = os.path.join(project_root, 'chapters')
    if not os.path.exists(chapters_dir):
        os.mkdir(chapters_dir)
    return chapters_dir

def create_chapter_files(chapters_dir):
    for filename, title in chapters:
        filepath = os.path.join(chapters_dir, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as f:
                # 写入章节基本结构注释
                f.write(f'% {title}\n\n')
                f.write(f'\\chapter{{{title}}}\n\n')
                f.write('% 这里开始写你的章节内容\n')
            print(f'已创建文件: {filepath}')
        else:
            print(f'文件已存在: {filepath}')

def create_main_tex(chapters_dir):
    main_tex_path = os.path.join(project_root, 'main.tex')
    with open(main_tex_path, 'w', encoding='utf-8') as f:
        f.write(r'''\documentclass[UTF8]{ctexbook}
\usepackage{geometry}
\geometry{a4paper,scale=0.8}
\usepackage{hyperref}

\title{软件定义网络项目实战}
\author{作者姓名}
\date{\today}

\begin{document}

\maketitle
\tableofcontents
\clearpage
''')
        for _, filename in chapters:
            f.write(f'\\input{{chapters/{filename}}}\n\n')
        f.write(r'\end{document}')
    print(f'已创建主文件: {main_tex_path}')

def main():
    chapters_dir = make_dirs()
    create_chapter_files(chapters_dir)
    create_main_tex(chapters_dir)

if __name__ == '__main__':
    main()
