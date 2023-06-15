from slack_sdk.webhook import WebhookClient


def post_error_slack(url, context):
    """
    'on_failure_callback'時にslackへの通知を行う

    Args:
        url (string): slackのIncoming Webhooks の URL
        context (dict): 実行したタスクのコンテキスト

    Returns:
    """

    webhook = WebhookClient(url)

    blocks = [
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Failed to execute DAG on Airflow.",
            },
            "fields": [
                {"type": "mrkdwn", "text": "*DAG*"},
                {"type": "mrkdwn", "text": "*Task*"},
                {"type": "plain_text", "text": f"{context['dag']}"},
                {"type": "plain_text", "text": f"{context['task']}"},
            ],
        }
    ]

    body = {
        "text": "fallback",
        "blocks": blocks,
    }

    response = webhook.send_dict(body=body)
