from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User


class UserList(TemplateView):
    template_name = 'user_list.html'

    def get(self, request, *args, **kwargs):
        user_list_obj = User.objects.all().defer('username', 'email').order_by('id')
        paginator = Paginator(user_list_obj, 5, 2)
        page = request.GET.get('page', 1)

        try:
            customer = paginator.page(page)  # 当前对象
        except PageNotAnInteger:
            customer = paginator.page(1)
        except EmptyPage:
            customer = paginator.page(paginator.num_pages)  # 最后一页




        return render(request,
                      self.template_name,
                      {"obj_list": customer}
                      )
