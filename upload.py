import requests
import json
import os
import datetime

build_type = os.getenv("build_type") or ''
job_url = os.getenv("JOB_URL") or ''
qrcode_url = job_url + "ws/qrcode.jpg"
fei_shu_webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/eb3678c4-e82c-405d-8b2c-61ea7597ed38"
title = "shy 体验版已发布"
deploy_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if build_type == "prod":
    title = "shy 正式版已发布"


def post_msg(msg):
    res = requests.post(
        url=fei_shu_webhook,
        headers={'Content-Type': "application/json; charset=utf-8"},
        data=json.dumps(msg)
    )
    content = res.json()
    if content.get("StatusCode") == 0:
        return content
    else:
        raise Exception("飞书消息通知失败: %s" % (content))


post_msg({
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": title,
                "content": [
                    [
                        {
                            "tag": "text",
                            "text": "日期: "
                        },
                        {
                            "tag": "text",
                            "text": deploy_date
                        }
                    ],
                    [
                        {
                            "tag": "text",
                            "text": "二维码: "
                        },
                        {
                            "tag": "a",
                            "text": "查看二维码",
                            "href": qrcode_url
                        }
                    ]
                ]
            }
        }
    }
})
