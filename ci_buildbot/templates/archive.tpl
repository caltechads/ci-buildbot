{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
                "text": "*{{ name }}-{{ version }}*: archived to S3"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
                    "text": "Completed {{ completed_date }}"
				}
			]
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
                    "text": "*Branch*\n{{ branch }}"
				},
				{
					"type": "mrkdwn",
                    "text": "*Version:*\n{{ version }}"
				},
				{
					"type": "mrkdwn",
					"text": "*Committer:*\n{{ committer }}"
				},
				{
					"type": "mrkdwn",
                    "text": "*Authors:*\n{{ authors|join('\\n') }}"
                }
                {% if diff_url %}
                ,
				{
					"type": "mrkdwn",
                    "text": "*Changes since {{ previous_version }}*\n<{{ diff_url }}|Click here>"
				}
                {% endif %}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
                "text": "*Changelog*\n{{ changelog|join('\\n') }}"
			}
		}
	]
}
