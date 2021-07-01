from django.db import models
from django.contrib.auth.models import User


#속성 정의


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    likes= models.ManyToManyField(User,through='Like',through_fields=('blog','user'),related_name="likes")   #through가 통과한다는 것인데 Like를 통해 통과하겠단 뜻  그 사이에 중계모델을 두겠다는 의미
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    body=models.TextField(max_length=500)
    pub_date= models.DateTimeField('data published')
    writer= models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE)


class Like(models.Model):          #foreinkey로 한 이유는 다대 다 관계지만 좋아요 입장에서 생각해야됨
    blog= models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)   #user, blog를 통해 바로 접근가능하게 만듦