class PersonUpdateView(UpdateView):
    model = Person
    fields = ['gender', 'last_name']

class PersonCreate(CreateView):
    model = Person
    fields = ['gender', 'last_name']
    redirect_name = "people"

    field_attrs = {'gender':  {'onchange':"alert('G')"},
                   'last_name': {'onclick': "alert('LN')"},
                   }     

    def get_form(self, form_class=None):
        form = super(PersonCreate, self).get_form(form_class)
        for key, value in self.field_attrs.items():
            form.fields[key].widget.attrs = value;
        return form
		
		
		
		
		
# 使用通用混合类
## 基类
class CreateUpdateMixin(object):

    model = Person
    fields = ['gender', 'last_name']

    field_attrs = {'gender':  {'onchange':"alert('G')"},
                   'last_name': {'onclick': "alert('LN')"},
                   }
				   
## views.py
class PersonUpdateView(CreateUpdateMixin, UpdateView):
    pass

class PersonCreate(CreateUpdateMixin, CreateView):
    redirect_name = "people"   

    def get_form(self, form_class=None):
        form = super(PersonCreate, self).get_form(form_class)
        for key, value in self.field_attrs.items():
            form.fields[key].widget.attrs = value;
        return form				   