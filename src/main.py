from modules.message_input.cli import message_input
from thought.clarify_issue.clarify_issue import clarify_issue
from thought.summarize_issue.summarize_issue import summarize_issue


"""
Issueの一例（Google製品のサポートページより）:

URLを掲載していないページからの流入が計測されてしまいます。
あるWEBページにどのメディアから来ているか調べたく、
レポート＞エンゲージメント＞ランディングページ内で、
トラフィックソースを「セッションの参照元／メディア」で検索しました。

しかし数は少ないですが、バナーを掲載していないページからの流入がいくつか見られました。
こちら原因などご存知の方いらっしゃいますでしょうか？
"""


def main():
    # ユーザーにIssueを入力してもらう
    issue_content = message_input()

    # 処理中のログ
    print(f"\nあなたの質問: {issue_content}\n")
    print("\n回答を生成中...\n")

    # Issueのサマリを作成
    summarize_issue(issue_content=issue_content)

    # Issueの不足情報をリストアップして確認する
    clarify_issue(issue_content=issue_content)


if __name__ == "__main__":
    main()
