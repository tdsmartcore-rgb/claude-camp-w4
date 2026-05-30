import json
import os
print(f"文件保存在： {os.path.abspath('todo.json')}")

TODO_FILE = "todo.json"

def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []
    

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(todos, text):
    new_id = max(item["id"] for item in todos) +1 if todos else 1

    new_todo = {
        "id": new_id,
        "text": text,
        "done": False    
    }

    todos.append(new_todo)
    save_todos(todos)
    print(f"✅ 已添加待办事项：{text}")


def complete_todos(todos, todo_id):
    for item in todos:
        if item["id"] == todo_id:
            item["done"] = True
            save_todos(todos)
            print(f"✅ 已完成待办事项：{item['text']}")
            return
    
    print(f"⚠️  没有找到 id 为 {todo_id} 的待办事项。")

def list_todos(todos):
    if not todos:
        print("📭 没有待办事项了！")
        return
    
    print("📋 待办事项列表：")
    for item in todos:
        status = "✅" if item["done"] else "❌"
        print(f"{status} {item['id']}. {item['text']}")
    
    remaining = sum(1 for item in todos if not item["done"])
    print(f"📊 还有 {remaining} 条待办事项未完成。")


def main():
    todos = load_todos()

    while True:
        print("\n请选择操作：")
        print("1. 添加待办事项")
        print("2. 完成待办事项")
        print("3. 列出所有待办事项")
        print("4. 退出程序")

        command = input(">> ").strip()

        if command == "1":
            text = input("请输入待办事项内容：").strip()
            if text:
                add_todo(todos, text)
            else:
                print("⚠️  待办事项内容不能为空。")

        elif command == "2":
            try:
                todo_id = int(input("请输入待办事项 id：").strip())
                complete_todos(todos, todo_id)
            except ValueError:
                print("⚠️  请提供一个有效的数字 id。")

        elif command == "3":
            list_todos(todos)

        elif command == "4":
            print("👋 再见！")
            break

        else:
            print("⚠️  无效的命令，请重新输入。")

if __name__ == "__main__":
    main()