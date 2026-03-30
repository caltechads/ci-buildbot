[
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*{{ last_version_url }}*: code archive to code-drop *FAILED*\n*Pipeline*: {{pipeline_url}}\n*App*: {{ app_name }}\n*Build log*: {{ build_status_url }}\n*Build time*: {{ build_time }}\n*Git*: {{ git_info }}\n*Committer*: {{ committer }}\n*Authors*: {{ authors|join('\\n') }}"
    },
    "accessory": {
      "type": "image",
      "image_url":  "https://ads-utils-icons.s3-us-west-2.amazonaws.com/ci-buildbot/thumbs-down.png",
      "alt_text": "Code archive to code-drop failed"
    }
  },
  {
    "type": "context",
    "elements": [
      {
        "type": "mrkdwn",
        "text": "{{ completed_date }} {{buildbot}}"
      }
    ]
  }
]
