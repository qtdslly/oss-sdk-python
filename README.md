# 适用于 Python 的 云存储开发工具包

`oss-sdk-python` 是适用于 Python 编程语言的开发工具包。

SDK 需要 `Python 3.7` 的最低版本。

入门
---------------
假设您安装了受支持的 Python 版本，您可以先设置您的环境：

```
$ python -m venv .venv
...
$ . .venv/bin/activate
```

然后，您可以使用以下命令从 PyPI 安装 boto3：

```
$ python -m pip install oss-sdk-python
```

或从源代码安装：
```
$ git clone https://github.com/oss/oss-sdk-python.git
$ cd oss-sdk-python
$ python -m pip install -e .
```

###### 代码示例

```
import oss

s3 = oss.resource('s3', endpoint_url='',
access_key_id='jvv4i43jx5jjszcjwxn4xvlf72kq',
secret_access_key='j27ksdw63rbqmalfge23ss4aqg5tbfmkz7qeanrbguvyysp7xokh2',
)
s3.create_bucket(Bucket="bucket1")
```
