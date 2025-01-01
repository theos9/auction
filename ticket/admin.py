from django.contrib import admin
from .models import TicketModel
# from django.core.mail import send_mail
from django.utils.timezone import now
@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    list_display=['subject','user','created_at','is_answered','answered_by','answered_at']
    list_filter = ['is_answered', 'created_at']
    search_fields = ['subject', 'user__national_id', 'user__email']
    readonly_fields = ['user', 'subject', 'message', 'created_at', 'answered_at','is_answered','answered_by']
    def save_model(self, request, obj, form, change):
        if not obj.is_answered and obj.answer:
            obj.is_answered = True
            obj.answered_by = request.user
            obj.answered_at = now()
            # send_mail(
            subject=f"Answer to your ticket: {obj.subject}",
            message=f"Answer text: {obj.answer}",
            recipient_list=[obj.user.email],
            # )
            print(f'{subject}\n{message}\n{recipient_list}')
        super().save_model(request, obj, form, change)