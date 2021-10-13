from sql import db,Puppy
db.create_all()

sam = Puppy('sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)
print(frank.id)
