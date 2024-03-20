default_user_input = "ユーザー登録時に500エラーが発生します。どうしたらいいですか？"


def message_input() -> str:
    print(
        "Issueを入力してください。\nsubmitするには空行を2回連続で入力してください。\n\n入力:"
    )

    lines = []
    empty_line_count = 0

    while True:
        line = input()
        if line == "":
            empty_line_count += 1
            if empty_line_count == 2:
                break
        else:
            empty_line_count = 0
            lines.append(line)

    user_input = "\n".join(lines)
    if not user_input:
        print("入力がなかったため、デフォルト値を用います。: " + default_user_input)
        return default_user_input
    else:
        return user_input
