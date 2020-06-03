[
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "{{ last_version_url }}: Deployfish deploy *STARTED*\n*Service*: {{service}}\n*Build info*: {{ build_status_url }}\n"
    },
    "accessory": {
      "type": "image",
      "image_url":  "https://ads-utils-icons.s3-us-west-2.amazonaws.com/ci-buildbot/deploy-start.png",
      "alt_text": "Deploy start"
    }
  },
  {
    "type": "context",
    "elements": [
      {
        "type": "mrkdwn",
        "text": "{{ completed_date }}"
      }
    ]
  }
]

