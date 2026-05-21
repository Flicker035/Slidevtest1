import asyncio
import os
from xiaohongshu_mcp import login, search_notes, get_note_content

async def main():
    # 先登录小红书
    print("正在登录小红书...")
    login_result = await login()
    print(f"登录结果: {login_result}")
    
    if "登录成功" not in login_result:
        print("请先完成登录操作")
        return
    
    # 搜索"量化交易"相关的笔记
    print("正在搜索'量化交易'相关的笔记...")
    search_result = await search_notes("量化交易", limit=1)
    print(f"搜索结果:\n{search_result}")

    # 如果找到笔记，获取第一篇的内容
    if "链接:" in search_result:
        # 提取URL
        lines = search_result.split('\n')
        for line in lines:
            if line.startswith("   链接: "):
                url = line.replace("   链接: ", "").strip()
                print(f"正在获取笔记内容，URL: {url}")
                content_result = await get_note_content(url)
                print(f"获取内容结果: {content_result}")

                # 保存到桌面
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "a.txt")
                with open(desktop_path, 'w', encoding='utf-8') as f:
                    f.write(content_result)
                print(f"内容已保存到: {desktop_path}")
                break
    else:
        print("未找到相关笔记")

if __name__ == "__main__":
    asyncio.run(main())