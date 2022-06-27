# not-a-blog-scraper

A webscraper, to scrape data from George R.R. Martin's [Not A Blog](https://georgerrmartin.com/notablog/), in particular.

## Setup

Be sure to use a virtual environment:
> ```sh
> $ python3 -m venv venv
> ```
Here, `venv` is just an example, the virtual environment can be given *any* name.

To activate the virtual environment, run the following command:
> ```sh
> $ source venv/bin/activate
> ```

Upon activation, run `pip list`. Only `pip` and `setuptools` should be installed in the virtual environment.

Once the venv has been activated, install requirements:
> ```sh
> $ pip install -r requirements.txt
> ```