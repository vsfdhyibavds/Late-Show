import csv
from app import app, db
from models import Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Load episodes
        episodes = {}
        with open('episodes.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                episode = Episode(date=row['date'], number=int(row['number']))
                db.session.add(episode)
                db.session.flush()
                episodes[episode.id] = episode

        # Load guests
        guests = {}
        with open('guests.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                guest = Guest(name=row['name'], occupation=row['occupation'])
                db.session.add(guest)
                db.session.flush()
                guests[guest.id] = guest

        db.session.commit()

        # Load appearances
        with open('appearances.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                appearance = Appearance(
                    rating=int(row['rating']),
                    episode_id=int(row['episode_id']),
                    guest_id=int(row['guest_id'])
                )
                db.session.add(appearance)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
