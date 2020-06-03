[
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "{{ last_version_url }}: Deployfish deploy *SUCCESS*\n*Service*: {{ service }}\n*Build info*: {{ build_status_url }}\n*Elapsed time*: {{ build_time }}\n"
    },
    "accessory": {
      "type": "image",
      "image_url":  "https://ads-utils-icons.s3-us-west-2.amazonaws.com/ci-buildbot/deploy-success.png",
      "alt_text": "Docker build"
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
