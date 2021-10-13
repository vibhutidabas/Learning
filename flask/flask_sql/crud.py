from sql import db,Puppy

## create

m = Puppy('Rufus',5)
db.session.add(m)
db.session.commit()

## read

a = Puppy.query.all()
print(a)

## select by id

one = Puppy.query.get(1)
print(one)

## filter

pf = Puppy.query.filter_by(name = 'Frankie')
print(pf)

## update

p = Puppy.query.get(1)
p.age = 10
db.session.add(p)
db.session.commit()

##delete

s = Puppy.query.get(2)
db.session.delete(s)
db.session.commit()

##final printing

ap = Puppy.query.all()
print(ap)