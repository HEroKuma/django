from django.shortcuts import render_to_response
from testdb.models import testList, testForeign
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@permission_required('testdb.can_watch', login_url = '/accounts/login/')
def share(request):
	List = testList.objects.all()
	return render_to_response('test.html',locals())