from django.db import models


class Conversation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'conversations'
        managed = True


class Message(models.Model):
    conversation_id = models.IntegerField(db_column='conversationId')
    sender_id = models.IntegerField(db_column='senderId')
    body = models.TextField(null=True, blank=True, db_column='body')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'messages'
        managed = True
