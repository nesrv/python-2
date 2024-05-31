



Что такое коллбэк
Коллбэк — это функция, которая передаётся на вход другой функции (или другому участку кода), чтобы её запустили в ответ на какое-то событие. 

С помощью этого приёма работают чатботы и интерактивные веб-странички: пользователь нажимает на кнопку, его действие генерирует событие и на событие реагирует колбэк (функция-обработчик).

```python
from time import sleep

def parser(site_name):
    for page in range(1,4):
        sleep(1)
        print(site_name, page)


parser('product')
parser('price')
parser('action')
```


## Асинхронный вариант

```python
from time import *
from asyncio import *

t0 = time()

async def parser(site_name): # корутина
    for page in range(1, 4):
        await sleep (1)
        print(site_name, page)


parsers = [
    ensure_future(parser('product')),
    ensure_future(parser('price')),
    ensure_future(parser('action')),
]

event_loop = get_event_loop()
event_loop.run_until_complete(gather(*parsers))
event_loop.close()
print(time() - t0)
```


Результат выполнения
```
product 1
price 1
action 1
product 2
price 2
action 2
product 3
price 3
action 3
```

## Вызов функций по расписанию

```python
def loader(url):
    print(f'Load from {url}')


async def parser(site_name): # корутина
    for page in range(1, 4):
        await sleep (1)
        print(site_name, page)


parsers = [
    ensure_future(parser('product')),
    ensure_future(parser('price')),
    ensure_future(parser('action')),
]

event_loop = get_event_loop()

loader('url-1')
event_loop.run_until_complete(gather(*parsers))
loader('url-2')

event_loop.close()
```

Результат

```python
Load from url-1
product 1
price 1
action 1
product 2
price 2
action 2
product 3
price 3
action 3
Load from url-2
```

Регистрируем функию

```python
event_loop = get_event_loop()

event_loop.call_soon(loader, 'url-1')

event_loop.run_until_complete(gather(*parsers))

event_loop.call_soon(loader, 'url-2')

```

Результат

```
Load from url-1
product 1
price 1
action 1
product 2
price 2
action 2
product 3
price 3
action 3
```
нет второго вызова `Load from url-1` ?!
Потому что он должен выполнится когда await уйдет в режим ожидания. 

т.е после того как event_loop.run_until_complete(gather(*parsers)) уйдет в режим ожидания

Поменяем местами `print` и `await`

```
async def parser(site_name): # корутина
    for page in range(1, 4):
        print(site_name, page)
        await sleep (1)
```

Результат
```python
product 1
price 1
action 1
Load from url-1
product 2
...
```

Все колбэки нужно помещать до eventloop
```python
event_loop.call_soon(loader, 'url-2') 
# колбэк (ф-ция обратного вызова)

```

Реализуем
```python
def loader(url):
    print(f'Load from {url} время - {time() - t0}')


event_loop = get_event_loop()

event_loop.call_soon(loader, 'url-1') # колбэк 
event_loop.call_later(2, loader, 'url-2') 

event_loop.run_until_complete(gather(*parsers))


event_loop.close()

```

Результат
```
product 1
price 1
action 1
Load from url-1 время - 0.000997304916381836
product 2
price 2
action 2
Load from url-2 время - 2.0124127864837646
price 3
product 3
action 3
3.046332836151123
```


далее 
```python
from time import time as ttime, sleep as sleeping
from asyncio import *

t0 = ttime()

def loader(url):
    print(f'Load from {url} время - {ttime()}')


async def parser(site_name): # корутина
    for page in range(1, 4):
        print(site_name, page)
        #алгоритм
        sleeping(1)
        await sleep (2)



parsers = [
    ensure_future(parser('product')),
    ensure_future(parser('price')),
    ensure_future(parser('action')),
]

event_loop = get_event_loop()

event_loop.call_soon(loader, 'url-1')
event_loop.call_later(2, loader, 'url-2') # колбэк (ф-ция обратного вызова)

event_loop.run_until_complete(gather(*parsers))


event_loop.close()

print(ttime() - t0)

```

## Запуск по времени

```python
event_loop.call_soon(loader, 'url-1')
event_loop.call_later(2, loader, 'url-2') # колбэк (ф-ция обратного вызова)
event_loop.call_at(now + 5, loader, 'url-5') # колбэк (ф-ция обратного вызова)
```