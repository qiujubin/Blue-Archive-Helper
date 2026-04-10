import json
import os

def main():
    input_file = "code.txt"      # 输入文件名
    output_file = "result.json"  # 输出文件名

    # 1. 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 找不到文件 '{input_file}'")
        print("请确保 code.txt 和本脚本在同一个文件夹中。")
        return

    try:
        # 2. 读取并解析 JSON 数据
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 3. 创建名字到ID的映射字典
        name_to_id = {}

        # 遍历 data 数组中的每一个角色
        for char in data.get("data", []):
            char_id = char["id"]
            # 添加正式名称
            name_to_id[char["name"]] = char_id

            # 如果有别名，添加别名
            # 注意：有些角色的 nameAlias 可能是空数组或不存在
            aliases = char.get("nameAlias", [])
            for alias in aliases:
                name_to_id[alias] = char_id

        # 4. 将结果写入新文件
        with open(output_file, 'w', encoding='utf-8') as f:
            # ensure_ascii=False 保证中文不被转义
            # indent=2 让文件格式好看，如果文件太大可以改为 indent=None
            json.dump(name_to_id, f, ensure_ascii=False, indent=2)

        print(f"成功!")
        print(f"共处理了 {len(name_to_id)} 个名字。")
        print(f"结果已保存为 '{output_file}'")

        # 简单测试几个名字
        test_names = ["爱露", "水白子", "小狐狸", "星野（武装）"]
        print("\n--- 测试查询 ---")
        for name in test_names:
            if name in name_to_id:
                print(f"{name} -> ID: {name_to_id[name]}")
            else:
                print(f"{name} -> 未找到")

    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    main()
