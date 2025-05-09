import pandas as pd
from models import db, City, Country

def load_data():
    if Country.query.first():
        return

    df = pd.read_csv("worldcities.csv").head(5000)

    for _, row in df.iterrows():
        country_name = row['country']
        city_name = row['city']
        population = int(row['population']) if not pd.isna(row['population']) else 0

        country = Country.query.filter_by(name=country_name).first()
        if not country:
            country = Country(name=country_name)
            db.session.add(country)
            db.session.commit()

        city = City(name=city_name, population=population, country_id=country.id)
        db.session.add(city)

    db.session.commit()
