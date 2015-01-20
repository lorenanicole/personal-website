from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    text = models.CharField(max_length=1600)
    image_url = models.CharField(max_length=200)

    def __unicode__(self):
        return "id=%s Title=%s Pub_Date=%s" % (self.id, self.title, self.published_date)

    @classmethod
    def most_recent(self):
        all_articles = Article.objects.all()
        if len(all_articles) < 3:
            return all_articles
        else:
            return all_articles[:-3]