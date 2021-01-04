from urllib import parse

from xiaohongshu.shield import get_sign


def main():
    # 根据main_hmac和device_id，初始化签名加密
    main_hmac = 'Cx/42gpfP6HWLvF0t0oCl0jcEJcsNs0IbYSP+TY1JRXE+U7uMUTq8lnLnMbCckbv' \
                'LQ9MYHiwbJwf1uyZ+c1SsRBy2ZcFQWmJiKoCAgIvEEnEGJg1nZ5vzXD/0fbzn2P/'

    device_id = '10cf4b49-52d7-344d-887c-1ddcc969855'

    # 对接口路径、url参数、header中的xy-common-params、xy-platform-info、请求的data进行签名
    path = '/api/sns/v4/note/user/posted'
    params = parse.urlencode({'user_id': '5eeb209d000000000101d84a'})
    xy_common_params = parse.urlencode({})
    xy_platform_info = parse.urlencode({})
    data = parse.urlencode({})

    # 生成签名
    sign = get_sign(
        path=path,
        params=params,
        xy_common_params=xy_common_params,
        xy_platform_info=xy_platform_info,
        data=data,
        main_hmac=main_hmac,
        device_id=device_id
    )
    print(sign)


if __name__ == '__main__':
    main()
