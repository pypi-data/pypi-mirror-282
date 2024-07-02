class Course:

    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self): # En vez de __str__ _repr__ Para representarlo y de esta forma poder iterar con la lista creada (en este caso)
        return f"{self.name} [{self.duration} horas]: ({self.link})"

courses = [
    Course("Introducción a Linux", 15, "https://Intro-Linux"),
    Course("Personalización de Linux", 3, "https://Perso-Linux"),
    Course("Introducción al Hacking", 54, "https://Hacking")
]
def list_courses():
    for course in courses:
        print(course)

def search_course_by_name(name):
    for course in courses:
        if course.name == name:
            return course

    return None
