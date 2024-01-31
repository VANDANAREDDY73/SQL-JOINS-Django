from django.shortcuts import render
from app.models import *
# Create your views here.
def equijoins(request):
  EMPOBJECTS=Emp.objects.select_related('deptno').all()
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
  EMPOBJECTS=Emp.objects.select_related('deptno').all()
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
  EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
  EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
  d={'EMPOBJECTS':EMPOBJECTS}
  
  return render(request,'equijoins.html',d)



def selfjoins(request):
  empmgrobjects=Emp.objects.select_related('mgr').all()
  empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=2000)
  empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
  d={'empmgrobjects':empmgrobjects}
  return render(request,'selfjoins.html',d)