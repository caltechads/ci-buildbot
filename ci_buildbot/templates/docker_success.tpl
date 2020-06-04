[
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "{{ last_version_url }}: Docker build and push *SUCCESS*\n*Pipeline*: {{pipeline_url}}\n*Image*: {{ short_image }}\n*Build log*: {{ build_status_url }}\n*Build time*: {{ build_time }}\n*Image Size*: {{ "%0.2f" % image_size|float }}MB\n*Git*: {{ git_info }}"
    },
    "accessory": {
      "type": "image",
      "image_url":  "https://ads-utils-icons.s3-us-west-2.amazonaws.com/ci-buildbot/success-box.png",
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
