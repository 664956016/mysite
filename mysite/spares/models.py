from django.db import models


# Create your models here.
class Spare(models.Model):
    apply_time = models.DateField(name='申购时间')
    spares_name = models.CharField(name='零件名称', max_length=30)
    equip_name = models.CharField(name='设备名', max_length=30, null=True)
    asset_type = models.CharField(name='资产类型', max_length=10, null=True)
    model_number = models.CharField(name='型号', max_length=30)
    brand = models.CharField(name='品牌', max_length=10, null=True)
    detail = models.CharField(name='详细细节', max_length=30, null=True)
    amount = models.IntegerField(name='数量')
    unit = models.CharField(name='单位', max_length=5)
    usage = models.CharField(name='用途', max_length=30, null=True)
    applyer = models.CharField(name='采购人', max_length=8)
    user = models.CharField(name='申购人', max_length=8)
    hurry_or_not = models.CharField(name='即用备用', max_length=3)
    pic = models.CharField(name='是否有图片附件', max_length=5)

    def __str__(self):
        return self.设备名

