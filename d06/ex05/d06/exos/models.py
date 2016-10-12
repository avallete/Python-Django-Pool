from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AUser(AbstractUser):
    pass

class Tip(models.Model):
    content = models.TextField()
    auteur = models.ForeignKey(AUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, editable=False)
    upvotes = models.ManyToManyField(AUser, related_name='upvotes')
    downvotes = models.ManyToManyField(AUser, related_name='downvotes')

    def upvote(self, user):
        if self.downvotes.filter(id=user.id).count():
            self.downvotes.remove(user)
        if self.upvotes.filter(id=user.id).count():
            self.upvotes.remove(user)
        else:
            self.upvotes.add(user)

    def downvote(self, user):
        if user.has_perm('exos.downvote_tip') or self.auteur == user:
            if self.upvotes.filter(id=user.id).count():
                self.upvotes.remove(user)
            if self.downvotes.filter(id=user.id).count():
                self.downvotes.remove(user)
            else:
                self.downvotes.add(user)

    class Meta:
        permissions = (('downvote_tip', 'Can downvote a tip.'),)