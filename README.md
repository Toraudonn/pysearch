# Search Engine and Web Crawler in Python

- Implement a web crawler
- japanese morphological analysis using [janome](https://github.com/mocobeta/janome)
- Implement search engine
- Store in MongoDB
- Web frontend using [Flask](http://flask.pocoo.org/)


## Requirements

- Python 3.5

## Setup

1. Clone repository

    ```
    $ git clone https://github.com/Toraudonn/pysearch
    ```
    
2. Install python packages

    ```
    $ cd SearchEngine
    $ pip install -r requirements.txt -c constraints.txt
    ```

3. MongoDB settings
4. Run

    ```
    $ python manage.py crawler # build a index
    $ python manage.py webpage # access to http://127.0.0.1:5000
    ```
