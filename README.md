# Flipped activities for COMP0034 2022-23 Week 4

## Set-up

You will need to a Python environment. You can install all the dependencies using the [requirements.txt](/requirements.txt) file:, e.g. `pip3 install -r requirements.txt`

To complete the paralympics charts requires geojson which is zipped. Unzip the file from [/src/paralympics_app/data/countries.geojson.zip](/src/paralympics_app/data/countries.geojson.zip)

All of the packages have been moved to an 'src' directory. To avoid package import issues during testing please run the following in VS Code Terminal:

```python
pip install --upgrade setuptools

pip install --editable .
```

Further info on [setup.py and packaging](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) and [installing in development mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).

## Activities

The activities are accessed from [activities/activities.md](/activities/activities.md)

This week the activities build on the following apps:

- recycle_app
- paralympics_app

## Week 3 solutions

Possible solutions to the week 3 activities are in the [/src/recycle_app](/src/recycle_app/) and [/src/paralympics_app](/src/paralympics_app/) folders.


To run the apps try:

`python src/recycle_app/recycle_dash_app.py`

and 

`python src/paralympics_app/paralympics_dash_app.py`