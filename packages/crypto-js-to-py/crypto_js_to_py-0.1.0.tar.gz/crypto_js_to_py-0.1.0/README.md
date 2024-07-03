# 介绍

这是一个crypto-js的Python复刻版,对ECB和CBC进行了简单的复刻

# 安装与导入
```bash
pip install crypto-js-to-py
```
```python
from crypto_py import CryptoPY
```

# 代码示例
* 一个简单的crypto-js移植python的示例代码
  * 这是一段crypto-js的示例代码
      ```js
      const CryptoJS = require("crypto-js")
    
      key = CryptoJS.enc.Utf8.parse("1234567890123456")
      iv = CryptoJS.enc.Utf8.parse("1234567890123456")
      data = "我是帅哥"
    
      encrypt = CryptoJS.AES.encrypt(data,key,{
          "iv": iv,
          "mode":CryptoJS.mode.CBC,
          "padding":CryptoJS.pad.pkcs7
      }).toString()
    
      console.log(encrypt)  
      // Z/Gl0yMSttfh9jR9zWX7iw==
      ```

  * 这是移植到python的代码
      ```python
    
      from crypto_py import CryptoPY as CryptoJS
    
      # 以下操作都相同
      key = CryptoJS.enc.Utf8.parse("1234567890123456")
      iv = CryptoJS.enc.Utf8.parse("1234567890123456")
      data = "我是帅哥"
    
      encrypt = CryptoJS.AES.encrypt(data,key,{
          "iv": iv,
          "mode":CryptoJS.mode.CBC,
          "padding":CryptoJS.pad.Pkcs7
      }).decode()
    
      print(encrypt)
      # Z/Gl0yMSttfh9jR9zWX7iw==
      ```

* 同时也支持NoPadding和ciphertext
   * `CryptoPY.pad.NoPadding` <font color="red">暂时未能测试是否无BUG</font>
   * `CryptoPY.AES.encrypt(...).ciphertext.decode()`
   * `CryptoPY.AES.decrypt(...).ciphertext.decode()`

