from faker import Faker
fake = Faker('en_IN')



age_min = input('Minimum age?')
age_max = input('Maximum age?')

def create():
    print('Name: ' + fake.name())
    print('Address: ' + fake.address())
    print('City of birth: ' + fake.city())
    print('Date of Birth: ' + str(fake.date_of_birth(minimum_age = int(age_min), maximum_age = int(age_max))))
    print('Occupation: ' + fake.job())


create()


