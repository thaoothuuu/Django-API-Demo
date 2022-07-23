
class CoursesService(object):
    @classmethod
    def is_high_price(cls, courses_price):
        if courses_price > 500:
            return True
        else:
            return False

