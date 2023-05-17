from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):
    damage_deal = 'DD'
    tanks = 'TA'
    heal = 'HE'
    dealers = 'DE'
    guild_master = 'GM'
    quest_givers = 'GG'
    smiths = 'SM'
    skinners = 'SK'
    potion_master = 'PM'
    spell_master = 'SP'

    category = [(tanks, 'Танки'),
                (heal, 'Хилы'),
                (damage_deal, 'ДД'),
                (dealers, 'Торговцы'),
                (guild_master, 'Гилдмастеры'),
                (quest_givers, 'Квестгиверы'),
                (smiths, 'Кузнецы'),
                (skinners, 'Кожевники'),
                (potion_master, 'Зельевары'),
                (spell_master, 'Мастера заклинаний'),
                ]

    category = models.CharField(max_length=2, choices=category)
    title = models.CharField(max_length=255)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/advert/{self.id}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
