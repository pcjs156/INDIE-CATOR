from django.db import models
from django.utils import timezone

# 유저가 CRUD 가능할 예정(사실 비현실적이지만,, 일단 웹페이지상에서 CRUD할 수 있는 모델이 필요하니까)
class Artist(models.Model):
    name = models.CharField(max_length=20) # 아티스트 이름
    debut_date = models.DateField() # 결성 일자
    member = models.TextField() # 멤버 소개(목록)
    description = models.TextField() # 상세 설명
    interest = models.PositiveIntegerField(default=0) # 관심도
    profile_image = models.ImageField(upload_to="indiecator/", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return str(self.name)