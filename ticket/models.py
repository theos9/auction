from django.db import models
from user.models import User

class TicketModel(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='user')
    subject=models.CharField(max_length=100,verbose_name='subject')
    message=models.TextField(verbose_name='message')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='created at')
    is_answered=models.BooleanField(default=False,verbose_name='is answered')
    answered_by=models.ForeignKey(User, verbose_name="answered by", on_delete=models.SET_NULL,related_name="answered_tickets",null=True, blank=True)
    answer=models.TextField(verbose_name='answer',null=True,blank=True)
    answered_at= models.DateTimeField(null=True,blank=True,verbose_name='answered at')
    def __str__(self):
        return f'ticket from {self.user} - {self.subject}'
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural ='Tickets'
