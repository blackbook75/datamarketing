# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PageinfoPagegroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'PageInfo_pagegroup'


class PageinfoPageinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    page_name = models.CharField(max_length=255, blank=True, null=True)
    page_url = models.CharField(max_length=500, blank=True, null=True)
    page_group = models.ForeignKey(PageinfoPagegroup, models.DO_NOTHING)
    is_business_page = models.BooleanField(blank=True, null=True)
    page_address = models.CharField(max_length=500, blank=True, null=True)
    page_category = models.CharField(max_length=255, blank=True, null=True)
    page_description = models.TextField(blank=True, null=True)
    page_email = models.CharField(max_length=254, blank=True, null=True)
    page_id = models.CharField(max_length=100, blank=True, null=True)
    page_likes_count = models.CharField(max_length=100, blank=True, null=True)
    page_phone = models.CharField(max_length=100, blank=True, null=True)
    page_talking_count = models.CharField(max_length=100, blank=True, null=True)
    page_username = models.CharField(max_length=255, blank=True, null=True)
    page_website = models.CharField(max_length=500, blank=True, null=True)
    page_were_here_count = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.CharField(max_length=500, blank=True, null=True)
    page_followers = models.CharField(max_length=100, blank=True, null=True)
    page_followers_count = models.IntegerField(blank=True, null=True)
    page_likes = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=20)
    post_count = models.IntegerField(blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    following_count = models.CharField(max_length=100, blank=True, null=True)
    page_join_date = models.CharField(max_length=100, blank=True, null=True)
    page_total_views = models.BigIntegerField(blank=True, null=True)
    page_videos_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PageInfo_pageinfo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FacebookCommentsApril18(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_comments_april18'


class FacebookCommentsApril182568(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_comments_april18_2568'


class FacebookCommentsGroupTest2(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)
    hygiene_color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_comments_group_test2'


class FacebookCommentsGroupTest3(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)
    refer_to_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_comments_group_test3'


class FacebookCommentsGroupTest4(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_comments_group_test4'


class FacebookCommentsWithImageSentiment(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    post_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_comments_with_image_sentiment'


class FacebookPosts(models.Model):
    post_id = models.TextField(primary_key=True)
    group_id = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    post_image = models.TextField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    post_likes = models.IntegerField(blank=True, null=True)
    post_comments_total = models.IntegerField(blank=True, null=True)
    post_shares = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facebook_posts'


class HeartbeatTiktok(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heartbeat_tiktok'


class Hygienepage1(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.FloatField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hygienepage1'


class Hygp1(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    reaction = models.FloatField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hygp1'


class Hygp2(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    reaction = models.FloatField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hygp2'


class Hygp3(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    reaction = models.FloatField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hygp3'


class Ivygp001(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivygp001'


class Ivygp002(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivygp002'


class Ivypg2(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivypg2'


class Ivypg3(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivypg3'


class Ivypg4(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivypg4'


class Ivypg5(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.FloatField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivypg5'


class Ivypostgroup1(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    reaction = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivypostgroup1'


class Ivyt1(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt1'


class Ivyt2(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt2'


class Ivyt3(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt3'


class Ivyt4(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt4'


class Ivyt5(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt5'


class Ivyt6(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt6'


class Ivyt7(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt7'


class Ivyt8(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ivyt8'


class TiktokComments(models.Model):
    author = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    likes = models.BigIntegerField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    sentiment = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    keyword_group = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiktok_comments'
