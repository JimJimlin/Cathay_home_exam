# Cathay_home_exam

This repo is used to demo home exam which is written in python3.

## Prerequisites

What things you need to install if you need to build the same env.

```
pip -r requirements.txt
```

## Edit the config file

```
[setting]
year = <year> #seprate by comma ; <iteration number>
season = <season> #seprate by comma ; <list>
region = <region> #基隆市
type = <int> #1 = 不動產買賣,2 = 預售屋買賣,3 = 不動產租賃
```

## Running the program

```
python3 lvr_crawler.py <config.file>
python3 lvr_refine.py
```

## Authors

* **Jim** - *Initial work* - [linkedin](https://www.linkedin.com/in/jimlin790505/)
