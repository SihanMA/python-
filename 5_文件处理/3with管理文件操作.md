```python
with open('32.txt', 'rt', encoding='utf8') as f:
    print(f.read())
```

with open()方法不仅提供自动释放操作系统占用的方法，并且with open可以使用逗号分隔，一次性打开多个文件，实现文件的快速拷贝。

```
with open('32.txt', 'rb') as fr, \
        open('35r.txt', 'wb') as fw:
    f.write(f.read())
```

