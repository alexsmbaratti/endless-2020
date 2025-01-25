# Endless 2020

A joke Python datetime implementation based on a [semi-popular internet meme](https://youtube.com/shorts/cJt1v4JReMQ)

## How it works

Simply create an instance of `Endless2020DateTime` with a date of your choosing.
Then, you can print it out as if 2020 never ended.

```python
from endless_2020.endless_2020 import Endless2020DateTime

timestamp = Endless2020DateTime(2025, 1, 25)  # Represents Saturday, January 25, 2025
print(timestamp.strftime("%A, %B %d, %Y"))
```

Which will produce the following output:

```bash
Saturday, December 1517, 2020
```
