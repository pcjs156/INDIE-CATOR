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

# 유저가 CRUD 할 수 없고, admin 페이지를 통해 CRUD할 예정
class Event(models.Model):
    name = models.CharField(max_length=100) # 콘서트 이름
    start_date = models.DateTimeField() # 시작일
    end_date = models.DateTimeField() # 종료일
    location = models.CharField(max_length=100) # 장소
    description = models.TextField() # 상세설명
    poster = models.ImageField(upload_to="indiecator/", blank=True, null=True) # 포스터

    artists = models.ManyToManyField('Artist') # 공연 참가 아티스트

    def __str__(self):
        s = [str(i) for i in self.artists.all()]

        # [참여아티스트1, 아티스트2, ...](공연이름) - (위치) 형식으로 정의
        return f"[{', '.join(s)}]{self.name} - ({self.location})"

    def artist_list(self):
        return self.artists.all()

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE) # 해당 공연 일정 / 게시물(공연) 삭제시 자동 삭제
    author = models.CharField(max_length=20)
    commented_date = models.DateTimeField()
    body = models.TextField()

    # (사용자이름) : (댓글 내용)
    def __str__(self):
        return "{0:^20} | {1:<25}:  ".format(self.author, self.summary_body())

    # 댓글 내용이 10자 이상이면 뒤에 " ... "를 붙여 10글자까지만 리턴
    # 10자 미만이면 그냥 리턴
    def summary_body(self):
        return self.body[:10] + (" ... " if len(self.body) > 10 else "")