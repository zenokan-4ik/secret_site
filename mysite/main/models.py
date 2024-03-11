from django.db import models

class Secret(models.Model):
    text = models.TextField('Текст')

    def get_data(self):
        return {
            'text': self.text
        }