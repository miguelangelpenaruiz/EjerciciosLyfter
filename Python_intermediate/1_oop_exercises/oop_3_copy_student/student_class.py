class Student:
    fields_students = {'complete_name': str,'section': str, 'spanish_grade': float, 'english_grade': float, 'social_studies_grade': float, 'science_grade': float}
    
    def __init__(self, data):
        try:
            for field, field_type in self.fields_students.items():
                setattr(self, field, field_type(data[field]))
        except KeyError:
            raise KeyError(f"{field} field is missing")
        except ValueError:
            raise ValueError(f'{field} value_type must be {field_type.__name__}')

    def to_dict(self):
        data = {}
        for field in self.fields_students:
            data[field] = getattr(self, field)
        return data