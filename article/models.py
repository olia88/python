from django.db import models

class Article(models.Model):	
	class Meta():
		db_table='article'  #название таблицы
		
	article_title=models.CharField(max_length=200)
	article_text=models.TextField()
	article_date=models.DateTimeField()
	article_likes=models.IntegerField(default=0)
	
class Comments(models.Model):
	class Meta():
		db_table='Comments'
	
	comments_text=models.TextField(verbose_name='Текст комментария')
	comments_article=models.ForeignKey(Article)
