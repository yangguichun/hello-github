def build_person2(first, last, *hobby, **user_profile):
    person = {}
    person['姓'] = first
    person['名'] = last
    for key, value in user_profile.items():
        person[key] = value
    person['爱好'] = hobby
    return person