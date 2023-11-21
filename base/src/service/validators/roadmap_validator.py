from back.resume.models import Roadmap
from base.src.model.validator import Validator


class RoadmapValidator(Validator):

    def validate(self, obj: dict[Roadmap], type_elm: str):
        if type_elm == 'create':
            res = self.create_validation(obj)
        if type_elm == 'update':
            res = self.update_validation(obj)
        if type_elm == 'delete':
            res = self.delete_validation(obj)
        return res

    def create_validation(self, obj: dict[Roadmap]):
        for key, value in obj.items():
            if key in ['name', 'type_item', 'title', 'priority', 'complexity',
                       'goal_completion', 'added', 'user_id', 'id']:
                if not obj[key]:
                    return False
        return True

    def update_validation(self, obj: dict[Roadmap]):
        for key, value in obj.items():
            if key in ['name', 'type_item', 'title', 'priority', 'complexity',
                       'goal_completion', 'added', 'user_id', 'id']:
                if not obj[key]:
                    return False
        return True

    def delete_validation(self, obj: dict[Roadmap]):
        for key, value in obj.items():
            if key in ['name', 'type_item', 'title', 'priority', 'complexity',
                       'goal_completion', 'added', 'user_id', 'id']:
                if not obj[key]:
                    return False
        return True


