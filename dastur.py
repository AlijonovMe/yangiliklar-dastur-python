import json

def save_news(data, name, content, i):
    data.append(
        {"id": i + 1, "name": name, "content": content, "views": 0, "likes": 0, "dislikes": 0}
    )
    with open("news.json", mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


i = 0
while True:
    command = input("Buyruq: ").lower()
    if command == 'stop':
        break
    elif command == "add news":
        name = input("Name: ")
        content = input("Matni: ")

        try:
            with open("news.json", mode="r", encoding="utf-8") as f:
                data = json.load(f)
                i = data[-1]["id"]
        except:
            data = []

        save_news(data, name, content, i)
        print("News qo'shildi!!!")
        i += 1

    elif command == "show news":
        try:
            with open("news.json", mode="r", encoding="utf-8") as f:
                data = json.load(f)

            for news in data:
                print(f"ID: {news['id']} | Name: {news['name']}")

            news_id = input("Qaysi Newsni ko'rishni xohlaysiz? (ID yoki no): ").lower()
            if news_id == "no":
                continue

            selected_news = next((news for news in data if news['id'] == int(news_id)), None)
            if selected_news:
                print(
                    f"Name: {selected_news['name']}\nContent: {selected_news['content']}\nViews: {selected_news['views'] + 1}\nLikes: {selected_news['likes']}\nDislikes: {selected_news['dislikes']}")
                selected_news['views'] += 1

                feedback = input("Maqola sizga yoqdimi? (yes/no): ").lower()
                if feedback == "yes":
                    selected_news['likes'] += 1
                    print("Siz like bosdingiz.")
                elif feedback == "no":
                    selected_news['dislikes'] += 1
                    print("Siz dislike bosdingiz.")

                with open("news.json", mode="w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            print("Hozircha hech qanday news mavjud emas.")

    else:
        print("Noma'lum buyruq!")
