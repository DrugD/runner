from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.BigAutoField(primary_key=True,verbose_name='用户id')
    nickname = models.CharField(max_length=30, verbose_name="昵称")
    picture = models.CharField(max_length=300, verbose_name="微信头像")
    telNumber = models.CharField(null=True, blank=True, max_length=50, verbose_name="收货人手机号码")
    class Meta:
        db_table = "User"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

#训练计划表
class Plan(models.Model):
    plan_id = models.BigAutoField(primary_key=True, verbose_name="训练表id")
    plan_content = models.CharField(max_length=300, verbose_name="训练内容",)
    plan_type = models.CharField(max_length=30, verbose_name="训练科目")
    plan_speed =models.CharField(max_length=30, verbose_name="训练配速")
    plan_place=models.CharField(max_length=30, verbose_name="训练地点")
    plan_mileage=models.CharField(max_length=30, verbose_name="训练距离")

    plan_manager=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="管理者")

    time = models.DateField(auto_now_add=True, verbose_name="时间")

    class Meta:
        db_table = "plan"
        verbose_name = "训练表"
        verbose_name_plural = verbose_name

#参与训练计划表
class JoinPlan(models.Model):
    join_id= models.BigAutoField(primary_key=True,verbose_name='参与id')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default ='', verbose_name="参与者")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE,default ='', verbose_name="训练计划")
    detail=models.CharField(null=True,blank=True,max_length=30, verbose_name="参与训练的备注")
    time = models.DateField(auto_now_add=True, verbose_name="时间")
    class Meta:
        db_table = "participate"
        verbose_name = "参与"
        verbose_name_plural = verbose_name


# ['马拉松赛事', '趣味比赛', '技巧传授', '名人堂'],
class Table_1(models.Model):
    table_id =models.BigAutoField(primary_key=True,verbose_name='表一id')
    table_1_content=models.CharField(null=True,blank=True,max_length=3000, verbose_name="表一内容")
    table_1_title = models.CharField(null=True, blank=True, max_length=30, verbose_name="表一标题")
    writer=models.CharField(null=True,blank=True,max_length=30, verbose_name="表一作者")
    time = models.DateField(auto_now_add=True, verbose_name="时间")
    table_type=models.IntegerField(editable=False,default='1',verbose_name="表种类")
    malasong_location=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛地点")
    malasong_startbook_time=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛开始抽签时间")
    malasong_overbook_time=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛关闭抽签时间")
    malasong_time=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛时间")
    malasong_name=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛名称")

    class Meta:
        db_table = "table_1"
        verbose_name = "表一"
        verbose_name_plural = verbose_name


class Table_2(models.Model):
    table_id =models.BigAutoField(primary_key=True,verbose_name='表二id')
    table_2_content=models.CharField(null=True,blank=True,max_length=3000, verbose_name="表二内容")
    table_2_title = models.CharField(null=True, blank=True, max_length=30, verbose_name="表二标题")
    writer=models.CharField(null=True,blank=True,max_length=30, verbose_name="表二作者")
    time = models.DateField(auto_now_add=True, verbose_name="时间")
    table_type = models.IntegerField(editable=False, default='2', verbose_name="表种类")

    happy_raceg_name=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛名称")
    happy_race_time=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛时间")
    happy_race_startbook_time=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛开始预约时间")
    happy_race_overbook_time=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛停止预约时间")
    malasong_location=models.CharField(null=True,blank=True,max_length=30, verbose_name="比赛地点")
    class Meta:
        db_table = "table_2"
        verbose_name = "表二"
        verbose_name_plural = verbose_name

class Table_3(models.Model):
    table_id =models.BigAutoField(primary_key=True,verbose_name='表三id')
    table_3_content=models.CharField(null=True,blank=True,max_length=3000, verbose_name="表三内容")

    writer = models.CharField(null=True, blank=True, max_length=30, verbose_name="表三作者")
    table_type = models.IntegerField(editable=False, default='3', verbose_name="表种类")

    skill_time = models.DateField(auto_now_add=True, verbose_name="时间")
    skill_title=models.CharField(null=True,blank=True,max_length=30, verbose_name="skill_title")
    skill_brief=models.CharField(null=True,blank=True,max_length=30, verbose_name="skill_brief")
    skill_own=models.CharField(null=True,blank=True,max_length=30, verbose_name="内容提供作者")
    class Meta:
        db_table = "table_3"
        verbose_name = "表三"
        verbose_name_plural = verbose_name

class Table_4(models.Model):
    table_id =models.BigAutoField(primary_key=True,verbose_name='表四id')
    table_4_content=models.CharField(null=True,blank=True,max_length=3000, verbose_name="名人事迹详述")
    writer = models.CharField(null=True, blank=True, max_length=30, verbose_name="表四作者")
    table_type = models.IntegerField(editable=False, default='4', verbose_name="表种类")

    runner_main_achievement = models.CharField(null=True, blank=True, max_length=30, verbose_name="名人事迹总结")
    runner_name=models.CharField(null=True,blank=True,max_length=30, verbose_name="名人名字")
    time = models.DateField(auto_now_add=True, verbose_name="时间")

    class Meta:
        db_table = "table_4"
        verbose_name = "表四"
        verbose_name_plural = verbose_name