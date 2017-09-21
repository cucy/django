class AssetCreateView(CreateView):

    def get_form(self, form_class=None):
        form = super(AssetCreateView, self).get_form(form_class)
        form.fields['group'].widget.attrs.update({'class': 'mdb-select'})
        return form
