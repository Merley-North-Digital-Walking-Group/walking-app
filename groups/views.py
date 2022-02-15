from django.shortcuts import get_object_or_404, render
from groups.models import Group


# Create your views here.
def group_details(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/group_details.html', {'group': group}) 
    

    
    