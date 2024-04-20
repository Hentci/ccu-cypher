`main.py`包含了AES-CTR和ChaCha20加密演算法的加密和解密功能。而AES-CCM在`AES-CCM.py`中實現。測速與驗證解密結果code都在裡面。
`gen_data.py`用來生成100MB的data.txt

### how to run

- 生成100MB的隨機plaintext

```
python3 gen_data.py
```

- AES-CCM 加密 (測速和比對功能都在裡面)

```
python3 AES-CCM.py
```

- AES-CTR 和 ChaCha20 加密.py (測速和比對功能都在裡面)

```
python3 main.py
```

- 問題2

```
python3 prob2.py
```