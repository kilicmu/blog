from django.db import models
from django.utils.html import format_html
from DjangoUeditor.models import UEditorField
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


class Article(models.Model):
    a_title = models.CharField(max_length=30, verbose_name='标题')
    a_content = UEditorField(
        verbose_name='内容',
        height=500,
        width=900,
        default='test',
        imagePath="img",
        toolbars='besttome',
        filePath='upload',
        blank=True
        )
    a_uploadTime = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    a_readnum = models.IntegerField(verbose_name='阅读数', default=0 , editable=False)
    a_likenum = models.IntegerField(verbose_name='赞赏数', default=0 , editable=False)
    a_pic = models.ImageField(upload_to = "blog/article_img",storage = None, verbose_name='图片')
    a_isdelete = models.BooleanField(default=False)
    objects = models.Manager()

    def AContent(self):
        return format_html(self.a_content)

    def image_data(self):
        return format_html("<img src='/media/{}' width='100px'/>", self.a_pic)

    def __str__(self):
        return self.a_title
    

class Comments(models.Model):
    Comments_Article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    Cuser = models.CharField(max_length = 30)
    Ccontent = models.CharField(max_length=200)
    Cdate = models.DateField(auto_now=True, null=True)
    Cisdelete = models.BooleanField(default=False)
    objects = models.Manager()


    @classmethod
    def create(cls, a_id, u_id, u_content):
        
        comment = cls(Comments_Article_id_id=a_id, Cuser=u_id,Ccontent=u_content)
        return comment
    
    
    def __str__(self):
        return self.Ccontent
    
    
class Tags(models.Model):
    Tags_Article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    Filter_Tags_id = models.ForeignKey('Filter', on_delete=models.CASCADE)
    
    objects = models.Manager()


class User(models.Model):
    Uname = models.CharField(max_length=20, verbose_name='用户名')
    Ucontent = models.CharField(max_length=100, verbose_name='个人简介')
    Uisdelete = models.BooleanField(default=False, verbose_name='已删除')
    Uimg = models.ImageField(upload_to = "blog/user_img", storage = None, verbose_name='头像')
    objects = models.Manager()

    def __str__(self):
        return self.Uname
    

class Filter(models.Model):
    Fname = models.CharField(max_length=20, verbose_name='标签名')
    Fisdelete = models.BooleanField(default=False, verbose_name='已删除')

    header_pic = models.ImageField(upload_to = 'blog/tags_pic',storage = None, verbose_name='图片', default='')
    objects = models.Manager()

    def __str__(self):
        return self.Fname


class Headpic(models.Model):
    h_pic = models.ImageField(upload_to = "blog/article_img",storage = None, verbose_name='图片')
    h_title = models.CharField(max_length=20, verbose_name='主题')
    h_content = models.CharField(max_length=20, verbose_name='简介')
    objects = models.Manager()

    def image_data(self):
        return format_html("<img src='/media/{}' width='100px'/>", self.h_pic)

    def __str__(self):
        return self.h_title



# host：记录主机ip
# count：记录请求的次数
# start_time：记录请求的时间
# is_lock：记录该ip的状态，默认为2   2代表未锁定，1代表锁定
class Host_info(models.Model):
        host = models.CharField(max_length=32)
        count = models.IntegerField()
        start_time = models.DateTimeField()
        is_lock = models.CharField(max_length=32,default='2')