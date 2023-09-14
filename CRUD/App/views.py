from .models import Candidate
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views  import SuccessMessageMixin
from django.contrib import messages



#(C) CREATE
class Create(SuccessMessageMixin, CreateView):
     
     model = Candidate
     fields = '__all__'
     success_url = reverse_lazy('read')
     success_message = 'Candidate: %(name)s Registered Successfully'


#(R)  READ

class Read(ListView):
     model = Candidate
     queryset = Candidate.objects.all()

#(U) UPDATE
class Update(SuccessMessageMixin, UpdateView):
     model = Candidate
     fields = '__all__'
     success_url = reverse_lazy('read')
     success_message = 'Candidate: %(name)s Registered Successfully'


#(D)   DELETE
class Delete(DeleteView):
     model = Candidate
     def get_success_url(self):
          messages.success(self.request, 'Candidate Record Deleted Successfully')
          return reverse('read')
     