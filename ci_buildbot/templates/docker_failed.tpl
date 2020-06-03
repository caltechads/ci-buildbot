[
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*{{ last_version_url }}*: Docker build and push *FAILED*\n*Image*: {{ short_image }}\n*Build info*: {{ build_status_url }}\n*Build time*: {{ build_time }}\n*Git*: {{ git_info }}"
    },
    "accessory": {
      "type": "image",
      "image_url":  "https://ads-utils-icons.s3-us-west-2.amazonaws.com/ci-buildbot/thumbs-down.png",
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
