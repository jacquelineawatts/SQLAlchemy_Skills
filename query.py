"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
db.session.query(Model).filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter_by(founded=1903, discontinued=None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()

# Get all models whose brand_name is not Chevrolet.
db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    results = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter_by(year=year).all()

    for result in results:
        print 'Model name:', result[0]
        print 'Brand name:', result[1]
        print 'Headquarters: ', result[2]


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    results = db.session.query(Model.brand_name, Model.name).order_by(Model.brand_name).all()

    brands_summary = {}
    for result in results:
        models_set = brands_summary.get(result[0], set())
        models_set.add(result[1])
        brands_summary[result[0]] = models_set

    for brand, models in brands_summary.items():
        print brand + ":"
        for model in models:
            print "\t", model
        print '-' * 20

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

    # Building a query without the .all(), .first(), .one(), or .get() returns
    # a SQLAlchemy base query. This can be helpful to reuse the query in multiple
    # places or with multiple filters.


# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

    # An association table is a table whose sole purpose is to bring together a
    # many-to-many relationship between two other tables. The association table
    # contains only a primary key and the two foreign keys (of the two tables it
    # is bringing together), and contains no additional relevant attributes
    # (else it would be called a middle table).


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Returns a list of Brand objects whose name matches or contains input string."""

    return Brand.query.filter(Brand.name.like('%{}%'.format(mystr))).all()


def get_models_between(start_year, end_year):
    """Returns a list of Model objects whose year falls between the start_year(incl) and end_year (excl)."""

    return Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()
